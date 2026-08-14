import os, re

file_path = r'c:\my files\A1technoksha (1)\project\12-08-2026\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .sol-card-img CSS
css_old = r'''    \.sol-card-img \{
      width: 100%;
      height: 220px;
      object-fit: contain;
      display: block;
      flex-shrink: 0;
      background: #fff;
    \}'''
css_new = '''    .sol-img-wrapper {
      width: 100%;
      height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #fff;
      padding: 16px;
      flex-shrink: 0;
    }
    .sol-card-img {
      max-width: 100%;
      max-height: 100%;
      display: block;
      border-radius: 12px;
      object-fit: contain;
    }'''
content = re.sub(css_old, css_new, content)

# Wrap the imgs
content = re.sub(
    r'(<img[^>]+class="sol-card-img"[^>]*>)', 
    r'<div class="sol-img-wrapper">\1</div>', 
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html')
