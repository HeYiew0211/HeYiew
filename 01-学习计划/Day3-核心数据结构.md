# Day 3：核心数据结构

> **预计学习时间：2 小时（今天内容最重要，请慢慢消化）**
>
> 数据结构 = 组织和存储数据的方式。如果说变量是一个盒子，数据结构就是一组盒子、一个柜子、一排货架。今天学 4 种核心数据结构：**list（列表）、dict（字典）、tuple（元组）、set（集合）**。

---

## 一、今日目标

- 掌握 list 的索引、切片和常用方法
- 理解 dict 的键值对模型，会用 dict 存取数据
- 知道 tuple 的不可变性及其应用场景
- 了解 set 的去重特性与集合运算
- 能根据实际需求选择合适的数据结构

---

## 二、知识点讲解

### 2.1 list（列表）—— 最常用的数据结构

list 是一个**有序、可变**的容器，可以放任何类型的数据。

#### 2.1.1 创建 list

```python
# 空 list
empty = []

# 存放同类型数据
numbers = [1, 2, 3, 4, 5]
names = ["张三", "李四", "王五"]

# 可以混合存放不同类型（但不推荐，通常保持类型一致）
mixed = [1, "hello", 3.14, True]

# 用 list() 函数从其他序列创建
chars = list("abc")  # ['a', 'b', 'c']
```

#### 2.1.2 索引（index）—— 访问单个元素

索引从 **0** 开始。负数索引表示**从末尾倒着数**，-1 是最后一个。

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]

# 正索引：  0       1       2       3       4
# 负索引： -5      -4      -3      -2      -1

print(fruits[0])    # 苹果（第一个）
print(fruits[2])    # 橘子（第三个）
print(fruits[-1])   # 西瓜（最后一个）
print(fruits[-2])   # 葡萄（倒数第二个）

# 索引越界会报 IndexError
# print(fruits[10])  # ❌ IndexError: list index out of range

# 修改某个位置的元素
fruits[1] = "芒果"
print(fruits)       # ['苹果', '芒果', '橘子', '葡萄', '西瓜']
```

#### 2.1.3 切片（slice）—— 访问一段元素

语法：`list[start:end:step]`，三个值都可以省略。

**核心记忆：`[start:end]` 是左闭右开区间 —— 包含 start，不包含 end。**

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])     # [2, 3, 4]     从索引 2 到 4（不含 5）
print(nums[:4])      # [0, 1, 2, 3]  省略 start = 从开头
print(nums[6:])      # [6, 7, 8, 9]  省略 end = 到末尾
print(nums[:])       # [0, 1, ..., 9] 省略两者 = 复制整个 list
print(nums[::2])     # [0, 2, 4, 6, 8]  step=2，每隔一个取一个
print(nums[::-1])    # [9, 8, 7, ..., 0] step=-1 实现反转

# 切片公式：start + step * n < end（step 为正时）
```

#### 2.1.4 常用方法

下面这些方法都是**原地修改** list（除了 `sorted()` 和 `len()`）。

```python
fruits = ["苹果", "香蕉"]

# ---- 增加 ----
fruits.append("橘子")        # 在末尾追加一个元素
print(fruits)                # ['苹果', '香蕉', '橘子']

fruits.insert(1, "葡萄")     # 在索引 1 的位置插入
print(fruits)                # ['苹果', '葡萄', '香蕉', '橘子']

# ---- 删除 ----
removed = fruits.pop()       # 删除并返回最后一个元素
print(removed)               # 橘子
print(fruits)                # ['苹果', '葡萄', '香蕉']

removed = fruits.pop(0)      # pop(索引) 删除指定位置的元素
print(removed)               # 苹果

fruits.remove("葡萄")        # 删除第一个匹配的值（不知道索引时用）
print(fruits)                # ['香蕉']

# ---- 查找 ----
nums = [10, 20, 30, 20, 40]
print(len(nums))             # 5 —— 元素个数，不是方法而是内置函数
print(nums.index(30))        # 2 —— 查找值第一次出现的索引
print(20 in nums)            # True —— 判断值是否在 list 中
print(50 in nums)            # False

# ---- 排序 ----
scores = [85, 92, 78, 90]
scores.sort()                # 原地升序排序
print(scores)                # [78, 85, 90, 92]

scores.sort(reverse=True)    # 原地降序排序
print(scores)                # [92, 90, 85, 78]

# sorted() 返回新 list，不修改原 list（重要区别！）
original = [3, 1, 2]
new_list = sorted(original)  # 返回新 list [1, 2, 3]
print(original)              # [3, 1, 2] —— 原 list 没变

# ---- 反转 ----
letters = ['a', 'b', 'c']
letters.reverse()            # 原地反转
print(letters)               # ['c', 'b', 'a']
```

#### 2.1.5 遍历 list

