# **How to Create Tutorials for the AI Learning Hub** 📝

Thank you for contributing to the AI Learning Hub! This guide explains how to create tutorials that fit seamlessly into the project. By following these steps, we can maintain consistency, organization, and high-quality content.

* * *

## **Step 1: Prerequisites**

Before you start working on your tutorial:

1. **Create or Select an Issue**: Ensure you’ve created or selected an issue in the [GitHub Issues](https://github.com/dankornas/ailearninghub/issues) section and received approval to proceed.
2. **Set Up Your Environment**: Follow the [How to Contribute](#) guide to set up your development environment, including installing dependencies and activating your virtual environment.

* * *

## **Step 2: File Structure**

After your issue has been approved and you’re ready to start, you’ll need to create a new file in the appropriate directory under `ai-learning-roadmap`. The directory structure is as follows:

```markdown
docs/
└── ai-learning-roadmap/
    ├── 0_programming/
    ├── 1_working_with_data/
    ├── 2_machine_learning/
    ├── 3_deep_learning/
    └── 4_mlop_deployment/
```

* **Choose the directory** that best matches your tutorial topic:
    * **`0_programming`**: Tutorials on programming fundamentals like Python, algorithms, and basic data structures.
    * **`1_working_with_data`**: Tutorials on working with data, including data cleaning, Pandas, NumPy, and visualization.
    * **`2_machine_learning`**: Tutorials on machine learning models, algorithms, and workflows.
    * **`3_deep_learning`**: Tutorials on neural networks, advanced AI techniques, and frameworks like TensorFlow and PyTorch.
    * **`4_mlop_deployment`**: Tutorials on deploying machine learning models, pipelines, and MLOps best practices.

* * *

## **Step 3: Working with Jupyter Notebooks**

The tutorials in this project will primarily be created using **Jupyter Notebooks** (`.ipynb` files). MkDocs-Jupyter will render these notebooks as interactive pages, so it’s important to follow formatting conventions to ensure proper rendering.

### **How to Create and Save Your Notebook**

1. Navigate to the directory where your tutorial will live (e.g., `docs/ai-learning-roadmap/2_machine_learning`).
2. Open Jupyter Notebook or Jupyter Lab in your terminal:
    
    ```bash
    jupyter notebook
    ```
    
3. Create a new notebook and save it with a descriptive name, such as:
    
    ```
    tutorial_name.ipynb
    ```
    
4. Add your content using the structure outlined below.

* * *

## **Step 4: Formatting Standards**

When using **MkDocs-Jupyter**, you’ll need to follow specific formatting conventions to ensure the notebook renders correctly. Here’s a breakdown:

### **Markdown Cells**

Use markdown cells for explanations, headings, and structured text. Below are some formatting guidelines:

* **Headings**: Use markdown syntax for section headers.
    * `# Main Title`
    * `## Section Title`
    * `### Subsection Title`
* **Text Emphasis**:
    * _Italics_: Surround text with single asterisks or underscores:  
        `_italic text_` or `*italic text*`
    * **Bold**: Surround text with double asterisks:  
        `**bold text**`
    * _**Bold Italics**_: Combine both:  
        `***bold italic text***`
* **Bullet Points**: Use `-` or `*` for unordered lists:
    
    ```markdown
    - First item
    - Second item
    ```
    
* **Numbered Lists**: Use numbers for ordered lists:
    
    ```markdown
    1. Step one
    2. Step two
    ```
    
* **Links**: Use `[text](url)` to create hyperlinks:
    
    ```markdown
    [GitHub Repository](https://github.com/dankornas/ailearninghub)
    ```
    
* **Inline Code**: Use backticks for inline code:
    
    ```markdown
    Use `print()` to display output in Python.
    ```
    

### **Code Cells**

Use Python code cells for any programming examples or exercises. MkDocs-Jupyter renders these as executable cells. Ensure the following:

1. Include relevant comments for clarity:
    
    ```python
    # This function adds two numbers
    def add(a, b):
        return a + b
    ```
    
2. Provide input/output examples where possible:
    
    ```python
    result = add(5, 10)
    print(result)  # Output: 15
    ```
    
3. Keep code concise and avoid overly complex examples.

### **Tables**

You can create tables in markdown cells for structured data:

```markdown
| Parameter | Description     | Example  |
|-----------|-----------------|----------|
| Name      | The user's name | John Doe |
| Age       | User's age      | 25       |
```

### **Images**

Add images by linking them with markdown syntax:

```markdown
![Alt Text](path/to/image.png)
```

### **Tips and Notes**

Use blockquotes for additional tips, notes, or warnings:

```markdown
> **Note:** Ensure your Python version matches the required dependencies.
```

* * *

## **Step 5: Add Author Information**

While creating your tutorial or immediately after, include a section at the end of your Jupyter notebook to provide information about yourself. This helps recognize contributors and builds a sense of community.

### **Template for Author Information**

At the end of your Jupyter notebook, add the following markdown cell:

```markdown
---

## About the Author

This tutorial was created by **Your Name**.

- **GitHub**: [@your-github-username](https://github.com/your-github-username)
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
- **Twitter**: [@your-twitter-handle](https://twitter.com/your-twitter-handle) (optional)

If you have any questions or feedback, feel free to reach out or submit an issue in the [AI Learning Hub GitHub repository](https://github.com/dankornas/ailearninghub).

---
```

* * *

## **Step 6: Content Guidelines**

* Write tutorials in **simple, clear, and engaging language**.
* **Structure** your tutorial into sections:
    1. **Introduction**: Briefly explain the topic and what learners will achieve.
    2. **Prerequisites**: List any tools, libraries, or knowledge needed.
    3. **Step-by-Step Guide**: Explain each step clearly with examples.
    4. **Conclusion**: Summarize the key takeaways and encourage further exploration.
* Use **real-world examples** whenever possible to demonstrate practical applications.
* Avoid overly long sections—break content into digestible chunks.

* * *

## **Step 7: Testing and Previewing**

Before submitting your tutorial:

1. Run your Jupyter notebook end-to-end to ensure:
    * All code runs without errors.
    * Outputs match what’s expected.
2. Use the `mkdocs serve` command to preview your tutorial locally:
    
    ```bash
    mkdocs serve
    ```
    
3. Open the provided URL (usually `http://127.0.0.1:8000`) to verify formatting and readability.

* * *

## **Step 8: Submit Your Tutorial**

Once your tutorial is complete and tested:

* **Commit your changes** with a descriptive message.
* Create a **pull request** and link it to your issue.
* Be open to feedback from maintainers to refine your work.

* * *

Thank you for contributing to the AI Learning Hub and helping us create a world-class learning resource! 🚀
