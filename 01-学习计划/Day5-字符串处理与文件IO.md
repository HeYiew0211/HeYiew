# Day 5：字符串处理与文件 IO

> **预计学习时间：1.5 ~ 2 小时**

---

## 一、今日目标

- 掌握字符串的常用操作方法
- 能用 f-string 做高级格式化输出
- 会用 Python 读取和写入文件
- 理解 `with` 语句和文件打开模式

---

## 二、知识点讲解

### 2.1 字符串常用方法

字符串是**不可变对象** —— 所有方法都返回新字符串，不会修改原字符串。

#### 2.1.1 拆分与合并：split() 和 join()

```python
# split()：按分隔符拆分字符串，返回 list
text = "苹果,香蕉,橘子,葡萄"
fruits = text.split(",")
print(fruits)  # ['苹果', '香蕉', '橘子', '葡萄']

# 默认按空白字符（空格、换行、Tab）拆分
sentence = "Python 是一门  很棒的   语言"
words = sentence.split()
print(words)   # ['Python', '是一门', '很棒的', '语言']（多个空格被当作一个分隔符）

# join()：用分隔符把 list 的元素拼成字符串
fruits = ["苹果", "香蕉", "橘子"]
result = " | ".join(fruits)
print(result)  # 苹果 | 香蕉 | 橘子

# join() 的经典组合：把 list 的元素用逗号拼接
numbers = ["1", "2", "3"]  # 注意：元素必须是 str
print(",".join(numbers))   # 1,2,3

# 如果 list 里是数字，需要先转换
nums = [1, 2, 3]
print(",".join(str(n) for n in nums))  # 1,2,3
```

#### 2.1.2 清理空白：strip(), lstrip(), rstrip()

```python
# strip()：去掉首尾的空白字符（空格、换行、Tab 等）
raw = "   你好，世界！   \n"
clean = raw.strip()
print(f"「{clean}」")  # 「你好，世界！」

# lstrip()：只去掉左边（开头）的空白
# rstrip()：只去掉右边（结尾）的空白

# 也可以去掉指定字符
text = "...重要消息..."
print(text.strip("."))    # 重要消息

name = "---张三---"
print(name.strip("-"))    # 张三
```

#### 2.1.3 替换：replace()

```python
text = "我喜欢 Java，Java 很好用"
new_text = text.replace("Java", "Python")
print(new_text)  # 我喜欢 Python，Python 很好用

# 第三个参数指定替换次数
text = "aaa bbb aaa ccc aaa"
print(text.replace("aaa", "xxx", 2))  # 只替换前 2 次
# xxx bbb xxx ccc aaa
```

#### 2.1.4 查找与判断

```python
filename = "photo_2026.jpg"

# find()：返回子串第一次出现的索引，找不到返回 -1
print(filename.find("."))       # 13（点的位置）
print(filename.find("xyz"))     # -1（不存在）

# startswith() / endswith()：判断开头/结尾
print(filename.endswith(".jpg"))   # True
print(filename.startswith("IMG"))  # False

# 实用：检查文件扩展名
if filename.endswith((".jpg", ".png", ".gif")):
    print("这是一个图片文件")

# in：判断子串是否在字符串中
print("2026" in filename)  # True
```

#### 2.1.5 大小写转换

```python
text = "Hello, Python!"

print(text.upper())      # HELLO, PYTHON!    全部大写
print(text.lower())      # hello, python!     全部小写
print(text.title())      # Hello, Python!     每个单词首字母大写

# 实用：不区分大小写的比较
user_input = "YES"
if user_input.upper() == "YES":
    print("用户确认了")
```

---

### 2.2 f-string 进阶

#### 2.2.1 格式化数字

```python
pi = 3.1415926
price = 19990

# :.nf —— 保留 n 位小数，自动四舍五入
print(f"圆周率：{pi:.2f}")      # 圆周率：3.14
print(f"圆周率：{pi:.4f}")      # 圆周率：3.1416

# :, —— 千位分隔符
print(f"价格：{price:,} 元")     # 价格：19,990 元

# 百分比
ratio = 0.856
print(f"完成率：{ratio:.1%}")    # 完成率：85.6%
```

#### 2.2.2 对齐与填充

```python
name = "张三"
score = 95

# :<N 左对齐，占 N 个字符宽度
# :>N 右对齐
# :^N 居中对齐
print(f"姓名：{name:<10} 分数：{score:>5}")
# 姓名：张三         分数：   95

# 用自定义字符填充
print(f"进度：[{'='*10:.<20}]")  # 进度：[==========..........]

# 实用的表格输出
print(f"{'姓名':<8}{'年龄':<6}{'分数':<6}")
print("-" * 20)
print(f"{'张三':<8}{18:<6}{95:<6}")
print(f"{'李四':<8}{20:<6}{88:<6}")
```

#### 2.2.3 其他技巧

```python
# = 号在 f-string 中输出变量名和值（Python 3.8+）
name = "小明"
score = 95
print(f"{name=}, {score=}")  # name='小明', score=95

# 大括号里可以写表达式
a = 3
b = 5
print(f"{a} + {b} = {a + b}")  # 3 + 5 = 8

# datetime 格式化
import datetime as dt
now = dt.datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
```

---

