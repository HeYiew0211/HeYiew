# Day 2：控制流

> **预计学习时间：1.5 ~ 2 小时**

---

## 一、今日目标

- 会用 `if / elif / else` 写出条件分支
- 理解 `and`, `or`, `not` 逻辑运算符
- 会用 `for` 循环遍历 list、字符串和 `range()`
- 会用 `while` 循环处理不确定次数的重复
- 能正确使用 `break` 和 `continue`

---

## 二、知识点讲解

### 2.1 条件判断：if / elif / else

程序中的"如果…就…否则…"。

**核心规则：Python 使用 4 个空格缩进来表示代码块。**

```python
score = 85

if score >= 90:
    print("优秀")       # 这行前面有 4 个空格缩进
elif score >= 80:
    print("良好")       # elif = else if 的缩写
elif score >= 60:
    print("及格")
else:
    print("不及格")     # else 处理所有剩下的情况

# 输出：良好
```

**缩进是 Python 的语法，不是可选的！缺少缩进或缩进不一致都会报错。**

```python
# ❌ 错误：缺少缩进
# if x > 0:
# print("正数")    # IndentationError

# ❌ 错误：缩进不一致（混用空格和 Tab）
# if x > 0:
#     print("正数")
#   print("继续")   # 缩进不对齐
```

#### 条件判断可以嵌套

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以入场")
    else:
        print("请先购票")
else:
    print("未成年人禁止入场")
```

---

### 2.2 逻辑运算符：and, or, not

| 运算符 | 含义 | 示例 | 结果为 True 的条件 |
|--------|------|------|--------------------|
| `and` | 且 | `a > 0 and b > 0` | 两边都为 True |
| `or` | 或 | `a > 0 or b > 0` | 至少一边为 True |
| `not` | 非 | `not a > 0` | 原条件为 False |

```python
age = 22
has_id = True

# and：两个条件都要满足
if age >= 18 and has_id:
    print("验证通过")

# or：满足一个就行
is_admin = True
is_vip = False
if is_admin or is_vip:
    print("有特殊权限")

# not：取反
is_banned = False
if not is_banned:
    print("该用户未被封禁")

# 可以组合使用，复杂条件建议加括号让意图更清晰
score = 88
if (score >= 80 and score < 90) or score == 100:
    print("表现优异")
```

---

### 2.3 for 循环

当你明确知道要循环多少次，或者要遍历一个集合时，用 `for`。

#### 2.3.1 遍历 list

```python
fruits = ["苹果", "香蕉", "橘子"]

for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 输出：
# 我喜欢吃苹果
# 我喜欢吃香蕉
# 我喜欢吃橘子
```

#### 2.3.2 遍历字符串

```python
word = "Python"

for char in word:
    print(char)

# 输出：每个字母一行
# P
# y
# t
# h
# o
# n
```

#### 2.3.3 使用 range()

`range()` 是 for 循环的好搭档，用来生成一系列数字。

```python
# range(n)：从 0 到 n-1（共 n 个数字）
for i in range(5):
    print(i, end=" ")
# 输出：0 1 2 3 4

print()  # 换行

# range(start, stop)：从 start 到 stop-1
for i in range(2, 6):
    print(i, end=" ")
# 输出：2 3 4 5

print()

# range(start, stop, step)：从 start 到 stop-1，步长为 step
for i in range(1, 10, 2):
    print(i, end=" ")
# 输出：1 3 5 7 9
```

**常见用法：**
```python
# 重复做某件事 N 次
for i in range(3):
    print(f"第 {i+1} 次执行")

# 遍历 list 的同时获取索引
fruits = ["苹果", "香蕉", "橘子"]
for i in range(len(fruits)):
    print(f"第 {i} 个水果是 {fruits[i]}")
```

---

### 2.4 while 循环

当你不确定要循环多少次，而是"当某个条件成立时一直做"，用 `while`。

```python
# 基本用法
count = 1
while count <= 5:
    print(f"第 {count} 次")
    count += 1  # count = count + 1 的简写，每轮 +1

