"""
GitHub Setup - Push your AI Agent project to GitHub
"""

GITHUB_SETUP = r"""
╔═════════════════════════════════════════════════════╗
║   PUSH PROJECT TO GITHUB - STEP BY STEP             ║
╚═════════════════════════════════════════════════════╝

STEP 1: Create a GitHub Repository
═════════════════════════════════

1. Go to https://github.com/new
2. Fill in:
   - Repository name: "ai-phone-agent" (or your choice)
   - Description: "AI voice agent that controls Android phone via ADB"
   - Choose: Public (so others can see it)
   - ✓ Add a README file (optional but recommended)
3. Click "Create repository"
4. Copy the HTTPS URL (looks like: https://github.com/YOUR_USERNAME/ai-phone-agent.git)

STEP 2: Initialize Git in Your Project
════════════════════════════════════

Open PowerShell in your project folder:
cd "c:\Users\giris\OneDrive\Desktop\dsa programming\ai-phone-agent"

Then run:
git init
git add .
git commit -m "Initial commit: AI phone agent with voice control"

STEP 3: Add Remote Repository
═════════════════════════════

Replace YOUR_HTTPS_URL with the URL from Step 1:
git remote add origin YOUR_HTTPS_URL

Example:
git remote add origin https://github.com/girishjose/ai-phone-agent.git

STEP 4: Push to GitHub
═════════════════════

git branch -M main
git push -u origin main

When prompted, enter your GitHub credentials:
- Username: your GitHub username
- Password: your GitHub personal access token (NOT your password!)

HOW TO CREATE GITHUB PERSONAL ACCESS TOKEN:
═════════════════════════════════════════════

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name it: "ai-phone-agent"
4. Select scopes: repo (full control of private repositories)
5. Click "Generate token"
6. Copy the token (you won't see it again!)
7. Use this token as your password when git asks

STEP 5: Verify on GitHub
════════════════════════

1. Go to https://github.com/YOUR_USERNAME/ai-phone-agent
2. You should see all your files!
3. Add a nice README.md with:
   - Project description
   - How to install
   - How to use
   - Features
   - Requirements

QUICK COMMANDS
═══════════════

Check git status:
git status

See commits:
git log

Pull latest changes (if you made changes on GitHub):
git pull origin main

Make changes and push:
git add .
git commit -m "Your commit message"
git push origin main

EXAMPLE WORKFLOW:
═════════════════

# Initial setup
cd "c:\Users\giris\OneDrive\Desktop\dsa programming\ai-phone-agent"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-phone-agent.git
git branch -M main
git push -u origin main

# Later, after making changes
git add .
git commit -m "Added feature X"
git push origin main

CREATE A GOOD README.md
══════════════════════

Add this to README.md:

---
# AI Phone Agent

Control your Android phone with voice commands!

## Features
- 🎤 Voice command recognition
- 📱 Control WhatsApp, YouTube, and other apps
- 📞 Make calls and send messages
- 📋 Manage daily tasks
- 👥 Access contacts and messages
- 🔋 Check battery and device info
- 📸 Take screenshots

## Installation

1. Clone the repo:
   git clone https://github.com/YOUR_USERNAME/ai-phone-agent.git
   cd ai-phone-agent

2. Install dependencies:
   pip install -r requirements.txt

3. Connect Android phone via USB and enable USB Debugging

4. Run the agent:
   python main.py

## Usage

Say voice commands like:
- "Call mom"
- "Send message to john hello"
- "Open WhatsApp"
- "Show contacts"
- "Device info"

## Requirements

- Python 3.8+
- Android phone with USB Debugging enabled
- ADB (Android Debug Bridge)

## Testing

Test without phone:
python demo.py

Verify phone connection:
python verify_connection.py

---

TROUBLESHOOTING GITHUB
══════════════════════

❌ "Permission denied" or "Authentication failed"
─────────────────────────────────────────────────
Solution:
1. Use GitHub Personal Access Token (not your password)
2. Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

❌ "fatal: not a git repository"
─────────────────────────────────
Solution:
Run: git init

❌ "fatal: destination path already exists"
─────────────────────────────────────────────
Solution:
Your repo already exists, use:
git add .
git commit -m "message"
git push origin main

USEFUL LINKS
════════════

- GitHub Quick Start: https://docs.github.com/en/get-started/quickstart/hello-world
- Git Handbook: https://docs.github.com/en/github/getting-started-with-github/git-handbook
- SSH Setup: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

Happy pushing! 🚀
"""

print(GITHUB_SETUP)
