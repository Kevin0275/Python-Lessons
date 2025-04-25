# Instruction(windows)

## Part 1. Install and set up

1. Download the Git for windows:

   - Website: https://git-scm.com/downloads/win

   - verify whether it's successful: 

     ```bash 
     git --version
     ```

     expected output:

     ```bash
     git version 2.x.x.windows.x
     ```

2. Set up git

   - Once Git is installed, we need to configure it will user details.
     ```bash
     git config --global user.name
     git config --global user.email
     ```

     The commands above should be exerted in Git Bash

   - verify:
     ```bash
     git config --list
     ```

3. Once you have created the directory in local computer, there are few commands you need to run:
   ```bash
   git init
   ```

   This will create the .git directory in the local folder, which is where Git will store all the version control information.

## Part 2: Connect Git to GitHub

1. Create a GitHub account

2. Set up SSH keys: secure.

   1. Generate SSH Key Pair: use Git Bash and run:
      ```bash
      ssh-keygen -t rsa -b 4096 -C 'youremail@example.com'
      ```

   2. Add SSH key to SSH agent:
      ```bash
      eval "$(ssh-agent -s)"
      ssh-add ~/.ssh/id_rsa(based on where you created it)
      ```

   3. Add SSH Key to GitHub:
      ```bash
      clip < ~/.ssh/id_rsa.pub
      ```

   4. Test connection:
      ```bash
      ssh -T git@github.com
      ```



## Part 3: Cloning a Repository from GitHub(if the project already exists): Create a local copy of the project.

1. Get the SSH

2. Open the Git Bash:
   ```bash
   git clone git@github.com:username/repository.git
   ```

   But remember do make sure you opened the right directory

## Part 3(if the project isn't created or you just want to link the directory to repository)

1. You need to get the SSH first.

2. run the command:
   ```bash
   git remote add origin git@github.com:yourusername/test-repo.git
   ```

   

## Part 4: Basic Git Commands

1. Checking the Status of the repository
   ```bash
   git status
   ```

2. Making changes and staging files:

   1. After you have made some changes:
      ```bash
      git add filename
      ```

      This will add the file to the staging area. Or to add all modified files:
      ```bash
      git add .
      ```

3. Commit the changes:
   ```bash
   git commit -m 'Some explanation or annotation.'
   ```

4. Push the changes to GitHub
   ```bash
   git push origin master(or other branch name)
   ```

5. If others have changed the files, you can pull the files to local
   ```bash
   git pull origin master
   ```

   

## Part 5: Working with Branches

1. Create a new branch
   ```bash
   git checkout -b new-branch-name
   ```

2. Switching between branches
   ```bash
   git checkout branch-name
   ```

3. Merging the changes from another branch
   ```bash
   git merge feature-branch
   ```

   