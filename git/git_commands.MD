# Git Basics  

## Set up your information
```
git config --global user.name "John Doe"  
git config --global user.email "jdoe@domain.com"  
git config --global github.user jdoe  
```


## Clone a repository
```
git clone https://github.com/ktbyers/pynet_ons  
```


## Add file to a repository
```
git add my_file.py  
git commit -m "Adding my_file.py"  
```


## Remove a file
```
git rm ex1_strings.py  
git commit -m "Removin ex1_strings.py  
```


## Push changes to remote repository
```
git push origin master  

where 'origin' is defined in 'git remote -v'  
where 'master' branch is the src branch; dest branch is same as src branch  
```


## Pull changes from remote repository
```
git pull origin master  

where 'origin' is defined in 'git remote -v'  
where 'master' branch is the src branch; dest branch is same as src branch  
```


## Branches
```
git branch                          # Look at branches  
git branch dev                      # Create a 'dev' branch  
git checkout dev                    # Switch to 'dev' branch  
git checkout master                 # Switch back to 'master' branch  
git push origin dev                 # Push changes up to GitHub for 'dev' branch jj
git merge dev                       # merge 'dev' into master (switch to 'master' branch first)  
git branch -d dev                   # delete this branch  
git branch -vv                      # To see the remote branch that it is tracking
git branch -u origin/develop        # Set current branch to track origin/develop (must exist)
```


## Misc
```
git status                          # View the status of the repository  
git log                             # View the commit log  
git log -p -1                       # Show the changes in the last commit  
git stash                           # Temporarily save uncommitted changes  
git stash pop                       # Remove changes from stash and reapply to repository  
```

