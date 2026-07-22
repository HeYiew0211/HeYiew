# Day 1：基础语法与数据类型

> **预计学习时间：1.5 ~ 2 小时**

---

## 一、今日目标

- 能在自己的电脑上运行 Python 代码
- 理解变量和基本数据类型（int, float, str, bool）
- 会使用 `print()` 和 `input()` 做输入输出
- 掌握常用运算符和比较运算符
- 能写一个简单的交互式小程序

---

## 二、知识点讲解

### 2.1 Python 安装验证

打开终端（macOS 用"终端"，Windows 用 PowerShell 或 CMD），输入：

```bash
python3 --version
```

如果看到类似 `Python 3.x.x` 的输出，说明安装成功。

### 2.2 VS Code 使用

推荐安装 VS Code + Python 扩展：
1. 下载 [VS Code](https://code.visualstudio.com/)
2. 安装 Python 扩展（搜索 "Python"，作者 Microsoft）
3. 新建 `.py` 文件，点击右上角 ▶ 运行

**小技巧：** 在 VS Code 中按 `Ctrl + `` ` 可以打开内置终端。

---

### 2.3 变量赋值与命名规范

变量就是一个有名字的"盒子"，用来存放数据。

```python
# 变量赋值：把右边的值放进左边的变量里
name = "张三"        # 字符串用引号包裹
age = 25            # 整数直接写数字
height = 1.75       # 小数用小数点
is_student = True   # 布尔值：True 或 False（首字母大写）

print(name)         # 输出：张三
```

**命名规范（snake_case）：**
- 只使用小写字母、数字、下划线
- 单词之间用下划线连接
- 见名知意（如 `user_age` 比 `ua` 好）

```python
# ✅ 好的命名
user_name = "李四"
max_score = 100
total_price = 99.5

# ❌ 不好的命名
UserName = "李四"    # 不要用驼峰命名
a = 100             # 见名不知意
1st_place = "冠军"   # 不能以数字开头（会报错）
```

---

### 2.4 基本数据类型

Python 有 4 种最常用的基本数据类型。用 `type()` 可以查看任何值的类型。

| 类型 | 名称 | 示例 | 说明 |
|------|------|------|------|
| `int` | 整数 | `42`, `-10`, `0` | 没有小数点的数字 |
| `float` | 浮点数 | `3.14`, `-0.5`, `2.0` | 带小数点的数字 |
| `str` | 字符串 | `"hello"`, `'你好'` | 单引号或双引号包裹的文本 |
| `bool` | 布尔值 | `True`, `False` | 只有两个值，注意首字母大写 |

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

---

### 2.5 类型转换

用内置函数在不同类型之间转换：

```python
# str → int：字符串必须是纯数字
age = int("25")       # 25 (int)

# str → float
price = float("9.99") # 9.99 (float)

# int/float → str
s = str(100)          # "100" (str)

# 任何类型 → bool（规则：0、空字符串、None 为 False，其他为 True）
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("hello"))  # True

# 常见错误：不能把非数字字符串直接转成数字
# int("abc")   # ❌ 报错：ValueError
# int("3.14")  # ❌ 报错："3.14" 不是整数，应该用 float("3.14")
```

---

### 2.6 输入输出

#### print() —— 输出到屏幕

```python
# 基本用法
print("你好，世界！")

# 打印多个值（默认用空格分隔）
print("苹果", "香蕉", "橘子")  # 苹果 香蕉 橘子

# sep 参数：自定义分隔符
print("苹果", "香蕉", "橘子", sep=" | ")  # 苹果 | 香蕉 | 橘子

# end 参数：自定义结尾（默认是换行 \n）
print("第一行", end="...")
print("还是第一行")  # 输出：第一行...还是第一行
```

#### input() —— 接收用户输入

```python
# input() 始终返回字符串（str）
name = input("请输入你的名字：")
print(f"你好，{name}！")

# 如果需要数字，要手动转换
age_str = input("请输入你的年龄：")
age = int(age_str)  # 转换成整数
print(f"你明年 {age + 1} 岁")
```

#### f-string —— 格式化字符串（Python 3.6+）

```python
name = "小明"
age = 10
score = 98.5

# 在字符串前加 f，用 {变量名} 嵌入变量
print(f"{name} 今年 {age} 岁，考了 {score} 分")

# 花括号里可以写表达式
print(f"10 年后他 {age + 10} 岁")
```

---

### 2.7 运算符

#### 算术运算符

```python
a = 10
b = 3

print(a + b)   # 13  加法
print(a - b)   # 7   减法
print(a * b)   # 30  乘法
print(a / b)   # 3.333...  除法（结果永远是 float）
print(a // b)  # 3   整除（向下取整，丢掉小数部分）
print(a % b)   # 1   取余（模运算，a 除以 b 的余数）
print(a ** b)  # 1000 幂运算（a 的 b 次方）
```

#### 比较运算符

比较运算符的结果始终是 `bool`（True 或 False）。

```python
x = 5
y = 10

print(x == y)   # False  等于（注意是双等号！）
print(x != y)   # True   不等于
print(x > y)    # False  大于
print(x < y)    # True   小于
print(x >= 5)   # True   大于等于
print(x <= 3)   # False  小于等于
```

**常见坑：不要把 `=`（赋值）和 `==`（比较）搞混！**

```python
# ❌ 错误：把比较写成了赋值
# if x = 5:  # 这会报错

# ✅ 正确
if x == 5:   # 这才是在比较
    print("x 等于 5")
```

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| `input()` 返回的是字符串 | 拿到数字一定要 `int()` 或 `float()` 转换 |
| `=` vs `==` | 一个等号是赋值，两个等号是比较 |
| Python 文件名不要和标准库重名 | 不要把文件命名为 `random.py`、`json.py` 等 |
| 字符串引号要配对 | `"hello'` 会报错，引号要前后一致 |
| `bool("False")` 是 True | 非空字符串转 bool 都是 True |

---

## 四、今日题目链接

完成以下练习来巩固今天的内容：

1. 写一个程序，让用户输入姓名和年龄，输出 `{姓名} 同学，你生于 {当前年份 - 年龄} 年左右`
2. 让用户输入一个三位数，输出它的个位、十位、百位数字（提示：用 `//` 和 `%`）
3. 让用户输入圆的半径，计算并输出面积（`面积 = 3.14 * 半径**2`）

---

## 五、检查清单

- [ ] 我能在终端中成功运行 `python3 --version`
- [ ] 我能在 VS Code 中编写并运行一个 `.py` 文件
- [ ] 我能说出 int, float, str, bool 的区别
- [ ] 我会用 `type()` 查看变量类型
- [ ] 我会用 `int()`, `str()`, `float()` 做类型转换
- [ ] 我会用 f-string 格式化输出
- [ ] 我理解 `//`（整除）和 `%`（取余）的用法
- [ ] 我不会把 `=` 和 `==` 搞混
