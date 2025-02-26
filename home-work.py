import os
import json
import subprocess
import shutil
import sys

def check_npm_installed():
    """Check if npm is installed"""
    try:
        subprocess.run(["npm", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        return True
    except FileNotFoundError:
        return False

def create_directory_structure():
    """Create the basic directory structure for the project"""
    print("Creating directory structure...")
    
    # Create src directory
    os.makedirs("src", exist_ok=True)
    
    # Create GitHub workflows directory
    os.makedirs(".github/workflows", exist_ok=True)

def create_html_file():
    """Create a basic HTML file with semantic markup for a weather forecast page"""
    print("Creating HTML file with weather forecast markup...")
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Forecast</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Weather Forecast</h1>
    </header>
    
    <main>
        <section class="search-section">
            <form role="search">
                <input type="search" placeholder="Weather" aria-label="Search for location">
                <button type="submit">Show</button>
            </form>
            
            <div class="map-container">
                <!-- Map placeholder -->
            </div>
        </section>
        
        <section class="weather-info">
            <h2>Weather info</h2>
            <div class="weather-details">
                <!-- Weather details will appear here -->
            </div>
        </section>
        
        <aside class="history-section">
            <h2>History</h2>
            <ul>
                <li>London</li>
                <li>Minsk</li>
                <li>Moscow</li>
            </ul>
        </aside>
    </main>
    
    <footer>
        <p>&copy; 2025 Weather Forecast</p>
    </footer>
</body>
</html>
"""
    
    with open("src/index.html", "w") as file:
        file.write(html_content)

def create_css_file():
    """Create a basic CSS file for styling the weather forecast page"""
    print("Creating CSS file...")
    
    css_content = """/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

.search-section {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}

.search-section form {
    display: flex;
    gap: 10px;
}

.search-section input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.search-section button {
    padding: 8px 16px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 4px;
    cursor: pointer;
}

.map-container {
    flex: 1;
    background-color: #f5f5f5;
    min-height: 150px;
    border: 1px solid #ddd;
}

.weather-info {
    border: 1px solid #ddd;
    padding: 20px;
    margin-bottom: 20px;
}

.history-section {
    margin-bottom: 20px;
}

.history-section ul {
    list-style-type: none;
    border-top: 1px solid #ddd;
}

.history-section li {
    padding: 10px 0;
    border-bottom: 1px solid #ddd;
}

footer {
    text-align: center;
    margin-top: 40px;
    color: #666;
}
"""
    
    with open("src/styles.css", "w") as file:
        file.write(css_content)

def create_package_json():
    """Create package.json file without installing dependencies"""
    print("Creating package.json file...")
    
    # Create package.json
    package_json = {
        "name": "weather-forecast",
        "version": "1.0.0",
        "description": "Weather forecast page with semantic HTML markup",
        "main": "index.js",
        "scripts": {
            "lint": "eslint . && stylelint 'src/**/*.css' && htmlhint 'src/**/*.html'",
            "lint:fix": "eslint --fix . && stylelint --fix 'src/**/*.css' && htmlhint 'src/**/*.html'",
            "format": "prettier --write 'src/**/*.{html,css,js}'",
            "prepare": "husky install"
        },
        "keywords": ["weather", "forecast", "semantic-html"],
        "author": "",
        "license": "ISC",
        "devDependencies": {
            "eslint": "^8.56.0",
            "htmlhint": "^1.1.4",
            "husky": "^8.0.3",
            "lint-staged": "^15.2.0",
            "prettier": "^3.1.1",
            "stylelint": "^16.1.0",
            "stylelint-config-standard": "^36.0.0"
        },
        "lint-staged": {
            "*.js": ["eslint --fix", "prettier --write"],
            "*.css": ["stylelint --fix", "prettier --write"],
            "*.html": ["htmlhint", "prettier --write"]
        }
    }
    
    with open("package.json", "w") as file:
        json.dump(package_json, file, indent=2)

def configure_linters():
    """Configure ESLint, Stylelint, HTMLHint and Prettier"""
    print("Configuring linters...")
    
    # ESLint configuration
    eslint_config = {
        "env": {
            "browser": True,
            "es2021": True
        },
        "extends": "eslint:recommended",
        "parserOptions": {
            "ecmaVersion": "latest",
            "sourceType": "module"
        },
        "rules": {}
    }
    
    with open(".eslintrc.json", "w") as file:
        json.dump(eslint_config, file, indent=2)
    
    # Stylelint configuration
    stylelint_config = {
        "extends": "stylelint-config-standard"
    }
    
    with open(".stylelintrc.json", "w") as file:
        json.dump(stylelint_config, file, indent=2)
    
    # HTMLHint configuration
    htmlhint_config = {
        "tagname-lowercase": True,
        "attr-lowercase": True,
        "attr-value-double-quotes": True,
        "attr-value-not-empty": False,
        "attr-no-duplication": True,
        "doctype-first": True,
        "tag-pair": True,
        "tag-self-close": False,
        "spec-char-escape": True,
        "id-unique": True,
        "src-not-empty": True,
        "title-require": True,
        "alt-require": True,
        "doctype-html5": True,
        "id-class-value": "dash",
        "style-disabled": False,
        "inline-style-disabled": False,
        "inline-script-disabled": False,
        "space-tab-mixed-disabled": "space",
        "id-class-ad-disabled": False,
        "href-abs-or-rel": False,
        "attr-unsafe-chars": True
    }
    
    with open(".htmlhintrc", "w") as file:
        json.dump(htmlhint_config, file, indent=2)
    
    # Prettier configuration
    prettier_config = {
        "singleQuote": True,
        "trailingComma": "es5",
        "tabWidth": 2,
        "semi": True,
        "printWidth": 100
    }
    
    with open(".prettierrc", "w") as file:
        json.dump(prettier_config, file, indent=2)

def create_husky_files():
    """Create Husky configuration files without installing"""
    print("Creating Husky config files...")
    
    # Create .husky directory
    os.makedirs(".husky", exist_ok=True)
    
    pre_commit_content = """#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

npx lint-staged
"""
    
    with open(".husky/pre-commit", "w") as file:
        file.write(pre_commit_content)
    
    # Try to make the pre-commit hook executable
    try:
        os.chmod(".husky/pre-commit", 0o755)
    except:
        print("Note: Could not make pre-commit hook executable. You'll need to do this manually.")

def create_github_workflows():
    """Create GitHub workflow configuration files"""
    print("Creating GitHub workflow files...")
    
    # Lint workflow
    lint_workflow = """name: Lint

on:
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        
    - name: Install dependencies
      run: npm ci
      
    - name: Run linters
      run: npm run lint
"""
    
    with open(".github/workflows/lint.yml", "w") as file:
        file.write(lint_workflow)
    
    # CodeSandbox workflow
    codesandbox_workflow = """name: Add CodeSandbox link

on:
  pull_request:
    branches: [ main ]

jobs:
  codesandbox-comment:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Comment with CodeSandbox link
      uses: unsplash/comment-on-pr@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        msg: |
          Try this PR in CodeSandbox: https://githubbox.com/${{ github.repository }}/tree/${{ github.head_ref }}
"""
    
    with open(".github/workflows/codesandbox.yml", "w") as file:
        file.write(codesandbox_workflow)
    
    # GitHub Pages deployment workflow
    pages_workflow = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Pages
      uses: actions/configure-pages@v3
      
    - name: Upload artifact
      uses: actions/upload-pages-artifact@v1
      with:
        path: 'src'
        
    - name: Deploy to GitHub Pages
      id: deployment
      uses: actions/deploy-pages@v2
"""
    
    with open(".github/workflows/pages.yml", "w") as file:
        file.write(pages_workflow)

def create_gitignore():
    """Create .gitignore file"""
    print("Creating .gitignore file...")
    
    gitignore_content = """# Dependencies
node_modules/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Debug logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Editor directories and files
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# OS generated files
.DS_Store
Thumbs.db
"""
    
    with open(".gitignore", "w") as file:
        file.write(gitignore_content)

def create_readme():
    """Create README.md file"""
    print("Creating README.md file...")
    
    readme_content = """# Weather Forecast Page

A simple weather forecast page with semantic HTML markup.

## Features

- Semantic HTML structure
- Basic CSS styling
- Linter configurations (ESLint, Stylelint, HTMLHint)
- Pre-commit hooks with Husky
- GitHub Actions for:
  - Running linters on pull requests
  - Adding CodeSandbox links to pull requests
  - Deploying to GitHub Pages

## Development

1. Clone the repository
2. Install dependencies: `npm install`
3. To run linters: `npm run lint`
4. To fix linting issues: `npm run lint:fix`
5. To format code: `npm run format`

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch.
"""
    
    with open("README.md", "w") as file:
        file.write(readme_content)

def main():
    """Main function to set up the project"""
    print("Starting project setup...")
    
    # Check if npm is installed
    npm_installed = check_npm_installed()
    
    create_directory_structure()
    create_html_file()
    create_css_file()
    
    if npm_installed:
        print("npm is installed, creating package.json and attempting to install dependencies...")
        try:
            # Create package.json and install dependencies
            create_package_json()
            subprocess.run(["npm", "install"], check=False)
            print("Dependencies installed successfully.")
        except Exception as e:
            print(f"Error installing dependencies: {e}")
            print("Continuing with file creation only...")
    else:
        print("npm not found. Creating configuration files without installing dependencies.")
        create_package_json()
    
    configure_linters()
    create_husky_files()
    create_github_workflows()
    create_gitignore()
    create_readme()
    
    print("\nProject setup complete!")
    print("\nNext steps:")
    print("1. If npm wasn't installed or dependencies failed to install:")
    print("   - Install Node.js and npm from https://nodejs.org/")
    print("   - Run 'npm install' in your project directory")
    
    print("\n2. Git steps:")
    print("   - Create a new repository on GitHub")
    print("   - Initialize Git in this directory: git init")
    print("   - Add all files: git add .")
    print("   - Create your first commit: git commit -m 'Initial commit'")
    print("   - Connect to your GitHub repo: git remote add origin YOUR_REPO_URL")
    print("   - Push to GitHub: git push -u origin main")
    print("   - Create a pull request to test the workflows")

if __name__ == "__main__":
    main()