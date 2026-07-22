#!/usr/bin/env python3
"""将 Mermaid 思维导图内容转换为 FreeMind (.mm) 格式，XMind 可直接打开。"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def esc(text: str) -> str:
    """转义 XML 特殊字符"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def mindmap(root_text: str, children: list[dict]) -> str:
    """递归生成 FreeMind XML 节点树"""
    lines = [f'<node TEXT="{esc(root_text)}">']
    for child in children:
        lines.append(mindmap(child["text"], child.get("children", [])))
    lines.append("</node>")
    return "\n".join(lines)


def save_mm(filename: str, root_text: str, children: list[dict]):
    """保存一个 .mm 文件"""
    xml = f"""<map version="1.0.1">
{mindmap(root_text, children)}
</map>"""
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"✅ {filename} ({len(xml)} bytes)")


# ============================================================
# 00 - Python 核心全景图
# ============================================================
save_mm("00-Python核心全景图.mm", "Python 核心 20%", [
    {"text": "Day 1 基础语法", "children": [
        {"text": "变量与命名", "children": [{"text": "赋值 ="}, {"text": "命名规范 snake_case"}, {"text": "动态类型"}]},
        {"text": "数据类型", "children": [{"text": "int"}, {"text": "float"}, {"text": "str"}, {"text": "bool"}, {"text": "type()"}]},
        {"text": "类型转换", "children": [{"text": "int()"}, {"text": "str()"}, {"text": "float()"}, {"text": "bool()"}]},
        {"text": "I/O", "children": [{"text": "print()"}, {"text": "input()"}, {"text": "f-string"}]},
        {"text": "运算符", "children": [{"text": "算术 + - * / // % **"}, {"text": "比较 == != > < >= <="}]},
    ]},
    {"text": "Day 2 控制流", "children": [
        {"text": "条件判断", "children": [{"text": "if"}, {"text": "elif"}, {"text": "else"}]},
        {"text": "逻辑运算", "children": [{"text": "and"}, {"text": "or"}, {"text": "not"}]},
        {"text": "循环", "children": [{"text": "for"}, {"text": "while"}, {"text": "range()"}]},
        {"text": "循环控制", "children": [{"text": "break"}, {"text": "continue"}]},
    ]},
    {"text": "Day 3 数据结构 ⭐", "children": [
        {"text": "list", "children": [
            {"text": "索引与切片"}, {"text": "增删改查 append pop insert"}, {"text": "排序 sort sorted"},
        ]},
        {"text": "dict", "children": [
            {"text": "键值对 key-value"}, {"text": "get()"}, {"text": "遍历 keys values items"},
        ]},
        {"text": "tuple", "children": [{"text": "不可变 immutable"}, {"text": "解包 unpacking"}]},
        {"text": "set", "children": [{"text": "去重 unique"}, {"text": "集合运算 & | - ^"}]},
    ]},
    {"text": "Day 4 函数与模块", "children": [
        {"text": "函数", "children": [
            {"text": "def"}, {"text": "参数 默认 关键字 可变"}, {"text": "return"}, {"text": "作用域 LEGB"},
        ]},
        {"text": "模块", "children": [{"text": "import"}, {"text": "from...import"}, {"text": "__name__"}]},
        {"text": "常用标准库", "children": [{"text": "random"}, {"text": "math"}, {"text": "datetime"}]},
    ]},
    {"text": "Day 5 字符串与文件", "children": [
        {"text": "字符串方法", "children": [
            {"text": "split join"}, {"text": "strip replace"}, {"text": "upper lower"},
        ]},
        {"text": "f-string 进阶", "children": [{"text": "格式化数字 :.2f"}, {"text": "对齐 :< :> :^"}, {"text": "千分位 :,"}]},
        {"text": "文件操作", "children": [
            {"text": "open()"}, {"text": "模式 r w a"}, {"text": "read write readlines"}, {"text": "with 语句"},
        ]},
    ]},
    {"text": "Day 6 异常与推导式", "children": [
        {"text": "异常处理", "children": [
            {"text": "try except finally"}, {"text": "常见异常 ValueError TypeError KeyError"}, {"text": "raise"},
        ]},
        {"text": "推导式", "children": [{"text": "list comprehension"}, {"text": "dict comprehension"}]},
        {"text": "面向对象入门", "children": [{"text": "class"}, {"text": "__init__"}, {"text": "self"}, {"text": "实例方法"}]},
    ]},
    {"text": "Day 7 综合项目 🎯", "children": [
        {"text": "命令行 CLI 工具", "children": [{"text": "argparse"}, {"text": "交互菜单"}]},
        {"text": "数据持久化", "children": [{"text": "JSON 读写"}, {"text": "json.dump json.load"}]},
        {"text": "模块化设计", "children": [{"text": "拆分文件"}, {"text": "__init__.py"}]},
        {"text": "项目打包", "children": [{"text": "requirements.txt"}]},
    ]},
])