# 输出：
# 第 1 次
# 第 2 次
# 第 3 次
# 第 4 次
# 第 5 次
```

#### 避免死循环

**死循环 = 条件永远为 True，程序停不下来。**

```python
# ❌ 死循环！因为 count 永远不变
# count = 1
# while count <= 5:
#     print(count)    # 忘记 count += 1，count 永远是 1

# ✅ 正确做法：确保循环变量在变化
count = 1
while count <= 5:
    print(count)
    count += 1        # 每次循环 count 增加，最终会超过 5
```

#### 实用示例：验证用户输入

```python
# 一直询问直到用户输入有效内容
password = ""
while password != "123456":
    password = input("请输入密码：")
print("密码正确，登录成功！")
```

---

### 2.5 break 和 continue

这两个关键字用于在循环中做特殊控制。

| 关键字 | 作用 |
|--------|------|
| `break` | 立即跳出整个循环（循环到此结束） |
| `continue` | 跳过本轮循环的剩余代码，直接开始下一轮 |

```python
# break：找到目标就停止
numbers = [3, 7, 2, 9, 4]
for num in numbers:
    if num == 9:
        print(f"找到了 {num}，停止搜索")
        break                # 找到 9 就退出，不再看后面的 4
    print(f"检查了 {num}")

# 输出：
# 检查了 3
# 检查了 7
# 检查了 2
# 找到了 9，停止搜索
```

```python
# continue：只跳过偶数
for num in range(1, 7):
    if num % 2 == 0:   # 如果是偶数
        continue       # 跳过 print，直接进入下一轮
    print(num, end=" ")

# 输出：1 3 5
```

#### 实际组合使用

```python
# 猜数字游戏：最多猜 5 次，猜对就提前结束
import random
answer = random.randint(1, 100)  # 生成 1~100 的随机数
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"第 {attempt} 次猜测，请输入数字（1-100）："))

    if guess == answer:
        print("恭喜你，猜对了！")
        break         # 猜对就结束循环
    elif guess > answer:
        print("太大了")
    else:
        print("太小了")
else:
    # for/while 循环的 else：循环正常结束（没被 break 打断）时执行
    print(f"很遗憾，正确数字是 {answer}")
```

> **小知识点：** for/while 后面可以接 `else`，它只在循环**没有被 break 打断**时执行。上面的例子中，如果用户 5 次都没猜对（没触发 break），就会执行 `else` 块。

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| 缩进错误 | 缩进必须是**一致的 4 个空格**，不要混用 Tab |
| `=` 写成 `==` | `if x = 5` 会报错，应该是 `if x == 5` |
| while 死循环 | 循环体内必须有改变条件的代码，否则永远停不下来 |
| `elif` 顺序 | 条件从上到下依次判断，匹配到第一个就停止，所以范围条件要从严格到宽松排列 |
| 遍历 list 时修改 list | 不要在 for 循环中增删正在遍历的 list，可能导致奇怪的行为 |
| `range(5)` 是 0~4 | 不包含 5，和 `list` 索引一样是左闭右开 |

---

## 四、今日题目链接

1. 写程序判断用户输入的年份是否是闰年（能被 4 整除但不能被 100 整除，或能被 400 整除）
2. 用 for 循环打印九九乘法表
3. 让用户不断输入数字，输入 0 时停止，最后输出所有数字的总和与平均值（用 while）

---

## 五、检查清单

- [ ] 我会写 if / elif / else 判断，知道每个分支的执行顺序
- [ ] 我理解 and（且）、or（或）、not（非）的含义
- [ ] 我会用 for 循环遍历 list 和字符串
- [ ] 我理解 `range(n)`, `range(start, stop)`, `range(start, stop, step)` 的区别
- [ ] 我会用 while 循环处理"知道停止条件但不清楚次数"的情况
- [ ] 我知道如何避免死循环
- [ ] 我能用 break 提前退出循环，用 continue 跳过当前轮
- [ ] 我的缩进始终是 4 个空格
