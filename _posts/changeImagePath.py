import os
import re

# 获取当前脚本所在目录
directory = os.path.dirname(os.path.abspath(__file__))

# 遍历目录下所有的md文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):  # 只处理md文件
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 使用正则表达式查找符合格式的图片链接
            new_content = re.sub(
                r'!\[([^\]]+)\]\(\./assets/([^\)]+)\)',
                r'![\1](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/assets/\2?raw=true)',
                content
            )

            # 如果内容有变化，则写回文件
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("完成图片链接替换！")
