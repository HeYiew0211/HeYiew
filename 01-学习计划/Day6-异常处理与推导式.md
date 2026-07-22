# Day 6：异常处理与推导式

> **预计学习时间：1.5 ~ 2 小时**

---

## 一、今日目标

- 理解什么是异常，为什么需要处理异常
- 会用 `try / except / finally` 捕获和处理异常
- 掌握 list comprehension 写出简洁优雅的代码
- 了解 dict comprehension
- 认识 class 的基本概念：类、对象、`__init__`、`self`

---

## 二、知识点讲解

### 2.1 为什么需要异常处理？

程序运行时如果遇到错误，默认会**崩溃并打印一大段红色错误信息**。异常处理让你能够：

1. **优雅地处理错误**而不让程序崩溃
2. **给用户友好的提示**而不是技术错误信息
3. **在出错时做清理工作**（如关闭文件、保存数据）

```python
# 没有异常处理：用户输入非数字就崩溃
# age = int(input("请输入年龄："))  # 输入 "abc" → 程序崩溃

# 有异常处理：优雅处理
try:
    age = int(input("请输入年龄："))
    print(f"你明年 {age + 1} 岁")
except ValueError:
    print("输入的不是有效数字，请重新运行程序")
```

---

### 2.2 try / except / finally 结构

#### 2.2.1 基本语法

```python
try:
    # 尝试执行的代码（可能出错的代码）
    result = 10 / 0
except ZeroDivisionError:
    # 捕获到 ZeroDivisionError 时执行
    print("不能除以零！")
finally:
    # 无论是否发生异常，都会执行（通常用来做清理工作）
    print("程序结束")
```

#### 2.2.2 捕获异常并获取详细信息

```python
try:
    num = int("abc")
except ValueError as e:          # as e 捕获异常对象
    print(f"转换失败：{e}")       # 输出：转换失败：invalid literal for int() with base 10: 'abc'
```

#### 2.2.3 捕获多个异常

```python
# 方式一：多个 except 分支
try:
    data = [10, 20, 30]
    index = int(input("请输入索引："))
    value = data[index]
    print(f"值是：{value}")
except ValueError:
    print("请输入一个数字！")
except IndexError:
    print("索引超出范围！")

# 方式二：一个 except 捕获多个异常类型
try:
    num = int(input("输入一个数字："))
    result = 100 / num
    print(f"100 / {num} = {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"出错了：{e}")
```

#### 2.2.4 else 子句

`else` 在**没有发生异常时**执行。

```python
try:
    num = int(input("请输入一个数字："))
except ValueError:
    print("这不是数字！")
else:
    # 只有在没有异常时才执行
    print(f"你输入的数字是 {num}，它的平方是 {num**2}")
```

#### 2.2.5 完整结构

```python
try:
    # 可能发生异常的代码
    pass
except SomeError:
    # 处理特定异常
    pass
except AnotherError as e:
    # 处理另一个异常，并获取信息
    pass
else:
    # 没有异常发生时执行
    pass
finally:
    # 无论是否异常都执行（清理工作）
    pass
```

**执行顺序总结：**
- 有异常：`try → except → finally`
- 无异常：`try → else → finally`

---

### 2.3 常见异常类型

| 异常类型 | 何时发生 | 示例 |
|----------|----------|------|
| `ValueError` | 类型转换失败 | `int("abc")` |
| `TypeError` | 操作类型不对 | `"hello" + 5` |
| `IndexError` | list 索引越界 | `[1,2,3][10]` |
| `KeyError` | dict 中 key 不存在 | `d = {}; d["x"]` |
| `FileNotFoundError` | 文件不存在 | `open("不存在.txt")` |
| `ZeroDivisionError` | 除以 0 | `1 / 0` |
| `NameError` | 使用了未定义的变量 | `print(undefined_var)` |

```python
# 各种异常的示例
def demo_exceptions():
    # FileNotFoundError
    try:
        with open("不存在的文件.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("文件不存在，请检查路径")

    # KeyError
    info = {"name": "张三"}
    try:
        print(info["email"])
    except KeyError:
        print("字典中没有 'email' 这个 key，使用 get() 更安全")

    # TypeError
    try:
        result = "价格：" + 100  # 字符串不能直接加数字
    except TypeError:
        print("类型不匹配，应该先转换为字符串")
```

---

### 2.4 list comprehension（列表推导式）

list comprehension 是用一行代码创建新 list 的语法，比传统的 for 循环更简洁。

#### 2.4.1 基本语法

```python
# 语法：[表达式 for 变量 in 序列]

# 传统 for 循环
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# 用 list comprehension：一行搞定
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

#### 2.4.2 带条件过滤

```python
# 语法：[表达式 for 变量 in 序列 if 条件]

# 只取偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 过滤并转换：取偶数，求平方
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

#### 2.4.3 更多实用例子

```python
# 字符串处理
names = ["张三", "李四", "王五", "赵六"]
upper_names = [name.upper() for name in names]

# 筛选长度大于等于 3 的单词
words = ["a", "ab", "abc", "abcd", "abcde"]
long_words = [w for w in words if len(w) >= 3]

# 嵌套循环（展平二维 list）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# if-else 表达式（注意：这里 if-else 在 for 前面）
numbers = [1, 2, 3, 4, 5]
labels = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']
```

#### 2.4.4 什么时候用/不用 comprehension

| 适合用 | 不适合用 |
|--------|----------|
| 简单的映射（转换每个元素） | 逻辑复杂，有多层嵌套的条件 |
| 简单的过滤 | 超过一行的 comprehension |
| 结果仍然是可读的 | 需要调试、打断点的时候 |

**原则：代码是写给人看的。如果 comprehension 让人费解，就拆成普通 for 循环。**

---

