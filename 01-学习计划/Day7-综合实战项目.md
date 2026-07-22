# Day 7：综合实战项目 —— 命令行联系人管理器

> **预计学习时间：2 小时**
>
> 今天是最后一天！我们将把前 6 天学到的知识融会贯通，动手做一个完整的命令行程序：**联系人管理器**。

---

## 一、今日目标

- 独立完成一个完整的 Python 小项目
- 综合运用 list、dict、函数、文件 IO、异常处理、模块
- 学会"先分析设计，再逐步实现"的开发思路
- 理解 JSON 数据持久化的基本方法

---

## 二、项目需求

做一个命令行联系人管理器，支持以下功能：

1. **添加联系人**：输入姓名、电话、邮箱
2. **查看所有联系人**：以表格形式列出
3. **搜索联系人**：按姓名搜索（支持模糊匹配）
4. **删除联系人**：按姓名删除
5. **数据持久化**：所有数据保存到 JSON 文件，程序启动时自动加载
6. **命令行菜单**：循环显示菜单，让用户选择操作

---

## 三、分析与设计

在写代码之前，先想清楚三个问题：

### 3.1 用什么数据结构？

- 每个联系人是一个 **dict**：`{"name": "张三", "phone": "138...", "email": "z@x.com"}`
- 所有联系人存在一个 **list** 里：`[contact1, contact2, contact3, ...]`

### 3.2 文件怎么保存？

- 使用 `json` 模块
- 保存：`json.dump(contacts, f, ensure_ascii=False, indent=2)`
- 读取：`contacts = json.load(f)`
- 文件名：`contacts.json`
- 首次启动时文件不存在，用 `try/except FileNotFoundError` 处理

### 3.3 功能怎么拆成函数？

```
main()                    # 主函数：显示菜单 + 分发操作
├── load_contacts()       # 从 JSON 文件加载联系人 list
├── save_contacts()       # 保存联系人 list 到 JSON 文件
├── add_contact()         # 添加联系人
├── show_all_contacts()   # 显示所有联系人
├── search_contacts()     # 搜索联系人
└── delete_contact()      # 删除联系人
```

---

## 四、逐步实现

### 第 1 步：搭建框架

先写出程序骨架——菜单循环和函数占位。

```python
import json

# 存储所有联系人的 list（全局变量）
contacts = []


def load_contacts():
    """从 JSON 文件加载联系人"""
    pass  # 先占位，后面再实现


def save_contacts():
    """保存联系人到 JSON 文件"""
    pass


def add_contact():
    """添加新联系人"""
    pass


def show_all_contacts():
    """显示所有联系人"""
    pass


def search_contacts():
    """搜索联系人"""
    pass


def delete_contact():
    """删除联系人"""
    pass


def main():
    """主函数：显示菜单并处理用户选择"""
    # 启动时加载数据
    load_contacts()

    while True:
        # 打印菜单
        print("\n" + "=" * 40)
        print("       联系人管理系统")
        print("=" * 40)
        print("1. 查看所有联系人")
        print("2. 添加联系人")
        print("3. 搜索联系人")
        print("4. 删除联系人")
        print("5. 退出程序")
        print("-" * 40)

        choice = input("请选择操作（1-5）：").strip()

        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
            print("再见！")
            break
        else:
            print("无效的选择，请输入 1-5 之间的数字")


# 程序入口（习惯写法）
if __name__ == "__main__":
    main()
```

> **`if __name__ == "__main__":`** 是什么意思？
>
> 当直接运行这个文件时，`__name__` 变量的值是 `"__main__"`，此时执行 `main()`。
> 如果这个文件被其他文件 import，`__name__` 是文件名，不会自动运行。
> **习惯上所有 Python 脚本都加上这一行。**

---

### 第 2 步：实现数据加载与保存

