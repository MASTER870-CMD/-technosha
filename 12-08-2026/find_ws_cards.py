import re
with open(r'c:\my files\A1technoksha (1)\project\12-08-2026\workstations.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find sections or cards
cards = re.findall(r'<div class="sol-card.*?>(.*?)</div>\s*</div>', content, re.DOTALL)
print(f'Found {len(cards)} cards')
if cards:
    print('Card 1 snippet:', cards[0][:200])

models = re.findall(r'<div class="model-img.*?>(.*?)</div>', content, re.DOTALL)
print(f'Found {len(models)} model images')
if models:
    for model in models:
        print(model.strip())
