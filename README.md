# Getting Started
## Organization of this Github page 

Explanation of folders: 

- __cluster__: contains helpful commands for working on Slurm-based clusters. Within this folder, there are three subfolders containing information specific to the TTIC, LLNL, and RCC clusters.
- __resolved_errors__: contains reports of error messages along with the lines of code executed that resolved the issue
- __scripts__: contains general purpose code files 


## Setting up Github to contribute to this repository

Cloning this respository:

```git clone https://github.com/Melissa3248/Code-Help.git```

Initializing Github to track changes in your local copy of the Code-Help folder (commands should be run in the Code-Help folder):

```git init```

```git remote add origin git@github.com:Melissa3248/Code-Help.git```


Add all changed files to be committed:

```git add -A```

Commit and add a short, descriptive message about the changes:

```git commit -m "message"```

Push changes to Github:

```git push origin main```

Pull new changes made to the respository to a local copy:

```git pull origin main```