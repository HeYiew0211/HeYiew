# 05 - FizzBuzz 答案

```python
# 遍历 1 到 100
for num in range(1, 101):
    # 条件判断：顺序很关键！
    if num % 3 == 0 and num % 5 == 0:   # 或 num % 15 == 0
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

**运行结果（前 20 行）：**

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
...
```

## 知识点

- **条件判断的顺序**：在 `if-elif-else` 中，将最特殊的条件（同时被 3 和 5 整除）放在最前面，避免被前面的条件"拦截"
- **and 逻辑运算符**：`A and B` 表示 A 和 B 两个条件同时成立
- **range(1, 101)**：生成 1 到 100 的整数（左闭右开，所以写 101）
