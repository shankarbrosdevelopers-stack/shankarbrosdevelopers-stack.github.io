import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the hero section
content = re.sub(r'<section class="hero">.*?</section>', '', content, flags=re.DOTALL)

# Remove the reviews section
content = re.sub(r'<section class="reviews-section">.*?</section>', '', content, flags=re.DOTALL)

# Remove the about section
content = re.sub(r'<section id="about".*?</section>', '', content, flags=re.DOTALL)

# Add padding to apps section so it doesn't hide under the navbar
content = content.replace('<section id="apps" class="container">', '<section id="apps" class="container" style="padding-top: 8rem;">')

# Update title and meta
content = content.replace('<title>Shankarbros.dev | Colorful Android Apps</title>', '<title>Our Apps | Shankarbros.dev</title>')
content = content.replace('content="https://shankarbros.dev/index.html"', 'content="https://shankarbros.dev/apps.html"')

# Save to apps.html
with open('apps.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created apps.html")
