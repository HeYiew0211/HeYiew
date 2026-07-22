# Day 4：函数与模块

> **预计学习时间：1.5 ~ 2 小时**

---

## 一、今日目标

- 会用 `def` 定义自己的函数
- 理解位置参数和默认参数的区别
- 理解局部变量和全局变量的作用域
- 掌握 `import` 的三种写法
- 会使用 `random`, `math`, `datetime` 常用标准库

---

## 二、知识点讲解

### 2.1 为什么需要函数？

函数是一段**有名字的、可重复使用的代码块**。它解决三个问题：

1. **避免重复** —— 同样的代码写一次，多次调用
2. **逻辑封装** —— 把复杂操作包装成简单接口
3. **易于维护** —— 修改逻辑只需改一处

```python
# 没有函数时：每次都要重复写
print("=== 欢迎光临 ===")
print("张三")
print("=== 欢迎光临 ===")
print("李四")
print("=== 欢迎光临 ===")
print("王五")

# 有函数后：定义一次，反复调用
def greet(name):
    """打印欢迎信息（这是 docstring，用来描述函数做什么）"""
    print("=== 欢迎光临 ===")
    print(name)

greet("张三")
greet("李四")
greet("王五")
```

---

### 2.2 定义函数与返回值

#### 基本语法

```python
def 函数名(参数1, 参数2, ...):
    """文档字符串（可选，但推荐写）"""
    # 函数体（缩进 4 空格）
    return 结果  # 可选，没有 return 时返回 None
```

#### return 返回值

```python
def add(a, b):
    """返回两个数的和"""
    return a + b

result = add(3, 5)
print(result)  # 8

# 函数可以返回多个值（实际上返回的是 tuple）
def divide_and_remainder(a, b):
    """返回商和余数"""
    return a // b, a % b

quotient, remainder = divide_and_remainder(10, 3)
print(f"商={quotient}, 余数={remainder}")  # 商=3, 余数=1

# 没有 return 的函数返回 None
def say_hello():
    print("你好")

result = say_hello()  # 输出：你好
print(result)         # None（因为函数没有 return）
```

#### return 后的代码不会执行

```python
def demo():
    print("这行会执行")
    return "结束了"
    print("这行永远不会执行")  # return 后面的代码是"死代码"

demo()
# 输出：
# 这行会执行
```

---

### 2.3 参数类型

#### 位置参数（Positional Arguments）

最常见的参数方式：按**位置顺序**一一对应。

```python
def describe_person(name, age, city):
    print(f"{name}，{age} 岁，来自 {city}")

# 参数按位置传递
describe_person("小明", 18, "上海")
# 小明，18 岁，来自 上海
```

#### 默认参数（Default Arguments）

给参数一个默认值，调用时可以不传。**默认参数必须放在非默认参数后面。**

```python
def describe_person(name, age, city="北京"):
    print(f"{name}，{age} 岁，来自 {city}")

describe_person("小明", 18)           # city 用默认值 "北京"
describe_person("小红", 20, "上海")   # city 被覆盖为 "上海"

# ❌ 错误：默认参数不能在位置参数前面
# def greet(msg="你好", name):  # SyntaxError
#     print(f"{msg}，{name}")

# ✅ 正确
def greet(name, msg="你好"):
    print(f"{msg}，{name}")
```

#### 关键字参数（Keyword Arguments）

调用时明确指出参数名，可以不按顺序。

```python
def order(entree, drink, dessert):
    print(f"主菜：{entree}，饮品：{drink}，甜点：{dessert}")

# 按参数名传递，顺序无所谓
order(drink="可乐", dessert="冰淇淋", entree="牛排")
# 主菜：牛排，饮品：可乐，甜点：冰淇淋

# 可以混合使用，但位置参数必须在前
order("牛排", dessert="蛋糕", drink="橙汁")
```

#### 危险的默认参数：不要用可变对象做默认值

```python
# ❌ 危险写法：用 list 做默认参数
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_item("苹果"))   # ['苹果']
print(add_item("香蕉"))   # ['苹果', '香蕉'] ← 咦，为什么苹果还在？！
# 原因：默认参数只在函数定义时计算一次，多次调用共享同一个 list

# ✅ 正确写法
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []   # 每次调用都创建新 list
    shopping_list.append(item)
    return shopping_list

print(add_item("苹果"))   # ['苹果']
print(add_item("香蕉"))   # ['香蕉'] ← 正常了
```

---

### 2.4 变量作用域

#### 局部变量 vs 全局变量

```python
total = 0  # 全局变量：在函数外面定义

def add_score(score):
    total = total + score  # ❌ 错误！这样赋值会在函数内创建新的局部变量 total
    # UnboundLocalError: 局部变量 total 在赋值前被引用
    return total
```

```python
total = 0  # 全局变量

def add_score(score):
    global total          # 声明要使用全局变量
    total = total + score
    return total

print(add_score(10))  # 10
print(total)          # 10（全局变量也被修改了）
```

**最佳实践：尽量避免使用 `global`。用参数传递和返回值代替。**

```python
# ✅ 更好的写法：不依赖全局变量
def add_score(current_total, score):
    return current_total + score

total = 0
total = add_score(total, 10)  # 把结果赋回给 total
print(total)  # 10
```

#### 作用域规则总结