```python
names = ["张三", "李四", "王五"]

# 方式一：直接遍历元素
for name in names:
    print(name)

# 方式二：需要索引时用 enumerate()
for i, name in enumerate(names):
    print(f"{i}: {name}")
# 输出：
# 0: 张三
# 1: 李四
# 2: 王五
```

---

### 2.2 dict（字典）—— 最灵活的数据结构

dict 是**键值对（key-value pair）**的集合。你可以把 key 理解为"标签"，通过标签快速找到对应的 value。

**核心特点：key 必须不可变（str, int, tuple 可以；list 不行），value 可以是任意类型。**

#### 2.2.1 创建和访问

```python
# 创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 通过 key 访问 value
print(person["name"])   # 张三
print(person["age"])    # 25

# ❌ 访问不存在的 key 会报 KeyError
# print(person["email"])  # KeyError: 'email'

# ✅ 用 get() 安全访问：key 不存在返回 None（或你指定的默认值）
print(person.get("email"))           # None
print(person.get("email", "无"))      # 无（key 不存在时返回默认值）
```

#### 2.2.2 增删改

```python
student = {"name": "小明", "score": 90}

# 增加：直接给新 key 赋值
student["age"] = 15
print(student)  # {'name': '小明', 'score': 90, 'age': 15}

# 修改：给已有 key 赋新值
student["score"] = 95
print(student)  # {'name': '小明', 'score': 95, 'age': 15}

# 删除：用 del 或 pop()
del student["age"]
removed_value = student.pop("score")  # pop 返回被删除的 value
print(student)  # {'name': '小明'}
print(removed_value)  # 95
```

#### 2.2.3 遍历 dict

```python
info = {"name": "李四", "age": 30, "job": "工程师"}

# 遍历所有 key
for key in info.keys():
    print(key)

# 遍历所有 value
for value in info.values():
    print(value)

# 同时遍历 key 和 value（最常用）
for key, value in info.items():
    print(f"{key}: {value}")

# 也可以直接遍历（默认遍历 key）
for key in info:
    print(key)
```

#### 2.2.4 实用技巧

```python
# dict 做计数器
word_count = {}
text = "苹果 香蕉 苹果 橘子 苹果 香蕉"
for word in text.split():
    # word_count[word] = word_count.get(word, 0) + 1
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  # {'苹果': 3, '香蕉': 2, '橘子': 1}

# dict 做查找表（替代多个 if/elif）
color_code = {"红": "#FF0000", "绿": "#00FF00", "蓝": "#0000FF"}
print(color_code.get("红"))  # #FF0000
```

> **为什么用 dict 而不用 list？** dict 通过 key 查找的速度是 O(1)（固定时间），不管字典有多大都很快。list 查找需要遍历，数据量大时很慢。

---

### 2.3 tuple（元组）—— 不可变的 list

tuple 和 list 几乎一样，唯一的区别：**tuple 一旦创建就不能修改**（不能增、删、改元素）。

```python
# 创建 tuple（用圆括号）
point = (3, 4)
colors = ("红", "绿", "蓝")

# 也可以用 tuple() 函数
chars = tuple("abc")  # ('a', 'b', 'c')

# 索引和切片用法和 list 一模一样
print(point[0])       # 3
print(colors[1:])     # ('绿', '蓝')

# ❌ 不可变：以下操作都会报错
# point[0] = 10       # TypeError: 'tuple' object does not support item assignment
# colors.append("黄")   # AttributeError: 'tuple' object has no attribute 'append'
```

#### 单元素 tuple 的陷阱

```python
# ❌ 这不是 tuple，这就是一个带括号的数字！
not_a_tuple = (5)
print(type(not_a_tuple))  # <class 'int'>

# ✅ 单元素 tuple 必须在后面加逗号
real_tuple = (5,)
print(type(real_tuple))   # <class 'tuple'>
```

#### 解包（unpacking）—— 最常用的 tuple 功能

```python
# 把 tuple 的元素分别赋值给多个变量
coordinate = (10, 20)
x, y = coordinate
print(x)  # 10
print(y)  # 20

# 实用：交换两个变量的值（不需要临时变量）
a = 1
b = 2
a, b = b, a        # 右边 (b, a) 构成一个临时 tuple，然后解包
print(a, b)        # 2 1

# 多返回值实际上返回的就是 tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)  # 返回 (min, max) tuple

low, high = get_min_max([3, 1, 4, 1, 5])
print(low, high)   # 1 5
```

#### 什么时候用 tuple？

| 场景 | 用哪种 |
|------|--------|
| 数据需要修改 | list |
| 数据不会变（如坐标、RGB 颜色） | tuple |
| 用作 dict 的 key | tuple（list 不行） |

---

### 2.4 set（集合）—— 去重利器

set 是**无序、不重复**的元素集合。可以把它想象成"把 list 的重复项去掉了，但顺序也不保证"。

