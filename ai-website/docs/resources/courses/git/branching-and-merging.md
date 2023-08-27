---
title: Branching and Merging
hide:
  - path
  - navigation
---

# Git & Github: Branching and Merging

## Branches

In the vast world of Git, branches are a cornerstone. They allow developers to work on different features or bug fixes simultaneously without affecting the main codebase. Think of branches as parallel universes where you can experiment without consequences.

To create a new branch:

```bash
git branch <branch-name>
```

To switch to a branch:

```bash
git checkout <branch-name>
```

**Example**

```bash
git branch feature-login
git checkout feature-login
```

## Merge Branches

Once you've completed the work on a branch, you might want to integrate those changes into the main branch (often called the `master` or `main` branch). This process is called merging.

```bash
git checkout master
git merge <branch-name>
```

**Example**

```bash
git checkout master
git merge feature-login
```

## Delete Branch

After merging, if you no longer need a branch, you can delete it to keep your repository organized.

```bash
git branch -d <branch-name>
```

**Example**

```bash
git branch -d feature-login
```

## Merge Conflicts

Sometimes, when you try to merge branches, Git might get confused if changes in the two branches overlap. This results in a merge conflict. Git will highlight the problematic areas in your code. You'll need to manually resolve these conflicts by choosing which changes to keep.

Once resolved, you can continue the merge process:

```bash
git add .
git commit -m "Resolved merge conflicts"
```

* * *

Branching and merging are fundamental aspects of Git, enabling seamless collaboration and feature development. By understanding and mastering these concepts, you can ensure efficient and conflict-free code collaboration.


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
