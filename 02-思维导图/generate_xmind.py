#!/usr/bin/env python3
"""生成 XMind 原生格式 (.xmind) —— XMind 2020+ 可直接打开。

.xmind 文件本质是 ZIP 包，内含：
  - content.json  思维导图数据（JSON）
  - metadata.json 元数据
  - manifest.json 文件清单
"""

import json
import os
import uuid
import zipfile

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── 辅助函数 ──────────────────────────────────────────────


def topic(title: str, children: list[dict] | None = None) -> dict:
    """创建一个 topic 节点"""
    node = {
        "id": uuid.uuid4().hex[:12],
        "class": "topic",
        "title": title,
    }
    if children:
        node["children"] = {"attached": children}
    return node


def make_xmind(root_title: str, children: list[dict], filename: str):
    """生成一个 .xmind 文件"""
    content = [
        {
            "id": uuid.uuid4().hex[:12],
            "class": "sheet",
            "title": "Sheet 1",
            "rootTopic": topic(root_title, children),
        }
    ]

    metadata = {
        "creator": {"name": "Python 7-Day Study Plan", "version": "1.0"},
    }

    manifest = {"file-entries": {
        "content.json": {},
        "metadata.json": {},
    }}

    path = os.path.join(OUTPUT_DIR, filename)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("content.json", json.dumps(content, ensure_ascii=False, indent=2))
        zf.writestr("metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    size_kb = os.path.getsize(path) / 1024
    print(f"✅ {filename} ({size_kb:.1f} KB)")


# ═══════════════════════════════════════════════════════════
# 00 - Python 核心全景图
# ═══════════════════════════════════════════════════════════
make_xmind("Python 核心 20%", [
    topic("Day 1 基础语法", [
        topic("变量与命名", [topic("赋值 ="), topic("命名规范 snake_case"), topic("动态类型")]),
        topic("数据类型", [topic("int"), topic("float"), topic("str"), topic("bool"), topic("type()")]),
        topic("类型转换", [topic("int()"), topic("str()"), topic("float()"), topic("bool()")]),
        topic("I/O", [topic("print()"), topic("input()"), topic("f-string")]),
        topic("运算符", [topic("算术 + - * / // % **"), topic("比较 == != > < >= <=")]),
    ]),
    topic("Day 2 控制流", [
        topic("条件判断", [topic("if"), topic("elif"), topic("else")]),
        topic("逻辑运算", [topic("and"), topic("or"), topic("not")]),
        topic("循环", [topic("for"), topic("while"), topic("range()")]),
        topic("循环控制", [topic("break"), topic("continue")]),
    ]),
    topic("Day 3 数据结构 ⭐", [
        topic("list", [topic("索引与切片"), topic("增删改查 append pop insert"), topic("排序 sort sorted")]),
        topic("dict", [topic("键值对 key-value"), topic("get()"), topic("遍历 keys values items")]),
        topic("tuple", [topic("不可变 immutable"), topic("解包 unpacking")]),
        topic("set", [topic("去重 unique"), topic("集合运算 & | - ^")]),
    ]),
    topic("Day 4 函数与模块", [
        topic("函数", [topic("def"), topic("参数 默认 关键字 可变"), topic("return"), topic("作用域 LEGB")]),
        topic("模块", [topic("import"), topic("from...import"), topic("__name__")]),
        topic("常用标准库", [topic("random"), topic("math"), topic("datetime")]),
    ]),
    topic("Day 5 字符串与文件", [
        topic("字符串方法", [topic("split join"), topic("strip replace"), topic("upper lower")]),
        topic("f-string 进阶", [topic("格式化数字 :.2f"), topic("对齐 :< :> :^"), topic("千分位 :,")]),
        topic("文件操作", [topic("open()"), topic("模式 r w a"), topic("read write readlines"), topic("with 语句")]),
    ]),
    topic("Day 6 异常与推导式", [
        topic("异常处理", [topic("try except finally"), topic("常见异常 ValueError TypeError KeyError"), topic("raise")]),
        topic("推导式", [topic("list comprehension"), topic("dict comprehension")]),
        topic("面向对象入门", [topic("class"), topic("__init__"), topic("self"), topic("实例方法")]),
    ]),
    topic("Day 7 综合项目 🎯", [
        topic("命令行 CLI 工具", [topic("argparse"), topic("交互菜单")]),
        topic("数据持久化", [topic("JSON 读写"), topic("json.dump json.load")]),
        topic("模块化设计", [topic("拆分文件"), topic("__init__.py")]),
        topic("项目打包", [topic("requirements.txt")]),
    ]),
], "00-Python核心全景图.xmind")

# ═══════════════════════════════════════════════════════════
# 01 - Day 1：基础语法与数据类型
# ═══════════════════════════════════════════════════════════
make_xmind("Day 1 基础语法与数据类型", [
    topic("环境准备", [
        topic("Python 安装"),
        topic("VS Code / PyCharm"),
        topic("运行第一行代码 hello world"),
    ]),
    topic("变量", [
        topic("赋值 ="),
        topic("命名规范 snake_case"),
        topic("不能以数字开头"),
        topic("区分大小写"),
        topic("动态类型"),
    ]),
    topic("数据类型", [
        topic("int 整数", [topic("a = 10"), topic("无大小上限")]),
        topic("float 浮点数", [topic("b = 3.14"), topic("科学计数法 1e-5")]),
        topic("str 字符串", [
            topic("单引号 ' '"),
            topic('双引号 " "'),
            topic("三引号 ''' ''' 多行"),
        ]),
        topic("bool 布尔值", [topic("True"), topic("False")]),
        topic("type() 查看类型"),
    ]),
    topic("类型转换", [
        topic('int("10") → 10'),
        topic('str(3.14) → "3.14"'),
        topic('float("3.14") → 3.14'),
        topic("bool(0) → False"),
    ]),
    topic("输入输出", [
        topic("print()", [
            topic("sep 分隔符"),
            topic("end 结束符"),
            topic('print(a, b, sep=",")'),
        ]),
        topic("input()", [
            topic("永远返回 str"),
            topic('name = input("请输入: ")'),
        ]),
        topic("f-string", [
            topic('f"我的名字是{name}"'),
            topic('f"价格: {price:.2f}"'),
        ]),
    ]),
    topic("运算符", [
        topic("算术运算符", [
            topic("+ 加"), topic("- 减"), topic("* 乘"),
            topic("/ 除 得 float"), topic("// 整除"),
            topic("% 取余"), topic("** 幂"),
        ]),
        topic("比较运算符", [
            topic("== 等于"), topic("!= 不等于"),
            topic("> 大于"), topic("< 小于"),
            topic(">= 大于等于"), topic("<= 小于等于"),
        ]),
    ]),
], "01-Day1-基础语法与数据类型.xmind")

# ═══════════════════════════════════════════════════════════
# 02 - Day 2：控制流
# ═══════════════════════════════════════════════════════════
make_xmind("Day 2 控制流", [
    topic("条件判断 if", [
        topic("if 条件:"),
        topic("    缩进代码块"),
        topic("elif 条件:", [topic("多重判断")]),
        topic("else:", [topic("兜底分支")]),
        topic("嵌套 if"),
        topic("pass 占位符"),
    ]),
    topic("逻辑运算", [
        topic("and", [topic("全 True 才 True"), topic("短路求值")]),
        topic("or", [topic("有一个 True 就 True"), topic("短路求值")]),
        topic("not", [topic("取反"), topic("not True → False")]),
    ]),
    topic("循环 for", [
        topic("for item in sequence:", [
            topic("遍历 list"),
            topic('for c in "hello"'),
            topic("遍历 dict"),
        ]),
        topic("range()", [
            topic("range(n) 0 到 n-1"),
            topic("range(start, stop)"),
            topic("range(start, stop, step)"),
        ]),
        topic("enumerate()", [topic("同时拿索引与值")]),
        topic("zip()", [topic("并行遍历多个序列")]),
    ]),
    topic("循环 while", [
        topic("while 条件:"),
        topic("条件为 True 时重复"),
        topic("小心死循环"),
        topic("循环变量更新"),
    ]),
    topic("循环控制", [
        topic("break", [topic("终止整个循环")]),
        topic("continue", [topic("跳过本次，继续下一次")]),
        topic("for...else", [topic("循环正常结束才执行 else")]),
    ]),
], "02-Day2-控制流.xmind")

# ═══════════════════════════════════════════════════════════
# 03 - Day 3：数据结构 ⭐
# ═══════════════════════════════════════════════════════════
make_xmind("Day 3 数据结构 ⭐", [
    topic("list 列表", [
        topic("创建", [topic("[]"), topic("list()")]),
        topic("索引", [topic("正向 从 0 开始"), topic("反向 从 -1 开始")]),
        topic("切片 slicing", [topic("[start:stop:step]"), topic("[::-1] 反转")]),
        topic("增", [
            topic("append(x) 末尾追加"),
            topic("insert(i, x) 指定位置"),
            topic("extend(iterable) 合并"),
        ]),
        topic("删", [
            topic("pop(i) 按索引删除并返回"),
            topic("remove(x) 按值删除"),
            topic("del lst[i]"),
        ]),
        topic("改", [topic("lst[i] = new_value")]),
        topic("查", [
            topic("in 判断存在"),
            topic("index(x) 查找位置"),
            topic("count(x) 计数"),
        ]),
        topic("排序", [
            topic("lst.sort() 原地排序"),
            topic("sorted(lst) 返回新列表"),
            topic("reverse=True 降序"),
            topic("key 参数 自定义排序"),
        ]),
    ]),
    topic("dict 字典", [
        topic("创建", [topic("{}"), topic("dict()")]),
        topic("键值对", [topic("key: value"), topic("key 必须不可变类型")]),
        topic("访问", [topic('d["key"]'), topic("d.get(key, default)")]),
        topic("增改", [topic('d["new_key"] = value')]),
        topic("删", [topic("pop(key)"), topic("del d[key]")]),
        topic("遍历", [
            topic("for k in d.keys()"),
            topic("for v in d.values()"),
            topic("for k, v in d.items()"),
        ]),
    ]),
    topic("tuple 元组", [
        topic("创建", [topic("()"), topic("tuple()"), topic("单元素 (x,)")]),
        topic("不可变 immutable", [topic("不能修改"), topic("可以包含可变元素")]),
        topic("解包 unpacking", [
            topic("a, b = (1, 2)"),
            topic("a, *rest = (1, 2, 3)"),
        ]),
    ]),
    topic("set 集合", [
        topic("创建", [topic("set()"), topic("{1, 2, 3}")]),
        topic("去重", [topic("自动去重")]),
        topic("增删", [topic("add(x)"), topic("remove(x)"), topic("discard(x) 不报错")]),
        topic("集合运算", [
            topic("交集 &"), topic("并集 |"),
            topic("差集 -"), topic("对称差 ^"),
        ]),
    ]),
], "03-Day3-核心数据结构.xmind")

# ═══════════════════════════════════════════════════════════
# 04 - Day 4：函数与模块
# ═══════════════════════════════════════════════════════════
make_xmind("Day 4 函数与模块", [
    topic("函数 function", [
        topic("定义 def", [
            topic("def 函数名():"),
            topic("缩进代码块"),
            topic("docstring 文档字符串"),
        ]),
        topic("参数", [
            topic("位置参数"),
            topic("默认参数 def f(a, b=10)"),
            topic("关键字参数 f(a=1, b=2)"),
            topic("可变参数 *args 元组"),
            topic("关键字可变参数 **kwargs 字典"),
        ]),
        topic("返回值 return", [
            topic("单个值"),
            topic("多个值 自动打包为 tuple"),
            topic("无 return → None"),
        ]),
        topic("作用域 LEGB", [
            topic("Local 局部"),
            topic("Enclosing 闭包"),
            topic("Global 全局"),
            topic("Built-in 内置"),
            topic("global 关键字"),
        ]),
    ]),
    topic("模块 module", [
        topic("导入方式", [
            topic("import 模块名"),
            topic("import 模块名 as 别名"),
            topic("from 模块 import 函数"),
            topic("from 模块 import *"),
        ]),
        topic("模块搜索路径", [topic("sys.path")]),
        topic("常用技巧", [
            topic('if __name__ == "__main__":'),
            topic("dir() 查看模块内容"),
        ]),
    ]),
    topic("常用标准库", [
        topic("random", [
            topic("randint(a, b)"),
            topic("choice(seq)"),
            topic("shuffle(lst)"),
            topic("random() 0-1 浮点"),
        ]),
        topic("math", [
            topic("sqrt(x) 开方"),
            topic("pi"),
            topic("ceil() / floor()"),
        ]),
        topic("datetime", [
            topic("datetime.now()"),
            topic("timedelta()"),
            topic("strftime() / strptime()"),
        ]),
    ]),
], "04-Day4-函数与模块.xmind")

# ═══════════════════════════════════════════════════════════
# 05 - Day 5：字符串与文件
# ═══════════════════════════════════════════════════════════
make_xmind("Day 5 字符串与文件", [
    topic("字符串方法", [
        topic("分割与合并", [
            topic("s.split(sep) 分割为列表"),
            topic("s.splitlines() 按行分割"),
            topic("sep.join(iterable) 合并"),
        ]),
        topic("清理", [
            topic("s.strip() 去两端空白"),
            topic("s.lstrip() / s.rstrip()"),
            topic("s.replace(old, new) 替换"),
        ]),
        topic("大小写", [
            topic("s.upper() 全大写"),
            topic("s.lower() 全小写"),
            topic("s.title() 首字母大写"),
        ]),
        topic("查找与判断", [
            topic("s.find(sub) 找子串"),
            topic("s.startswith(prefix)"),
            topic("s.endswith(suffix)"),
            topic("s.count(sub) 计数"),
        ]),
        topic("判断方法", [
            topic("s.isdigit()"),
            topic("s.isalpha()"),
            topic("s.isalnum()"),
        ]),
    ]),
    topic("f-string 进阶", [
        topic("格式化数字", [
            topic("{num:.2f} 保留两位小数"),
            topic("{num:.0%} 百分比"),
            topic("{num:.2e} 科学计数"),
        ]),
        topic("对齐与填充", [
            topic("{text:<10} 左对齐"),
            topic("{text:>10} 右对齐"),
            topic("{text:^10} 居中对齐"),
            topic("{text:*^10} 填充字符"),
        ]),
        topic("千分位与进制", [
            topic("{num:,} 千分位"),
            topic("{num:b} 二进制"),
            topic("{num:x} 十六进制"),
        ]),
    ]),
    topic("文件操作", [
        topic("打开文件", [
            topic("f = open(path, mode)"),
            topic("模式 r 读 / w 写 / a 追加"),
            topic('encoding="utf-8"'),
        ]),
        topic("读取", [
            topic("f.read() 读全部"),
            topic("f.readline() 读一行"),
            topic("f.readlines() 读所有行"),
            topic("for line in f 逐行"),
        ]),
        topic("写入", [
            topic("f.write(text)"),
            topic("f.writelines(lines)"),
        ]),
        topic("with 语句", [
            topic("with open() as f:"),
            topic("自动关闭文件"),
            topic("推荐始终使用 with"),
        ]),
        topic("pathlib", [
            topic("Path 对象"),
            topic("路径拼接 /"),
            topic(".read_text()"),
        ]),
    ]),
], "05-Day5-字符串处理与文件IO.xmind")

# ═══════════════════════════════════════════════════════════
# 06 - Day 6：异常处理与推导式
# ═══════════════════════════════════════════════════════════
make_xmind("Day 6 异常处理与推导式", [
    topic("异常处理", [
        topic("try...except", [
            topic("try 包裹可能出错的代码"),
            topic("except 捕获指定异常"),
            topic("多个 except 分支"),
            topic("except Exception as e"),
        ]),
        topic("finally", [
            topic("无论是否异常都执行"),
            topic("常用于释放资源"),
        ]),
        topic("else", [topic("try 无异常时执行")]),
        topic("常见异常", [
            topic("ValueError 值错误"),
            topic("TypeError 类型错误"),
            topic("KeyError 键不存在"),
            topic("IndexError 索引越界"),
            topic("FileNotFoundError 文件未找到"),
            topic("ZeroDivisionError 除以零"),
        ]),
        topic("raise", [
            topic("手动抛出异常"),
            topic('raise ValueError("原因")'),
        ]),
        topic("自定义异常", [
            topic("class MyError(Exception)"),
        ]),
    ]),
    topic("list comprehension", [
        topic("基本语法", [
            topic("[表达式 for item in 可迭代对象]"),
            topic("[x*2 for x in range(10)]"),
        ]),
        topic("带条件过滤", [
            topic("[x for x in lst if x > 0]"),
        ]),
        topic("嵌套", [
            topic("[(x, y) for x in a for y in b]"),
        ]),
    ]),
    topic("dict comprehension", [
        topic("基本语法", [
            topic("{k: v for item in seq}"),
            topic("{x: x**2 for x in range(5)}"),
        ]),
        topic("带条件", [
            topic("{k: v for k,v in d.items() if v > 0}"),
        ]),
        topic("键值互换", [
            topic("{v: k for k,v in d.items()}"),
        ]),
    ]),
    topic("面向对象入门", [
        topic("类与对象", [
            topic("class 类名:"),
            topic("类名用 PascalCase"),
        ]),
        topic("构造方法", [
            topic("def __init__(self, ...):"),
            topic("self.属性 = 参数"),
        ]),
        topic("self", [
            topic("代表实例本身"),
            topic("必须显式写"),
        ]),
        topic("实例方法", [
            topic("def method(self, ...):"),
        ]),
        topic("创建实例", [
            topic("obj = ClassName(args)"),
            topic("obj.method()"),
        ]),
    ]),
], "06-Day6-异常处理与推导式.xmind")

# ═══════════════════════════════════════════════════════════
# 07 - Day 7：综合实战项目 🎯
# ═══════════════════════════════════════════════════════════
make_xmind("Day 7 综合实战项目 🎯", [
    topic("命令行工具 CLI", [
        topic("argparse", [
            topic("ArgumentParser"),
            topic("add_argument()"),
            topic("parse_args()"),
        ]),
        topic("交互菜单", [
            topic("while True 循环菜单"),
            topic("数字选择功能"),
            topic("input() 读取选项"),
        ]),
        topic("sys.argv", [topic("简单参数获取")]),
    ]),
    topic("数据持久化", [
        topic("JSON", [
            topic("基本用法", [
                topic("json.dumps() dict → str"),
                topic("json.loads() str → dict"),
                topic("indent=2 美化输出"),
                topic("ensure_ascii=False"),
            ]),
            topic("文件读写", [
                topic("json.dump(data, f)"),
                topic("data = json.load(f)"),
            ]),
            topic("适用场景", [
                topic("配置文件 config.json"),
                topic("数据存储"),
                topic("简单数据库"),
            ]),
        ]),
    ]),
    topic("模块化设计", [
        topic("代码拆分", [
            topic("主程序 main.py"),
            topic("工具函数 utils.py"),
            topic("数据模型 models.py"),
        ]),
        topic("包 package", [
            topic("文件夹 + __init__.py"),
            topic("from package import module"),
        ]),
        topic('if __name__ == "__main__":', [
            topic("入口判断"),
        ]),
    ]),
    topic("项目打包", [
        topic("requirements.txt", [
            topic("pip freeze > requirements.txt"),
            topic("pip install -r requirements.txt"),
        ]),
        topic(".gitignore", [
            topic("__pycache__/"),
            topic("*.pyc"),
            topic("venv/"),
        ]),
    ]),
    topic("项目示例：命令行备忘录", [
        topic("功能", [
            topic("添加记录"),
            topic("查看记录"),
            topic("删除记录"),
            topic("保存到 JSON 文件"),
        ]),
        topic("文件组织", [
            topic("memo/"),
            topic("  __init__.py"),
            topic("  cli.py"),
            topic("  storage.py"),
            topic("  models.py"),
            topic("main.py"),
        ]),
    ]),
], "07-Day7-综合实战项目.xmind")

print(f"\n🎉 完成！8 个 .xmind 文件已生成到：{OUTPUT_DIR}")
print("  用 XMind 直接双击打开即可。")
