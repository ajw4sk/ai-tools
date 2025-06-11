# UV Install Guide
A practical guide to using UV - the fastest Python package manager, with code examples and shell optimizations.

### UV Installation & Setup (Personal Recommendation)

If you've never used UV, go to: ([https://docs.astral.sh/uv/getting-started/installation])

UV is implemented in Rust by Astral and is **by far the best Python package manager I've used**. 

```bash
# Recommended installation method - simple curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternative installation methods available:**
- pip
- Cargo  
- Homebrew
- Scoop
- Docker
- Winget
- GitHub releases

But honestly, just do the curl request - it's straightforward.

### Important UV Setup Tips

**Enable Shell Auto-Completion** - This is a game changer! 
- Instructions are on the installation page towards the bottom
- It gives you guidance on figuring out what shell you're using if you don't know
- Just put it into your shell configuration
- Makes the experience way easier

**Take 15 minutes to explore UV** if you've never seen it before:
- Run through the scripts and guides - it's a little different but worth it
- Tools like UVX let you invoke tools without installing them in the virtual environment
- Much easier virtual environment and package management

## 🔍 Check if UV is Installed

```bash
# Check if UV is installed and get version
uv --version

# Check where UV is installed
which uv

# Get help and see available commands
uv --help
```

## 📦 UV Project Setup Tutorial

### 1. Create a New Python Project

```bash
# Create a new directory and navigate to it
mkdir my-ai-project
cd my-ai-project

# Initialize a new UV project (creates pyproject.toml)
uv init

# Or initialize with specific Python version
uv init --python 3.11
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
# .venv\Scripts\activate
```

### 3. Install Packages

```bash
# Install packages (automatically uses the venv)
uv add requests
uv add pandas numpy
uv add anthropic  # For AI/LLM work

# Install development dependencies
uv add --dev pytest black flake8

# Install from requirements.txt
uv pip install -r requirements.txt

# Install package for editing (development mode)
uv add -e .
```

### 4. Working with the Environment

```bash
# List installed packages
uv pip list

# Show package info
uv pip show pandas

# Run Python in the environment
uv run python script.py

# Run a command in the environment
uv run pytest

# Exit virtual environment
deactivate
```

## ⚡ Shell Aliases for Speed

Add these to your shell configuration file (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
# UV Aliases for faster workflow
alias uvi="uv init"                    # Initialize project
alias uvv="uv venv"                    # Create virtual environment  
alias uva="source .venv/bin/activate"  # Activate environment
alias uvd="deactivate"                 # Deactivate environment
alias uvadd="uv add"                   # Add package
alias uvr="uv run"                     # Run command in environment
alias uvl="uv pip list"                # List packages
alias uvs="uv pip show"                # Show package info

# Combined aliases for common workflows
alias uvstart="uv init && uv venv && source .venv/bin/activate"  # Full project setup
alias uvclean="deactivate && rm -rf .venv"                       # Clean environment

# Quick project setup with common AI packages
alias uv-ai="uvstart && uv add anthropic openai requests pandas numpy"
```

## 🎨 Oh My Zsh Integration

I use [Oh My Zsh](https://ohmyz.sh/) for enhanced shell experience. It pairs perfectly with UV workflows.

### Installation
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Useful Oh My Zsh Plugins for Python Development
Add these to your `~/.zshrc` plugins array:
```bash
plugins=(
  git
  python
  pip
  virtualenv
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```

### UV + Oh My Zsh Functions

Add these functions to your `~/.zshrc`:

```bash
# Quick UV project setup function
uvproject() {
    if [ -z "$1" ]; then
        echo "Usage: uvproject <project-name>"
        return 1
    fi
    
    mkdir "$1"
    cd "$1"
    uv init
    uv venv
    source .venv/bin/activate
    echo "✅ Project $1 created and environment activated!"
}

# UV environment status in prompt
uv_env_status() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        echo " (uv:$(basename $VIRTUAL_ENV))"
    fi
}

# Add to your prompt (if using custom theme)
# PROMPT='${ret_status} %{$fg[cyan]%}%c%{$reset_color%}$(git_prompt_info)$(uv_env_status) %# '
```

## 🚀 Complete Workflow Examples

### Starting a New AI Project
```bash
# Using aliases
uvproject my-ai-app
uv add anthropic openai requests pandas
echo "print('Hello AI!')" > main.py
uvr python main.py
```

### Working with Existing Project
```bash
# Clone and setup
git clone <repo-url>
cd <repo-name>
uv venv
uva
uv pip install -r requirements.txt

# Or if using pyproject.toml
uv sync
```

### Daily Development Workflow
```bash
# Start working
cd my-project
uva

# Add new dependency
uvadd scipy

# Run tests
uvr pytest

# Run your app
uvr python app.py

# Done for the day
uvd
```

## 🔧 Advanced UV Features

### Using UVX (Run Tools Without Installing)
```bash
# Run tools without installing globally
uvx black .              # Format code
uvx flake8 .             # Lint code  
uvx pytest              # Run tests
uvx jupyter notebook     # Start Jupyter

# Pin tool versions
uvx black==23.1.0 .
```

### Lock Files and Reproducible Environments
```bash
# Generate lock file
uv lock

# Install from lock file (exact versions)
uv sync

# Update dependencies
uv lock --upgrade
```

### Multiple Python Versions
```bash
# List available Python versions
uv python list

# Install specific Python version
uv python install 3.11

# Create venv with specific Python
uv venv --python 3.11
uv venv --python python3.12
```

## 💡 Pro Tips

1. **Always use `uv run`** instead of activating environment for one-off commands
2. **Use `uv sync`** instead of `pip install -r requirements.txt` when pyproject.toml exists
3. **UVX is great** for tools you don't want to install globally
4. **Pin versions in production** using lock files
5. **Use aliases** to speed up your workflow significantly

## 🐛 Common Issues & Solutions

### Path Issues
```bash
# If UV not found, add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Environment Not Activating
```bash
# Make sure you're in project directory
pwd
ls -la .venv

# Recreate if needed
rm -rf .venv
uv venv
source .venv/bin/activate
```

### Permission Issues
```bash
# Fix permissions on macOS/Linux
chmod +x .venv/bin/activate
```

---

*UV is seriously fast and reliable. Once you set up these aliases and functions, you'll never want to go back to pip and virtualenv!*
