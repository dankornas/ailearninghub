---
title: Unsupervised Learning
hide:
  - path
  - navigation
---

# Machine Learning: Unsupervised Learning

## **What is Unsupervised Learning?**

**Unsupervised learning** is one of the core categories of machine learning techniques. Unlike its counterpart, supervised learning, where we teach the algorithm what to do by providing it with labeled data, unsupervised learning involves training the algorithm using data that is neither classified nor labeled. This means the system tries to learn the patterns and the structure from the data without any prior training of data.

### **Why is it called "Unsupervised?"**

The term "unsupervised" refers to the fact that the algorithm isn't given explicit instructions on how to perform the task. Instead, it must figure out for itself how to perform the task, typically by discovering and adapting to patterns in the data.

## **Applications of Unsupervised Learning**

From business to healthcare, unsupervised learning has a wide array of applications. Here are some of the most common:

### **Market Segmentation**

Companies often have vast amounts of data about their customers but may not know which customers share common characteristics. Using clustering, a type of unsupervised learning, companies can identify these segments and tailor their marketing strategies accordingly.

### **Anomaly Detection**

Credit card companies use unsupervised learning to detect fraudulent transactions. If a new transaction doesn't fit the established pattern of a user's previous transactions, it may be flagged for further investigation.

### **Recommendation Systems**

Popular platforms like Netflix or Amazon use unsupervised learning to group similar items. When a user watches a movie or buys a product, these systems can recommend other items from the same group.

## **Key Techniques in Unsupervised Learning**

There are several techniques in unsupervised learning. The two most commonly used are:

### **Clustering**

This is about grouping a set of data points based on similarity. Common algorithms for clustering include K-means, hierarchical clustering, and DBSCAN.

#### **K-means Clustering**

K-means clustering aims to partition a set of points into K clusters, where each point belongs to the cluster with the nearest mean. The algorithm iteratively assigns points to clusters and recalculates cluster means until convergence.

### **Dimensionality Reduction**

Dimensionality reduction is about reducing the number of random variables under consideration and obtaining a set of principal variables. Principal Component Analysis (PCA) is a popular technique in this category.

#### **Principal Component Analysis (PCA)**

PCA is a statistical procedure that uses an orthogonal transformation to convert correlated features into a set of values of linearly uncorrelated features called principal components.

## **Advantages and Disadvantages of Unsupervised Learning**

Every machine learning technique has its strengths and weaknesses. Let's delve into the pros and cons of unsupervised learning.

### **Advantages**

1. **No Labeling Required**: Since unsupervised learning doesn't require labeled data, the data preparation phase is often quicker and less intensive.
2. **Discovery of Unknown Patterns**: Unsupervised learning can identify patterns and relationships in the data that may not be apparent or known beforehand.
3. **Flexibility**: It's adaptable to changes and can handle new, unseen data without requiring a retrain.

### **Disadvantages**

1. **Less Accuracy**: As there's no single source of truth (i.e., labels), the accuracy of unsupervised learning models can be lower than that of supervised models.
2. **Complexity**: These models can sometimes be hard to interpret, making it challenging to derive actionable insights.
3. **Requires Expertise**: Due to its complexity and subtlety, unsupervised learning often requires a higher level of expertise to implement effectively.

## **Wrapping Up**

Unsupervised learning offers a unique approach to extracting knowledge from data. While it may not always provide the pinpoint accuracy of supervised methods, its ability to uncover hidden patterns and relationships makes it invaluable in many domains. As with all machine learning techniques, understanding its strengths, limitations, and ideal use-cases is key to effectively leveraging its power.

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