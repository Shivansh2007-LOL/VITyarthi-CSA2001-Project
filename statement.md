# Problem Statement

Online platforms have made it easier than ever for people to share their thoughts, but with that freedom comes a downside: toxic and abusive language. Comments and posts can quickly turn harmful, creating an unhealthy environment for users.  

The problem is scale. Manually moderating millions of comments isn’t realistic, and rule‑based filters often miss the nuances of language. A simple keyword check can’t tell the difference between a joke, sarcasm, or a genuinely harmful statement.  

To tackle this, I built a deep learning model that can automatically detect toxic comments. Instead of just looking for keywords, the model learns context — it understands how words fit together in a sentence and uses that to classify different types of toxicity.

---

# Objective

The goals of this project were pretty straightforward:

* Build a multi‑label classification model to detect different types of toxic comments  
* Use a **TextVectorization** layer to turn raw text into numbers the model can understand  
* Implement a **Bidirectional LSTM** to capture context from both directions in a sentence  
* Train the model on a labeled dataset of comments  
* Keep training and prediction consistent by saving and reusing the vocabulary  
* Evaluate the model based on how well it predicts toxicity  

---

# Scope of the Project

This project focuses on English text comments only. It doesn’t handle other data types like images, audio, or video.  

The model is trained on a specific dataset, so its accuracy depends on the quality and diversity of that data. It works well for common patterns of toxicity but may struggle with brand‑new slang or very subtle cases.

---

# Expected Outcomes

By the end of the project, I had:

* A trained deep learning model that can detect toxic comments  
* A multi‑label classification system that predicts different categories of toxicity  
* A consistent pipeline for training and prediction using the same vocabulary  
* A working prediction script that takes user input and returns toxicity scores  
* A clearer understanding of how NLP models process and classify text  

---

This project shows how deep learning can help automate content moderation and why consistency in NLP pipelines is so important.
