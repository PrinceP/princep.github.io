import os
import glob
import re
import nbformat
from nbconvert import HTMLExporter
from pathlib import Path

# Paths
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
NOTEBOOKS_DIR = ROOT_DIR / "_notebooks"
BLOGS_OUT_DIR = ROOT_DIR / "blogs"
BLOG_INDEX_FILE = BLOGS_OUT_DIR / "blog.html"

# Ensure output dir exists
BLOGS_OUT_DIR.mkdir(parents=True, exist_ok=True)

# Post Layout Template
POST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} - Prince</title>
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <link rel="stylesheet" href="../assets/styles.css" />
  </head>
  <body class="bg-gray-50 text-gray-900 w-full max-w-3xl mx-auto px-5 md:px-0 pb-10 font-sans">
    <nav class="flex justify-between items-center py-6 border-b border-gray-300" data-aos="fade-down" data-aos-duration="800">
      <h1 class="font-serif text-3xl font-bold tracking-tight">
          <a href="../index.html" class="hover:text-blue-600 transition">Prince</a>
      </h1>
      <div class="flex gap-6 text-sm font-medium">
        <a href="../index.html" class="hover:text-blue-600 transition">Home</a>
        <a href="blog.html" class="text-blue-600 transition">Blogs</a>
        <a href="../projects/projects.html" class="hover:text-blue-600 transition">Projects</a>
      </div>
    </nav>
    <article class="mt-12 markdown-body" data-aos="fade-up" data-aos-duration="1000">
      <header class="mb-8">
          <h1 class="text-4xl font-bold text-gray-900 mb-2">{title}</h1>
          <p class="text-sm text-gray-500">{date}</p>
      </header>
      <div class="prose max-w-none">
        {content}
      </div>
    </article>
    <script>
      lucide.createIcons();
      AOS.init({{ once: true }});
    </script>
  </body>
</html>"""

def extract_metadata(filename):
    """Extract date and title from the old fastpages filename convention (YYYY-MM-DD-title.ipynb)"""
    basename = os.path.basename(filename)
    match = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.ipynb$', basename)
    
    emoji_map = {
        'Flops Model': '🧠',
        'Image Formats': '🖼️',
        'Pruning Neural Networks': '✂️'
    }
    
    if match:
        date_str = match.group(1)
        title_str = match.group(2).replace('-', ' ').title()
        title_with_emoji = f"{emoji_map.get(title_str, '📝')} {title_str}"
        return date_str, title_with_emoji
    
    # Fallback
    raw_title = basename.replace('.ipynb', '').replace('-', ' ').title()
    return "Unknown Date", f"📝 {raw_title}"

def main():
    exporter = HTMLExporter()
    exporter.template_name = 'basic' # basic template strips out full HTML head/body
    
    notebooks = glob.glob(str(NOTEBOOKS_DIR / "*.ipynb"))
    
    posts_list_html = []
    
    # Sort backwards so newest is first
    notebooks.sort(reverse=True)
    
    for nb_path in notebooks:
        print(f"Processing {nb_path}...")
        date_str, title_str = extract_metadata(nb_path)
        
        # Output filename
        out_basename = os.path.basename(nb_path).replace('.ipynb', '.html')
        out_path = BLOGS_OUT_DIR / out_basename
        
        # Read the notebook
        with open(nb_path, 'r', encoding='utf-8') as f:
            notebook_node = nbformat.read(f, as_version=4)
        
        # Convert to HTML
        (body, resources) = exporter.from_notebook_node(notebook_node)
        
        # Wrap in our template
        full_html = POST_TEMPLATE.format(
            title=title_str, 
            date=date_str, 
            content=body
        )
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        # Add to list
        link_href = out_basename
        item_html = """
        <div class="group border border-gray-200 bg-white rounded-xl p-5 shadow-sm hover:shadow-md transition">
            <h3 class="text-xl font-bold text-blue-900 mb-1 group-hover:text-blue-600 transition">
                <a href="{href}">{title}</a>
            </h3>
            <p class="text-sm text-gray-500">{date}</p>
        </div>
        """
        # Fix: href using out_basename
        item_html = item_html.replace('{href}', link_href).replace('{title}', title_str).replace('{date}', date_str)
        posts_list_html.append(item_html)
        
    print(f"Processed {len(notebooks)} notebooks. Updating blog index...")
    
    # Update Blog index
    if BLOG_INDEX_FILE.exists():
        with open(BLOG_INDEX_FILE, 'r', encoding='utf-8') as f:
            blog_index_content = f.read()
            
        # Replace everything between the marker
        marker = "<!-- BLOG_LIST_INSERT_MARKER -->"
        if marker in blog_index_content:
            new_content = blog_index_content.replace(marker, marker + "\n        " + "\n        ".join(posts_list_html))
            
            # Since we could run this multiple times, we need a better replacement strategy.
            # Actually, using regex to replace everything inside the div is better.
            import re
            blog_index_content = re.sub(
                r'<!-- BLOG_LIST_INSERT_MARKER -->.*?(?=</div)', 
                '<!-- BLOG_LIST_INSERT_MARKER -->\n        ' + "\n        ".join(posts_list_html) + '\n      ', 
                blog_index_content, 
                flags=re.DOTALL
            )
            
            with open(BLOG_INDEX_FILE, 'w', encoding='utf-8') as f:
                f.write(blog_index_content)
        
    print("Done!")

if __name__ == "__main__":
    main()
