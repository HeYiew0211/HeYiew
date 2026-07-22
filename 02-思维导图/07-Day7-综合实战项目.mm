<map version="1.0.1">
<node TEXT="Day 7 综合实战项目 🎯">
<node TEXT="命令行工具 CLI">
<node TEXT="argparse">
<node TEXT="ArgumentParser">
</node>
<node TEXT="add_argument()">
</node>
<node TEXT="parse_args()">
</node>
</node>
<node TEXT="交互菜单">
<node TEXT="while True 循环菜单">
</node>
<node TEXT="数字选择功能">
</node>
<node TEXT="input() 读取选项">
</node>
</node>
<node TEXT="sys.argv">
<node TEXT="简单参数获取">
</node>
</node>
</node>
<node TEXT="数据持久化">
<node TEXT="JSON">
<node TEXT="基本用法">
<node TEXT="json.dumps() dict -&gt; str">
</node>
<node TEXT="json.loads() str -&gt; dict">
</node>
<node TEXT="indent=2 美化输出">
</node>
<node TEXT="ensure_ascii=False">
</node>
</node>
<node TEXT="文件读写">
<node TEXT="json.dump(data, f)">
</node>
<node TEXT="data = json.load(f)">
</node>
</node>
<node TEXT="适用场景">
<node TEXT="配置文件 config.json">
</node>
<node TEXT="数据存储">
</node>
<node TEXT="简单数据库">
</node>
</node>
</node>
</node>
<node TEXT="模块化设计">
<node TEXT="代码拆分">
<node TEXT="主程序 main.py">
</node>
<node TEXT="工具函数 utils.py">
</node>
<node TEXT="数据模型 models.py">
</node>
</node>
<node TEXT="包 package">
<node TEXT="文件夹 + __init__.py">
</node>
<node TEXT="from package import module">
</node>
</node>
<node TEXT="if __name__ == &quot;__main__&quot;:">
<node TEXT="入口判断">
</node>
</node>
</node>
<node TEXT="项目打包">
<node TEXT="requirements.txt">
<node TEXT="pip freeze &gt; requirements.txt">
</node>
<node TEXT="pip install -r requirements.txt">
</node>
</node>
<node TEXT=".gitignore">
<node TEXT="__pycache__/">
</node>
<node TEXT="*.pyc">
</node>
<node TEXT="venv/">
</node>
</node>
</node>
<node TEXT="项目示例：命令行备忘录">
<node TEXT="功能：添加/查看/删除记录，保存到 JSON">
</node>
<node TEXT="文件组织">
<node TEXT="memo/">
</node>
<node TEXT="  __init__.py">
</node>
<node TEXT="  cli.py">
</node>
<node TEXT="  storage.py">
</node>
<node TEXT="  models.py">
</node>
<node TEXT="main.py">
</node>
</node>
</node>
</node>
</map>