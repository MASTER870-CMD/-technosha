import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\workstations.html', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'<img\s+[^>]*src=[\"\'](.*?)[\"\'][^>]*>', content)
for i, img in enumerate(images):
    print(f'Image {i}: {img}')
