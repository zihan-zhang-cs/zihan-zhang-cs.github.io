import os
import re
import subprocess
from datetime import datetime

# 获取当前脚本所在目录
directory = os.path.dirname(os.path.abspath(__file__))


def get_modified_md_files():
    """获取git状态中被修改的md文件"""
    result = subprocess.run(['git', 'diff', '--name-only'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print("Error getting git status:", result.stderr)
        return []
    modified_files = result.stdout.splitlines()
    return [file for file in modified_files if file.endswith(".md")]


def get_current_timestamp():
    """返回当前时间字符串"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 获取被修改的md文件列表
modified_md_files = get_modified_md_files()

if not modified_md_files:
    print("No modified md files found, exit script.")
    exit()

modified_md_files = [os.path.relpath(file, directory)
                     for file in modified_md_files]

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, directory)

            if relative_file_path in modified_md_files:
                print(f"Processing: {file_path}")
                subdirectory = os.path.relpath(root, directory)

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replace_local_image(match):
                    alt_text = match.group(1)
                    image_path = match.group(2)
                    # 如果是网络图片，不修改
                    if image_path.startswith("http://") or image_path.startswith("https://"):
                        return match.group(0)
                    # 替换为 GitHub 图片链接
                    return f'![{alt_text}](https://github.com/zihan-zhang-cs/zihan-zhang-cs.github.io/blob/master/_posts/{subdirectory}/{image_path}?raw=true)'

                # 匹配本地图片链接，形如 ![alt](./xxx) 或 ![alt](image/xxx)
                new_content = re.sub(
                    r'!\[([^\]]+)\]\((?:\.\/)?([^)]+)\)',
                    replace_local_image,
                    content
                )

                if new_content != content:
                    timestamp = get_current_timestamp()
                    new_content += f"\n\n上传于 {timestamp}"

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

print("✅ Replace image links in modified md files successfully (network images kept unchanged), and add timestamp watermark.")
