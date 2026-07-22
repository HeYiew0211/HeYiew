<map version="1.0.1">
<node TEXT="Day 6 异常处理与推导式">
<node TEXT="异常处理">
<node TEXT="try...except">
<node TEXT="try 包裹可能出错的代码">
</node>
<node TEXT="except 捕获指定异常">
</node>
<node TEXT="多个 except 分支">
</node>
<node TEXT="except Exception as e">
</node>
</node>
<node TEXT="finally">
<node TEXT="无论是否异常都执行">
</node>
<node TEXT="常用于释放资源">
</node>
</node>
<node TEXT="else">
<node TEXT="try 无异常时执行">
</node>
</node>
<node TEXT="常见异常">
<node TEXT="ValueError 值错误">
</node>
<node TEXT="TypeError 类型错误">
</node>
<node TEXT="KeyError 键不存在">
</node>
<node TEXT="IndexError 索引越界">
</node>
<node TEXT="FileNotFoundError 文件未找到">
</node>
<node TEXT="ZeroDivisionError 除以零">
</node>
</node>
<node TEXT="raise">
<node TEXT="手动抛出异常">
</node>
<node TEXT="raise ValueError(&quot;原因&quot;)">
</node>
</node>
<node TEXT="自定义异常">
<node TEXT="class MyError(Exception)">
</node>
</node>
</node>
<node TEXT="list comprehension">
<node TEXT="基本语法">
<node TEXT="[表达式 for item in 可迭代对象]">
</node>
<node TEXT="[x*2 for x in range(10)]">
</node>
</node>
<node TEXT="带条件过滤">
<node TEXT="[x for x in lst if x &gt; 0]">
</node>
</node>
<node TEXT="嵌套">
<node TEXT="[(x, y) for x in a for y in b]">
</node>
</node>
</node>
<node TEXT="dict comprehension">
<node TEXT="基本语法">
<node TEXT="{k: v for item in seq}">
</node>
<node TEXT="{x: x**2 for x in range(5)}">
</node>
</node>
<node TEXT="带条件">
<node TEXT="{k: v for k, v in d.items() if v &gt; 0}">
</node>
</node>
<node TEXT="键值互换">
<node TEXT="{v: k for k, v in d.items()}">
</node>
</node>
</node>
<node TEXT="面向对象入门">
<node TEXT="类与对象">
<node TEXT="class 类名:">
</node>
<node TEXT="类名用 PascalCase">
</node>
</node>
<node TEXT="构造方法">
<node TEXT="def __init__(self, ...):">
</node>
<node TEXT="self.属性 = 参数">
</node>
</node>
<node TEXT="self">
<node TEXT="代表实例本身">
</node>
<node TEXT="必须显式写">
</node>
</node>
<node TEXT="实例方法">
<node TEXT="def method(self, ...):">
</node>
<node TEXT="必须带 self 参数">
</node>
</node>
<node TEXT="创建实例">
<node TEXT="obj = ClassName(args)">
</node>
<node TEXT="obj.method()">
</node>
</node>
</node>
</node>
</map>