```python
# 创建 set（用花括号）
fruits = {"苹果", "香蕉", "橘子"}

# 或用 set() 函数
nums = set([1, 2, 2, 3, 3, 3])
print(nums)  # {1, 2, 3} —— 重复的自动去掉

# 空 set 必须用 set()，因为 {} 是空 dict
empty_set = set()
empty_dict = {}       # 这才是空 dict
```

#### 基本操作

```python
skills = {"Python", "JavaScript"}

# 增加
skills.add("SQL")
print(skills)  # {'Python', 'JavaScript', 'SQL'}

# 删除（remove 在元素不存在时抛错，discard 不会）
skills.remove("JavaScript")   # 删除，不存在报错
skills.discard("Java")        # 删除，不存在也不报错（更安全）

# 判断是否存在
print("Python" in skills)     # True
```

#### 集合运算

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}  并集 —— 两个集合的所有元素
print(a & b)   # {3, 4}                交集 —— 两个集合共有的元素
print(a - b)   # {1, 2}                差集 —— 在 a 中但不在 b 中的元素
print(b - a)   # {5, 6}                差集 —— 在 b 中但不在 a 中的元素
```

#### 实际应用：快速去重

```python
# 用户 ID 列表中有重复，用 set 去重
user_ids = [101, 102, 101, 103, 102, 104, 103]
unique_ids = list(set(user_ids))
print(unique_ids)  # [101, 102, 103, 104]（顺序不保证）

# 找两个列表的共同元素
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common = list(set(list_a) & set(list_b))
print(common)  # [3, 4]
```

---

### 2.5 数据结构选择指南

| 需求 | 用什么 | 原因 |
|------|--------|------|
| 有顺序、需要修改内容 | `list` | 有序可变，最通用 |
| 通过"标签"快速查数据 | `dict` | key 查找 O(1)，极快 |
| 数据不应被修改 | `tuple` | 不可变性提供安全保障 |
| 需要去重 | `set` | 自动去重 |
| 需要判断"有没有" | `set` | `in` 操作 O(1)，比 list 快很多 |
| 这组数据有固定的含义 | `tuple`（配合解包） | 如坐标 `(x, y)` |
| 每个元素都有"名字" | `dict` | key 让代码更有自解释性 |

**决策口诀：先问自己——数据有没有顺序？要不要按位置访问？有没有"标签/名字"？需要去重吗？**

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| list 索引从 0 开始 | `list[1]` 是第二个元素，不是第一个 |
| 切片是左闭右开 | `[1:4]` 包含索引 1, 2, 3，不包含 4 |
| `sort()` vs `sorted()` | `list.sort()` 原地修改返回 None；`sorted(list)` 返回新 list |
| dict 的 key 必须不可变 | list 不能做 key，tuple 和 str 可以 |
| `dict["key"]` 可能报 KeyError | 不确定 key 是否存在时用 `dict.get("key")` |
| 单元素 tuple 要加逗号 | `(5)` 是 int，`(5,)` 才是 tuple |
| `{}` 是空 dict 不是空 set | 空 set 必须用 `set()` |
| 不要一边遍历 list 一边删除 | 会导致元素跳过或索引越界，应该用新 list 或倒序删除 |

---

## 四、今日题目链接

1. **list 综合练习：** 写一个程序，让用户输入 5 个数字存入 list，然后输出：最大值、最小值、总和、平均值、排序后的结果
2. **dict 综合练习：** 用一个 dict 存储 3 个学生的姓名和成绩，实现：添加学生、查询学生成绩、删除学生、打印所有学生信息
3. **set 练习：** 两个班级的学号 list 如下，找出：两个班共有多少人（去重总数）、报了这两个班的学生（交集）、只报了一个班的学生（并集 - 交集）
4. **混合练习：** 将下面的数据转换成合适的数据结构存储，然后从中找出价格最高的商品：
   ```
   苹果 5元, 香蕉 3元, 橘子 4元, 葡萄 8元, 西瓜 12元
   ```

---

## 五、检查清单

- [ ] 我理解 list 的索引（正/负）和切片 `[start:end:step]`
- [ ] 我会用 `append`, `insert`, `pop`, `remove` 操作 list
- [ ] 我能区分 `sort()`（原地排序）和 `sorted()`（返回新 list）
- [ ] 我理解 dict 的键值对概念，会用 key 访问 value
- [ ] 我会用 `get()` 安全地访问 dict，避免 KeyError
- [ ] 我能用 `items()` 同时遍历 dict 的 key 和 value
- [ ] 我知道 tuple 不可变，会写单元素 tuple 的逗号
- [ ] 我会用 tuple 解包，能用 `a, b = b, a` 交换变量
- [ ] 我理解 set 的去重特性，会做交集、并集、差集
- [ ] 我能根据实际需求选择合适的数据结构
