with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\siemens-nx-cad.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines):
    if 'class="hero-inner"' in line:
        start = max(0, i-2)
        end = min(len(lines), i+15)
        for j in range(start, end):
            print(lines[j])
