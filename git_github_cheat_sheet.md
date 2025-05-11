
# 🧠 Git + GitHub: Beginner Cheat Sheet

## 🔧 1. Set Up Git on Your Machine
Install Git: [https://git-scm.com](https://git-scm.com)

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

---

## 📁 2. Start a New Project
```bash
mkdir my-ml-project
cd my-ml-project
git init
```

---

## ✍️ 3. Add Files and First Commit
```bash
echo "# My ML Project" > README.md
git add README.md
git commit -m "First commit"
```

---

## ☁️ 4. Push to GitHub
1. Create a new repository on GitHub.
2. Then connect and push:

```bash
git remote add origin https://github.com/yourusername/my-ml-project.git
git branch -M main
git push -u origin main
```

---

## 💡 5. Make and Push Changes
```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

---

## 🌿 6. Use Branches
```bash
git checkout -b new-feature
# work and commit
git checkout main
git merge new-feature
git push
```

---

## 🔄 7. Clone a Repo
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

---

## 🚫 8. .gitignore
```bash
echo "__pycache__/" >> .gitignore
echo "*.csv" >> .gitignore
git add .gitignore
git commit -m "Add .gitignore"
```

---

## ✅ Common Git Commands

| Action              | Command                            |
|---------------------|-------------------------------------|
| Init repo           | `git init`                          |
| Add files           | `git add .`                         |
| Commit              | `git commit -m "message"`           |
| Connect to GitHub   | `git remote add origin <URL>`       |
| Push                | `git push -u origin main`           |
| Create branch       | `git checkout -b branch-name`       |
| Merge branch        | `git merge branch-name`             |
| Clone repo          | `git clone <URL>`                   |
| Status              | `git status`                        |
| Log                 | `git log`                           |
