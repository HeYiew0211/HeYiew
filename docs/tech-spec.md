# 贪吃蛇 — 技术规范

## 技术栈
- **HTML5**：Canvas API 渲染游戏画面
- **CSS3**：Flexbox 布局、Transitions 动画
- **JavaScript (ES6+)**：游戏逻辑、事件处理
- **零依赖**：无任何第三方库或框架

## 架构概览

### 单文件组织
`index.html` 按以下顺序组织：
```
1. <!DOCTYPE html> + <head>（meta、title、style）
2. <style>  CSS 全部样式
3. <body>   5 个页面/弹窗的 HTML 结构
4. <script> 全部 JavaScript 逻辑
```

### 页面管理
- 所有"页面"是顶层 `<div class="page">`，通过添加/移除 `.active` 类切换显示
- 所有"弹窗"是 `<div class="modal">`，固定定位覆盖在页面上方，带半透明遮罩
- 核心函数：`switchPage(id)`、`showModal(id)`、`hideModal(id)`

```
CSS:
.page        { display: none; }
.page.active { display: flex; }
.modal       { display: none; position: fixed; ... }
.modal.active { display: flex; }
```

## 核心数据结构

### gameState（全局单一状态对象）
```javascript
const gameState = {
  difficulty: 'normal',      // 'easy' | 'normal' | 'hard'
  snake: [],                 // [{x, y}, ...]  head 在 index 0
  direction: 'right',        // 当前移动方向
  nextDirection: 'right',    // 按键缓存的下一方向（防 180° 掉头）
  food: null,                // {x, y} | null
  obstacles: [],             // [{x, y}, ...]
  bosses: [],                // [{body: [{x,y},...], direction}, ...]  head 在 body[0]
  score: 0,
  isPaused: false,
  isGameOver: false,
  hasStarted: false,         // 蛇是否已开始移动（首次按键后变为 true）
  snakeIntervalId: null,     // 蛇移动的 setInterval ID
  bossIntervals: [],         // Boss 移动的 setInterval ID 数组
};
```

### DIFFICULTY_CONFIG（难度配置表）
```javascript
const DIFFICULTY_CONFIG = {
  easy:   { obstacles: 0,  bosses: 0, snakeSpeed: 150, bossSpeed: 0 },
  normal: { obstacles: 8,  bosses: 1, snakeSpeed: 120, bossSpeed: 300 },
  hard:   { obstacles: 15, bosses: 2, snakeSpeed: 90,  bossSpeed: 200 },
};
```

## Canvas 渲染

### 参数
- Canvas 尺寸：500 × 500 像素
- 网格：25 × 25 格
- 每格尺寸：500 ÷ 25 = 20px

### 渲染函数
```
render()
  ├── clearRect()          清空画布
  ├── drawGrid()           绘制 25×25 网格线
  ├── drawObstacles()      绘制障碍物（灰色方块）
  ├── drawFood()           绘制食物（红色圆形）
  ├── drawBosses()         绘制 Boss（红色方块+脉冲）
  └── drawSnake()          绘制蛇（头深绿、身湖绿）
```

### 单元格绘制
```javascript
function drawCell(x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
}
```

## 游戏循环

```
initGame()
  ├── stopGameLoop() + 重置状态
  ├── initSnake() / generateObstacles() / generateBosses() / spawnFood()
  ├── render() — 绘制初始画面
  └── drawStartHint() — 半透明遮罩提示"按方向键或 WASD 开始"
  └── 等待用户首次按键…

首次方向键按下:
  ├── gameState.hasStarted = true
  ├── gameState.direction = 按键方向
  └── startGameLoop() → 启动所有 interval

startGameLoop()
  ├── gameState.snakeIntervalId = setInterval(gameTick, snakeSpeed)
  └── for each boss i:
       └── gameState.bossIntervals.push(setInterval(() => bossTick(i), bossSpeed))

stopGameLoop()
  ├── clearInterval(gameState.snakeIntervalId)
  └── gameState.bossIntervals.forEach(id => clearInterval(id))
  └── gameState.bossIntervals = []

gameTick()  // 每个蛇移动间隔执行一次
  1. 检查 hasStarted / isPaused / isGameOver
  2. 应用 nextDirection 到 direction（验证非反向）
  3. 计算新头部位置（含边界穿越）
  4. 碰撞检测（障碍物 → 死、Boss 任意身体段 → 死、自身 → 死）
  5. 食物检测（吃到 → 加分+增长+刷新食物）
  6. 更新蛇数组（unshift 头，pop 尾 或 不pop=增长）
  7. render()
```

## 碰撞检测

每 tick 对新头部位置 `(newX, newY)` 进行：
1. **障碍物碰撞**：`obstacles.some(o => o.x === newX && o.y === newY)`
2. **Boss 碰撞**：遍历所有 Boss 的 `body` 数组，逐一比较坐标
3. **自身碰撞**：`snake.slice(1).some(s => s.x === newX && s.y === newY)`

任一命中 → `handleDeath()`

## Boss 追逐算法（红色敌方蛇）

Boss 是一条红色蛇（3 段），头部追逐食物。每 tick：

1. 计算到食物的距离（考虑 wrap-around 选择较短路径）
2. 优先在距离更大的轴上移动
3. 检查障碍物和自身身体 → 如受阻，尝试次优方向
4. 移动后检查是否吃到食物 → 食物被抢夺，重新生成
5. 移动后检查 Boss 头部是否碰到玩家蛇身 → 玩家死亡

```javascript
function bossTick(index) {
  const boss = gameState.bosses[index];
  const head = boss.body[0];
  // 计算到食物的最优方向（含 wrap-around）
  const dirPriority = buildDirectionPriority(head, food);
  for (const dir of dirPriority) {
    const newPos = calcNewPosition(head, dir); // 含边界穿越
    if (!isObstacle(newPos) && !isOwnBody(newPos, boss.body)) {
      boss.body.unshift(newPos);   // 插入新头
      if (ate_food(newPos)) spawnFood();
      boss.body.pop();             // 去尾（不增长）
      if (hitPlayer(newPos)) handleDeath();
      break;
    }
  }
}
```

## 障碍物生成（安全区机制）

安全区 = 蛇的初始 3 个格子 + 曼哈顿距离 ≤ 2 的所有格子

障碍物随机放置在安全区之外的格子上，不重叠。

## 方向队列机制

- `keydown` 事件只写入 `gameState.nextDirection`
- `gameTick()` 开头才真正应用方向
- 若 `nextDirection` 与 `direction` 完全相反 → 忽略（防止掉头自杀）
- 这解决了"两次快速按键之间蛇还没移动导致自杀"的问题

## 暂停/恢复机制

暂停时：
- 保存所有 interval ID
- `clearInterval` 停止所有循环
- `gameState.isPaused = true`
- 忽略方向键输入

恢复时：
- 用保存的延迟重新创建所有 interval
- `gameState.isPaused = false`
