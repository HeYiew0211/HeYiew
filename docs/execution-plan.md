# 贪吃蛇 — 执行步骤

> 每个阶段完成后，将 `[ ]` 改为 `[x]`，并在当天的开发日志中记录。

---

## Phase 1：项目骨架搭建
- [x] 创建 `docs/` 和 `dev-logs/` 目录
- [x] 创建 `CLAUDE.md`（项目导航文件）
- [x] 创建 `docs/requirements.md`（需求文档）
- [x] 创建 `docs/tech-spec.md`（技术规范）
- [x] 创建 `docs/design-spec.md`（设计规范）
- [x] 创建 `docs/execution-plan.md`（本文件）
- [x] 创建 `dev-logs/2026-07-21.md`（首日开发日志）

**验证**：`find` 命令确认 6 个文件全部存在，内容完整。

---

## Phase 2：index.html 静态结构 + 页面切换
- [x] 创建 `index.html`，包含全部 5 个页面/弹窗 div
- [x] 编写 CSS 基础样式（重置、背景、字体、居中）
- [x] 编写 CSS 页面/弹窗切换规则（`.page` / `.modal` / `.active`）
- [x] 编写 JS 函数：`switchPage()`、`showModal()`、`hideModal()`
- [x] 绑定"开始游戏"→ 切换到游戏页面
- [x] 绑定"游戏设置"→ 打开难度弹窗
- [x] 弹窗支持点击遮罩关闭

**验证**：浏览器打开可看到主菜单，按钮可切换页面/弹窗。

---

## Phase 3：难度设置弹窗
- [x] 三个难度按钮（简单/普通/困难）+ 样式
- [x] `selectDifficulty(level)` 函数写入选中的难度
- [x] 选中状态高亮（填充色 vs 描边）
- [x] 默认选中"普通"
- [x] 重新打开弹窗时保持上次选择

**验证**：选择不同难度，console 确认存储正确，视觉高亮正确。

---

## Phase 4：Canvas 画布 + 网格渲染
- [x] 在 `#page-game` 中添加 `<canvas>` 元素
- [x] `initCanvas()` — 获取 2D context
- [x] `drawGrid()` — 绘制 25×25 网格线
- [x] `render()` — 渲染入口函数
- [x] 切换到游戏页面时初始化 Canvas

**验证**：点击开始游戏看到清晰的 25×25 网格。

---

## Phase 5：蛇的初始化与移动
- [x] `DIFFICULTY_CONFIG` 常量定义
- [x] `initSnake()` — 3 节蛇身，中心起始，方向向右
- [x] `gameTick()` — 计算新头位置 + 边界穿越 + 更新蛇数组
- [x] `drawSnake()` — 绘制蛇身和蛇头
- [x] `startGameLoop()` / `stopGameLoop()`
- [x] 键盘监听：方向键 + WASD → `nextDirection`
- [x] 方向队列验证（防 180° 掉头）

**验证**：蛇自动移动，方向可控，穿墙正常，不会反向自杀。

---

## Phase 6：食物 + 得分
- [x] `spawnFood()` — 随机空位生成食物
- [x] 吃食物检测：头==食物 → 增长+加分+刷新食物
- [x] `drawFood()` — 红色圆形
- [x] 得分显示在 `#score-display`

**验证**：吃豆变长、分数递增、新食物位置合法。

---

## Phase 7：障碍物 + 自碰死亡
- [x] `generateObstacles(count)` — 安全区外随机放置
- [x] `drawObstacles()` — 灰色方块
- [x] 障碍物碰撞检测 → `handleDeath()`
- [x] 自身碰撞检测 → `handleDeath()`
- [x] 简单 0 / 普通 8 / 困难 15

**验证**：障碍物数量正确、位置不堵蛇、碰到死亡。

---

## Phase 8：Boss 系统
- [x] `generateBosses(count)` — 不与蛇/食物/障碍物重叠
- [x] `bossTick(index)` — 随机方向、避障重试、边界穿越
- [x] Boss 独立 setInterval（普通 300ms / 困难 200ms）
- [x] `drawBosses()` — 红色方块 + 脉冲效果
- [x] Boss 碰撞检测 → `handleDeath()`

**验证**：Boss 数量正确、随机移动、穿越边界、避障。

---

## Phase 9：死亡弹窗
- [x] `handleDeath()` — 停止循环、显示弹窗
- [x] 弹窗显示最终得分
- [x] "重试"按钮 → 同难度重新开始
- [x] "退出"按钮 → 回主菜单
- [x] `initGame()` 完整初始化/重置逻辑

**验证**：死亡弹窗正常、重试归零、退出回菜单。

---

## Phase 10：暂停弹窗
- [x] 齿轮 ⚙ 图标 → 暂停弹窗
- [x] P 键 → 切换暂停
- [x] "继续"→ 恢复所有 interval
- [x] "退出"→ 回主菜单
- [x] 暂停时忽略方向键

**验证**：暂停/恢复正常、方向键在暂停时无效。

---

## Phase 11：视觉打磨
- [x] 统一湖水绿配色
- [x] 按钮 hover 效果（scale+阴影+颜色过渡）
- [x] 弹窗入场动画（淡入+缩放）
- [x] Canvas 圆角 + 阴影
- [x] Boss 脉冲动画
- [x] 蛇头圆角、食物高光
- [x] 中文字体栈检查

**验证**：所有页面视觉一致、动画流畅。

---

## Phase 12：文档完善
- [x] 审查所有文档内容准确性
- [x] 更新本文件各阶段完成状态
- [x] 首日开发日志总结
- [x] CLAUDE.md 最终检查

**验证**：6 个文件齐全、内容准确、格式正确。

---

## Phase 13：游戏体验优化（2026-07-21 第二轮）
- [x] **蛇出生静止**：游戏开始后蛇不动，按方向键才开始移动，Canvas 显示半透明提示遮罩
- [x] **Boss 改为红色敌方蛇**：多段蛇身，追逐食物（可抢夺），碰到玩家致死
- [x] **主菜单 Logo 重设计**：120px 内联 SVG 简约蛇形图标，替换原 emoji
- [x] **背景动态粒子**：8 个湖水绿圆点 CSS 漂移动画
- [x] 难度标签文字更新：「Boss」→「红蛇」
- [x] 暂停功能仅在游戏启动后可用
- [x] 更新全部文档（tech-spec、design-spec、dev-log）

**验证**：浏览器打开测试四个改动均正常。
