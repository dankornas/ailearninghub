---
title: K-Nearest Neighbor
hide:
  - path
  - navigation
---

# Machine Learning: K-Nearest Neighbor

## **What is K Nearest Neighbor (KNN)?**

K Nearest Neighbor, commonly abbreviated as KNN, stands tall as one of the simplest yet most intuitive machine learning algorithms in the toolkit of a data scientist. It is a supervised learning algorithm, which means it learns from labeled data, and then uses this learned backdrop to classify new data points or predict continuous values.

Imagine you're in a room filled with people of various professions. If you want to guess the profession of a person, one intuitive way might be to look at the professions of the people standing closest to him or her. If, for instance, most of them are doctors, there's a good chance the person in question is also a doctor. KNN operates on a similar principle, but in the realm of data.

* * *

## **How Does It Work?**

The mechanics behind KNN are straightforward:

1. **Distance Calculation:** For a given data point that needs classification or prediction, KNN starts by calculating the distance (e.g., Euclidean, Manhattan, etc.) between the point in question and all the other data points in the dataset.
    
2. **Selecting K Neighbors:** It then sorts these distances and selects the top 'K' data points which are nearest to the given data point. Here, 'K' can be any integer.
    
3. **Decision Making:**
    
    * For **classification tasks**, KNN counts the number of data points in each category among the 'K' neighbors. The category with the highest count becomes the predicted category for the given data point.
    * For **regression tasks**, it might take the average or median of the 'K' neighbors as the prediction.
4. **Choosing the Right 'K':** A smaller 'K' value, like 1 or 3, can be noisy and subject to outliers, while a larger 'K' can be computationally expensive and might smooth over the data too much. Finding the right 'K' is crucial and often done through experimentation.
    

* * *

## **What is KNN Used For?**

KNN is incredibly versatile, finding its use-cases across various domains:

1. **Medical Diagnoses:** Predicting whether a tumor is benign or malignant based on its characteristics, by looking at other similar cases.
2. **Recommendation Systems:** Recommending products, movies, or music based on user preferences. If a user likes certain items, they're likely to like other items that similar users have preferred.
3. **Financial Services:** Assessing creditworthiness by comparing a client's profile with profiles of other clients with known credit histories.
4. **Image Recognition:** Identifying what object or category an image belongs to by comparing its features with features of labeled images.

Given its simplicity and the fact that it makes no underlying assumptions about the data, KNN is often a good starting point in the data exploration phase.

* * *

## **A Very Detailed Example with Code and Thorough Explanations**

Let's embark on a journey through a classic example: **Classifying Iris flowers based on their features**.

**Data**

The Iris dataset is renowned in the machine learning community. It consists of 150 samples from each of three species of Iris flowers (Setosa, Virginica, and Versicolor). Four features were measured from each sample: the lengths and the widths of the sepals and petals.


### **1. Data Loading and Preparation**

To kick things off, we'll load the data and prepare it for our KNN model.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

### **2. Building the KNN Model**

With our data ready, we can now build and train our KNN model.

```python
from sklearn.neighbors import KNeighborsClassifier

# Initialize the model with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the model
knn.fit(X_train, y_train)
```

### **3. Making Predictions**

It's time to put our model to the test!

```python
# Predict on test data
y_pred = knn.predict(X_test)

# Check accuracy
accuracy = (y_pred == y_test).mean()
print(f"Accuracy: {accuracy * 100:.2f}%")
```

### **4. Understanding the Outcome**

After running the code, you'll get an accuracy score. This score tells you how well the model performed on the test data. A higher score indicates that the model was able to correctly classify the Iris flowers based on their features with a high degree of accuracy.

* * *

To sum up, the K Nearest Neighbor algorithm is a testament to the fact that sometimes, simplicity can be incredibly effective. Its intuitive approach, coupled with its adaptability, makes it an indispensable tool for both budding and seasoned machine learning practitioners. Whether you're classifying flowers or recommending movies, KNN stands ready to be your algorithmic ally.

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