# 05 - CSV 解析 - 答案

## 完整代码

```python
def parse_csv(file_path):
    """读取 CSV 文件，解析为 list of dict 格式
    
    参数:
        file_path: CSV 文件路径
    
    返回:
        list[dict]: 每一行数据对应一个字典，key 为列名
    """
    result = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # 第一行是 header（列名）
    # strip() 去掉行末换行符，split(',') 按逗号分割
    headers = lines[0].strip().split(',')
    
    # 从第二行开始是数据
    for line in lines[1:]:
        # 跳过空行
        if not line.strip():
            continue
        
        # 按逗号分割数据行
        values = line.strip().split(',')
        
        # 用 zip() 将 headers 和 values 配对，转换为字典
        row_dict = dict(zip(headers, values))
        result.append(row_dict)
    
    return result


# ========== 主程序 ==========
if __name__ == "__main__":
    # 先创建测试文件
    test_data = """name,age,city
Alice,25,Beijing
Bob,30,Shanghai
Charlie,28,Guangzhou"""

    test_path = "test_data.csv"
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(test_data)
    
    # 解析并打印
    result = parse_csv(test_path)
    print("解析结果：")
    for i, person in enumerate(result, 1):
        print(f"  第{i}行：{person}")
    
    # 按属性访问
    print(f"\n所有姓名：{[p['name'] for p in result]}")
    print(f"所有城市：{[p['city'] for p in result]}")


# ========== 进阶：处理引号内的逗号 ==========
# 真正的 CSV 可能包含引号内的逗号，如 '"Beijing, China",30'
# Python 有内置的 csv 模块可以处理这些复杂情况：
"""
import csv

def parse_csv_advanced(file_path):
    result = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append(dict(row))
    return result
"""
```

## 关键要点

1. **`zip()` 函数**：将两个列表按位置配对，返回一个迭代器。`dict(zip(headers, values))` 是 Python 中将两个列表组合成字典的标准写法
2. **`readlines()` vs 逐行读取**：`readlines()` 一次性读入内存，适合小文件；大文件用 `for line in f` 更省内存
3. **跳过空行**：`if not line.strip():` 检查去除空白后是否为空
4. **内置 `csv` 模块**：Python 标准库自带 `csv` 模块，可以处理更复杂的 CSV 格式（如引号转义、不同分隔符等），上面的进阶代码展示了用法
5. **`strip()` 的重要性**：去除每行末尾的 `\n` 和可能的空白字符