```python
import json
import os

FILENAME = "contacts.json"  # 用一个常量定义文件名，方便修改


def load_contacts():
    """从 JSON 文件加载联系人到全局 list"""
    global contacts
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            contacts = json.load(f)
        print(f"已加载 {len(contacts)} 个联系人")
    except FileNotFoundError:
        # 第一次运行，文件还不存在，初始化为空 list
        contacts = []
        print("未找到数据文件，已初始化为空列表")
    except json.JSONDecodeError:
        # 文件存在但格式有问题
        print("数据文件损坏，已初始化为空列表")
        contacts = []


def save_contacts():
    """保存联系人 list 到 JSON 文件"""
    global contacts
    with open(FILENAME, "w", encoding="utf-8") as f:
        # ensure_ascii=False 保留中文不转义
        # indent=2 让 JSON 文件格式化，人类可读
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(contacts)} 个联系人")
```

---

### 第 3 步：实现添加联系人

```python
def add_contact():
    """让用户输入联系人信息并添加到 list 中"""
    print("\n--- 添加联系人 ---")

    name = input("姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return  # 提前返回，不执行后面的代码

    # 检查是否已存在同名联系人（可选）
    for contact in contacts:
        if contact["name"] == name:
            print(f"联系人「{name}」已存在！")
            return

    phone = input("电话：").strip()
    email = input("邮箱：").strip()

    # 创建联系人 dict
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    # 添加后立即保存（自动保存模式）
    save_contacts()
    print(f"联系人「{name}」添加成功！")
```

**设计要点：**
- `.strip()` 去除用户输入的首尾空格
- 检查空姓名和重复姓名，做好输入校验
- 添加后**立即自动保存**，防止数据丢失

---

### 第 4 步：实现查看所有联系人

```python
def show_all_contacts():
    """以表格形式显示所有联系人"""
    print("\n--- 所有联系人 ---")

    if not contacts:
        print("暂无联系人")
        return

    # 格式化表格输出
    # 计算每列的最大宽度（至少保证表头宽度）
    header = f"{'序号':<5}{'姓名':<10}{'电话':<16}{'邮箱':<25}"
    print(header)
    print("-" * len(header))

    for i, contact in enumerate(contacts, start=1):
        print(
            f"{i:<5}"
            f"{contact['name']:<10}"
            f"{contact['phone']:<16}"
            f"{contact['email']:<25}"
        )

    print(f"\n共 {len(contacts)} 个联系人")
```

**设计要点：**
- `enumerate(contacts, start=1)` 生成从 1 开始的序号
- 用 f-string 的左对齐格式化（`:<N`）让表格列对齐

---

### 第 5 步：实现搜索联系人

```python
def search_contacts():
    """按姓名搜索联系人（支持模糊匹配）"""
    print("\n--- 搜索联系人 ---")

    keyword = input("请输入要搜索的姓名或关键字：").strip()
    if not keyword:
        print("搜索关键字不能为空！")
        return

    # 使用 list comprehension 过滤：姓名中包含关键字（不区分大小写）
    results = [
        c for c in contacts
        if keyword.lower() in c["name"].lower()
    ]

    if not results:
        print(f"未找到姓名中包含「{keyword}」的联系人")
        return

    # 显示搜索结果
    print(f"\n找到 {len(results)} 个匹配的联系人：")
    print(f"{'姓名':<10}{'电话':<16}{'邮箱':<25}")
    print("-" * 51)
    for c in results:
        print(f"{c['name']:<10}{c['phone']:<16}{c['email']:<25}")
```

**设计要点：**
- `keyword.lower() in c["name"].lower()` 实现**不区分大小写**的模糊匹配
- 用 list comprehension 一行完成过滤，简洁优雅

---

### 第 6 步：实现删除联系人

```python
def delete_contact():
    """按姓名删除联系人"""
    print("\n--- 删除联系人 ---")

    if not contacts:
        print("暂无联系人，无法删除")
        return

    name = input("请输入要删除的联系人姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    # 精确匹配删除
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            # 确认删除
            confirm = input(f"确定要删除「{name}」吗？（y/n）：").strip().lower()
            if confirm == "y":
                removed = contacts.pop(i)  # 按索引删除
                save_contacts()            # 保存更新后的数据
                print(f"联系人「{name}」已删除")
            else:
                print("已取消删除")
            return  # 找到并处理后就返回

    # 循环结束没找到
    print(f"未找到名为「{name}」的联系人")
```

