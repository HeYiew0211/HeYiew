# 05 - CSV 解析 ⭐

## 题目描述

编写函数 `parse_csv(file_path)`，读取一个用逗号分隔的文本文件（简易 CSV 格式），将其解析成 **list of dict** 的格式。

文件格式：
- 第一行是列名（header），如 `name,age,city`
- 之后每一行是一条数据记录

返回格式示例：
```python
[
    {"name": "Alice", "age": "25", "city": "Beijing"},
    {"name": "Bob", "age": "30", "city": "Shanghai"},
    {"name": "Charlie", "age": "28", "city": "Guangzhou"}
]
```

要求：
- 使用 `split(',')` 按逗号分割
- 使用 `strip()` 去除每行末尾的换行符和每个值的前后空白
- 用 `zip()` 将 header 和数据行组合成 dict

## 输入输出示例

假设 `data.txt` 文件内容：
```
name,age,city
Alice,25,Beijing
Bob,30,Shanghai
Charlie,28,Guangzhou
```

```python
result = parse_csv("data.txt")
for person in result:
    print(person)

# 输出:
# {'name': 'Alice', 'age': '25', 'city': 'Beijing'}
# {'name': 'Bob', 'age': '30', 'city': 'Shanghai'}
# {'name': 'Charlie', 'age': '28', 'city': 'Guangzhou'}
```

## 解题思路

> 💡 提示：
> - 先用 `readlines()` 或 `for line in f` 逐行读取
> - 第一行是 header：`headers = lines[0].strip().split(',')`
> - 接下来每行数据：`values = line.strip().split(',')`
> - `zip(headers, values)` 将两个列表配对，然后传给 `dict()` 转换为字典
> - 如 `dict(zip(['name', 'age'], ['Alice', '25']))` 得到 `{'name': 'Alice', 'age': '25'}`

---

答案见：[05-CSV解析-答案.md](answers/05-CSV解析-答案.md)
