# Python 核心 20% 全景图

> **怎么使用这张导图？**
>
> 1. **纵览全局**：从中心向四周发散阅读，了解 Python 核心 20% 知识覆盖了哪些领域。
> 2. **模块化学习**：每天聚焦一个 Day 分支，不贪多、不跳步。
> 3. **标注含义**：`⭐` 表示重点模块，`🎯` 表示综合实战。
> 4. **学完后回顾**：用这张图做 checklist，逐项自测，查漏补缺。

```mermaid
mindmap
  root(Python 核心 20%)
    Day 1 基础语法
      变量与命名
        赋值 =
        命名规范 snake_case
        动态类型
      数据类型
        int
        float
        str
        bool
        type()
      类型转换
        int()
        str()
        float()
        bool()
      I/O
        print()
        input()
        f-string
      运算符
        算术 + - * / // % **
        比较 == != > < >= <=
    Day 2 控制流
      条件判断
        if
        elif
        else
      逻辑运算
        and
        or
        not
      循环
        for
        while
        range()
      循环控制
        break
        continue
    Day 3 数据结构 ⭐
      list
        索引与切片
        增删改查 append pop insert
        排序 sort sorted
      dict
        键值对 key-value
        get()
        遍历 keys values items
      tuple
        不可变 immutable
        解包 unpacking
      set
        去重 unique
        集合运算 & | - ^
    Day 4 函数与模块
      函数
        def
        参数 默认 关键字 可变
        return
        作用域 LEGB
      模块
        import
        from...import
        __name__
      常用标准库
        random
        math
        datetime
    Day 5 字符串与文件
      字符串方法
        split join
        strip replace
        upper lower
      f-string 进阶
        格式化数字 :.2f
        对齐 :< :> :^
        千分位 :,
      文件操作
        open()
        模式 r w a
        read write readlines
        with 语句
    Day 6 异常与推导式
      异常处理
        try except finally
        常见异常 ValueError TypeError KeyError
        raise
      推导式
        list comprehension
        dict comprehension
      面向对象入门
        class
        __init__
        self
        实例方法
    Day 7 综合项目 🎯
      命令行 CLI 工具
        argparse
        交互菜单
      数据持久化
        JSON 读写
        json.dump json.load
      模块化设计
        拆分文件
        __init__.py
      项目打包
        requirements.txt
```

**学习策略建议：**

- 每天 1.5—2 小时，7 天完成。
- 每天动手写 50—100 行代码，光看不练等于零。
- 遇到不懂的概念，先往下走，Day 7 项目会把碎片知识串起来。
- 图中列出的每个子节点都是一道"自测题"：你能用自己的话解释它吗？你能写出一个示例吗？
