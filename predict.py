import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

df = pd.read_csv("C:\\aiml project vityarthi sem2\\Toxicity Detector\\train.csv")

X = df['comment_text']
y = df[df.columns[2:]].values

MAX_FEATURES = 30000

vectorizer = TextVectorization(
    max_tokens=MAX_FEATURES,
    output_sequence_length=400,
    output_mode='int'
)

vectorizer.adapt(X.values)
vectorized_text = vectorizer(X.values)

model = tf.keras.models.load_model('Toxicity_Detector.h5')

for i in range(10):
    comment=input("Text: ")
    input_text = vectorizer([comment])
    res = model.predict(input_text)

    labels = df.columns[2:]
    
    print("result")
    for i, label in enumerate(labels):
        print(f"{label}: {res[0][i]:.4f}")