**设计要点：**
- `contacts.pop(i)` 按索引删除，可以拿到被删除的元素
- 删除前做**二次确认**，防止误删
- 删除后**立即保存**

---

### 第 7 步：完整代码整合

将以上所有代码组合起来，就是完整的联系人管理器：

```python
"""
联系人管理器 - Python 初学者综合实战项目
功能：添加、查看、搜索、删除联系人，数据保存为 JSON
"""

import json

FILENAME = "contacts.json"
contacts = []


def load_contacts():
    """从 JSON 文件加载联系人"""
    global contacts
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            contacts = json.load(f)
        print(f"已加载 {len(contacts)} 个联系人")
    except FileNotFoundError:
        contacts = []
        print("未找到数据文件，已初始化为空列表")
    except json.JSONDecodeError:
        print("数据文件损坏，已初始化为空列表")
        contacts = []


def save_contacts():
    """保存联系人到 JSON 文件"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(contacts)} 个联系人")


def add_contact():
    """添加新联系人"""
    print("\n--- 添加联系人 ---")
    name = input("姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    # 检查重复
    if any(c["name"] == name for c in contacts):
        print(f"联系人「{name}」已存在！")
        return

    phone = input("电话：").strip()
    email = input("邮箱：").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print(f"联系人「{name}」添加成功！")


def show_all_contacts():
    """显示所有联系人"""
    print("\n--- 所有联系人 ---")
    if not contacts:
        print("暂无联系人")
        return

    header = f"{'序号':<5}{'姓名':<10}{'电话':<16}{'邮箱':<25}"
    print(header)
    print("-" * len(header))

    for i, c in enumerate(contacts, start=1):
        print(f"{i:<5}{c['name']:<10}{c['phone']:<16}{c['email']:<25}")

    print(f"\n共 {len(contacts)} 个联系人")


def search_contacts():
    """搜索联系人（按姓名模糊匹配）"""
    print("\n--- 搜索联系人 ---")
    keyword = input("请输入搜索关键字：").strip()
    if not keyword:
        print("搜索关键字不能为空！")
        return

    results = [c for c in contacts if keyword.lower() in c["name"].lower()]

    if not results:
        print(f"未找到姓名中包含「{keyword}」的联系人")
        return

    print(f"\n找到 {len(results)} 个匹配：")
    print(f"{'姓名':<10}{'电话':<16}{'邮箱':<25}")
    print("-" * 51)
    for c in results:
        print(f"{c['name']:<10}{c['phone']:<16}{c['email']:<25}")


def delete_contact():
    """按姓名删除联系人"""
    print("\n--- 删除联系人 ---")
    if not contacts:
        print("暂无联系人")
        return

    name = input("请输入要删除的联系人姓名：").strip()
    if not name:
        print("姓名不能为空！")
        return

    for i, c in enumerate(contacts):
        if c["name"] == name:
            if input(f"确定要删除「{name}」吗？（y/n）：").strip().lower() == "y":
                contacts.pop(i)
                save_contacts()
                print(f"联系人「{name}」已删除")
            else:
                print("已取消删除")
            return

    print(f"未找到名为「{name}」的联系人")


def main():
    """主程序"""
    load_contacts()

    while True:
        print("\n" + "=" * 40)
        print("       联系人管理系统")
        print("=" * 40)
        print("1. 查看所有联系人")
        print("2. 添加联系人")
        print("3. 搜索联系人")
        print("4. 删除联系人")
        print("5. 退出程序")
        print("-" * 40)

        choice = input("请选择操作（1-5）：").strip()

        if choice == "1":
            show_all_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
            print("再见！")
            break
        else:
            print("无效的选择，请输入 1-5")


if __name__ == "__main__":
    main()
```

---

## 五、运行测试

1. 将上面的完整代码保存为 `contact_manager.py`
2. 在终端运行：`python3 contact_manager.py`
3. 按菜单提示逐个测试 5 项功能
4. 退出程序后，检查目录下是否生成了 `contacts.json` 文件
5. 再次运行程序，验证之前添加的联系人是否还在

