# Git is a version control system
# Tracks changes in code over time, lets you collaborate with others safely
# "Save As" + "Undo" on steroids

# git init - initializes a new git repository
# git status - shows status of changes
# git log - shows commit history
# git log --online
# git diff <file> - shows unstaged changes
# git restore <file> - discards changes for a file
# git rm <file> - removes a file

# a branch is an independent line of development
# Doesn't affect the original (main) until you merge
# Perfect for features, bug fixes, and experiments
# git merge <name> merges another branch into current
# git branch -d <name> deletes a branch (safely)
# git branch - creates a branch
# git checkout -b <name> creates a new branch (if <name> doesn't exist) and switches to it
print("Hello World!")
name = input("Enter your name: ")
print(f"Hello {name.title()}!")
# There can be merging conflicts, such as the branches having different print statments

print("New feature")
