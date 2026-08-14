import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\siemens-nx-cad.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = re.findall(r'<section.*?id=["\']([^"\']+)["\'].*?>', content)
print('Sections with IDs:', sections)

headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
print('Headings:')
for h in headings: print(h)
