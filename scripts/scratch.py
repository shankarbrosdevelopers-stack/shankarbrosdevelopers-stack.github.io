import re
import os

base_dir = os.path.dirname(__file__)
index_path = os.path.join(base_dir, "..", "index.html")
orig_path = os.path.join(base_dir, "..", "original_index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

with open(orig_path, "r", encoding="utf-16") as f:
    orig_html = f.read()

# Extract SVGs from original file
svg_map = {}
# Find href="..."
for match in re.finditer(r'<a href="([^"]+)"', orig_html):
    href = match.group(1)
    if href.startswith('#'): continue
    
    # Try to find the app-icon div for this href
    card_start = orig_html.find(f'<a href="{href}"')
    if card_start != -1:
        card_end = orig_html.find('</a>', card_start)
        card_content = orig_html[card_start:card_end]
        svg_div_match = re.search(r'<div class="app-icon"[^>]*>[\s\S]*?</div>', card_content)
        if svg_div_match:
            svg_map[href] = svg_div_match.group(0)

print(f"Found {len(svg_map)} SVGs")

for href, svg_div in svg_map.items():
    card_start = index_html.find(f'<a href="{href}"')
    if card_start != -1:
        card_end = index_html.find('</a>', card_start)
        card_content = index_html[card_start:card_end]
        
        img_match = re.search(r'<img [^>]*class="app-icon"[^>]*>', card_content)
        if img_match:
            img_tag = img_match.group(0)
            
            img_clean = img_tag.replace('margin-bottom: 1.5rem;', 'margin-bottom: 0;')
            svg_clean = svg_div.replace('margin-bottom: 1.5rem;', 'margin-bottom: 0; width: 56px; height: 56px; flex-shrink: 0;')
            
            combined = f'<div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">\n{svg_clean}\n{img_clean}\n</div>'
            new_card_content = card_content.replace(img_tag, combined)
            
            index_html = index_html[:card_start] + new_card_content + index_html[card_end:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Icons fixed!")
