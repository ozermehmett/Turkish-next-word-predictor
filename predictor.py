import gradio as gr
import numpy as np
import pickle
import keras

# Load model
model_path = 'model_and_tokenizer/model.h5'
tokenizer_path = 'model_and_tokenizer/tokenizer.pkl'

model = keras.models.load_model(model_path)

# Load tokenizer
with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict_next_words(model_, tokenizer_, text):
    sequence = tokenizer_.texts_to_sequences([text])
    sequence = np.array(sequence)
    predictions = np.argmax(model_.predict(sequence), axis=-1)
    predicted_word = ""

    for key, value in tokenizer_.word_index.items():
        if value == predictions:
            predicted_word = key
            break

    return predicted_word


def word_processing(text):
    text = text.lower()
    text = text.split(" ")
    text = text[-5:]
    return text


def predict(text):
    processed_text = " ".join(word_processing(text))
    predicted_word = predict_next_words(model, tokenizer, processed_text)
    return predicted_word


interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
    outputs="text",
    title="Next Word Prediction",
    description="Enter a sequence of words and get the predicted next word."
)

interface.launch()
