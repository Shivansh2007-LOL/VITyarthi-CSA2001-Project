# VITyarthi-CSA2001-Project
# Toxic Comment Detector

This project is a deep learning model that identifies toxic comments in text. You give it a sentence, and it predicts whether it’s an insult, threat, obscene remark, or another harmful category.  

I built this to get practical experience with real NLP pipelines — from text preprocessing, to training, to making predictions.

---

## How it works

1. The input sentence is converted into numbers using a **TextVectorization** layer  
2. Those numbers are passed into a **Bidirectional LSTM** model that captures sequence and context  
3. The model outputs probabilities for different toxicity categories  

---

## Tech Stack

- Python  
- TensorFlow / Keras  
- Pandas  

---

## Project Files

- `Train.py` → trains the model  
- `Predict.py` → loads the trained model and makes predictions  
- `Toxicity_Detector.h5` → the saved model  
- `.gitignore` → keeps the dataset and extra files out of version control  

---

## Dataset

The dataset is about 66 MB, so it’s not included here.  
To run the project yourself:

1. Download the dataset from Kaggle: [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge)  
2. Place it in the project folder  
3. Update the file path in the code if needed  
4. Train the model with `Train.py`  
5. Test predictions with `Predict.py`  

---

## Why I built
I wanted to understand:  
- How text gets converted into numerical form  
- How LSTMs process sequential data  
- How to keep training and prediction consistent  

---

## Future Plans

- Improve accuracy  
- Reduce training time  
- Add a simple interface for predictions  

---

If you try this out and enjoy it — or if you run into issues and need help — feel free to reach out. I’d love to hear how it goes.
