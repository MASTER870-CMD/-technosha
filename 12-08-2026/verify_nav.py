import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
nav = re.search(r'<ul class="nav-links">(.*?)</ul>', content, re.DOTALL)
if nav:
    print(nav.group(1))
