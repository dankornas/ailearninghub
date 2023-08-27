---
title: Introduction to Github
hide:
  - path
  - navigation
---

# Git & Github: Introduction to Github

## GitHub: Your Gateway to Open Source Collaboration

GitHub is more than just a platform; it's a vibrant community where developers from around the world collaborate, contribute, and share their code. Whether you're a newbie or a seasoned developer, understanding GitHub is crucial in today's software development landscape. Let's dive into the basics of setting up and using GitHub.

## 1. Set Up GitHub Account

Before you can dive into the world of open-source collaboration, you need a GitHub account.

* Visit [GitHub's official website](https://github.com/).
* Click on the 'Sign Up' button.
* Follow the on-screen instructions to create your account.

## 2. Create a New Cloud Repository

Once you have an account, the next step is to create a repository where you'll store your projects.

* Click on the '+' icon on the top right corner of your GitHub dashboard.
* Select 'New repository'.
* Name your repository, provide a brief description, and choose whether to make it public or private.
* Click 'Create repository'.

**Example**

```markdown
Repository Name: MyFirstRepo
Description: This is my first GitHub repository.
Visibility: Public
```

## 3. Push Local Repo to GitHub

If you have a project on your local machine that you'd like to share with the world, you can push it to your GitHub repository.

First, navigate to your project directory in your terminal or command prompt:

```bash
cd path/to/your/project
```

Then, initialize a Git repository:

```bash
git init
```

Add all your files to the repository and commit them:

```bash
git add .
git commit -m "Initial commit"
```

Now, link your local repository to the GitHub repository:

```bash
git remote add origin https://github.com/YourUsername/YourRepoName.git
```

Finally, push your code to GitHub:

```bash
git push -u origin master
```

* * *

GitHub is the heart of open-source collaboration, offering a plethora of tools and features to enhance your coding journey. By understanding the basics of GitHub, you pave the way for endless opportunities in software development and collaboration.


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