# ============================================================
# 01 - Day 1：基础语法与数据类型
# ============================================================
save_mm("01-Day1-基础语法与数据类型.mm", "Day 1 基础语法与数据类型", [
    {"text": "环境准备", "children": [
        {"text": "Python 安装"},
        {"text": "VS Code / PyCharm"},
        {"text": "运行第一行代码 hello world"},
    ]},
    {"text": "变量", "children": [
        {"text": "赋值 ="},
        {"text": "命名规范 snake_case"},
        {"text": "不能以数字开头"},
        {"text": "区分大小写"},
        {"text": "动态类型"},
    ]},
    {"text": "数据类型", "children": [
        {"text": "int 整数", "children": [{"text": "a = 10"}, {"text": "无大小上限"}]},
        {"text": "float 浮点数", "children": [{"text": "b = 3.14"}, {"text": "科学计数法 1e-5"}]},
        {"text": "str 字符串", "children": [
            {"text": "单引号 ' '"}, {"text": '双引号 " "'}, {"text": "三引号 ''' ''' 多行"},
        ]},
        {"text": "bool 布尔值", "children": [{"text": "True"}, {"text": "False"}]},
        {"text": "type() 查看类型"},
    ]},
    {"text": "类型转换", "children": [
        {"text": 'int("10") → 10'},
        {"text": 'str(3.14) → "3.14"'},
        {"text": 'float("3.14") → 3.14'},
        {"text": "bool(0) → False"},
    ]},
    {"text": "输入输出", "children": [
        {"text": "print()", "children": [
            {"text": "sep 分隔符"}, {"text": "end 结束符"}, {"text": 'print(a, b, sep=",")'},
        ]},
        {"text": "input()", "children": [
            {"text": "永远返回 str"}, {"text": 'name = input("请输入: ")'},
        ]},
        {"text": "f-string", "children": [
            {"text": "f\"我的名字是{name}\""}, {"text": "f\"价格: {price:.2f}\""},
        ]},
    ]},
    {"text": "运算符", "children": [
        {"text": "算术运算符", "children": [
            {"text": "+ 加"}, {"text": "- 减"}, {"text": "* 乘"}, {"text": "/ 除 得 float"},
            {"text": "// 整除"}, {"text": "% 取余"}, {"text": "** 幂"},
        ]},
        {"text": "比较运算符", "children": [
            {"text": "== 等于"}, {"text": "!= 不等于"}, {"text": "> 大于"},
            {"text": "< 小于"}, {"text": ">= 大于等于"}, {"text": "<= 小于等于"},
        ]},
    ]},
])

# ============================================================
# 02 - Day 2：控制流
# ============================================================
save_mm("02-Day2-控制流.mm", "Day 2 控制流", [
    {"text": "条件判断 if", "children": [
        {"text": "if 条件:"}, {"text": "    缩进代码块"}, {"text": "elif 条件:", "children": [{"text": "多重判断"}]},
        {"text": "else:", "children": [{"text": "兜底分支"}]},
        {"text": "嵌套 if"}, {"text": "pass 占位符"},
    ]},
    {"text": "逻辑运算", "children": [
        {"text": "and", "children": [{"text": "全 True 才 True"}, {"text": "短路求值"}]},
        {"text": "or", "children": [{"text": "有一个 True 就 True"}, {"text": "短路求值"}]},
        {"text": "not", "children": [{"text": "取反"}, {"text": "not True → False"}]},
    ]},
    {"text": "循环 for", "children": [
        {"text": "for item in sequence:", "children": [
            {"text": "遍历 list"}, {"text": 'for c in "hello"'}, {"text": "遍历 dict"},
        ]},
        {"text": "range()", "children": [
            {"text": "range(n) 0 到 n-1"}, {"text": "range(start, stop)"}, {"text": "range(start, stop, step)"},
        ]},
        {"text": "enumerate()", "children": [{"text": "同时拿索引与值"}]},
        {"text": "zip()", "children": [{"text": "并行遍历多个序列"}]},
    ]},
    {"text": "循环 while", "children": [
        {"text": "while 条件:"}, {"text": "条件为 True 时重复"}, {"text": "小心死循环"}, {"text": "循环变量更新"},
    ]},
    {"text": "循环控制", "children": [
        {"text": "break", "children": [{"text": "终止整个循环"}]},
        {"text": "continue", "children": [{"text": "跳过本次，继续下一次"}]},
        {"text": "for...else", "children": [{"text": "循环正常结束才执行 else"}]},
    ]},
])

