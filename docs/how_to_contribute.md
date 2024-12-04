# **How to Contribute to the AI Learning Hub 🛠️**

We’re thrilled that you’re interested in contributing to the **AI Learning Hub**! This guide will walk you through the steps to make your contributions seamless. Whether you’re submitting new tutorials, fixing bugs, or suggesting improvements, your efforts make a difference.

* * *

## **Step 1: Familiarize Yourself with the Project**

Before contributing, take some time to:

* Explore the [GitHub repository](https://github.com/dankornas/ailearninghub).
* Understand the structure of the project and where your contribution fits.
* Review any open issues or pull requests to avoid duplication.

* * *

## **Step 2: Create or Select an Issue**

1. **Check for Existing Issues**:
    
    * Browse the [Issues](https://github.com/dankornas/ailearninghub/issues) section to see if your idea or task is already listed.
    * If you find an issue you'd like to work on, comment on it to let the maintainers know you're taking it up. Example comment:  
        _"I’d like to work on this issue. Please assign it to me!"_
2. **Create a New Issue**:
    
    * If your contribution is new and not listed, create a detailed issue describing your idea or proposed feature.
    * Include as much information as possible, such as the content type, purpose, and scope.
    * Wait for approval from the maintainers before proceeding.

👉 **[Submit or Review Issues Here](https://github.com/dankornas/ailearninghub/issues)**

* * *

## **Step 3: Fork the Repository**

1. Navigate to the [AI Learning Hub GitHub repository](https://github.com/dankornas/ailearninghub).
2. Click the **Fork** button in the top-right corner to create a personal copy of the repository.

* * *

## **Step 4: Clone Your Fork**

1. Open your terminal or command prompt.
    
2. Clone your forked repository to your local machine by running:
    
    ```bash
    git clone https://github.com/<your-username>/ailearninghub.git
    ```
    
    Replace `<your-username>` with your GitHub username.
    

* * *

## **Step 5: Set Up Your Development Environment**

1. Navigate to the project directory:
    
    ```bash
    cd ailearninghub
    ```
    
2. Create a virtual environment:
    
    ```bash
    python -m venv env
    ```
    
3. Activate the virtual environment:
    
    * On Windows:
        
        ```bash
        .\env\Scripts\activate
        ```
        
    * On macOS/Linux:
        
        ```bash
        source env/bin/activate
        ```
        
4. Install the required Python libraries:
    
    ```bash
    pip install -r requirements.txt
    ```
    

* * *

## **Step 6: Make Your Changes**

* Add or edit content, code, or documentation based on the approved issue or feature request.
* Follow the existing project structure and style guides.
* Test your changes locally to ensure everything works as expected.

### **Creating Tutorials**

1. **Use the Python Basics Template**:  
    When creating a new tutorial, base your tutorial off the Python Basics tutorial located at:
    
    ```plaintext
    docs/ai_learning_roadmap/0_programming/python/basics.ipynb
    ```
    
    This ensures consistency in structure and formatting.

2. **Place Your Tutorial Correctly**:  
    Save your tutorial in the appropriate category and subdirectory, similar to how the Python Basics tutorial is structured.
    
3. **Add Your Tutorial to the mkdocs.yml File**:  
    Once your tutorial is created, you need to add it to the `mkdocs.yml` file for it to appear in the website navigation. Follow these steps:
    * Open the `mkdocs.yml` file in the root directory of the project.
    * Locate the section corresponding to your tutorial's category (e.g., Programming, Working with Data).
    * Add your tutorial under the appropriate subcategory, following the same format as the Python Basics file:
        
        ```yaml
        - Programming:
            - "[Contribute]": 'ai_learning_roadmap/0_programming/contribute.md'
            - Python:
                - Basics: 'ai_learning_roadmap/0_programming/python/basics.ipynb'
                - Your Tutorial Title: 'path/to/your/tutorial/file.ipynb'
        ```
        
    * Use the example in the image below for guidance:
    * Ensure the file path matches the directory where your tutorial is saved.

* * *

## **Step 7: Preview Your Changes Locally**

Before creating a pull request, ensure your changes render correctly by using `mkdocs`:

1. Start the development server:
    
    ```bash
    mkdocs serve
    ```
    
2. Open the provided URL in your browser (usually `http://127.0.0.1:8000`) to preview your changes.
    
3. Verify that everything looks and functions as expected.
    

* * *

## **Step 8: Commit Your Changes**

1. Stage your changes:
    
    ```bash
    git add .
    ```
    
2. Commit your changes with a meaningful message:
    
    ```bash
    git commit -m "Add/Update [description of your changes]"
    ```
    

* * *

## **Step 9: Push to Your Fork**

Push your branch to your forked repository:

```bash
git push origin feature/your-feature-name
```

* * *

## **Step 10: Create a Pull Request**

1. Go to the original [AI Learning Hub repository](https://github.com/dankornas/ailearninghub).
2. Click the **Pull Requests** tab, then click **New Pull Request**.
3. Select **Compare Across Forks**.
4. Set the base repository to `dankornas/ailearninghub` and the compare repository to your fork.
5. Add a clear title and description of your changes, referencing the approved issue number (e.g., "Fixes #42").
6. Confirm that you’ve previewed your changes locally using `mkdocs serve` and include this note in your pull request description.
7. Submit the pull request.

* * *

## **Step 11: Collaborate and Refine**

* The maintainers will review your pull request.
* Be open to feedback and make necessary adjustments.

* * *

## **Step 12: Celebrate Your Contribution! 🎉**

Once your pull request is merged, your contribution becomes part of the AI Learning Hub! Share your achievement with the community.

* * *

## **Additional Tips**

* **Ask Questions**: If you’re unsure about anything, ask in our [Discord Community](https://discord.gg/VQCSmfWvm6).
    
* **Be Respectful**: Follow the [Contributor Code of Conduct](https://github.com/dankornas/ailearninghub/blob/main/CODE_OF_CONDUCT.md) to ensure a welcoming environment for all contributors.
    
* **Stay Updated**: Keep your fork in sync with the original repository by pulling updates regularly:
    
    ```bash
    git fetch upstream
    git merge upstream/main
    ```
    

* * *

We’re excited to have you on board! Together, we’re building something extraordinary for the AI community.