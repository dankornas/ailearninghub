---
title: Stacking
hide:
  - path
  - navigation
---

# Machine Learning: Stacking

## **What is Stacking?**

**Stacking** is a powerful ensemble learning technique that combines multiple machine learning models to achieve better predictive performance. Think of stacking as building a tower, where each block (or model) adds to the strength and stability of the overall structure.

In the context of machine learning, instead of relying on the predictions of a single model, stacking leverages the strengths of several models, allowing them to "collaborate" and produce a more accurate and robust prediction. It's like assembling a team of experts from different fields to solve a complex problem — each contributes their unique expertise, leading to a more comprehensive solution.

## **How Does It Work?**

Stacking might seem intricate at first glance, but its underlying principle is quite intuitive. Here's a breakdown:

### **1. Splitting the Data**

The dataset is typically divided into a training set and a validation set (or multiple validation sets in k-fold cross-validation).

### **2. Base Model Training**

Multiple models, known as "base models" or "level-0 models," are trained on the training dataset.

### **3. Base Model Predictions**

These base models then make predictions on the validation set. These predictions are treated as "new features" or "meta-features."

### **4. Meta-model Training**

A new model, often referred to as the "meta-model" or "level-1 model," is trained on the meta-features. Essentially, this model learns how to best combine the predictions of the base models to achieve a better result.

The beauty of stacking is that it allows models to correct each other's mistakes, leading to a more accurate ensemble prediction.

## **What is it Used For?**

Stacking, with its ensemble nature, finds applications in a variety of domains:

### **Performance Boost**

In competitions like those on Kaggle, stacking is often employed to squeeze out that extra bit of accuracy and climb the leaderboard.

### **Robustness**

By combining multiple models, stacking often results in a more stable and robust model that's resilient to outliers and noise.

### **Handling Diverse Data Sources**

In scenarios where data comes from various sources or has diverse features, different models might excel in capturing different data patterns. Stacking can effectively combine these models, ensuring comprehensive learning.

## **A Detailed Example with Code**

Let's dive into a hands-on example using the Iris dataset. We'll use three base models: Logistic Regression, Decision Tree, and K-Nearest Neighbors. Our meta-model will be a Random Forest.

### **Loading the Data**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### **Training Base Models**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Base models
lr = LogisticRegression()
dt = DecisionTreeClassifier()
knn = KNeighborsClassifier()

# Training base models
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
knn.fit(X_train, y_train)
```

### **Base Model Predictions**

```python
lr_pred = lr.predict(X_test)
dt_pred = dt.predict(X_test)
knn_pred = knn.predict(X_test)

# Stacking predictions to form new features
stacked_predictions = np.column_stack((lr_pred, dt_pred, knn_pred))
```

### **Training the Meta-model**

```python
from sklearn.ensemble import RandomForestClassifier

# Meta-model
rf = RandomForestClassifier(n_estimators=100)

# Training meta-model
rf.fit(stacked_predictions, y_test)
```

### **Making Predictions with the Stacked Model**

To predict using the stacked model, we'd first get predictions from our base models and then input these predictions into our meta-model:

```python
base_predictions = np.column_stack((lr.predict(X_test), dt.predict(X_test), knn.predict(X_test)))
final_predictions = rf.predict(base_predictions)
```

### **Evaluating the Stacked Model**

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, final_predictions)
print(f"Stacked Model Accuracy: {accuracy*100:.2f}%")
```

### **Interpreting the Results**

The stacked model's accuracy shows the combined predictive power of our base models and meta-model. In many cases, a well-constructed stacked model can outperform any individual base model. It's a testament to the old adage: "The whole is greater than the sum of its parts."

## **Wrapping Up**

Stacking offers a sophisticated approach to ensemble learning, allowing multiple models to come together in a harmonious symphony of predictions. It embodies the collaborative spirit of machine learning, where diverse algorithms join forces to tackle complex challenges. Whether you're a beginner just starting out or an experienced practitioner, understanding and harnessing the power of stacking can significantly elevate your machine learning endeavors.

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