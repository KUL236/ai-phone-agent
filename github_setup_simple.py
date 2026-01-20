"""
GitHub Setup - Push your AI Agent project to GitHub
"""

print("=" * 70)
print("PUSH PROJECT TO GITHUB - STEP BY STEP")
print("=" * 70)

print("""
STEP 1: Create a GitHub Repository
===================================

1. Go to https://github.com/new
2. Fill in:
   - Repository name: "ai-phone-agent"
   - Description: "AI voice agent to control Android phone"
   - Choose: Public
   - Check: Add a README file (recommended)
3. Click "Create repository"
4. Copy the HTTPS URL (looks like: https://github.com/YOUR_USERNAME/ai-phone-agent.git)

STEP 2: Initialize Git in Your Project
=======================================

Open PowerShell and run:

cd "c:\\Users\\giris\\OneDrive\\Desktop\\dsa programming\\ai-phone-agent"

Then:
git init
git add .
git commit -m "Initial commit: AI phone agent with voice control"

STEP 3: Add Remote Repository
==============================

Replace YOUR_HTTPS_URL with your repo URL:

git remote add origin YOUR_HTTPS_URL

Example:
git remote add origin https://github.com/YOUR_USERNAME/ai-phone-agent.git

STEP 4: Push to GitHub
======================

git branch -M main
git push -u origin main

When prompted, enter your GitHub credentials.

IMPORTANT: Use a Personal Access Token, NOT your password!

HOW TO CREATE PERSONAL ACCESS TOKEN:
====================================

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Name: "ai-phone-agent"
4. Select scope: repo (full control)
5. Generate and COPY the token
6. Use this token when git asks for password

STEP 5: Verify on GitHub
=========================

1. Go to https://github.com/YOUR_USERNAME/ai-phone-agent
2. You should see all your files!
3. Add/Edit README.md with project description

QUICK COMMANDS
==============

Check status:
git status

See commits:
git log

Push changes later:
git add .
git commit -m "Your message"
git push origin main

TROUBLESHOOTING
===============

"Permission denied" or "Authentication failed":
- Use GitHub Personal Access Token (not password)
- Or set up SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

"not a git repository":
- Run: git init

"destination path already exists":
- Already have a repo, just push:
  git add .
  git commit -m "message"
  git push origin main

NEXT STEPS:
===========

1. Create GitHub account if you don't have one
2. Create a new repository
3. Copy the HTTPS URL
4. Run the commands above in PowerShell
5. Your project will be on GitHub!

Good luck! Push to GitHub now!
""")
