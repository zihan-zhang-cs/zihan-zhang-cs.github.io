import os
import re
import subprocess
from datetime import datetime

# 获取当前脚本所在目录
directory = os.path.dirname(os.path.abspath(__file__))

# 获取当前git仓库中被修改的文件（只包含md文件）


def get_modified_md_files():
    # 获取git状态，找出修改过的文件
    result = subprocess.run(['git', 'diff', '--name-only'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("Error getting git status:", result.stderr)
        return []

    modified_files = result.stdout.splitlines()
    # 过滤出md文件
    md_files = [file for file in modified_files if file.endswith(".md")]
    return md_files

# 获取当前时间并格式化为 "YYYY-MM-DD HH:mm:ss"


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 获取被修改的md文件列表
modified_md_files = get_modified_md_files()

# 如果没有修改过的md文件，直接结束
if not modified_md_files:
    print("No modified md files found, exit script.")
    exit()

# 遍历目录下所有的md文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md") and os.path.join(root, file) in modified_md_files:
            file_path = os.path.join(root, file)

            # 获取当前文件所在的子目录（去掉根目录部分）
            subdirectory = os.path.relpath(root, directory)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 使用正则表达式查找符合格式的图片链接，并替换为新的URL
            new_content = re.sub(
                r'!\[([^\]]+)\]\(\./([^\)]+)\)',  # 查找 ./<任何路径>/<图片名> 的格式
                lambda m: f'![{m.group(1)}](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/{subdirectory}/{m.group(2)})',
                content
            )

            # 如果内容有变化，则写回文件，并添加时间水印
            if new_content != content:
                # 获取当前时间水印
                timestamp = get_current_timestamp()

                # 将时间水印添加到文件末尾
                new_content += f"\n\n上传于 {timestamp}"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print("Replace image links in modified md files successfully, and add timestamp watermark.")