### 2.5 dict comprehension（字典推导式）

```python
# 语法：{key表达式: value表达式 for 变量 in 序列}

# 基本用法：把 list 转成 dict
fruits = ["苹果", "香蕉", "橘子"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)  # {'苹果': 2, '香蕉': 2, '橘子': 2}

# 带条件过滤
scores = {"张三": 85, "李四": 92, "王五": 58, "赵六": 73}
passed = {name: score for name, score in scores.items() if score >= 60}
print(passed)  # {'张三': 85, '李四': 92, '赵六': 73}

# 交换 key 和 value（前提是 value 不重复）
code_to_name = {"CN": "中国", "US": "美国", "JP": "日本"}
name_to_code = {v: k for k, v in code_to_name.items()}
print(name_to_code)  # {'中国': 'CN', '美国': 'US', '日本': 'JP'}

# 用 comprehension 创建计数器
text = "hello world"
char_count = {ch: text.count(ch) for ch in set(text) if ch != " "}
print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
```

---

### 2.6 class 入门 —— 面向对象初体验

class 是把**数据（属性）**和**操作数据的方法（函数）**打包在一起的方式。今天只学最基础的概念。

#### 2.6.1 定义一个简单的 class

```python
# 定义一个"学生"类
class Student:
    """学生类"""   # docstring

    # __init__ 是构造方法，在创建对象时自动调用
    # self 代表"当前这个对象本身"（必须是第一个参数）
    def __init__(self, name, age, score):
        self.name = name    # 把参数 name 存到对象的 name 属性里
        self.age = age
        self.score = score

    # 定义一个方法（就是属于这个 class 的函数）
    def introduce(self):
        """自我介绍"""
        return f"我叫{self.name}，{self.age}岁，成绩{self.score}分"

    def is_passed(self):
        """判断是否及格"""
        return self.score >= 60


# 创建对象（实例化）
s1 = Student("张三", 18, 85)   # 自动调用 __init__
s2 = Student("李四", 20, 55)

# 访问属性
print(s1.name)          # 张三
print(s1.score)         # 85

# 调用方法
print(s1.introduce())   # 我叫张三，18岁，成绩85分
print(s1.is_passed())   # True
print(s2.is_passed())   # False
```

#### 2.6.2 self 的含义

`self` 是 Python 的约定（不是关键字），它代表**调用方法的那个具体对象**。

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        # self.name 指的是"当前这只狗"的名字
        print(f"{self.name}：汪汪！")

dog1 = Dog("大黄")
dog2 = Dog("小白")

dog1.bark()  # self = dog1，所以 self.name = "大黄"  → 大黄：汪汪！
dog2.bark()  # self = dog2，所以 self.name = "小白"  → 小白：汪汪！
```

#### 2.6.3 为什么要学 class？

| 概念 | 比喻 |
|------|------|
| class（类） | 模具/蓝图 |
| object / instance（对象/实例） | 模具做出来的产品 |
| attribute（属性） | 产品的特征（颜色、尺寸） |
| method（方法） | 产品能做的事情（开关、播放） |

```python
# 一个更实际的例子：Contact 类
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        """将联系人信息转换为 dict，方便保存"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def __str__(self):
        """返回可读的字符串表示，用于 print()"""
        return f"{self.name} | {self.phone} | {self.email}"

# 使用
c = Contact("张三", "13800138000", "zhangsan@example.com")
print(c)               # 张三 | 13800138000 | zhangsan@example.com
print(c.to_dict())     # {'name': '张三', 'phone': '13800138000', 'email': 'zhangsan@example.com'}
```

> **注意：** 今天只要求理解 class 的基本概念。明天的实战项目中我们会进一步使用 class。

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| 捕获过于宽泛的异常 | `except Exception` 或 `except:` 会掩盖真实 bug，应捕获具体类型 |
| except 后什么都不做 | `except: pass` 是调试噩梦，至少要打印日志 |
| comprehension 中变量泄漏 | Python 3.8 之前 comprehension 中的变量会泄漏到外部作用域 |
| 忘记 `self` 参数 | 类中定义方法时**第一个参数必须是 self**，调用时不用传 |
| `__init__` 拼写错误 | 是双下划线开头和结尾（dunder init），不是单下划线 |
| 混淆类属性和实例属性 | 在 `__init__` 外定义的属性是类属性，被所有实例共享 |

---

## 四、今日题目链接

1. 写一个程序，让用户输入两个数字并做除法，用 try/except 处理：输入不是数字（ValueError）、除数为 0（ZeroDivisionError）
2. 有一个数字 list = `[3, 7, -2, 0, 9, -5, 4]`，用 list comprehension：取所有正数、取所有正数的平方、用 if-else 生成一个 ["正", "负", "零"] 的标签 list
3. 有一个字符串列表 `["hello", "world", "python", "code"]`，用 dict comprehension 创建一个 `{单词: 单词长度}` 的字典，只包含长度大于 4 的单词
4. 定义一个 `Book` class，包含属性：书名、作者、价格，方法：`info()` 返回书籍简介，创建 3 本书并用 for 循环打印它们的简介

---

## 五、检查清单

- [ ] 我理解 `try / except / else / finally` 的完整结构
- [ ] 我至少认识 ValueError, TypeError, KeyError, IndexError, FileNotFoundError
- [ ] 我会用 `except SomeError as e:` 获取异常详情
- [ ] 我能区分"只过滤"的 comprehension 和"带 if-else 映射"的 comprehension
- [ ] 我会用 list comprehension 替代简单的 for 循环
- [ ] 我会写 dict comprehension 创建字典
- [ ] 我能用 `class` 定义一个类，写出 `__init__` 构造方法
- [ ] 我理解 `self` 代表实例本身
- [ ] 我能创建类的实例并访问属性和方法
