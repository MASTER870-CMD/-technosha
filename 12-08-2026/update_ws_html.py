import re

with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\workstations.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero image
content = content.replace(
    '<img src="./assets/cam.png" alt="Professional HP and Dell CAD workstations"',
    '<img src="./assets/professional-cad-workstations.jpg" alt="Professional HP and Dell CAD workstations"'
)

# Replace Tower icon with image
tower_icon = '''<div class="c-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <rect x="4" y="3" width="7" height="16" rx="1.4" />
              <rect x="13" y="7" width="7" height="12" rx="1.4" />
            </svg></div>'''
tower_img = '<img src="./assets/hp-z-tower-workstation-cad.jpg" alt="HP Tower Workstation" style="width:100%; height:200px; object-fit:cover; border-radius:12px; margin-bottom:16px;">'
content = content.replace(tower_icon, tower_img)

# Replace Mobile icon with image
mobile_icon = '''<div class="c-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <rect x="3" y="4" width="18" height="12" rx="1.5" />
              <path d="M2 19h20" />
            </svg></div>'''
mobile_img = '<img src="./assets/dell-precision-mobile-workstation-cad.jpg" alt="Dell Mobile Workstation" style="width:100%; height:200px; object-fit:cover; border-radius:12px; margin-bottom:16px;">'
content = content.replace(mobile_icon, mobile_img)

# Also fix the duplicate nav link issue if present. 
# Oh wait, I noticed "<li><a href="workstations.html">Workstations</a></li>" twice in my previous regex replacement?
# Let's clean it up just in case
content = content.replace('<li><a href="workstations.html">Workstations</a></li>\n          <li><a href="workstations.html">Workstations</a></li>', '<li><a href="workstations.html">Workstations</a></li>')

with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\workstations.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated workstations.html with images.")
