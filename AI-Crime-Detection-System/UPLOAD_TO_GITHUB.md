# Upload This Project to GitHub

## Option 1: GitHub Desktop

1. Install GitHub Desktop.
2. Sign in to your GitHub account.
3. Clone your existing repository:
   `patelsunny7323-ship-it/AI-Crime-Detection-System`
4. Copy all files from this project folder into the cloned repository folder.
5. Open GitHub Desktop.
6. Review the changed files.
7. Commit with:
   `Add complete AI crime detection project`
8. Click **Push origin**.
9. Refresh the GitHub repository in your browser.

## Option 2: Git Command Line

Open PowerShell in this project folder.

If this is a fresh local folder:

```bash
git init
git add .
git commit -m "Add complete AI crime detection project"
git branch -M main
git remote add origin https://github.com/patelsunny7323-ship-it/AI-Crime-Detection-System.git
git push -u origin main
```

If the GitHub repository already contains a README and Git reports that the remote contains work:

```bash
git pull origin main --allow-unrelated-histories
```

Resolve any conflict if Git reports one, then:

```bash
git add .
git commit -m "Merge GitHub README with project"
git push -u origin main
```

## Verify Before Submission

Clone the GitHub repository into a NEW folder and test it:

```bash
git clone https://github.com/patelsunny7323-ship-it/AI-Crime-Detection-System.git
cd AI-Crime-Detection-System
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python intrusion_detection.py
```

Then test the dashboard:

```bash
streamlit run dashboard/app.py
```

Do not submit until the cloned copy works.
