---
title: Working with Repositories
hide:
  - path
  - navigation
---

# Git & Github: Working with Repositories

## Initialize Repository

Starting with Git is as simple as creating a new repository. A repository (or "repo") is essentially a directory where Git has been initialized to start version tracking.

```bash
git init
```

Executing the above command will initialize a new Git repository and begin tracking an existing directory.

## Git Status

To understand the state of your repository – which files have been modified, which are staged, and which are not being tracked – use the `git status` command.

```bash
git status
```

This command provides a concise overview of changes that are yet to be committed.

## Track and Untrack Files

When you create or modify a file, Git doesn't automatically start tracking it. To start tracking a new file or stage modifications to existing files:

```bash
git add <filename>
```

To untrack a file that has been added but not yet committed, use:

```bash
git rm --cached <filename>
```

## Ignore Files with .gitignore

There might be files or directories that you don't want Git to track, like log files or the `node_modules` directory. For this, create a `.gitignore` file in the root of your repository. Any file or directory name listed in this file will be ignored by Git.

Example `.gitignore` content:

```bash
*.log
node_modules/
```

## Track All Files / Add to Staging

To add all the new or modified files to the staging area in one go:

```bash
git add .
```

## Commit

Once you've staged your changes, you can commit them to your repository with a descriptive message.

```bash
git commit -m "Your descriptive message here"
```

## Change Files and View Differences

After making changes to your files, you can view the differences between the staged changes and the last commit using:

```bash
git diff
```

## Bypass Staging and Commit

If you've modified a file but haven't staged it yet, you can bypass the staging area and commit changes directly:

```bash
git commit -a -m "Your message here"
```

This command is a shortcut that stages all tracked, modified files and commits them in one step.

* * *

Mastering the art of managing repositories is fundamental to becoming proficient with Git. By understanding the core commands and their applications, you're well on your way to leveraging the full power of Git in your projects.

---

!!! note "Version 1.0"

    This is currently an early version of the learning material and it will be updated over time with more detailed information.

    A video will be provided with the learning material as well.

    Be sure to subscribe to stay up-to-date with the latest updates.

<div style="padding: 20px; color: white; background-color: #0f1624; border-radius: 10px; margin: 10px 0 20px 0; text-align: center;">
    <h2 style="color: white;">Need help mastering Machine Learning?</h2>
    <p style="font-size: 16px;">Don't just follow along — join me!
    Get exclusive access to me, your instructor, who can help answer any of your questions. Additionally, get access to a private learning group where you can learn together and support each other on your AI journey.
    </p><br>
    <div style="text-align: center; margin-bottom: 20px;">
        <button style="display: inline-block; padding: 10px 20px; font-size: 20px; color: white; background: #1018A8; border: none; border-radius: 5px;">
            <a href="/subscribe" style="color: white; text-decoration: none;">Subscribe Now</a>
        </button>
    </div>
</div>
