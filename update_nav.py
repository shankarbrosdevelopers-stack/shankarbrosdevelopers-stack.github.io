import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the link
    new_content = content.replace('href="#apps">Apps</a>', 'href="apps.html">Apps</a>')
    new_content = new_content.replace('href="index.html#apps">Apps</a>', 'href="apps.html">Apps</a>')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

print("Done updating nav links.")