# ============================================================
# 03 - Day 3：数据结构 ⭐
# ============================================================
save_mm("03-Day3-核心数据结构.mm", "Day 3 数据结构 ⭐", [
    {"text": "list 列表", "children": [
        {"text": "创建", "children": [{"text": "[]"}, {"text": "list()"}]},
        {"text": "索引", "children": [{"text": "正向 从 0 开始"}, {"text": "反向 从 -1 开始"}]},
        {"text": "切片 slicing", "children": [{"text": "[start:stop:step]"}, {"text": "[::-1] 反转"}]},
        {"text": "增", "children": [
            {"text": "append(x) 末尾追加"}, {"text": "insert(i, x) 指定位置"}, {"text": "extend(iterable) 合并"},
        ]},
        {"text": "删", "children": [
            {"text": "pop(i) 按索引删除并返回"}, {"text": "remove(x) 按值删除"}, {"text": "del lst[i]"},
        ]},
        {"text": "改", "children": [{"text": "lst[i] = new_value"}]},
        {"text": "查", "children": [
            {"text": "in 判断存在"}, {"text": "index(x) 查找位置"}, {"text": "count(x) 计数"},
        ]},
        {"text": "排序", "children": [
            {"text": "lst.sort() 原地排序"}, {"text": "sorted(lst) 返回新列表"},
            {"text": "reverse=True 降序"}, {"text": "key 参数 自定义排序"},
        ]},
    ]},
    {"text": "dict 字典", "children": [
        {"text": "创建", "children": [{"text": "{}"}, {"text": "dict()"}]},
        {"text": "键值对", "children": [{"text": "key: value"}, {"text": "key 必须不可变类型"}]},
        {"text": "访问", "children": [{"text": 'd["key"]'}, {"text": "d.get(key, default)"}]},
        {"text": "增改", "children": [{"text": 'd["new_key"] = value'}]},
        {"text": "删", "children": [{"text": "pop(key)"}, {"text": "del d[key]"}]},
        {"text": "遍历", "children": [
            {"text": "for k in d.keys()"}, {"text": "for v in d.values()"}, {"text": "for k, v in d.items()"},
        ]},
    ]},
    {"text": "tuple 元组", "children": [
        {"text": "创建", "children": [{"text": "()"}, {"text": "tuple()"}, {"text": "单元素 (x,)"}]},
        {"text": "不可变 immutable", "children": [{"text": "不能修改"}, {"text": "可以包含可变元素"}]},
        {"text": "解包 unpacking", "children": [
            {"text": "a, b = (1, 2)"}, {"text": "a, *rest = (1, 2, 3)"},
        ]},
    ]},
    {"text": "set 集合", "children": [
        {"text": "创建", "children": [{"text": "set()"}, {"text": "{1, 2, 3}"}]},
        {"text": "去重", "children": [{"text": "自动去重"}]},
        {"text": "增删", "children": [
            {"text": "add(x)"}, {"text": "remove(x)"}, {"text": "discard(x) 不报错"},
        ]},
        {"text": "集合运算", "children": [
            {"text": "交集 &"}, {"text": "并集 |"}, {"text": "差集 -"}, {"text": "对称差 ^"},
        ]},
    ]},
])

# ============================================================
# 04 - Day 4：函数与模块
# ============================================================
save_mm("04-Day4-函数与模块.mm", "Day 4 函数与模块", [
    {"text": "函数 function", "children": [
        {"text": "定义 def", "children": [
            {"text": "def 函数名():"}, {"text": "缩进代码块"}, {"text": "docstring 文档字符串"},
        ]},
        {"text": "参数", "children": [
            {"text": "位置参数"}, {"text": "默认参数 def f(a, b=10)"},
            {"text": "关键字参数 f(a=1, b=2)"}, {"text": "可变参数 *args 元组"},
            {"text": "关键字可变参数 **kwargs 字典"},
        ]},
        {"text": "返回值 return", "children": [
            {"text": "单个值"}, {"text": "多个值 自动打包为 tuple"}, {"text": "无 return → None"},
        ]},
        {"text": "作用域 LEGB", "children": [
            {"text": "Local 局部"}, {"text": "Enclosing 闭包"}, {"text": "Global 全局"},
            {"text": "Built-in 内置"}, {"text": "global 关键字"},
        ]},
    ]},
    {"text": "模块 module", "children": [
        {"text": "导入方式", "children": [
            {"text": "import 模块名"}, {"text": "import 模块名 as 别名"},
            {"text": "from 模块 import 函数"}, {"text": "from 模块 import *"},
        ]},
        {"text": "模块搜索路径", "children": [{"text": "sys.path"}]},
        {"text": "常用技巧", "children": [
            {"text": 'if __name__ == "__main__":'}, {"text": "dir() 查看模块内容"},
        ]},
    ]},
    {"text": "常用标准库", "children": [
        {"text": "random / randint / choice / shuffle / random()"},
        {"text": "math / sqrt / pi / ceil / floor"},
        {"text": "datetime / now / timedelta / strftime / strptime"},
    ]},
])

