# VITyarthi-CSA2001-Project
# Toxic Comment Detector

This project is a deep learning model that identifies toxic comments in text. You give it a sentence, and it predicts whether it’s an insult, threat, obscene remark, or another harmful category.  

I built this to get practical experience with real NLP pipelines — from text preprocessing to training and simultaneously to making predictions.

---

## How it works

1. The input sentence is converted into numbers using a **TextVectorization** layer  
2. Those numbers are passed in a **Bidirectional LSTM** model that captures sequence and context  
3. The model ultimately outputs probabilities for various amount of different toxicity categories  

---

## Tech Stack / Modules and Library

- Python  
- TensorFlow / Keras  
- Pandas  

---

## Project Files used 

- `Train.py` → trains the model  
- `Predict.py` → loads the trained model and makes predictions  
- `Toxicity_Detector.h5` → the saved model  

---

## Dataset

The dataset is about 40+ MB, so i have not included it here.  
To run the project yourself:

1. Download the dataset from Kaggle: [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge)  
2. Place it inside the project folder  
3. Update the file path in the code if needed as it may pose problems afterwards  
4. Train the model with `Train.py`  
5. Test predictions with `Predict.py`  

---

## My aim behind building this project
I wanted to understand:  
- How text gets converted into numerical form  
- How LSTMs process sequential data  
- How to keep training and prediction consistent  

---

## Future Plans

- Improving accuracy  
- Reducing training time  
- Adding a simple interface for predictions  

---

If you try this out and enjoy it — or if you run into issues and need help — or if you have more to suggest — feel free to reach out.
I’d definitely love to hear how it goes.
