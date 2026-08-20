import re
import os
import glob

base_dir = os.path.dirname(__file__)
html_files = glob.glob(os.path.join(base_dir, "..", "*.html"))
gen_script = os.path.join(base_dir, "gen_scraped.py")

# Update all HTML files
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to remove the spaces around the span and use a very small margin, e.g. 0.2rem
    # Original: Shankarbros.dev <span style="color: var(--text-secondary); margin: 0 0.1rem; font-weight: 300;">/</span> App Name
    # Target: Shankarbros.dev<span style="color: var(--text-secondary); margin: 0 0.3rem; font-weight: 300;">/</span>App Name
    
    new_content = re.sub(
        r'Shankarbros\.dev\s*<span style="([^"]*margin:[^"]*)">/</span>\s*([^<]+)',
        r'Shankarbros.dev<span style="\1">/</span>\2',
        content
    )
    
    # Let's also adjust the margin to be exactly what we want
    new_content = re.sub(
        r'margin:\s*0\s*0\.1rem;',
        r'margin: 0 0.3rem;',
        new_content
    )
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)

# Update gen_scraped.py so it generates the right spacing in the future
with open(gen_script, "r", encoding="utf-8") as f:
    gen_content = f.read()

gen_content = gen_content.replace(
    'Shankarbros.dev <span style="color: var(--text-secondary); margin: 0 0.1rem; font-weight: 300;">/</span> {s_app["nav_name"]}',
    'Shankarbros.dev<span style="color: var(--text-secondary); margin: 0 0.3rem; font-weight: 300;">/</span>{s_app["nav_name"]}'
)

with open(gen_script, "w", encoding="utf-8") as f:
    f.write(gen_content)

print("Gap decreased across all files!")
