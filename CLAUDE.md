# 贪吃蛇 (Snake Game) — 项目导航

## 项目简介
单人贪吃蛇网页游戏，单 HTML 文件（内嵌 CSS + JS），零依赖，双击 `index.html` 即可在浏览器中运行。

## 文件地图

| 文件 | 用途 |
|------|------|
| `index.html` | 全部代码：HTML 结构 + CSS 样式 + JavaScript 逻辑 |
| `docs/requirements.md` | 功能需求文档：页面结构、游戏玩法、难度配置 |
| `docs/tech-spec.md` | 技术规范：Canvas API、数据结构、算法、架构 |
| `docs/design-spec.md` | 设计规范：配色方案、排版、布局、视觉标准 |
| `docs/execution-plan.md` | 执行步骤：12 个开发阶段的详细追踪 |
| `dev-logs/` | 开发日志目录：每天一个 `YYYY-MM-DD.md` 文件 |
| `macOS/` | Xcode macOS 原生应用项目（WKWebView 封装） |

## 运行方式

### 方式一：浏览器（双击即可）
双击 `index.html` 在 Chrome 或 Safari 中打开。

### 方式二：Xcode（macOS 原生应用）
```bash
open macOS/SnakeGame.xcodeproj
```
然后在 Xcode 中按 `Cmd+R` 运行，或：
```bash
cd macOS && xcodebuild -project SnakeGame.xcodeproj -scheme SnakeGame build && open ~/Library/Developer/Xcode/DerivedData/SnakeGame-*/Build/Products/Debug/贪吃蛇.app
```

## 工作说明

### 代码规范
- **所有代码写在 `index.html` 一个文件中**——不要创建单独的 CSS 或 JS 文件
- 每次只做一个小改动，改完就在浏览器中打开 `index.html` 测试
- 代码中用清晰的注释分隔不同区块（CSS 区域、HTML 区域、JS 区域）

### 开发流程
1. 查看 `docs/execution-plan.md` 了解当前进行到哪个阶段
2. 完成一个阶段的任务后，在 `dev-logs/YYYY-MM-DD.md` 中记录
3. 每个开发日志底部维护一个 TODO 列表
4. 新的一天开始开发时，创建新的日志文件，把未完成的 TODO 迁移过去

### 测试方式
- 双击 `index.html` 在 Chrome 或 Safari 中打开
- 每完成一个功能立即测试
- 用浏览器 DevTools（F12）查看 Console 是否有报错

## 快速参考

### 核心参数
- **主色**：`#5CAC9D`（湖水绿）
- **网格**：25×25 格，每格 20px，Canvas 500×500px
- **游戏循环**：`setInterval`（非 requestAnimationFrame）
- **操作**：↑↓←→ 方向键 + WASD，P 键暂停

### 难度配置速查
| 难度 | 障碍物 | Boss | Boss 速度 | 蛇速度 |
|------|--------|------|----------|--------|
| 简单 | 0 | 0 | - | 150ms |
| 普通 | 8 | 1 | 300ms | 120ms |
| 困难 | 15 | 2 | 200ms | 90ms |

### 页面/弹窗清单
1. `#page-menu` — 主菜单
2. `#page-game` — 游戏页面（含 Canvas）
3. `#modal-difficulty` — 难度设置弹窗
4. `#modal-death` — 死亡弹窗
5. `#modal-pause` — 暂停弹窗
