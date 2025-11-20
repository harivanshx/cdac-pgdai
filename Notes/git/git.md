## git architecture 
## git commands

- clone , in-it, push pull operations , staging area commands, concept of branches (creation , merging, Deletion ) 
- Basics operations at the local as well as remote 
- Merging via pull request 
- Fork Operations and synchronization of  local git with the remote server 
- Collaboration of git with Jenkins



# Git and Git-hub
Git hub is the central server where the remote repositories are connected and sync with the local  tool git bash
- Git bash is the command line utility tool that is used to connect the local with the remote .
- All the local operations done on the local are executed with the help of git commands.
- Git-hub is the store house of repositories where multiple projects are collaborated tracked and managed at the central server.


run this command 
![[Pasted image 20250929145442.png]]

Open windows credentials manager


![[Pasted image 20250929145415.png]]


# Version Control System
That is all the changes in the repo will have the revision - history and can be trapped accordingly
# Distributed VCS (Git)
- It is a distributed Version Control system 



## Personal User account vs Organizational Account 
Everything is same other then limits of size and some different features

![[Pasted image 20250929150953.png]]
![[Pasted image 20250929150957.png]]

![[Pasted image 20250929151153.png]]

- Repository can be created in public as well as private mode 
- The Default Branch is main branch 
- Any changes (New, Edit, Delete ) on the repositorary have to be always comitted
- The commit is identified by the commit id and commit message .
-  Every reposatory has to be represented by the url 
- ![[Pasted image 20250929151223.png]]
- you can also download the project using the download zip option 
- Uploading a file to git hub
![[Pasted image 20250929151304.png]]

-  
![[Pasted image 20250929151413.png]]



![[Pasted image 20250929151620.png]]


Editing the readme file 
![[Pasted image 20250929151807.png]]

![[Pasted image 20250929151748.png]]


 Create a new file 
 ![[Pasted image 20250929151850.png]]
  
 ![[Pasted image 20250929152237.png]]
 
 ![[Pasted image 20250929152211.png]]

 
 ![[Pasted image 20250929152118.png]]
empty folder can not be created like this you have to make a file in it first after that you will able to commit

- Every change commit has to be done 


![[Pasted image 20250929152436.png]]

![[Pasted image 20250929152459.png]]


![[Pasted image 20250929152510.png]]




### Cloning a repo 


```bash
git clone https://github.com/harivanshx/Cdac-Pgdai-Git-Session.git

```

Git folder has a hidden git folder that contais the git attribute of every local folder within that directory


Any changes done on the local must be added first to the staging area using the command 
```bash
git add file_name.extension
git add .

# for each and every file
git add -a


``` 


- After the add operation the commit operation will finally save the changes 
- you can use these command for commit in github 
``` bash
git commit -m "Commit Message"
git commit -m "Added index.js file to the code base"



```

- After commit the changes done will be saved to the git local directory
![[Pasted image 20250929154231.png]]
![[Pasted image 20250929154551.png]]

![[Pasted image 20250929154646.png]]


- The local changes can be updated on the remote by using the push operation from the same branch
```bash
git push origin main 
```

![[Pasted image 20250929155919.png]]


The changes done one the remote can be updated on the local by using the pull command 

```bash
git pull

```


![[Pasted image 20250929155903.png]]


In the local an empty repository can be initialize as a git local repository using the command init
```bash
git init
```


Create an empty folder in local 
![[Pasted image 20250929162510.png]]


![[Pasted image 20250929162532.png]]
![[Pasted image 20250929162539.png]]

![[Pasted image 20250929162601.png]]



![[Pasted image 20250929162711.png]]

- to rename the branch with the new name :
```
git branch -m main

```




```
git remote add origin https://github.com/harivanshx/localproject.git
git branch -M main
git push -u origin main
```


To verify the local connection with the remote 

```
git remote -v

```

How to reset git repo

How to revert back from a commit

- Git status is used to track the changes from the working directory towards the git local directory .
``` bash
git status
```


![[Pasted image 20250929165523.png]]



Adding files

![[Pasted image 20250929165950.png]]


Reverting the last commit 




![[Pasted image 20250929170307.png]]

![[Pasted image 20250929170314.png]]



### Concept of branches 
Branches are used for work segregation where multiple people working on a same repository are allocated different branches to manage there work . Finally the changes are updated towards the main branch with the help of merging process.
- The branches are managed locally as well as on remote .



## Q. For the locally created repository establish a connection with a remote, perform all the staging operations and complete the status history of all the commits and finally update the changes on the remote .





