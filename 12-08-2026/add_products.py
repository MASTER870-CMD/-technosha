import os, glob, re

directory = r'c:\my files\A1technoksha (1)\project\12-08-2026'
html_files = glob.glob(os.path.join(directory, '*.html'))

new_column = '''        <div class="foot-links">
          <h4 class="foot-heading">PRODUCTS</h4>
          <ul>
            <li><a href="siemens-nx-cad.html">Siemens NX CAD</a></li>
            <li><a href="zwcad.html">ZWCAD</a></li>
            <li><a href="hexagon-esprit-edge.html">Hexagon ESPRIT EDGE</a></li>
          </ul>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update grid columns
    content = re.sub(
        r'grid-template-columns:\s*1\.5fr\s+1fr\s+1fr\s+1fr;', 
        'grid-template-columns: 1.5fr 1.2fr 1.2fr 1fr 1fr;', 
        content
    )
    
    # Insert new column after COMPANY
    # First find the COMPANY div end
    company_pattern = r'(<div class="foot-links">\s*<h4 class="foot-heading">COMPANY</h4>\s*<ul>.*?</ul>\s*</div>)'
    content = re.sub(company_pattern, r'\1\n' + new_column, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Added PRODUCTS column to all HTML files.")
