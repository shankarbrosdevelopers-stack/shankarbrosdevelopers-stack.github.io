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
card_pattern = re.compile(r'<a href="([^"]+)" class="app-card">[\s\S]*?<div class="app-icon"[^>]*>.*?</div>', re.DOTALL)
for match in card_pattern.finditer(orig_html):
    href = match.group(1)
    svg_div_match = re.search(r'<div class="app-icon"[^>]*>.*?</div>', match.group(0), re.DOTALL)
    if svg_div_match:
        svg_map[href] = svg_div_match.group(0)

# Inject SVGs back into index.html next to the new img icons
for href, svg_div in svg_map.items():
    # Find the app card and its img tag
    card_start = f'<a href="{href}"'
    
    # We will just do a string replacement for the img tag inside this specific card
    start_idx = index_html.find(card_start)
    if start_idx != -1:
        end_idx = index_html.find('</a>', start_idx)
        card_content = index_html[start_idx:end_idx]
        
        img_match = re.search(r'<img [^>]*class="app-icon"[^>]*>', card_content)
        if img_match:
            img_tag = img_match.group(0)
            # Remove margin-bottom from img tag since it goes in a flex container
            img_tag_clean = img_tag.replace('margin-bottom: 1.5rem;', 'margin-bottom: 0;')
            svg_div_clean = svg_div.replace('margin-bottom: 1.5rem;', 'margin-bottom: 0;')
            
            combined = f'<div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">\n{svg_div_clean}\n{img_tag_clean}\n</div>'
            
            new_card_content = card_content.replace(img_tag, combined)
            index_html = index_html[:start_idx] + new_card_content + index_html[end_idx:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Icons successfully combined!")