### 2.3 文件读取

#### 2.3.1 打开文件的模式

| 模式 | 含义 | 文件不存在时 |
|------|------|------------|
| `'r'` | 只读（默认） | 报错 |
| `'w'` | 写入（会覆盖已有内容） | 创建新文件 |
| `'a'` | 追加（在末尾添加） | 创建新文件 |
| `'r+'` | 读写 | 报错 |

#### 2.3.2 读取文件的多种方式

假设有一个文件 `data.txt`，内容如下：

```
第一行内容
第二行内容
第三行内容
```

```python
# 方式 1：read() —— 一次性读取全部内容
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 方式 2：readlines() —— 读取所有行，返回 list
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)  # ['第一行内容\n', '第二行内容\n', '第三行内容\n']
    for line in lines:
        print(line.strip())  # 去掉行尾的换行符

# 方式 3：逐行读取（最推荐！内存友好，适合大文件）
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:            # 文件对象本身可以直接遍历
        print(line.strip())

# 方式 4：read(N) —— 读取 N 个字符
with open("data.txt", "r", encoding="utf-8") as f:
    chunk = f.read(10)        # 读取前 10 个字符
    print(chunk)
```

---

### 2.4 文件写入

```python
# 模式 'w'：覆盖写入（文件原有内容会被清空！）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")           # write() 不会自动加换行
    f.write("第二行\n")

# 写入多行：writelines() 也不会自动加换行
lines = ["苹果\n", "香蕉\n", "橘子\n"]
with open("fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# 模式 'a'：追加写入（保留原有内容，在末尾添加）
with open("log.txt", "a", encoding="utf-8") as f:
    import datetime as dt
    f.write(f"[{dt.datetime.now()}] 程序运行记录\n")

# 实用：逐行处理并写入新文件
with open("source.txt", "r", encoding="utf-8") as f_in, \
     open("result.txt", "w", encoding="utf-8") as f_out:
    for line in f_in:
        # 给每行加上行号
        f_out.write(f"处理结果：{line}")
```

---

### 2.5 with 语句 —— 自动管理资源

`with` 语句确保文件在使用完后**自动关闭**，即使发生异常也能正确关闭。

```python
# ❌ 不推荐：手动打开和关闭，容易忘记 f.close()
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()  # 容易忘记，程序异常时可能不执行

# ✅ 推荐：with 语句自动处理，离开 with 块时自动关闭
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 离开 with 块后，文件自动关闭，安全省心
```

**`with` 是 Python 的上下文管理器（Context Manager），不仅仅是文件操作，以后学数据库连接、网络请求等也都会用。**

---

### 2.6 实用综合示例

```python
# 统计一个文件中每个单词出现的次数
word_count = {}

with open("article.txt", "r", encoding="utf-8") as f:
    for line in f:
        # 清洗并拆分每一行
        words = line.strip().lower().split()
        for word in words:
            # 去掉标点符号（简单处理）
            word = word.strip(".,!?()[]\"'")
            if word:  # 跳过空字符串
                word_count[word] = word_count.get(word, 0) + 1

# 按出现次数排序输出前 5 名
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:5]:
    print(f"{word}: {count} 次")
```

---

## 三、常见坑点

| 坑点 | 说明 |
|------|------|
| 忘记 `encoding="utf-8"` | Windows 上中文可能乱码，**总是加上 encoding 参数** |
| `'w'` 模式会覆盖文件 | 用 `'w'` 打开已有文件，原有内容会丢失！追加用 `'a'` |
| `write()` 不自动加换行 | 需要手动加 `\n` |
| `join()` 要求所有元素是 str | list 里有数字要先转换：`",".join(str(n) for n in nums)` |
| 字符串是不可变的 | `s.upper()` 不改变 s，要接收返回值 `s = s.upper()` |
| 大文件不要用 `read()` 一次性读 | 内存可能爆掉，用逐行读取 `for line in f` |
| `find()` 找不到返回 -1 | `if s.find("x")` 可能误判（-1 也是真值），应用 `if "x" in s` |

---

## 四、今日题目链接

1. 写一个程序，读取一个包含多行数字的文件，每行一个数字，计算并输出总和与平均值
2. 写一个程序，让用户输入一段英文，统计其中每个单词出现的次数（忽略大小写）
3. 模拟一个简单的日志记录器：用户可以输入内容，程序把内容追加写入到 `log.txt`，每次加上时间戳
4. 读取一个 CSV 格式的文件（逗号分隔），解析后按某列排序，输出为格式化的表格

---

## 五、检查清单

- [ ] 我会用 `split()` 和 `join()` 在字符串与 list 之间转换
- [ ] 我会用 `strip()` 去掉首尾空白
- [ ] 我会用 `replace()` 替换字符串内容
- [ ] 我会用 `startswith()` / `endswith()` 做前缀后缀判断
- [ ] 我能用 f-string 做格式化数字（`:.2f`）、对齐（`:<10`）
- [ ] 我理解 `'r'`（读）、`'w'`（覆盖写）、`'a'`（追加写）的区别
- [ ] 我会用 `with open(...) as f:` 安全地读写文件
- [ ] 我知道打开文件要加 `encoding="utf-8"`
- [ ] 我会逐行读取文件（`for line in f`）