**测试检查点：**
- [ ] 添加联系人后，查看列表能显示
- [ ] 搜索"张"能匹配到"张三"
- [ ] 删除联系人后，列表不再显示
- [ ] 退出再重新运行，数据还在
- [ ] 输入无效菜单选项（如 "6" 或 "abc"），程序不崩溃

---

## 六、项目回顾

回顾一下这个项目中用到的知识点：

| 知识点 | 在项目中的应用 |
|--------|----------------|
| **list** | `contacts` 列表存储所有联系人 |
| **dict** | 每个联系人是一个 dict（name, phone, email） |
| **函数** | 每个功能封装成独立函数 |
| **f-string** | 格式化菜单和表格输出 |
| **if/elif/else** | 菜单选择分支 |
| **while 循环** | 菜单循环，直到用户选择退出 |
| **for 循环** | 遍历联系人列表、显示表格 |
| **list comprehension** | 搜索时的模糊匹配过滤 |
| **文件 IO（with open）** | 读写 JSON 文件 |
| **json 模块** | 数据的序列化与反序列化 |
| **异常处理（try/except）** | 处理文件不存在和 JSON 解析错误 |
| **global 变量** | 在函数中访问全局 contacts 列表 |
| **`__name__` == `__main__`** | 程序入口 |

---

## 七、扩展挑战（选做）

基础功能完成后，可以试试以下扩展：

### 挑战 1：按姓名排序显示
在 `show_all_contacts()` 中，让联系人按姓名拼音排序显示。

<details>
<summary>提示（点击展开）</summary>

```python
# 排序后再显示
sorted_contacts = sorted(contacts, key=lambda c: c["name"])
for i, c in enumerate(sorted_contacts, start=1):
    ...
```
</details>

### 挑战 2：修改联系人
增加"修改联系人"功能：输入姓名找到联系人，然后修改其电话或邮箱。

<details>
<summary>提示（点击展开）</summary>

```python
def edit_contact():
    name = input("请输入要修改的联系人姓名：").strip()
    for c in contacts:
        if c["name"] == name:
            new_phone = input(f"新电话（当前：{c['phone']}，直接回车保持不变）：").strip()
            new_email = input(f"新邮箱（当前：{c['email']}，直接回车保持不变）：").strip()
            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            save_contacts()
            print("修改成功！")
            return
    print(f"未找到「{name}」")
```
</details>

### 挑战 3：数据校验
在添加联系人时校验电话和邮箱格式（例如：电话必须是 11 位数字，邮箱必须包含 @）。

### 挑战 4：导出为 CSV
增加"导出联系人到 CSV 文件"功能。CSV 是一种可以用 Excel 打开的表格格式。

### 挑战 5：用 class 重构
把联系人管理器的数据和方法用 class 封装起来。

<details>
<summary>提示（点击展开）</summary>

```python
class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load()

    def load(self):
        ...

    def save(self):
        ...

    def add(self, name, phone, email):
        ...

    def search(self, keyword):
        ...

    def delete(self, name):
        ...

    def show_all(self):
        ...
```
</details>

---

## 八、检查清单

- [ ] 我完整阅读了项目的设计分析部分
- [ ] 我理解了每个函数的功能和实现思路
- [ ] 我能独立运行完整的联系人管理器
- [ ] 我测试了添加、查看、搜索、删除、退出所有功能
- [ ] 我验证了退出后再运行，数据能正确恢复
- [ ] 我至少尝试了一个扩展挑战

---

## 七天的学习之旅到此结束！

你已经从零开始掌握了 Python 的核心基础。接下来可以继续学习的方向：

- **面向对象编程**：深入理解 class、继承、多态
- **Web 开发**：Flask / Django / FastAPI
- **数据分析**：pandas, matplotlib
- **爬虫**：requests, BeautifulSoup, Scrapy
- **自动化**：批量处理文件、操作 Excel/Word

记住：**编程是一门手艺，光看不练是学不会的。每天写一点代码，保持手感！**
