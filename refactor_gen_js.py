import os

target = 'templates/blogs/generate_blog.html'

with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# Add lucide.createIcons() to submit hook
target_str = 'document.getElementById("loadingSkeleton").classList.remove("hidden");'
replacement = target_str + '\n    if (typeof lucide !== "undefined") { lucide.createIcons(); }'

if 'lucide.createIcons(); }' not in html:
    html = html.replace(target_str, replacement)

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print("Icons JS fixed")
