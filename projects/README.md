# Managing Projects

This document explains how to add or update projects on the Projects page.

## How to Add a New Project

The projects page (`projects.html`) is currently built with static HTML using Tailwind CSS for styling. To add a new project, you will need to manually edit the HTML file.

1.  **Open the File:**
    Open `projects/projects.html` in your preferred text editor.

2.  **Locate the Projects Grid:**
    Find the `<div>` containing the existing projects. It looks like this:
    ```html
    <div class="grid gap-6">
        <!-- Project cards are inside here -->
    </div>
    ```

3.  **Add a New Project Card:**
    Copy an existing project card block and paste it within the grid division. A standard project card looks like this:

    ```html
    <div class="p-6 bg-white border border-gray-200 rounded-xl shadow-sm hover:shadow-md transition">
        <h3 class="text-xl font-semibold mb-2 text-blue-900">Project Name</h3>
        <p class="text-gray-600 mb-4">Brief description of the project detailing the technologies used and what it accomplished.</p>
        <div class="flex items-center gap-4 text-sm font-medium">
            <!-- Link -->
            <a href="URL_LINK_HERE" target="_blank" class="flex items-center gap-1.5 text-blue-600 hover:text-blue-800 transition">
                <i data-lucide="external-link" class="w-4 h-4"></i> Link Text (e.g., App Link, Video Link)
            </a>
        </div>
    </div>
    ```

4.  **Update the Content:**
    *   Change `Project Name` to the name of your new project.
    *   Update the paragraph `<p>` with the project's description.
    *   Replace `URL_LINK_HERE` with the actual URL relating to the project (e.g., a GitHub repo, a YouTube video, a HackerEarth challenge).
    *   Change `Link Text` to something descriptive.
    *   *(Optional)* You can change the Lucide icon by modifying the `data-lucide` attribute. Common icons include `github`, `external-link`, `video`, `link`. You can find more icons at [lucide.dev](https://lucide.dev/).

5.  **Commit and Push:**
    Save the `projects.html` file, commit the changes, and push them to GitHub. It will automatically deploy.
    
    ```bash
    git add projects/projects.html
    git commit -m "Add new project: [Project Name]"
    git push origin master
    ```
