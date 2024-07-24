# Turkish Next Word Predictor

Welcome to the Turkish Next Word Predictor project! This repository contains the code and resources for building and deploying a machine learning model that predicts the next word in a given Turkish sentence.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Turkish Next Word Predictor uses a language model trained on Turkish text data to predict the next word in a given sentence. This tool can be useful for various applications, including text autocompletion, language learning, and more.

## Features

- Predicts the next word in a Turkish sentence.
- Utilizes state-of-the-art language modeling techniques.
- Easy-to-use interface for making predictions using Gradio.

## Installation

To get started with the Turkish Next Word Predictor, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/ozermehmett/Turkish-next-word-predictor.git
   cd Turkish-next-word-predictor
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the Turkish Next Word Predictor, you can run the provided script `predictor.py`. Here is an example:

```sh
python predictor.py
```

This will launch a Gradio interface where you can input a sequence of words and get the predicted next word.

## Model Training

If you want to train the model from scratch, follow these steps:

1. Prepare your dataset. Ensure it is in a suitable format for training.
2. Run the training script:
   ```sh
   jupyter notebook next-word-predictor-turkish.ipynb
   ```

The training process will save the trained model and tokenizer to the `model_and_tokenizer` directory.

## Contributing

We welcome contributions to improve the Turkish Next Word Predictor! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
