import torch
import numpy as np
import pandas as pd
from pathlib import Path


class IrisPyTorch():

    def __init__(self,root_dir:Path=Path.cwd()):

        self.root_dir = root_dir
        self.type = 'tabular'
        self.model_name = "Iris Classification PyTorch"
        self.short_description = "Iris Species Classification using PyTorch"
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

        self.architecture =  self.root_dir / 'media/iris_model_pytorch.png'
        self.comet_url = "https://www.comet.com/wereign/juan-ai/c58d9fa7e76d4a048d3943b18cc23ca4?experiment-tab=panels&showOutliers=true&smoothing=0&xAxis=step"
        self.model = torch.jit.load(self.root_dir / '../saved_models/iris_model_pytorch.pt')



    def inference(self,sep_len,sep_wid,pet_len,pet_wid):
            
        species = ['Iris-setosa','Iris-virginica','Iris-versicolor']
        input_tensor = torch.Tensor([sep_len,sep_wid,pet_len,pet_wid])
        preds = self.model.forward(input_tensor)
        label = torch.argmax(preds).item()

        return species[label]

if __name__ == "__main__":

    model_obj = IrisPyTorch()
    flowers = [[5.1,3.5,1.4,0.2],
                   [7.0,3.2,4.7,1.4],
                   [5.9,3.0,5.1,1.8]]
    

    for flower in flowers:
        model_obj.inference(*flower)