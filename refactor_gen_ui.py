import os

target = 'templates/blogs/generate_blog.html'

with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace ✅
check_svg = '<i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 inline-block -mt-1 mr-2"></i>'
html = html.replace('✅ ', check_svg)

# Replace ⏳ in HTML
load_svg = '<i data-lucide="loader-circle" class="w-5 h-5 text-blue-300 inline-block -mt-1 mr-2 animate-spin"></i>'
html = html.replace('⏳ ', load_svg)

# Replace ⏳ in JS
js_load = '<i data-lucide="loader-circle" class="w-5 h-5 inline-block -mt-1 mr-2 animate-spin"></i>'
html = html.replace('"⏳ Generating..."', f'"{js_load} Generating..."')

# Insert caution message
original_text = """Sit back and relax while we generate your article.

                    </p>"""

caution_msg = """Sit back and relax while we generate your article.

                    </p>
                    
                    <div class="mt-5 inline-flex items-center gap-3 bg-red-500/20 border border-red-400/30 text-white px-5 py-3 rounded-2xl backdrop-blur-md shadow-lg shadow-red-900/20">
                        <i data-lucide="alert-triangle" class="w-6 h-6 text-red-300"></i>
                        <span class="text-sm font-medium tracking-wide">CAUTION: Do not navigate away or refresh this page, or the blog generation will stop instantly.</span>
                    </div>"""

html = html.replace(original_text, caution_msg)

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print("Generate blog UI updated")
