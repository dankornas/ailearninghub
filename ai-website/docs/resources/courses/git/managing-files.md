---
title: Managing Files
hide:
  - path
  - navigation
---

# Git & Github: Managing Files


## Delete / Remove Files

In the course of your project, you might need to delete files that are no longer necessary. Git provides a straightforward command to handle this:

```bash
git rm <filename>
```

After executing the above command, the file will be removed from your working directory and the deletion will be staged for the next commit.

**Example**

```bash
git rm oldfile.txt
```

## Restore Files

Mistakes happen. If you've accidentally deleted a file, Git has got your back. You can easily restore a deleted file if it was tracked by Git:

```bash
git restore --source=HEAD~1 -- <filename>
```

This command will restore the file from the last commit (`HEAD~1`).

**Example**

```bash
git restore --source=HEAD~1 -- oldfile.txt
```

## Rename Files

Renaming files in Git ensures that you maintain the file's history. Instead of manually renaming the file and then adding it to Git, use the following command:

```bash
git mv <old-filename> <new-filename>
```

This command will rename the file and stage the renaming for the next commit.

**Example**

```bash
git mv oldfile.txt newfile.txt
```

* * *

Managing files efficiently in Git is crucial for maintaining a clean and organized codebase. By mastering these commands, you ensure that your project remains streamlined and you can easily track changes, deletions, and renames in your repository.

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
