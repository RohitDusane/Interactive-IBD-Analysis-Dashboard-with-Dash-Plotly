# IBD Clinical Data Analysis and Visualization Project

## 1. Introduction

### 1.1 Project Overview
The purpose of this project is to analyze clinical data related to **Inflammatory Bowel Disease (IBD)**. The goal is to explore relationships between **demographics**, **disease phenotype**, **treatment types**, and **outcomes** through statistical analysis, machine learning models, and visualizations.

The project involves:
- Collecting and preprocessing IBD clinical data.
- Performing **Exploratory Data Analysis (EDA)** to understand the data.
- Applying statistical tests (T-tests, ANOVA) and logistic regression for analysis.
- Creating interactive visualizations to analyze the results.
- Building a **web-based dashboard** for users to interact with the data.

---

## 2. Data Collection

### 2.1 Data Sources
The dataset used in this project includes clinical trial data related to **IBD**, and the data is assumed to come from a simulated or real clinical data source. Some common datasets that can be used are:
- Clinical trials related to IBD (e.g., **clinicaltrials.gov**).
- Open datasets like **IBD Registry** or datasets available through academic institutions.
- **Simulated IBD datasets** that mimic clinical trial results.

### 2.2 Dataset Features
The dataset contains the following key features:
- **Demographic Information**: Age, gender, ethnicity.
- **Disease Phenotype**: Disease severity, location, complications.
- **Treatment Information**: Type of treatment (medication, surgery), treatment response.
- **Clinical Outcomes**: Success or failure of the treatment, other clinical measures.

---

## 3. Data Preprocessing

### 3.1 Cleaning the Data
The preprocessing steps included:
- **Handling Missing Values**: Filling missing numerical values with the median and dropping rows with too many missing values.
- **Feature Engineering**: Adding new features like **age groups** and **disease severity classification**.
- **Data Transformation**: Converting categorical features into numerical (e.g., encoding **gender** as 0 or 1).

### 3.2 Data Transformation
We used one-hot encoding to transform categorical variables like **treatment type** and **age group** for logistic regression modeling.

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Visualizing Demographics
- **Age Distribution**: A histogram was used to visualize the distribution of patients’ ages.
- **Gender Distribution**: Bar charts were used to visualize the gender distribution across different age groups.
  
### 4.2 Disease Phenotype
- A **boxplot** was used to show the relationship between **age groups** and **disease severity**.
  
### 4.3 Correlation Analysis
- A **heatmap** was created to visualize correlations between various numerical features such as age, disease severity, and treatment success.

---

## 5. Statistical Analysis

### 5.1 Bivariate Comparison (ANOVA)
We performed an **ANOVA test** to compare disease severity across different **age groups**. The results showed significant differences in disease severity between groups, helping identify which demographic factors influence the disease.

### 5.2 Logistic Regression
We applied **logistic regression** to predict the likelihood of **severe disease** based on variables like **age**, **gender**, and **treatment type**. 
- The model's accuracy, precision, recall, and confusion matrix were used to evaluate its performance.

---

## 6. Data Visualization

### 6.1 Visualization Using Plotly
- An **interactive boxplot** was created to visualize disease severity across different age groups.
- The graph allows users to filter data based on different age groups, providing a clear visualization of how disease severity varies across different demographics.

### 6.2 Dash Dashboard
A **Dash-based web app** was developed to allow users to interact with the data. Key features include:
- **Age Group Selector**: A dropdown for selecting an age group to explore disease severity.
- **Interactive Graphs**: A dynamic boxplot that updates based on user selection.

---

## 7. Machine Learning Model

We built a logistic regression model to predict whether a patient’s disease is severe based on certain features:
- **Features Used**: Age, gender, treatment type.
- **Evaluation Metrics**: Accuracy, precision, recall, and confusion matrix were used to evaluate the model's performance.

---

## 8. Web Application

### 8 Dash Setup
We used **Dash**, a Python web framework for building interactive web applications. The app allows users to:
- Select age groups to filter data.
- View interactive plots based on selected filters.
- Understand the relationships between demographic factors and disease severity.  

### 8.2 Dash App in Python
- Run the script with python app.py.  
- Visit http://127.0.0.1:8050/ in your browser to interact with the dashboard.


---

## 9. Conclusion and Future Work

### 9.1 Conclusion
This project provides valuable insights into the demographics and clinical outcomes of IBD patients. It also demonstrates how to use Python for data preprocessing, statistical analysis, and visualization in the healthcare research domain.

### 9.2 Future Work
- **Expand Data**: Include more diverse data sources and larger datasets for deeper insights.
- **Add More Models**: Integrate machine learning models like **Random Forests** or **SVM** for predictive analysis.
- **Improve Dashboard**: Enhance the web app with more interactivity and additional insights.
