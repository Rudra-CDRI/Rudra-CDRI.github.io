import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the project entries from projectData
c = re.sub(r'const projectData = \{.*?(?=\'cw_robotics\':)', 'const projectData = {\n  ', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
