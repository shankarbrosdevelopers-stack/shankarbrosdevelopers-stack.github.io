import re
import os

base_dir = os.path.dirname(__file__)
index_path = os.path.join(base_dir, "..", "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

svgs = {
    "vastu-compass.html": '<div class="app-icon" style="background: var(--pastel-orange); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg></div>',
    "telugu-calendar.html": '<div class="app-icon" style="background: var(--pastel-pink); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ec4899" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>',
    "hanuman-chalisa.html": '<div class="app-icon" style="background: var(--pastel-yellow); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ca8a04" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>',
    "bubble-level.html": '<div class="app-icon" style="background: var(--pastel-green); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2" ry="2"></rect><circle cx="12" cy="12" r="2"></circle></svg></div>',
    "ftp-server.html": '<div class="app-icon" style="background: var(--pastel-blue); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg></div>',
    "floatprompt.html": '<div class="app-icon" style="background: var(--pastel-purple); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#9333ea" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6z"></path><path d="M14 3v5h5M16 13H8M16 17H8M10 9H8"></path></svg></div>',
    "telugu-toolkit.html": '<div class="app-icon" style="background: var(--pastel-orange); width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>'
}

for href, svg_div in svgs.items():
    card_start = index_html.find(f'<a href="{href}"')
    if card_start != -1:
        card_end = index_html.find('</a>', card_start)
        card_content = index_html[card_start:card_end]
        
        # Check if we already added a flex container
        if '<div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">' in card_content:
            continue
            
        img_match = re.search(r'<img [^>]*class="app-icon"[^>]*>', card_content)
        if img_match:
            img_tag = img_match.group(0)
            img_clean = img_tag.replace('margin-bottom: 1.5rem;', 'margin-bottom: 0;')
            
            combined = f'<div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">\n{svg_div}\n{img_clean}\n</div>'
            new_card_content = card_content.replace(img_tag, combined)
            
            index_html = index_html[:card_start] + new_card_content + index_html[card_end:]

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Icons successfully combined side-by-side!")
