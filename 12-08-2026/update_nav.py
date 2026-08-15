import re
import glob

files = glob.glob(r'C:\my files\A1technoksha (1)\project\12-08-2026\*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to add Workstation for All to nav-links ul
    # Let's find the nav-links ul
    # It might look like:
    # <ul class="nav-links" id="navLinks">
    #   <li><a href="index.html" class="active">Home</a></li>
    #   <li><a href="siemens-nx-cad.html">Siemens NX CAD</a></li>
    #   <li><a href="zwcad.html">ZWCAD</a></li>
    #   <li><a href="hexagon-esprit-edge.html">Hexagon ESPRIT EDGE</a></li>
    #   <li><a href="about.html">About</a></li>
    #   <li><a href="industries.html">Industries</a></li>
    #   <li><a href="#contact">Contact</a></li>
    # </ul>
    
    # We will insert it before the Contact link or after About/Industries.
    
    if '>Industries</a></li>' in content:
        if '>Workstation for All</a></li>' not in content:
            content = content.replace('>Industries</a></li>', '>Industries</a></li>\n          <li><a href="workstation-for-all.html">Workstation for All</a></li>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {file}')
