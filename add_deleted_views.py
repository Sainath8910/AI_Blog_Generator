import os

# 1. Update urls.py
urls_path = 'blogs/urls.py'
with open(urls_path, 'r', encoding='utf-8') as f:
    urls_content = f.read()

urls_content = urls_content.replace(
    'delete_blog,',
    'delete_blog,\n    restore_blog,\n    deleted_blogs,'
)

urls_content = urls_content.replace(
    'path("my/", my_blogs, name="my_blogs"),',
    'path("my/", my_blogs, name="my_blogs"),\n    path("deleted/", deleted_blogs, name="deleted_blogs"),'
)

urls_content = urls_content.replace(
    'path("<int:blog_id>/delete/", delete_blog, name="delete"),',
    'path("<int:blog_id>/delete/", delete_blog, name="delete"),\n    path("<int:blog_id>/restore/", restore_blog, name="restore"),'
)

with open(urls_path, 'w', encoding='utf-8') as f:
    f.write(urls_content)


# 2. Update views.py
views_path = 'blogs/views.py'
with open(views_path, 'a', encoding='utf-8') as f:
    f.write("""

def deleted_blogs(request):
    from django.db.models import Q
    search = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    sort = request.GET.get("sort", "-created_at").strip()

    blogs = Blog.objects.filter(is_deleted=True)
    if search:
        blogs = blogs.filter(
            Q(title__icontains=search) |
            Q(topic__icontains=search) |
            Q(description__icontains=search)
        )
    if category:
        blogs = blogs.filter(category=category)
    
    blogs = blogs.order_by(sort)

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    raw_categories = Blog.objects.filter(is_deleted=True).values_list("category", flat=True)
    categories = sorted(list(set(c.strip() for c in raw_categories if c and c.strip())))

    return render(
        request,
        "blogs/deleted_blogs.html",
        {
            "page_obj": page_obj,
            "search": search,
            "selected_category": category,
            "selected_sort": sort,
            "categories": categories,
        },
    )

@require_POST
def restore_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id, is_deleted=True)
        blog.is_deleted = False
        blog.save(update_fields=["is_deleted"])
        return JsonResponse({"success": True})
    except Blog.DoesNotExist:
        return JsonResponse({"success": False, "message": "Blog not found."}, status=404)
""")


# 3. Create deleted_blogs.html from my_blogs.html
my_blogs_path = 'blogs/templates/blogs/my_blogs.html'
with open(my_blogs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Change Titles and text
html = html.replace('My Blogs', 'Deleted Blogs')
html = html.replace('Your AI Blog', 'Your Deleted')
html = html.replace('Workspace', 'Trash')
html = html.replace('Browse, edit, regenerate and export every AI-generated', 'View and restore all your previously deleted AI articles.')
html = html.replace('article from one beautiful workspace.', '')
html = html.replace('Find Your Blogs', 'Recover Deleted Blogs')
html = html.replace('Search by title, topic or description and quickly locate your work.', 'Search your trash and restore deleted blogs to your library.')
html = html.replace('{{ page_obj.paginator.count }} Blogs', '{{ page_obj.paginator.count }} Deleted')
html = html.replace('No blogs found.', 'No deleted blogs found.')
html = html.replace("You haven't generated any blogs yet.", "Your trash is completely empty.")

# Change buttons on the card
# The delete button in my_blogs has:
# class="delete-btn flex items-center ... text-red-600 hover:bg-red-50" data-blog-id="{{ blog.id }}">
# <i data-lucide="trash-2" class="w-4 h-4"></i> Delete
# We want to change this to restore
html = html.replace('delete-btn ', 'restore-btn ')
html = html.replace('text-red-600', 'text-green-600')
html = html.replace('hover:bg-red-50', 'hover:bg-green-50')
html = html.replace('dark:hover:bg-red-500/10', 'dark:hover:bg-green-500/10')
html = html.replace('data-lucide="trash-2"', 'data-lucide="rotate-ccw"')
html = html.replace('Delete\n\n                                </button>', 'Restore\n\n                                </button>')
html = html.replace('                            Delete\n\n                        </button>', '                            Restore\n\n                        </button>')

# Change the Delete Modal to Restore Modal
html = html.replace('id="deleteModal"', 'id="restoreModal"')
html = html.replace('Delete Blog', 'Restore Blog')
html = html.replace('Are you sure you want to delete this blog? This action cannot be undone.', 'Are you sure you want to restore this blog to your library?')
html = html.replace('id="cancelDelete"', 'id="cancelRestore"')
html = html.replace('id="confirmDelete"', 'id="confirmRestore"')
html = html.replace('bg-red-600', 'bg-green-600')
html = html.replace('hover:bg-red-700', 'hover:bg-green-700')
html = html.replace('🗑 Delete', '♻ Restore')
# Modal icon icon
html = html.replace('<i data-lucide="alert-triangle"', '<i data-lucide="rotate-ccw"')
html = html.replace('bg-red-100 dark:bg-red-900/30 text-red-600 dark:text-red-400', 'bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400')

# Javascript logic replacements
html = html.replace('let blogIdToDelete = null;', 'let blogIdToRestore = null;')
html = html.replace('const deleteModal = document.getElementById("deleteModal");', 'const restoreModal = document.getElementById("restoreModal");')
html = html.replace('.delete-btn', '.restore-btn')
html = html.replace('blogIdToDelete', 'blogIdToRestore')
html = html.replace('deleteModal', 'restoreModal')
html = html.replace('cancelDelete', 'cancelRestore')
html = html.replace('confirmDelete', 'confirmRestore')

# Replace the fetch URL string
html = html.replace('/blogs/${blogIdToRestore}/delete/', '/blogs/${blogIdToRestore}/restore/')
html = html.replace('Delete\n\n            </button>', 'Restore\n\n            </button>')

deleted_blogs_path = 'blogs/templates/blogs/deleted_blogs.html'
with open(deleted_blogs_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 4. Update sidebar.html
sidebar_path = 'templates/components/sidebar.html'
with open(sidebar_path, 'r', encoding='utf-8') as f:
    sidebar_html = f.read()

sidebar_inject = """                    <a href="{% url 'blogs:deleted_blogs' %}"
                        class="flex items-center gap-3 px-4 py-3 rounded-2xl text-slate-600 dark:text-slate-400 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-blue-600 dark:hover:text-blue-400 transition-all font-medium {% if request.resolver_match.url_name == 'deleted_blogs' %}bg-slate-50 dark:bg-slate-800 text-blue-600 dark:text-blue-400{% endif %}">
                        <i data-lucide="trash-2" class="w-5 h-5"></i>
                        Trash
                    </a>"""

if "blogs:deleted_blogs" not in sidebar_html:
    sidebar_html = sidebar_html.replace(
        '<!-- Library -->',
        f'<!-- Library -->\n{sidebar_inject}'
    )
    with open(sidebar_path, 'w', encoding='utf-8') as f:
        f.write(sidebar_html)

print("Created deleted blogs features!")