```python
x = "全局"

def demo():
    x = "局部"       # 函数内创建了一个同名的局部变量，不会影响全局的 x
    print(x)         # 局部

demo()
print(x)             # 全局（函数内部的 x 和外面的 x 是两个不同的变量）

# 规则：LEGB 查找顺序
# L - Local（函数内）
# E - Enclosing（外层函数）
# G - Global（模块级别）
# B - Built-in（内置）
```

---

### 2.5 模块（Module）

模块就是一个 `.py` 文件，里面定义了一些函数和变量供你使用。

#### import 的三种方式

```python
# 方式 1：导入整个模块（推荐，清晰知道函数来自哪个模块）
import random

result = random.randint(1, 10)  # 模块名.函数名
print(result)

# 方式 2：从模块中导入特定函数（省去模块名前缀）
from math import sqrt, ceil

print(sqrt(16))  # 4.0   不需要写 math.sqrt
print(ceil(3.1)) # 4

# 方式 3：给模块取别名（名字太长时用）
import datetime as dt

now = dt.datetime.now()
print(now)

# ❌ 不推荐：导入所有内容（污染命名空间，可能冲突）
# from random import *
```

---

### 2.6 常用标准库

Python 自带了许多实用的模块，不需要安装就能用。

#### random —— 随机数

```python
import random

# randint(a, b)：返回 a 到 b 之间的随机整数（包含 a 和 b）
dice = random.randint(1, 6)
print(f"掷骰子：{dice}")

# random()：返回 0.0 到 1.0 之间的随机浮点数
print(random.random())  # 如 0.7234

# choice(seq)：从序列中随机选一个元素
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
lucky_fruit = random.choice(fruits)
print(f"今天的水果是：{lucky_fruit}")

# shuffle(list)：随机打乱 list（原地修改）
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print(f"洗牌后：{cards}")

# sample(seq, k)：从序列中随机取 k 个不重复的元素
winners = random.sample(["A", "B", "C", "D", "E"], 3)
print(f"中奖者：{winners}")
```

#### math —— 数学函数

```python
import math

print(math.sqrt(25))      # 5.0   平方根
print(math.ceil(3.1))     # 4     向上取整
print(math.floor(3.9))    # 3     向下取整
print(math.pi)            # 3.141592653589793  圆周率
print(math.fabs(-10))     # 10.0  绝对值（浮点数）
print(math.factorial(5))  # 120   阶乘 5! = 5×4×3×2×1
print(math.pow(2, 3))     # 8.0   幂运算（等价于 2**3）
```

#### datetime —— 日期时间

```python
import datetime as dt

# 获取当前时间
now = dt.datetime.now()
print(f"现在是：{now}")
print(f"年：{now.year}，月：{now.month}，日：{now.day}")
print(f"时：{now.hour}，分：{now.minute}，秒：{now.second}")

# 创建指定日期
birthday = dt.datetime(2000, 1, 15)
print(f"生日：{birthday}")

# 时间计算：timedelta（时间差）
today = dt.datetime.now()
one_week_later = today + dt.timedelta(weeks=1)
three_days_ago = today - dt.timedelta(days=3)
print(f"一周后：{one_week_later}")
print(f"三天前：{three_days_ago}")

# 计算时间差
diff = today - birthday
print(f"出生了 {diff.days} 天")

# 格式化输出
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2026-01-15 14:30:00
```

#### datetime 格式化常用代码

| 代码 | 含义 | 示例 |
|------|------|------|
| `%Y` | 四位年份 | 2026 |
| `%m` | 两位月份 | 01 |
| `%d` | 两位日期 | 15 |
| `%H` | 24小时制小时 | 14 |
| `%M` | 分钟 | 30 |
| `%S` | 秒 | 00 |

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| 默认参数用可变对象 | `def f(lst=[])` 有陷阱，应用 `lst=None` |
| 函数内给全局变量赋值 | 需要用 `global` 声明，否则创建局部变量（UnboundLocalError） |
| 忘记写 `return` | 函数返回 `None`，接收返回值时要注意 |
| `return` 后面的代码不执行 | 不要再在 `return` 后写逻辑 |
| `import` 的文件名冲突 | 不要让自己的 `.py` 文件与标准库重名 |
| 混淆 `math.ceil` 和 `math.floor` | ceil = 天花板（向上），floor = 地板（向下） |

---

## 四、今日题目链接

1. 写一个函数 `is_prime(n)` 判断 n 是否为质数，返回 True 或 False。然后用 for 循环打印 1 到 100 之间的所有质数
2. 写一个函数 `calculator(a, b, operator)`，根据 operator 的值（"+", "-", "*", "/"）返回计算结果，除以 0 时返回错误提示
3. 用 `random` 模块写一个猜数字游戏：随机生成 1~100 的整数，用户有 7 次机会猜，每次提示"大了"或"小了"
4. 写一个函数计算两个日期之间相差多少天

---

## 五、检查清单

- [ ] 我会用 `def` 定义函数，知道 `return` 的作用和位置
- [ ] 我理解位置参数和默认参数的区别，知道默认参数必须放在后面
- [ ] 我知道默认参数不要用 list/dict 等可变对象
- [ ] 我理解局部变量和全局变量的作用域差异
- [ ] 我会用 `import` 的三种方式导入模块
- [ ] 我至少用过 `random.randint`、`random.choice`
- [ ] 我至少用过 `math.sqrt`、`math.ceil`、`math.floor`
- [ ] 我能用 `datetime` 获取当前时间、计算时间差