# ============================================================
# 05 - Day 5：字符串与文件
# ============================================================
save_mm("05-Day5-字符串处理与文件IO.mm", "Day 5 字符串与文件", [
    {"text": "字符串方法", "children": [
        {"text": "分割与合并", "children": [
            {"text": "s.split(sep) 分割为列表"}, {"text": "s.splitlines() 按行分割"},
            {"text": "sep.join(iterable) 合并"},
        ]},
        {"text": "清理", "children": [
            {"text": "s.strip() 去两端空白"}, {"text": "s.lstrip() 去左侧"},
            {"text": "s.rstrip() 去右侧"}, {"text": "s.replace(old, new) 替换"},
        ]},
        {"text": "大小写", "children": [
            {"text": "s.upper() 全大写"}, {"text": "s.lower() 全小写"},
            {"text": "s.title() 首字母大写"}, {"text": "s.capitalize() 首字符大写"},
        ]},
        {"text": "查找与判断", "children": [
            {"text": "s.find(sub) 找子串"}, {"text": "s.startswith(prefix)"},
            {"text": "s.endswith(suffix)"}, {"text": "s.count(sub) 计数"},
        ]},
        {"text": "判断方法", "children": [
            {"text": "s.isdigit()"}, {"text": "s.isalpha()"}, {"text": "s.isalnum()"},
        ]},
    ]},
    {"text": "f-string 进阶", "children": [
        {"text": "格式化数字", "children": [
            {"text": "{num:.2f} 保留两位小数"}, {"text": "{num:.0%} 百分比"}, {"text": "{num:.2e} 科学计数"},
        ]},
        {"text": "对齐与填充", "children": [
            {"text": "{text:<10} 左对齐"}, {"text": "{text:>10} 右对齐"},
            {"text": "{text:^10} 居中对齐"}, {"text": "{text:*^10} 填充字符"},
        ]},
        {"text": "千分位与进制", "children": [
            {"text": "{num:,} 千分位"}, {"text": "{num:b} 二进制"}, {"text": "{num:x} 十六进制"},
        ]},
    ]},
    {"text": "文件操作", "children": [
        {"text": "打开文件", "children": [
            {"text": "f = open(path, mode)"}, {"text": "模式 r 读 w 写 a 追加"}, {"text": '编码 encoding="utf-8"'},
        ]},
        {"text": "读取", "children": [
            {"text": "f.read() 读全部"}, {"text": "f.readline() 读一行"},
            {"text": "f.readlines() 读所有行"}, {"text": "for line in f 逐行读取"},
        ]},
        {"text": "写入", "children": [
            {"text": "f.write(text)"}, {"text": "f.writelines(lines)"},
        ]},
        {"text": "with 语句", "children": [
            {"text": "with open() as f:"}, {"text": "自动关闭文件"}, {"text": "推荐始终使用 with"},
        ]},
        {"text": "pathlib", "children": [
            {"text": "Path 对象"}, {"text": "路径拼接 /"}, {"text": ".read_text()"},
        ]},
    ]},
])

