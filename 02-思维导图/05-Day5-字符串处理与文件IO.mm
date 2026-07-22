<map version="1.0.1">
<node TEXT="Day 5 字符串与文件">
<node TEXT="字符串方法">
<node TEXT="分割与合并">
<node TEXT="s.split(sep) 分割为列表">
</node>
<node TEXT="s.splitlines() 按行分割">
</node>
<node TEXT="sep.join(iterable) 合并">
</node>
</node>
<node TEXT="清理">
<node TEXT="s.strip() 去两端空白">
</node>
<node TEXT="s.lstrip() 去左侧">
</node>
<node TEXT="s.rstrip() 去右侧">
</node>
<node TEXT="s.replace(old, new) 替换">
</node>
</node>
<node TEXT="大小写">
<node TEXT="s.upper() 全大写">
</node>
<node TEXT="s.lower() 全小写">
</node>
<node TEXT="s.title() 首字母大写">
</node>
<node TEXT="s.capitalize() 首字符大写">
</node>
</node>
<node TEXT="查找与判断">
<node TEXT="s.find(sub) 找子串">
</node>
<node TEXT="s.startswith(prefix)">
</node>
<node TEXT="s.endswith(suffix)">
</node>
<node TEXT="s.count(sub) 计数">
</node>
</node>
<node TEXT="判断方法">
<node TEXT="s.isdigit()">
</node>
<node TEXT="s.isalpha()">
</node>
<node TEXT="s.isalnum()">
</node>
</node>
</node>
<node TEXT="f-string 进阶">
<node TEXT="格式化数字">
<node TEXT="{num:.2f} 保留两位小数">
</node>
<node TEXT="{num:.0%} 百分比">
</node>
<node TEXT="{num:.2e} 科学计数">
</node>
</node>
<node TEXT="对齐与填充">
<node TEXT="{text:&lt;10} 左对齐">
</node>
<node TEXT="{text:&gt;10} 右对齐">
</node>
<node TEXT="{text:^10} 居中对齐">
</node>
<node TEXT="{text:*^10} 填充字符">
</node>
</node>
<node TEXT="千分位与进制">
<node TEXT="{num:,} 千分位">
</node>
<node TEXT="{num:b} 二进制">
</node>
<node TEXT="{num:x} 十六进制">
</node>
</node>
</node>
<node TEXT="文件操作">
<node TEXT="打开文件">
<node TEXT="f = open(path, mode)">
</node>
<node TEXT="模式 r 读 w 写 a 追加">
</node>
<node TEXT="编码 encoding=&quot;utf-8&quot;">
</node>
</node>
<node TEXT="读取">
<node TEXT="f.read() 读全部">
</node>
<node TEXT="f.readline() 读一行">
</node>
<node TEXT="f.readlines() 读所有行">
</node>
<node TEXT="for line in f 逐行读取">
</node>
</node>
<node TEXT="写入">
<node TEXT="f.write(text)">
</node>
<node TEXT="f.writelines(lines)">
</node>
</node>
<node TEXT="with 语句">
<node TEXT="with open() as f:">
</node>
<node TEXT="自动关闭文件">
</node>
<node TEXT="推荐始终使用 with">
</node>
</node>
<node TEXT="pathlib">
<node TEXT="Path 对象">
</node>
<node TEXT="路径拼接 /">
</node>
<node TEXT=".read_text()">
</node>
</node>
</node>
</node>
</map>