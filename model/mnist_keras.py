import keras
import numpy as np
import pandas as pd
from pathlib import Path
from PIL import Image
class MNISTKeras():

    def __init__(self,root_dir:Path):
        self.root_dir = root_dir
        self.type = 'cv' # allowed types = "cv" or "tabular"
        self.model_name = 'Iris Classification MNIST'
        self.short_description = "MNIST Digit Classification using Keras"
        self.description = """
                This DNN model, built using Keras, is designed to predict the species of Iris flowers based on their sepal and petal measurements. The model is tailored for multi-class classification, distinguishing between three Iris species: Setosa, Versicolor, and Virginica.

                ### Model Architecture
                The DNN consists of an input layer with four features (sepal length, sepal width, petal length, and petal width), one or more hidden layers with ReLU activation functions, and an output layer with a softmax activation function. The output layer provides probability distributions over the three species classes.

                ### Training
                Training is performed using a labeled dataset, where the model learns to classify Iris flowers into their respective species. The loss function used for optimization is typically categorical cross-entropy, and the model's weights are updated through backpropagation.

                ### Evaluation
                To assess the model's performance, metrics like accuracy, precision, recall, and F1-score are computed on a separate test dataset. These metrics help measure the model's ability to accurately predict the Iris species.

                This DNN model serves as a powerful tool for automating the classification of Iris flowers and is applicable in various fields, such as botany and horticulture.
        """
        self.architecture = self.root_dir/ 'media/mnist_keras.png'
        self.cometml_url = "https://www.comet.com/wereign/solar-detection-v2/view/EjM3aobkDhccBouofxikIQtrc/panels"


    def inference(self,image):

        # print(image.shape)

        image = image.astype('float32') / 255.0
        image = image.reshape(-1,28,28,1)

        model = keras.models.load_model(self.root_dir / 'saved_models/mnist.keras')

        predictions = model.predict(image)
        print(predictions)
