import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\siemens-nx-cad.html', 'r', encoding='utf-8') as f:
    content = f.read()

for match in re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', content):
    print(match)
