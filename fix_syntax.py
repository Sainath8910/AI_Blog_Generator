import os

target = 'blogs/templates/blogs/deleted_blogs.html'
with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix category selected
html = html.replace('{% if category==selected_category %}', '{% if category == selected_category %}')

# Fix sort selection
html = html.replace('{% if selected_sort=="-created_at" %}', '{% if selected_sort == "-created_at" %}')
html = html.replace('{% if selected_sort=="created_at" %}', '{% if selected_sort == "created_at" %}')
html = html.replace('{% if selected_sort=="-updated_at" %}', '{% if selected_sort == "-updated_at" %}')
html = html.replace('{% if selected_sort=="title" %}', '{% if selected_sort == "title" %}')

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
