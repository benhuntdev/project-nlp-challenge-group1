**IronHack AI Engineering Bootcamp – January 2026**  

# Project NLP Challange (Group 1)
NLP Project by Ben, Armando, Quincy and Bianca

[Project in GitHub](https://github.com/benhuntdev/project-nlp-challenge-group1)

---

## Project Goal

The goal of the project is to build and test **Natural Language Processing (NLP)** models that correctly classify articles into two predefined categories: **real** (labeled as '1' in the file) or **fake** articles (labeled as '0' in the file).

---

## Project Overview

- **NLP Model Creation**
  - For data preprocessing, different techniques were implemented: stemming, lemmatization, tokenization, removal of stop words, lower case the text.
  - Different models of representing the texts were used: bag of words (BOW), Term Frequency – Inverse Document Frequency (TF-IDF).
  - Different classifiers were tested: Logistic Regression, Random Forest, Naive Bayes, SVM, Neural Networks.
  - Embeddings were as well tested (from OpenAI).

- **The dataset:**
  - It contains articles that are categorized or as real or as fake article. 
  - This dataset is used for training and validating the model. 
  - It is a balanced dataset.

- **Evaluation**
  - Perfomance metrics, like accuracy, were verified for each model.

- **Reporting**
  - Presentation to exhibit results, methodology, and findings.

---

## Project Results

- **Model metrics**

- **Historic overview**

- **Saved Models**
  - The trained models are stored for future usage.

---

## Project Content

### Description of Content Structure

- **code/**
  - `main`: notebook with the basic NLP used as the starting point for all other models
  - `modelXX`: notebooks containing the rest of the models. An overview of their metrics can be found in the `spreadsheet` folder

- **data/**
  - The folder were the datasets (training & testing) are stored.

- **data_output/**
  - The folder that stores the files containing the predictions done using the trained models.

- **models/**
  - The place were the already trained models are stored.

- **spreadsheet/**
  - `nlp project spreadsheet - g1.xlsx`: spreadsheet used to store model metrics and track progress.

- **presentation/**
  - `presentation n2.pptx`: presentation to exhibit results, methodology, and findings.

- **requirements/**
  - The `requirements.txt` file can be used to install the environment needed to run the notebooks  
  - It is recommended to use a **virtual environment**

---

## Environment Setup

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
