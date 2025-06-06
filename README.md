# Getting Started

## Organization of this Github page

Explanation of folders:

- **cluster/**: contains helpful commands for working on Slurm-based clusters. The README has tips on using conda for managing Python environments and tips for setting up SSH for accessing remote clusters.
  - **TTIC/**: Information specific to the TTIC cluster.
  - **LBNL/**: Information specific to Lawrence Berkeley National Laboratory's computing cluster.
  - **RCC/**: Information specific to UChicago Research Computing Center's resources.
- **resolved_errors/**: contains reports of error messages along with the lines of code executed that resolved the issue
- **LaTeX_paper_writing/**: Tips (and links to Overleaf guides) for preparing documents in LaTeX.
- **scripts/**: contains general purpose code files
- **sqlite_database/**: An example of a SQLite database for training many different models with interdependence.

The gitignore file is also meant to be educational (while also functioning as the actual gitignore file for the repo).

## How to Contribute

You can contribute in different ways, including asking a question or adding some knowledge:

### Asking a question

The preferred way to ask a question is to create an issue on GitHub. Here is a [link](https://github.com/Melissa3248/Code-Help/issues/new) to create a new issue. If the issue goes unanswered for a long time, it may be faster to start asking group members in person.

### Adding some knowledge

To add to the repository, you'll have to clone the repository to your personal computer, edit one or more of the files, and push the changes to GitHub:

1. Clone the repository to your personal computer. This means using git to make a local copy of all of the files on your computer, so you can edit them. You can do this with the following command:
   ```
   git clone https://github.com/Melissa3248/Code-Help.git
   ```
2. Pull any new changes from GitHub. Before doing any editing, it's important to make sure the local copy of the repository is up to date. The best way to do this is to run
   ```
   git pull origin main
   ```
3. Edit one or more of the files.
4. Push the changes to GitHub. This takes a few commands. First, you'll want to add the files you've changed. You can do this by running the following command to add all files at once.

   ```
   git add -A
   ```

   If you made some changes that you don't want to push, you can run `git add <file_name>` to add files one at a time. If you aren't sure which files you've changed, you can use `git status` to show which files have been changed.
   Next, you want to commit and add a short, descriptive message about the changes:

   ```
   git commit -m "message"
   ```

   And finally, push changes to Github:

   ```
   git push origin main
   ```
