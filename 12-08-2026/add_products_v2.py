import os, glob, re

directory = r'c:\my files\A1technoksha (1)\project\12-08-2026'
html_files = glob.glob(os.path.join(directory, '*.html'))

new_column = '''        <div class="foot-col">
          <h5>Products</h5>
          <ul>
            <li><a href="siemens-nx-cad.html">Siemens NX CAD</a></li>
            <li><a href="zwcad.html">ZWCAD</a></li>
            <li><a href="hexagon-esprit-edge.html">Hexagon ESPRIT EDGE</a></li>
          </ul>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update grid columns if not already updated (was 4 columns, now 5 columns)
    content = re.sub(
        r'grid-template-columns:\s*1\.5fr\s+1fr\s+1fr\s+1fr;', 
        'grid-template-columns: 1.5fr 1fr 1.2fr 1fr 1fr;', 
        content
    )
    
    # Also update if it got previously updated by mistake
    content = re.sub(
        r'grid-template-columns:\s*1\.5fr\s+1\.2fr\s+1\.2fr\s+1fr\s+1fr;', 
        'grid-template-columns: 1.5fr 1fr 1.2fr 1fr 1fr;', 
        content
    )
    
    # Check if PRODUCTS is already added
    if '<h5>Products</h5>' not in content:
        # Proper pattern based on actual HTML
        company_pattern = r'(<div class="foot-col">\s*<h5>Company</h5>\s*<ul>.*?</ul>\s*</div>)'
        
        new_content = re.sub(company_pattern, r'\1\n' + new_column, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Added PRODUCTS to {os.path.basename(file)}')
        else:
            print(f'Failed to add PRODUCTS to {os.path.basename(file)} (no match found)')

print('Done')
