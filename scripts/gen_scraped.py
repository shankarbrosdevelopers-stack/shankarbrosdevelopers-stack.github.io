import os
import re
import json

base_dir = os.path.dirname(__file__)
app_html_path = os.path.join(base_dir, "..", "app.html")

with open(app_html_path, "r", encoding="utf-8") as f:
    template = f.read()

apps_data_path = os.path.join(base_dir, "apps_data.json")
with open(apps_data_path, "r", encoding="utf-8") as f:
    scraped_data = json.load(f)

reviews_path = os.path.join(base_dir, "..", "reviews.json")
with open(reviews_path, "r", encoding="utf-8") as f:
    all_reviews = json.load(f)

# Map our static visual features to the scraped app IDs
static_apps = {
    "com.shankarbros.vastucompass": {
        "filename": "vastu-compass.html",
        "nav_name": "Vastu Compass",
        "badge": "🧭 Vastu Compass · Lifestyle",
        "badge_color": "var(--accent-purple)",
        "hero_h1": "AI-powered <span>guidance.</span>",
        "features": [
            ("var(--pastel-orange)", "🧭", "High Precision", "Accurate compass readings for your home."),
            ("var(--pastel-blue)", "🏠", "Room Analysis", "Check Vastu for bedroom, kitchen, and more."),
            ("var(--pastel-green)", "✨", "Expert Tips", "Get actionable Vastu remedies."),
            ("var(--pastel-purple)", "🌍", "12+ Languages", "Available in multiple Indian languages."),
            ("var(--pastel-pink)", "🔒", "Privacy First", "Minimum intrusive ads to safeguard focus."),
            ("var(--pastel-yellow)", "📱", "Material You", "Beautiful modern design interface.")
        ],
        "steps_title": "Three steps to harmony 🧭",
        "steps": [
            ("var(--pastel-orange)", "01", "Calibrate", "Calibrate your phone's compass."),
            ("var(--pastel-blue)", "02", "Point", "Point your phone towards a room."),
            ("var(--pastel-green)", "03", "Analyze", "Get instant Vastu feedback.")
        ],
        "cta_title": "Ready to harmonize your space?",
        "mockup": "bloom_mockup.png" # Ideally replace with real mockups if available
    },
    "com.shankarbros.telugu2026calendarandrasiphalalu": {
        "filename": "telugu-calendar.html",
        "nav_name": "Telugu Calendar",
        "badge": "📅 Telugu Calendar · Lifestyle",
        "badge_color": "var(--accent-pink)",
        "hero_h1": "Your daily <span>Panchangam.</span>",
        "features": [
            ("var(--pastel-yellow)", "📅", "Daily Panchangam", "Accurate daily astrological info."),
            ("var(--pastel-pink)", "🎉", "Festivals", "Never miss an important date."),
            ("var(--pastel-blue)", "🔮", "Rasi Phalalu", "Daily and weekly horoscopes."),
            ("var(--pastel-green)", "📖", "Vedic Slokas", "Read and learn important slokas."),
            ("var(--pastel-purple)", "🔔", "Reminders", "Set custom festival alerts."),
            ("var(--pastel-orange)", "📱", "Widgets", "Beautiful home screen widgets.")
        ],
        "steps_title": "Three steps to start 📅",
        "steps": [
            ("var(--pastel-yellow)", "01", "Open", "Launch the calendar app."),
            ("var(--pastel-pink)", "02", "Browse", "View today's Panchangam."),
            ("var(--pastel-blue)", "03", "Plan", "Check upcoming festivals.")
        ],
        "cta_title": "Ready to stay organized?",
        "mockup": "bloom_mockup.png"
    },
    "com.shankarbros.hanumanchalisa": {
        "filename": "hanuman-chalisa.html",
        "nav_name": "Hanuman Chalisa",
        "badge": "🕉️ Hanuman Chalisa · Spiritual",
        "badge_color": "var(--accent-orange)",
        "hero_h1": "Read, listen, <span>track.</span>",
        "features": [
            ("var(--pastel-orange)", "📖", "Read Clear", "Large, readable fonts."),
            ("var(--pastel-blue)", "🎧", "Listen Offline", "High-quality audio playback."),
            ("var(--pastel-green)", "✅", "Track Chants", "Keep a daily tally of your chants."),
            ("var(--pastel-purple)", "🌙", "Dark Mode", "Comfortable reading at night."),
            ("var(--pastel-pink)", "🛑", "Minimum Ads", "Designed to safeguard user focus."),
            ("var(--pastel-yellow)", "🌍", "Multiple Languages", "Read in Hindi, English, and more.")
        ],
        "steps_title": "Three steps to devotion 🕉️",
        "steps": [
            ("var(--pastel-orange)", "01", "Open", "Launch the app daily."),
            ("var(--pastel-blue)", "02", "Chant", "Read or listen along."),
            ("var(--pastel-green)", "03", "Track", "Log your completed chants.")
        ],
        "cta_title": "Ready to start chanting?",
        "mockup": "bloom_mockup.png"
    },
    "com.shankarbros.bubblelevel": {
        "filename": "bubble-level.html",
        "nav_name": "Bubble Level",
        "badge": "📐 Bubble Level · Tools",
        "badge_color": "var(--accent-green)",
        "hero_h1": "High precision <span>leveling.</span>",
        "features": [
            ("var(--pastel-green)", "📐", "High Accuracy", "Precise measurement to the degree."),
            ("var(--pastel-blue)", "🔒", "Lock Screen", "Lock readings for easy viewing."),
            ("var(--pastel-yellow)", "🔔", "Sound Alerts", "Beep when perfectly level."),
            ("var(--pastel-purple)", "📏", "Ruler Tool", "Built-in straight edge ruler."),
            ("var(--pastel-pink)", " Калибр", "Calibration", "Calibrate for perfect accuracy."),
            ("var(--pastel-orange)", "🌙", "Night Mode", "Easy to read in dark environments.")
        ],
        "steps_title": "Three steps to level 📐",
        "steps": [
            ("var(--pastel-green)", "01", "Place", "Place your phone on the surface."),
            ("var(--pastel-blue)", "02", "Adjust", "Move until the bubble centers."),
            ("var(--pastel-yellow)", "03", "Lock", "Lock the screen to save the reading.")
        ],
        "cta_title": "Ready to level up?",
        "mockup": "bloom_mockup.png"
    },
    "com.shankarbros.teleprompter": {
        "filename": "floatprompt.html",
        "nav_name": "FloatPrompt",
        "badge": "📝 FloatPrompt · Tools",
        "badge_color": "var(--accent-purple)",
        "hero_h1": "Smooth video <span>recording.</span>",
        "features": [
            ("var(--pastel-purple)", "📺", "Floating Widget", "Works over any app."),
            ("var(--pastel-blue)", "⚡", "Adjustable Speed", "Control scrolling speed easily."),
            ("var(--pastel-green)", "📝", "Import Scripts", "Easily load your text files."),
            ("var(--pastel-yellow)", "🎨", "Customizable", "Change font size and colors."),
            ("var(--pastel-pink)", "🔒", "Privacy", "No internet connection required."),
            ("var(--pastel-orange)", "📱", "Material Design", "Clean and intuitive interface.")
        ],
        "steps_title": "Three steps to record 📝",
        "steps": [
            ("var(--pastel-purple)", "01", "Import", "Load your script into the app."),
            ("var(--pastel-blue)", "02", "Float", "Launch the floating widget."),
            ("var(--pastel-green)", "03", "Record", "Open your camera and start reading.")
        ],
        "cta_title": "Ready for smooth recording?",
        "mockup": "bloom_mockup.png"
    },
    "com.shankarbros.telugutoolkit": {
        "filename": "telugu-toolkit.html",
        "nav_name": "Telugu Toolkit",
        "badge": "🛠️ Telugu Toolkit · Tools",
        "badge_color": "var(--accent-orange)",
        "hero_h1": "All-in-one <span>utility.</span>",
        "features": [
            ("var(--pastel-orange)", "🛠️", "Multiple Tools", "Everything you need in one place."),
            ("var(--pastel-blue)", "💬", "Telugu First", "Fully localized interface."),
            ("var(--pastel-green)", "⚡", "Fast & Light", "Takes up minimal storage space."),
            ("var(--pastel-purple)", "🔒", "Secure", "Your data stays on your device."),
            ("var(--pastel-pink)", "🛑", "Minimum Ads", "Designed to safeguard user focus."),
            ("var(--pastel-yellow)", "📱", "Modern UI", "Easy to navigate and use.")
        ],
        "steps_title": "Three steps to simplify 🛠️",
        "steps": [
            ("var(--pastel-orange)", "01", "Open", "Launch the toolkit."),
            ("var(--pastel-blue)", "02", "Select", "Choose the tool you need."),
            ("var(--pastel-green)", "03", "Use", "Enjoy a seamless experience.")
        ],
        "cta_title": "Ready to get the toolkit?",
        "mockup": "bloom_mockup.png"
    },
    "com.shankarbros.ftpserver": {
        "filename": "ftp-server.html",
        "nav_name": "FTP Server",
        "badge": "⚡ FTP Server · Productivity",
        "badge_color": "var(--accent-blue)",
        "hero_h1": "Wireless <span>transfer.</span>",
        "features": [
            ("var(--pastel-blue)", "⚡", "High speed", "Blazing fast transfer speeds over WiFi."),
            ("var(--pastel-purple)", "🔒", "Secure access", "Optional password protection and SSL/TLS support."),
            ("var(--pastel-green)", "🔄", "Background service", "Keep the server running even when the app is closed."),
            ("var(--pastel-pink)", "👥", "Multiple users", "Configure multiple accounts with specific permissions."),
            ("var(--pastel-yellow)", "⚙️", "Advanced settings", "Custom ports, root directory paths, and anonymous login."),
            ("var(--pastel-orange)", "📱", "Material Design", "Modern, beautiful interface with Material You support.")
        ],
        "steps_title": "Three steps to connect ⚡",
        "steps": [
            ("var(--pastel-blue)", "01", "Start", "Tap the power button to start the server."),
            ("var(--pastel-purple)", "02", "Connect", "Use the provided IP and Port in your FTP client."),
            ("var(--pastel-green)", "03", "Transfer", "Move your files instantly. No cables needed.")
        ],
        "cta_title": "Go wireless today.",
        "mockup": "ftp_server_mockup.jpg"
    }
}

