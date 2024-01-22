# Machine Learning Workflow Repository

This repository contains a series of Jupyter notebooks that demonstrate a complete machine learning workflow, from data cleaning to model training and evaluation. The project utilizes Weights & Biases (WANDB) for experiment tracking and is optimized for Google Colab Pro subscriptions.

## Notebooks Overview

1. **Data Cleaning**: Initial data cleaning steps to prepare the dataset for modeling.
2. **Transformer Data Cleaning**: Data cleaning steps specifically tailored for transformer models.
3. **Data Preprocessing New**: The latest data preprocessing techniques applied to the dataset.
4. **Exploratory Data Analysis (EDA)**: Analysis of the data to find patterns, anomalies, and understand the dataset.
5. **Word Embedding**: Generation and usage of word embeddings for model training.
6. **Logistic Regression**: A simple logistic regression model for baseline performance.
7. **XGBoost**: An XGBoost model for performance comparison.
8. **CNN without emoji**: A Convolutional Neural Network model that excludes emoji data.
9. **LSTM**: A Long Short-Term Memory network model for sequence data.
10. **Bert**: Implementation of BERT transformer model.
11. **Electra**: Implementation of ELECTRA model for performance comparison.
12. **RoBERTa**: Implementation of RoBERTa transformer model.

## Data Files

- `data_heavyclean.csv`: The cleaned dataset used for training machine learning and deep learning models.
- `Data_Cleaned_Transformer.csv`: The cleaned dataset used for training transformer models.

## Using WANDB

Use Weights & Biases for experiment tracking. To use WANDB:

1. Sign up for a free account at [WANDB](https://wandb.ai/).
2. Install the WANDB package in your notebook: `!pip install wandb`.
3. Log in to WANDB with `!wandb login` and follow the instructions to authenticate your account.

## Running Notebooks in Google Colab Pro

These notebooks are designed to be run in Google Colab Pro. If you have a subscription:

1. Open the notebook in GitHub and click on the 'Open in Colab' button.
2. Ensure that you're logged into your Google Colab Pro account.
3. Run the notebooks as usual, taking advantage of the enhanced resources offered by Colab Pro.

