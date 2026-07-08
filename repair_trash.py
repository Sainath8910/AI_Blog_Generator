import re

# 1. Update views.py for blog_detail
views_path = 'blogs/views.py'
with open(views_path, 'r', encoding='utf-8') as f:
    views_code = f.read()

old_detail = """def blog_detail(request, blog_id):

    blog = BlogRepository.get_blog(blog_id)"""
new_detail = """def blog_detail(request, blog_id):

    from django.shortcuts import get_object_or_404
    from blogs.models import Blog
    blog = get_object_or_404(Blog, id=blog_id)
    # prefetch not strictly necessary if template iterates normally, but good practice if needed"""

if old_detail in views_code:
    views_code = views_code.replace(old_detail, new_detail)
    with open(views_path, 'w', encoding='utf-8') as f:
        f.write(views_code)
    print("Fixed views.py blog_detail")


# 2. Update deleted_blogs.html
html_path = 'blogs/templates/blogs/deleted_blogs.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the fetch URL and success messages
html = html.replace('`/blogs/${deleteBlogId}/delete/`', '`/blogs/${deleteBlogId}/restore/`')
html = html.replace('showToast("Blog deleted successfully.");', 'showToast("Blog restored successfully.");')

# Remove Edit Button HTML block
edit_btn = """                        <a href="{% url 'blogs:edit' blog.id %}" class="
            inline-flex

            items-center

            gap-2

            rounded-xl

            border

            border-slate-300

            dark:border-slate-700

            px-5

            py-3

            hover:bg-slate-100

            dark:hover:bg-slate-800">

                            <i data-lucide="square-pen" class="w-4 h-4"></i>

                            Edit

                        </a>"""
html = html.replace(edit_btn, '')

# Remove Export Button HTML block
export_btn = """                        <button type="button" onclick="openExportModal('{{ blog.id }}')" class="
            inline-flex

            items-center

            gap-2

            rounded-xl

            border

            border-slate-300

            dark:border-slate-700

            px-5

            py-3

            hover:bg-slate-100

            dark:hover:bg-slate-800">

                            <i data-lucide="download" class="w-4 h-4"></i>

                            Export

                        </button>"""
html = html.replace(export_btn, '')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Repaired deleted_blogs.html feature endpoints and UI")