def replace_between(text, start_marker, end_marker, replacement):
    pattern = re.compile(f'({re.escape(start_marker)}).*?({re.escape(end_marker)})', re.DOTALL)
    return pattern.sub(f'\\1\\n{replacement}\\n\\2', text)

for app_data in scraped_data:
    app_id = app_data['appId']
    if app_id not in static_apps:
        continue
    
    s_app = static_apps[app_id]
    content = template
    
    # Simple replacements
    content = re.sub(r'<title>.*?</title>', f'<title>{app_data["title"]}</title>', content)
    content = re.sub(r'Shankarbros.dev <span.*?/</span> Bloom', f'Shankarbros.dev <span style="color: var(--text-secondary); margin: 0 0.1rem; font-weight: 300;">/</span> {s_app["nav_name"]}', content)
    content = re.sub(r'<span class="badge" style="color: var\(--accent-pink\);">.*?</span>', f'<span class="badge" style="color: {s_app["badge_color"]};">{s_app["badge"]}</span>', content)
    content = re.sub(r'<h1>.*?<span>.*?</span></h1>', f'<h1>{s_app["hero_h1"]}</h1>', content)
    
    # Use real summary for hero desc
    content = re.sub(r'<p>Bloom turns building good routines into a colorful little game.*?.</p>', f'<p>{app_data["summary"]}</p>', content)

    # SEO and Social Meta Replacements
    desc_content = f"Shankarbros.dev - {app_data['title']}. We build calm, minimal, and privacy-focused Android applications."
    content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc_content}">', content)
    content = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{app_data["title"]}">', content)
    content = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc_content}">', content)
    content = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://shankarbros.dev/{s_app["filename"]}">', content)
    content = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{app_data["title"]}">', content)
    content = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{desc_content}">', content)
    content = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://shankarbros.dev/{s_app["filename"]}">', content)
    
    # Inject real installs and dynamic rating
    score = app_data.get("score")
    if score and float(score) > 0:
        rating_text = f" · ⭐ {float(score):.1f}"
    else:
        rating_text = " · ⭐ New"
        
    installs = app_data.get("installs", "10k+")
    content = re.sub(r'<span>120k\+ happy bloomers · ⭐ 4\.9</span>', f'<span>{installs} downloads on Google Play{rating_text}</span>', content)
    
    content = re.sub(r'<h2>Three steps to bloom 🌱</h2>', f'<h2>{s_app["steps_title"]}</h2>', content)
    # Use the real screenshot as the hero image. Use the second screenshot ONLY for Vastu Compass.
    if app_data.get("screenshots"):
        if s_app.get("filename") == "vastu-compass.html" and len(app_data["screenshots"]) > 1:
            hero_screenshot = app_data["screenshots"][1]
        else:
            hero_screenshot = app_data["screenshots"][0]
    else:
        hero_screenshot = s_app['mockup']
        
    content = content.replace('bloom_mockup.png', hero_screenshot)
    
    # Adjust hero image styling slightly since it's a raw screenshot now, not a mockup frame
    content = content.replace('border-radius: 40px;', 'border-radius: 24px;')

    # Create a Screenshots Gallery section if there are multiple screenshots
    if app_data.get("screenshots"):
        gallery_images = ""
        
        # Filter out the hero screenshot so it's not duplicated in the gallery
        gallery_screenshots = [url for url in app_data["screenshots"] if url != hero_screenshot]
        
        # Limit to exactly 4 screenshots to form one perfect row in our new 4-column layout
        # This naturally excludes tablet screenshots which usually appear later in the list
        display_screenshots = gallery_screenshots[:4]
        
        for idx, url in enumerate(display_screenshots):
            gallery_images += f"""                <img src="{url}=w800" alt="Screenshot {idx+1}" style="width: 100%; height: auto; border-radius: 20px; box-shadow: 0 15px 35px -10px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05); object-fit: contain; background: var(--bg-secondary); transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)';" onmouseout="this.style.transform='none';">\n"""
        
        gallery_html = f'''
        <section class="container" style="margin-top: 4rem; margin-bottom: 4rem;">
            <div class="section-header" style="margin-bottom: 3rem; text-align: center;">
                <span class="badge" style="color: {s_app['badge_color']}; background: color-mix(in srgb, {s_app['badge_color']} 15%, transparent);">GALLERY</span>
                <h2 style="font-size: 2.5rem; margin-top: 1rem;">Inside the app</h2>
            </div>
            
            <style>
                .screenshots-grid {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 1.5rem;
                    align-items: start;
                }}
                @media (max-width: 900px) {{
                    .screenshots-grid {{ grid-template-columns: repeat(2, 1fr); }}
                }}
                @media (max-width: 500px) {{
                    .screenshots-grid {{ grid-template-columns: 1fr; }}
                }}
            </style>
            
            <div class="screenshots-grid">
{gallery_images}
            </div>
        </section>
'''
        # Inject the gallery right before the features section
        content = content.replace('<section id="features" class="container">', f'{gallery_html}\n        <section id="features" class="container">')

    # Video Section
    if app_data.get("video"):
        video_url = app_data["video"]
        video_html = f'''
        <section class="container" style="margin-top: 4rem; margin-bottom: 4rem;">
            <div class="section-header" style="margin-bottom: 3rem; text-align: center;">
                <span class="badge" style="color: {s_app['badge_color']}; background: color-mix(in srgb, {s_app['badge_color']} 15%, transparent);">VIDEO TUTORIAL</span>
                <h2 style="font-size: 2.5rem; margin-top: 1rem;">See it in action</h2>
            </div>
            <div style="max-width: 900px; margin: 0 auto; border-radius: 24px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);">
                <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
                    <iframe src="{video_url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>
        </section>
'''
        content = content.replace('<section id="features" class="container">', f'{video_html}\n        <section id="features" class="container">')

    # Features Grid
    features_html = ""
    for color, icon, ftitle, fdesc in s_app["features"]:
        features_html += f'''
                <div class="feature-card-app">
                    <div class="feature-icon-box" style="background: {color}; font-size: 1.5rem; display: flex; align-items: center; justify-content: center;">
                        {icon}
                    </div>
                    <h3>{ftitle}</h3>
                    <p>{fdesc}</p>
                </div>'''
    
    content = replace_between(content, '<div class="features-grid">', '</section>', f'{features_html}\n            </div>')
    
    # Steps Container
    steps_html = ""
    for color, num, stitle, sdesc in s_app["steps"]:
        steps_html += f'''
                <div class="step-card" style="background: {color};">
                    <div class="step-number">{num}</div>
                    <h3>{stitle}</h3>
                    <p>{sdesc}</p>
                </div>'''
    
    content = replace_between(content, '<div class="steps-container">', '</section>', f'{steps_html}\n            </div>')

    # Fix links
    content = content.replace('href="#" class="btn btn-dark"', f'href="{app_data["url"]}" class="btn btn-dark" target="_blank"')

    # Process description HTML to make it more interesting
    desc_html = app_data["descriptionHTML"]
    
    # 1. Convert <br><br> to proper paragraphs for better spacing
    desc_html = desc_html.replace('<br><br>', '</p><p style="margin-bottom: 1.5rem;">')
    desc_html = f'<p style="margin-bottom: 1.5rem;">{desc_html}</p>'
    
    # 2. Highlight headers (lines that end with a colon and don't contain other HTML)
    # We use a lookahead `(?=<br>|</p>)` so we don't consume the line break, allowing consecutive headers to match.
    desc_html = re.sub(r'(<br>|<p[^>]*>)\s*([^<]*?:)\s*(?=<br>|</p>)', r'\1<strong style="color: var(--text-primary); font-size: 1.2rem; display: block; margin-top: 2rem; margin-bottom: 0.5rem; border-bottom: 2px solid var(--bg-secondary); padding-bottom: 0.5rem;">\2</strong>', desc_html)
    
    # 3. Highlight list items (lines starting with a bullet or emoji list)
    # Removing the old list item regex as the user's manual emojis work perfectly for list styling now.

    # Inject the real descriptionHTML as a new section before the CTA
    about_html = f'''
        <section class="container" style="margin-top: 6rem; margin-bottom: 6rem;">
            <div style="background: white; padding: 4rem; border-radius: 40px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 20px 40px -15px rgba(0,0,0,0.05); position: relative; overflow: hidden;">
                <!-- Decorative background element -->
                <div style="position: absolute; top: 0; right: 0; width: 300px; height: 300px; background: {s_app['badge_color']}; opacity: 0.05; filter: blur(60px); border-radius: 50%;"></div>
                
                <div class="section-header" style="text-align: left; margin-bottom: 3rem; position: relative; z-index: 1;">
                    <span class="badge" style="color: {s_app['badge_color']}; background: color-mix(in srgb, {s_app['badge_color']} 15%, transparent);">ABOUT THE APP</span>
                    <h2 style="margin-top: 1rem; font-size: 2.5rem; letter-spacing: -0.02em;">{app_data["title"]}</h2>
                </div>
                
                <div class="app-description" style="line-height: 1.8; color: var(--text-secondary); font-size: 1.1rem; position: relative; z-index: 1; max-width: 800px;">
                    {desc_html}
                </div>
            </div>
        </section>
'''
    # We will insert `about_html` right before `<section class="container">\n            <div class="cta-banner">`
    app_reviews = [r for r in all_reviews if r["appId"] == app_id]
    
    # Generate marquee HTML if there are reviews
    marquee_section = ""
    if app_reviews:
        reviews_html = ""
        for r in app_reviews:
            # Format date: "2026-02-03T08:48:11.100Z" -> "Feb 2026"
            try:
                date_parts = r["date"].split("T")[0].split("-")
                year = date_parts[0]
                month_num = int(date_parts[1])
                months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                date_str = f"{months[month_num]} {year}"
            except Exception:
                date_str = ""
            
            user_image = r.get("userImage") or "https://via.placeholder.com/40"
            stars = "★" * int(r.get("score", 5))
            
            reviews_html += f'''
                    <div class="review-card">
                        <div class="review-header">
                            <img src="{user_image}" alt="{r['userName']}" class="review-avatar">
                            <div>
                                <div class="review-author">{r['userName']}</div>
                                <div class="review-stars" style="color: #f59e0b; font-size: 1rem; margin-top: 0.2rem;">{stars}</div>
                            </div>
                        </div>
                        <div class="review-text">"{r['text']}"</div>
                        <div class="review-date" style="font-size: 0.75rem; color: #9ca3af; align-self: flex-end;">{date_str}</div>
                    </div>'''
        
        if len(app_reviews) >= 4:
            # Active scrolling marquee (seamless loop needs 2 copies)
            marquee_content = reviews_html + reviews_html
            track_html = f'''<div class="marquee-container">
                {marquee_content}
            </div>'''
        else:
            # Static centered grid for few comments
            track_html = f'''<div class="reviews-static-grid">
                {reviews_html}
            </div>'''
            
        marquee_section = f'''
        <!-- Reviews Section -->
        <section class="reviews-section">
            <div style="text-align: center; margin-bottom: 2rem;">
                <span class="badge" style="color: {s_app['badge_color']}; border-color: color-mix(in srgb, {s_app['badge_color']} 15%, transparent); border: none; background: transparent; padding-left: 0;">USER REVIEWS</span>
                <h2 style="font-size: 2.25rem; margin-top: 0.5rem;">Loved by our users</h2>
            </div>
            {track_html}
        </section>
'''

    insertion = about_html
    if marquee_section:
        insertion += f"\n{marquee_section}"

    content = content.replace('<section class="container">\n            <div class="cta-banner">', f'{insertion}\n        <section class="container">\n            <div class="cta-banner">')


    output_path = os.path.join(base_dir, "..", s_app["filename"])
    with open(output_path, "w", encoding="utf-8") as out_f:
        out_f.write(content)

# --- UPDATE INDEX.HTML ---
index_path = os.path.join(base_dir, "..", "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    for app_data in scraped_data:
        app_id = app_data['appId']
        if app_id not in static_apps:
            continue
        
        s_app = static_apps[app_id]
        
        score = app_data.get("score")
        if score and float(score) > 0:
            rating = f"⭐ {float(score):.1f}"
        else:
            rating = "⭐ New"
            
        # We will show both rating and installs on the home page cards
        installs = app_data.get("installs", "10k+")
        new_stats_span = f"<span>{rating} · {installs}</span>"
        
        # Regex to find the specific app card and replace the first span inside its footer
        pattern = re.compile(f'(<a href="{re.escape(s_app["filename"])}"[\\s\\S]*?<div class="app-footer">\\s*)<span>.*?</span>', re.DOTALL)
        index_html = pattern.sub(rf'\g<1>{new_stats_span}', index_html)
        


    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)

print("Successfully generated HTML files and updated homepage using scraped data.")
