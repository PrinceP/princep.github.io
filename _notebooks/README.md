# Managing Blog Posts

This portfolio automatically generates blog posts from Jupyter Notebooks (`.ipynb` files). The conversion and site generation are handled by a custom Python script (`build.py`) that runs automatically via GitHub Actions whenever you push to the `master`/`main` branch.

## How to Add a New Blog Post

1.  **Create your Notebook:**
    Create a new Jupyter Notebook (`.ipynb`). You can use any environment (e.g., local JupyterLab, Google Colab, VS Code).
    
    *   Write your markdown content, code blocks, and output as usual.
    *   The build script will automatically render the markdown and code cells.

2.  **Name the File:**
    The filename **must** follow this specific convention for the script to correctly extract the date and title:
    
    `YYYY-MM-DD-Title-Of-The-Post.ipynb`
    
    *Example:* `2024-03-15-Introduction-to-Computer-Vision.ipynb`
    
    *Note:* The format must be exactly `YYYY-MM-DD-` followed by the title words separated by hyphens. The script converts these hyphens into spaces for the display title.

3.  **Place the File:**
    Save or move the correctly named `.ipynb` file into this directory (`_notebooks/`).

4.  **Automatic Emojis (Optional):**
    If you want a specific emoji to appear next to your post title on the blog index page, you need to update the `emoji_map` dictionary in the `build.py` script located in the root directory. If no specific map is found, a default 📝 emoji will be used.

5.  **Commit and Push:**
    Commit the new notebook file to your repository and push the changes to GitHub.
    
    ```bash
    git add _notebooks/2024-03-15-Introduction-to-Computer-Vision.ipynb
    git commit -m "Add new blog post about Computer Vision"
    git push origin master
    ```

6.  **Deployment:**
    Once pushed, the GitHub Action (`.github/workflows/deploy.yml`) will automatically run. It typically takes 1-2 minutes to convert the notebook, update the `blogs/blog.html` index list, and deploy the new static files to the `gh-pages` branch. Your new blog post will then be live!