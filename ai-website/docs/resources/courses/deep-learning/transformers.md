---
title: Transformers
hide:
  - path
  - navigation
---

# Deep Learning: Transformers

## **Unveiling the Power of Transformers**

In the ever-evolving world of deep learning, the Transformer architecture has emerged as a true game-changer, setting new benchmarks and reshaping the domain of sequence modeling. From the intricacies of language translation to the nuances of chatbots, Transformers are powering some of the most advanced models in natural language processing, like BERT and GPT.

### **The Backdrop: Why Transformers?**

While Recurrent Neural Networks (RNNs) and their advanced versions like LSTMs and GRUs made significant strides in sequence modeling, they often struggled with long-term dependencies and parallelization. Enter Transformers, with their ability to handle sequences without the inherent sequential nature of RNNs, ensuring faster processing and better handling of long-range dependencies.

## **Diving Deep into the Transformer Architecture**

At its core, the Transformer architecture is built upon attention mechanisms, allowing it to focus on different parts of the input data to produce outputs.

### **1. Attention Mechanism: The Star Player**

The crux of Transformers lies in their ability to weigh the importance of different parts of the input data, a phenomenon termed as 'attention'.

* **Scaled Dot-Product Attention**: This mechanism scores the relevance of different parts of the input, allowing the model to focus more on parts that are more relevant.
* **Multi-Head Attention**: Instead of having one set of attention weights, Transformers use multiple sets, enabling them to focus on different parts of the input simultaneously.

### **2. Positional Encoding: Giving Sense to Order**

Unlike RNNs, Transformers don't process data sequentially, which means they don't inherently understand the order of data. Positional encodings are added to ensure the model recognizes the position of each item in the sequence.

### **3. Feed-Forward Neural Networks: The Classic Touch**

Each Transformer layer contains a feed-forward neural network that operates independently on each position, processing the attention's output.

### **4. Residual Connections & Layer Normalization: Ensuring Stability**

To enhance training stability and speed, Transformers use residual connections around each sub-layer (including attention and feed-forward neural network). Layer normalization is also applied before each sub-layer.

## **The Transformer's Journey: Encoding & Decoding**

A classic Transformer model consists of an encoder that processes the input data and a decoder that produces the output.

### **1. Encoder: Processing the Input**

The encoder comprises stacked layers of multi-head attention and feed-forward neural networks. It takes in the input, applies attention mechanisms, and passes the data through feed-forward networks.

### **2. Decoder: Generating the Output**

The decoder also has stacked layers, but with an additional multi-head attention layer to attend to the encoder's output. This structure enables it to generate relevant and context-aware outputs.

## **Applications of Transformers: Beyond Just Text**

While Transformers made their mark in natural language processing, their applications span a variety of domains:

1. **Machine Translation**: Translating text from one language to another with remarkable accuracy.
2. **Text Summarization**: Creating concise summaries of lengthy texts.
3. **Image Processing**: With Vision Transformers (ViTs), the architecture is breaking grounds in computer vision tasks.
4. **Speech Recognition**: Handling audio data to convert speech into text or understand commands.

## **Training Transformers: A Delicate Affair**

Given their deep architectures, training Transformers requires careful strategies:

1. **Learning Rate Scheduling**: A warm-up and cool-down phase for learning rates ensures stable and faster convergence.
2. **Regularization**: Techniques like dropout and label smoothing help in preventing overfitting and enhancing generalization.
3. **Huge Datasets & Compute**: Transformers, especially larger variants, benefit from vast amounts of data and substantial computational resources.

## **Text Classification with Transformers**

For this tutorial, we'll use a Transformer to classify text sentiments as positive or negative.

### **1. Setting Up the Environment**

Ensure you have TensorFlow installed:

```python
pip install tensorflow
```

### **2. Preparing the Dataset**

We'll use a sample dataset for our tutorial. TensorFlow provides the IMDB dataset, which is perfect for our sentiment classification task.

```python
import tensorflow as tf
from tensorflow.keras.datasets import imdb

# Load the IMDB dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# Padding sequences
train_data = tf.keras.preprocessing.sequence.pad_sequences(train_data, maxlen=500)
test_data = tf.keras.preprocessing.sequence.pad_sequences(test_data, maxlen=500)
```

### **3. Building the Transformer Model**

For simplicity, we'll build a mini Transformer with essential components.

```python
from tensorflow.keras import layers

def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
    # Normalization and Attention
    x = layers.LayerNormalization(epsilon=1e-6)(inputs)
    x = layers.MultiHeadAttention(key_dim=head_size, num_heads=num_heads, dropout=dropout)(x, x)
    x = layers.Dropout(dropout)(x)
    res = x + inputs

    # Feed Forward Part
    x = layers.LayerNormalization(epsilon=1e-6)(res)
    x = layers.Conv1D(filters=ff_dim, kernel_size=1, activation="relu")(x)
    x = layers.Conv1D(filters=inputs.shape[-1], kernel_size=1)(x)
    return x + res

inputs = layers.Input(shape=(500,))
embedding_layer = layers.Embedding(input_dim=10000, output_dim=16)(inputs)
transformer_block = transformer_encoder(embedding_layer, head_size=16, num_heads=2, ff_dim=32)
pooled_output = layers.GlobalAveragePooling1D()(transformer_block)
dropout = layers.Dropout(0.1)(pooled_output)
outputs = layers.Dense(1, activation="sigmoid")(dropout)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

### **4. Compiling and Training the Model**

Let's compile and train our Transformer model.

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, train_labels, epochs=3, batch_size=32, validation_data=(test_data, test_labels))
```

### **5. Evaluating the Model**

After training, evaluate the model's performance on the test dataset.

```python
loss, accuracy = model.evaluate(test_data, test_labels)
print(f"Test accuracy: {accuracy}")
```

With our simple Transformer, you should expect an accuracy of around 85%. Advanced architectures and fine-tuning can further enhance this performance.

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