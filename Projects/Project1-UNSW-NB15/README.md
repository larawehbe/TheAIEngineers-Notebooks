# **Network Intrusion Detection using UNSW-NB15 Dataset**

## **Project Overview**
This project is divided into **two stages**. In the first stage, you will apply **supervised learning** to classify network traffic data into normal and malicious categories using labeled data. In the second stage, you'll explore the data using **unsupervised learning** techniques to detect anomalies and group traffic without using labels.

The goal is to give you hands-on experience with both approaches and allow you to compare the results of clustering (unsupervised) and classification (supervised).

---

### **Stage 1: Supervised Learning (Classification)**

#### **Objective**:
- Use supervised learning techniques (like **Random Forest**, **Decision Trees**, or **Neural Networks**) to classify network traffic as either normal or malicious.
- You’ll train the model using the labeled data provided in the UNSW-NB15 dataset and evaluate its performance.

#### **Instructions**:
1. **Data Preprocessing**:
   - Handle missing values and remove irrelevant or noisy data.
   - Scale and normalize the numerical features.
   - Encode categorical features (such as protocol types) using one-hot encoding.

2. **Model Training**:
   - Select and implement a supervised learning algorithm (e.g., **Random Forest**, **Decision Trees**, or a **Neural Network**).
   - Train the model using the labeled data.
   - Split the dataset into training and testing sets (e.g., 80% training, 20% testing) to evaluate the model.

3. **Model Evaluation**:
   - Evaluate the model’s performance using **accuracy**, **precision**, **recall**, and **F1-score**.
   - Generate a **confusion matrix** to better understand how well the model distinguishes between normal and malicious traffic.

#### **Deliverables**:
- A Jupyter Notebook showing preprocessing steps, model training, and performance evaluation.
- Visualizations like the confusion matrix and performance metrics.

---

### **Stage 2: Unsupervised Learning (Clustering)**

#### **Objective**:
- Use unsupervised learning techniques (like **K-means** or **DBSCAN**) to explore and cluster the network traffic data without using the labels.
- The goal is to detect anomalies and group the traffic based on patterns that emerge from the data itself.

#### **Instructions**:
1. **Data Preprocessing**:
   - Use the same preprocessing steps as in Stage 1 to ensure consistency.
   - Remove the labels from the dataset, as they won’t be used in this stage.

2. **Clustering**:
   - Apply a clustering algorithm like **K-means** or **DBSCAN** to group the network traffic data into clusters.
   - Experiment with different numbers of clusters for K-means or tuning the `eps` and `min_samples` parameters for DBSCAN.

3. **Dimensionality Reduction**:
   - Use **PCA** or **t-SNE** to reduce dimensionality and visualize the clusters in 2D or 3D space.

4. **Cluster Evaluation**:
   - After clustering, use the labels to evaluate how well the clusters represent normal vs. malicious traffic.
   - Compare the clusters with the supervised learning results from Stage 1.

#### **Deliverables**:
- A Jupyter Notebook showing unsupervised clustering, dimensionality reduction, and cluster evaluation.
- Visualizations of clusters and comparison with the results from Stage 1.

---

### **Final Deliverables**:
- Two Jupyter Notebooks (one for supervised and one for unsupervised learning) showing data preprocessing, model implementation, and evaluation.
- A short report comparing the results of the supervised classification vs. the unsupervised clustering, discussing strengths and limitations of each approach.

---

### **Acceptance Criteria**:

- **Stage 1 (Supervised)**:
  - Data is correctly preprocessed, a supervised model is trained, and performance metrics (accuracy, precision, recall, F1-score) are calculated.
  - The confusion matrix is visualized, and the results are explained clearly.

- **Stage 2 (Unsupervised)**:
  - Data is preprocessed, clustering is applied, and clusters are visualized.
  - Clusters are evaluated using labels, and comparisons are made with the supervised learning results.

---

### **Hints**:

- **Supervised Stage**:
  - Start simple with models like Decision Trees or Random Forest before moving to more complex models like Neural Networks.
  - Use cross-validation to fine-tune your model and avoid overfitting.

- **Unsupervised Stage**:
  - Experiment with different numbers of clusters for K-means.
  - For DBSCAN, the choice of `eps` (distance threshold) is critical to finding meaningful clusters. Start with small values and adjust based on data density.
  - Visualizing your clusters with PCA or t-SNE will help you see if normal and malicious traffic naturally group together.

