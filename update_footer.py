import glob

SOCIAL_ICONS = '''            <!-- Social Media Icons -->
            <div style="display: flex; gap: 1.25rem; align-items: center;">
                <a href="https://facebook.com/shankarbro.dev" target="_blank" rel="noopener noreferrer" title="Facebook" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#1877F2'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                </a>
                <a href="https://instagram.com/shankarbros.dev" target="_blank" rel="noopener noreferrer" title="Instagram" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#E1306C'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                </a>
                <a href="https://x.com/shankarbros_dev" target="_blank" rel="noopener noreferrer" title="X (Twitter)" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#000000'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="https://youtube.com/@shankarbros.developers" target="_blank" rel="noopener noreferrer" title="YouTube" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#FF0000'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 12a29 29 0 0 0 .46 5.58A2.78 2.78 0 0 0 3.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.95A29 29 0 0 0 23 12a29 29 0 0 0-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white"/></svg>
                </a>
                <a href="https://reddit.com/r/shankarbros" target="_blank" rel="noopener noreferrer" title="Reddit" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#FF4500'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"/><path d="M20 12a2 2 0 0 0-3.37-1.44 9.85 9.85 0 0 0-5.13-1.63l.87-4.1 2.83.6a1.5 1.5 0 1 0 1.55-1.47 1.5 1.5 0 0 0-1.35.85l-3.16-.67a.25.25 0 0 0-.29.19l-1 4.57a9.88 9.88 0 0 0-5.18 1.64A2 2 0 1 0 4 13a3.56 3.56 0 0 0 0 .5c0 2.55 3.58 4.62 8 4.62s8-2.07 8-4.62a3.56 3.56 0 0 0 0-.5A2 2 0 0 0 20 12zm-12.5 1a1 1 0 1 1 1 1 1 1 0 0 1-1-1zm5.5 2.81a3.34 3.34 0 0 1-2-.52.25.25 0 0 1 .3-.4 2.85 2.85 0 0 0 1.7.42 2.85 2.85 0 0 0 1.7-.42.25.25 0 1 1 .3.4 3.34 3.34 0 0 1-2 .52zm.5-1.81a1 1 0 1 1 1-1 1 1 0 0 1-1 1z" fill="white"/></svg>
                </a>
                <a href="https://linkedin.com/company/shankarbros" target="_blank" rel="noopener noreferrer" title="LinkedIn" style="color: var(--text-secondary); transition: color 0.2s;" onmouseover="this.style.color='#0A66C2'" onmouseout="this.style.color=''">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                </a>
            </div>
'''

MARKER = '            <div style="display: flex; gap: 1.5rem; font-size: 0.9rem;">'

for file in ['about.html', 'apps.html', 'contact.html', 'privacy.html', 'terms.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if MARKER in content and '<!-- Social Media Icons -->' not in content:
        # Find the footer's link div (the first occurrence that is in footer context)
        # Replace gap: 1rem with gap: 1.5rem in container to spread things out
        content = content.replace(
            'gap: 1rem; padding-top: 3rem; padding-bottom: 3rem;',
            'gap: 1.5rem; padding-top: 3rem; padding-bottom: 3rem;'
        )
        content = content.replace(MARKER, SOCIAL_ICONS + MARKER, 1)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} (already updated or marker not found)")

print("Done!")
