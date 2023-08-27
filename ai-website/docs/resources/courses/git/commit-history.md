---
title: Exploring Commit History
hide:
  - path
  - navigation
---

# Git & Github: Exploring Commit History

## View Commit History with Git Log

Git provides a powerful tool to view the commit history of your repository - the `git log` command. This command displays a list of commits in reverse chronological order, showing the commit hash, author, date, and commit message.

```bash
git log
```

You can also use various options to customize the output, such as `--oneline` for a concise view or `--graph` to see a graphical representation of the commit history.

**Example:**

```bash
git log --oneline --graph
```

## Amend Commit

If you've made a mistake in your last commit message or forgot to include a file, you can amend the commit using:

```bash
git commit --amend
```

This command opens the default text editor with the last commit message. You can edit the message, save, and close the editor. If you've added new changes to the staging area, they will be included in the amended commit.

**Example**

```bash
echo "New content" >> file.txt
git add file.txt
git commit --amend
```

## View Changes in Commits

To view the changes made in a specific commit, use the `git show` command followed by the commit hash:

```bash
git show <commit-hash>
```

This command displays the commit information and the differences introduced in that commit.

**Example**

```bash
git show a1b2c3d4
```

## Reset to Previous Commit

If you need to undo changes and revert your repository to a previous commit, use the `git reset` command:

```bash
git reset --hard <commit-hash>
```

This command discards all commits after the specified commit hash and resets the working directory to that commit.

**Example**

```bash
git reset --hard a1b2c3d4
```

## Rebase Git Repository

Rebasing is a powerful feature in Git that allows you to move or combine a sequence of commits to a new base commit. It's particularly useful for integrating changes from one branch into another.

```bash
git rebase <base-branch>
```

This command replays the commits from the current branch onto the base branch, creating a linear history.

**Example**

```bash
git checkout feature-branch
git rebase master
```

* * *

Exploring the commit history and manipulating commits are essential skills for every Git user. By mastering these commands, you gain a deeper understanding of your project's history and can effectively manage your repository.

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
