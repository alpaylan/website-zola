
# Remove Style from all HTML files in the current directory

import os

cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith(".html"):
        with open(file, 'r', encoding="utf-8") as f:
            content = f.read()
        style_start = content.find("<style>")
        style_end = content.find("</style>") + len("</style>")

        if style_start != -1 and style_end != -1:
            content = content[:style_start] + content[style_end:]
            with open(file, 'w', encoding="utf-8") as f:
                f.write(content)
        else:
            print(f"No style found in {file}")
