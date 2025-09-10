

**#username:**

git config --global user.name

git config --global user.email 

\# initialising and cloning:

git add

git clone

**#basic commands:**

git add # it will stage the file

git commit -m

git push -u origin Santhosh

git push

git pull

git merge

**#commit history**

git log

**#seeing if changes are made before committing:**

git diff

**#revert unstaged changes in git:**

git checkout filename

**#revert staged changes in git:**

git reset HEAD filename

**#amending most recent commits:**

git commit --amend  # better to amend local commit before it is made to public(push)

**#rollback the latest commit:**

git revert HEAD     #it will create a new commit that is the opposite of everything in the given commit

git revert commit\_id\_here   #You can revert an old commit using its commit id



