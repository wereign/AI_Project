import keras
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import streamlit as st



class IrisKeras():

    def __init__(self,root_dir:Path):
        self.root_dir = root_dir
        self.type = 'tabular' # allowed types = "cv" or "tabular"
        self.model_name = 'Iris Classification Keras'
        self.short_description = "Iris Species Classification using Keras"
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
        self.architecture = self.root_dir/ 'media/iris_keras.png'
        self.cometml_url = "https://www.comet.com/wereign/solar-detection-v2/view/EjM3aobkDhccBouofxikIQtrc/panels"


    def inference(self,sep_len,sep_wid,pet_len,pet_wid):

        # Load the Keras model and scaler
        self.model = keras.models.load_model(self.root_dir / 'saved_models/iris_model_from_colab.keras')
        
        # st.write(sep_len,sep_wid,pet_len,pet_wid)
        # st.write(self.model)
        
        scaler = joblib.load(self.root_dir / "saved_models/iris_keras_scaler.pkl")

        species = ["Iris-setosa","Iris-versicolor","Iris-virginica"]

        column_names = [
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm"
        ]
        df = pd.DataFrame([[sep_len,sep_wid,pet_len,pet_wid]],columns=column_names)
        x_test = scaler.transform(df)
        preds = self.model.predict(x_test)
        species_idx = np.argmax(preds,axis=-1).item()
        species_label = species[species_idx]
        print(species_label)
        return species_label


flowers = [[5.1,3.5,1.4,0.2],
                   [7.0,3.2,4.7,1.4],
                   [5.9,3.0,5.1,1.8]]