## Git command to create the local branch 
Local branches are created from any specific branch in which the entire content of the parent branch will be copied to the child branch 
- Only one folder will appear in the local , irrespective of the number of branches 



``` bash
git branch feature1
# this first command is used to create a branch with the branch name feature1

git branch 
# to list the branches 

git checkout feature1
# to switch to another branch 




```


![[Pasted image 20251001121309.png]]



all the files and folder are there in your main branch
- the branch you are using locally are called local branch 
- you have to create a remote branch first from the main branch 
- then you can create branch from other branches on your repository 


![[Pasted image 20251001122219.png]]

![[Pasted image 20251001122259.png]]
![[Pasted image 20251001122342.png]]




Remote merging of the branches is done with the help of pull requests (PR) 

it is an official request to the admin who will update the merge request 
![[Pasted image 20251001122431.png]]

Pull request is not the pull operation 
- it is like a official request so that the admin can see the changes
- We have to request in term of pr and admin or maintainer of the  repo will initiate the merging process
- merging process will update the work of a specific branch to the main branch
- Merging process will be only done from the branch that is ahead in terms of no. of commits or no. of files

No will will hit the button #compare_and_pull_request 


![[Pasted image 20251001122914.png]]


![[Pasted image 20251001122938.png]]


![[Pasted image 20251001122942.png]]




![[Pasted image 20251001122950.png]]


![[Pasted image 20251001123056.png]]

![[Pasted image 20251001123219.png]]



Using local repom


![[Pasted image 20251001124559.png]]


- Branches are used for work seggrigation


Command to merge the branch in the local 
``` sh
git merge l1
#give this command from the main branch or the active branch
```

To update the local branch on the remote 

```sh
#git push origin "name of branch "
git push origin l1


```
![[Pasted image 20251001131023.png]]



Deletion of branches 
- To delete the merged branches from the local 
```sh
git branch -d l1

```
- To delete the unmerged branches from the local 
``` sh
git branch -D l1
```

to delete the branch from the remote using the local we will write the command :
```sh
git push origin --delete l1
```


The remote branch can be update on the local with the help of fetch operation followed by a checkout
```sh

git fetch origin b1 && git checkout b1
```

if we give the command of fetch and then merge  then it will be a pull operation 

fetch + merge  =  Pull



### Undo Operations in the local 

#### Revert 
- This operation is used to undo the commit followed by a new commit id .

```sh
git revert c8e0cc1753342ea2e6e47d2e50f6ceee00a3a2e0

#git revert commit id

```

- head is a pointer that points to the latest commit
#### Reset Operations 
This is used to unstage the changes and also moves the head pointer to the any other commit  id

```sh
hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git log
commit 2cc93779b852e48689d8e4ef36623cb3f3288c9f (HEAD -> main)
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:27:15 2025 +0530

    added harivansh.py file

commit 257962e65f9bfcfdca5f0b17c2e226d8d63e3508
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:22:57 2025 +0530

    created Harivansh.md file and added some text

commit 4b03bf0446b96c8047113883fa5ba15aa8af4681
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:16:16 2025 +0530

    Reapply "New file doms.txt added"

    This reverts commit 1f5286432f9fc86640951321dcb6aec90308e4ca.

commit 9837c5b4b559f44c208a2712286f85337d7acdfe
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:10:34 2025 +0530

    New text file added

commit 3114fafee1bf94f949fdb5357fafd5d78b098f91
Merge: 1f52864 7fbd0f8
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 12:43:43 2025 +0530

    Merge branch 'main' of https://github.com/harivanshx/localproject

commit 7fbd0f801403a54c6a83dacdbf9a3a90dc83df78 (origin/main, origin/b1, origin/HEAD)
Merge: 84b5a85 bae72b1
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:32:12 2025 +0530

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git reset --soft 4b03bf0446b96c8047113883fa5ba15aa8af4681

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git log
commit 4b03bf0446b96c8047113883fa5ba15aa8af4681 (HEAD -> main)
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:16:16 2025 +0530

    Reapply "New file doms.txt added"

    This reverts commit 1f5286432f9fc86640951321dcb6aec90308e4ca.

commit 9837c5b4b559f44c208a2712286f85337d7acdfe
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:10:34 2025 +0530

    New text file added

commit 3114fafee1bf94f949fdb5357fafd5d78b098f91
Merge: 1f52864 7fbd0f8
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 12:43:43 2025 +0530

    Merge branch 'main' of https://github.com/harivanshx/localproject

commit 7fbd0f801403a54c6a83dacdbf9a3a90dc83df78 (origin/main, origin/b1, origin/HEAD)
Merge: 84b5a85 bae72b1
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:32:12 2025 +0530

    Merge pull request #1 from harivanshx/b1

    DUpdate index.txt

commit bae72b110d278e3ec1d08e662ba476de04b3e893
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:23:36 2025 +0530

    Update index.txt

:

```


