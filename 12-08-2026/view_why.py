import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\siemens-nx-cad.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<section.*?id="why".*?>(.*?)</section>', content, re.DOTALL)
if match:
    lines = match.group(1).split('\n')
    for line in lines[:60]:
        print(line)