# ============================================================
# 06 - Day 6：异常处理与推导式
# ============================================================
save_mm("06-Day6-异常处理与推导式.mm", "Day 6 异常处理与推导式", [
    {"text": "异常处理", "children": [
        {"text": "try...except", "children": [
            {"text": "try 包裹可能出错的代码"}, {"text": "except 捕获指定异常"},
            {"text": "多个 except 分支"}, {"text": "except Exception as e"},
        ]},
        {"text": "finally", "children": [{"text": "无论是否异常都执行"}, {"text": "常用于释放资源"}]},
        {"text": "else", "children": [{"text": "try 无异常时执行"}]},
        {"text": "常见异常", "children": [
            {"text": "ValueError 值错误"}, {"text": "TypeError 类型错误"},
            {"text": "KeyError 键不存在"}, {"text": "IndexError 索引越界"},
            {"text": "FileNotFoundError 文件未找到"}, {"text": "ZeroDivisionError 除以零"},
        ]},
        {"text": "raise", "children": [
            {"text": "手动抛出异常"}, {"text": 'raise ValueError("原因")'},
        ]},
        {"text": "自定义异常", "children": [{"text": "class MyError(Exception)"}]},
    ]},
    {"text": "list comprehension", "children": [
        {"text": "基本语法", "children": [
            {"text": "[表达式 for item in 可迭代对象]"}, {"text": "[x*2 for x in range(10)]"},
        ]},
        {"text": "带条件过滤", "children": [{"text": "[x for x in lst if x > 0]"}]},
        {"text": "嵌套", "children": [{"text": "[(x, y) for x in a for y in b]"}]},
    ]},
    {"text": "dict comprehension", "children": [
        {"text": "基本语法", "children": [
            {"text": "{k: v for item in seq}"}, {"text": "{x: x**2 for x in range(5)}"},
        ]},
        {"text": "带条件", "children": [{"text": "{k: v for k, v in d.items() if v > 0}"}]},
        {"text": "键值互换", "children": [{"text": "{v: k for k, v in d.items()}"}]},
    ]},
    {"text": "面向对象入门", "children": [
        {"text": "类与对象", "children": [
            {"text": "class 类名:"}, {"text": "类名用 PascalCase"},
        ]},
        {"text": "构造方法", "children": [
            {"text": "def __init__(self, ...):"}, {"text": "self.属性 = 参数"},
        ]},
        {"text": "self", "children": [{"text": "代表实例本身"}, {"text": "必须显式写"}]},
        {"text": "实例方法", "children": [
            {"text": "def method(self, ...):"}, {"text": "必须带 self 参数"},
        ]},
        {"text": "创建实例", "children": [
            {"text": "obj = ClassName(args)"}, {"text": "obj.method()"},
        ]},
    ]},
])

# ============================================================
# 07 - Day 7：综合实战项目 🎯
# ============================================================
save_mm("07-Day7-综合实战项目.mm", "Day 7 综合实战项目 🎯", [
    {"text": "命令行工具 CLI", "children": [
        {"text": "argparse", "children": [
            {"text": "ArgumentParser"}, {"text": "add_argument()"}, {"text": "parse_args()"},
        ]},
        {"text": "交互菜单", "children": [
            {"text": "while True 循环菜单"}, {"text": "数字选择功能"}, {"text": "input() 读取选项"},
        ]},
        {"text": "sys.argv", "children": [{"text": "简单参数获取"}]},
    ]},
    {"text": "数据持久化", "children": [
        {"text": "JSON", "children": [
            {"text": "基本用法", "children": [
                {"text": "json.dumps() dict -> str"}, {"text": "json.loads() str -> dict"},
                {"text": "indent=2 美化输出"}, {"text": "ensure_ascii=False"},
            ]},
            {"text": "文件读写", "children": [
                {"text": "json.dump(data, f)"}, {"text": "data = json.load(f)"},
            ]},
            {"text": "适用场景", "children": [
                {"text": "配置文件 config.json"}, {"text": "数据存储"}, {"text": "简单数据库"},
            ]},
        ]},
    ]},
    {"text": "模块化设计", "children": [
        {"text": "代码拆分", "children": [
            {"text": "主程序 main.py"}, {"text": "工具函数 utils.py"}, {"text": "数据模型 models.py"},
        ]},
        {"text": "包 package", "children": [
            {"text": "文件夹 + __init__.py"}, {"text": "from package import module"},
        ]},
        {"text": 'if __name__ == "__main__":', "children": [{"text": "入口判断"}]},
    ]},
    {"text": "项目打包", "children": [
        {"text": "requirements.txt", "children": [
            {"text": "pip freeze > requirements.txt"}, {"text": "pip install -r requirements.txt"},
        ]},
        {"text": ".gitignore", "children": [
            {"text": "__pycache__/"}, {"text": "*.pyc"}, {"text": "venv/"},
        ]},
    ]},
    {"text": "项目示例：命令行备忘录", "children": [
        {"text": "功能：添加/查看/删除记录，保存到 JSON"},
        {"text": "文件组织", "children": [
            {"text": "memo/"}, {"text": "  __init__.py"}, {"text": "  cli.py"},
            {"text": "  storage.py"}, {"text": "  models.py"}, {"text": "main.py"},
        ]},
    ]},
])

print("\n🎉 全部完成！共生成 8 个 .mm 文件，可用 XMind 直接打开。")
print(f"📁 输出目录: {OUTPUT_DIR}")
