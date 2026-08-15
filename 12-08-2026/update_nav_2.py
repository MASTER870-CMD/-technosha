import glob
import os

html_files = glob.glob(r'C:\my files\A1technoksha (1)\project\12-08-2026\*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_link = '<li><a href="workstation-for-all.html">Workstation for All</a></li>'
    new_link = '<li><a href="workstations.html">Workstations</a></li>'
    
    if old_link in content:
        content = content.replace(old_link, new_link)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {os.path.basename(file)}')