#### Git Rm
This command is used to delete the file from the git repository

#### Git Stash
Git stash is used to save or store the status of the working directory without commit the change to one branch and switch over to the other branch.

```sh

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git checkout
AUTO_MERGE    HEAD          b1            main          origin/b1
FETCH_HEAD    ORIG_HEAD     l2            origin/HEAD   origin/main

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git checkout b1
error: Your local changes to the following files would be overwritten by checkout:
        New Text Document.txt
Please commit your changes or stash them before you switch branches.
Aborting

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git stash
Saved working directory and index state WIP on main: 533612c added 2 files

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git checkout b1
branch 'b1' set up to track 'origin/b1'.
Switched to a new branch 'b1'

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (b1)
$ git checkout main
Switched to branch 'main'

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git stash pop
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   New Text Document.txt
        deleted:    harivansh.md
        deleted:    harivansh.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (dfc282d49c7e912bf8636b4b6eb9fd1b062d641b)

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)



```

#### Tag
- This is used to give a bookmark to the committed work 
```sh
git tag v1.1
 
```

``` sh

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git tag v1.1

hariv@Victus MINGW64 /d/CDAC DAI COMPLETE/Classes/AITrends/Git Github Class/localproject (main)
$ git log
commit 533612c6c6488873c05116e426d2cae9c9b8d157 (HEAD -> main, tag: v1.1)
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:34:41 2025 +0530

    added 2 files

commit 4b03bf0446b96c8047113883fa5ba15aa8af4681
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:16:16 2025 +0530

    Reapply "New file doms.txt added"

    This reverts commit 1f5286432f9fc86640951321dcb6aec90308e4ca.

commit 9837c5b4b559f44c208a2712286f85337d7acdfe
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:10:34 2025 +0530

    New text file added

commit 3114fafee1bf94f949fdb5357fafd5d78b098f91
Merge: 1f52864 7fbd0f8
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 12:43:43 2025 +0530

    Merge branch 'main' of https://github.com/harivanshx/localproject

commit 7fbd0f801403a54c6a83dacdbf9a3a90dc83df78 (origin/main, origin/b1, origin/HEAD, b1)
Merge: 84b5a85 bae72b1
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:32:12 2025 +0530

    Merge pull request #1 from harivanshx/b1

    DUpdate index.txt

:
commit 533612c6c6488873c05116e426d2cae9c9b8d157 (HEAD -> main, tag: v1.1)
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:34:41 2025 +0530

    added 2 files

commit 4b03bf0446b96c8047113883fa5ba15aa8af4681
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:16:16 2025 +0530

    Reapply "New file doms.txt added"

    This reverts commit 1f5286432f9fc86640951321dcb6aec90308e4ca.

commit 9837c5b4b559f44c208a2712286f85337d7acdfe
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 15:10:34 2025 +0530

    New text file added

commit 3114fafee1bf94f949fdb5357fafd5d78b098f91
Merge: 1f52864 7fbd0f8
Author: harivanshx <harivanshbhardwaj57@gmail.com>
Date:   Wed Oct 1 12:43:43 2025 +0530

    Merge branch 'main' of https://github.com/harivanshx/localproject

commit 7fbd0f801403a54c6a83dacdbf9a3a90dc83df78 (origin/main, origin/b1, origin/HEAD, b1)
Merge: 84b5a85 bae72b1
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:32:12 2025 +0530

    Merge pull request #1 from harivanshx/b1

    DUpdate index.txt

commit bae72b110d278e3ec1d08e662ba476de04b3e893
Author: Harivansh Bhardwaj <65931691+harivanshx@users.noreply.github.com>
Date:   Wed Oct 1 12:23:36 2025 +0530

```
#### Git Tag

```sh
git tag
```
- to list the tags in the local we use git tag 
- to check how many or which tags we have
	- To push the tag to the github
	```sh
	git push origin v1.1
	```


#### Fork Operation 

To copy someone else work onto your own github account is called forking 🍴
you can not fork your own reposetory on your github account 
the repos reflect somehing like this 