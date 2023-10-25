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
        ### MNIST Dataset with Keras

        The MNIST dataset, when utilized with the Keras deep learning framework, serves as a fundamental benchmark for image classification tasks. It consists of a collection of 28x28 pixel grayscale images, each depicting handwritten digits ranging from 0 to 9. This dataset is widely recognized and used as an introductory step into the field of deep learning and computer vision.

        ### Model Architecture

        Keras, a high-level neural networks API, provides a user-friendly platform for constructing neural network models for image classification. A typical MNIST model in Keras often starts with convolutional layers that learn features from the images, followed by pooling layers for dimensionality reduction. These are then connected to fully connected layers for making predictions. Keras simplifies model creation by allowing users to easily stack layers with just a few lines of code.

        ### Training

        Training a Keras model on the MNIST dataset involves feeding the network the training data and iteratively adjusting the model's internal parameters through backpropagation to minimize a chosen loss function (commonly cross-entropy). Stochastic gradient descent (SGD) and other optimization techniques are often employed for this purpose. The dataset is typically split into training and validation sets to monitor model performance, preventing overfitting.

        ### Evaluation

        Keras provides various evaluation metrics to assess the model's performance, with accuracy being one of the most commonly used. Confusion matrices and classification reports are often generated to gain deeper insights into the model's classification abilities. The ultimate objective is to achieve high accuracy on the MNIST test dataset, demonstrating the model's proficiency in correctly classifying handwritten digits.

        ### Use Cases

        The MNIST dataset with Keras is an essential stepping stone for deep learning practitioners and researchers. It's used in various applications, including digit recognition in diverse forms and documents, automated sorting of mail, and as a building block in more advanced optical character recognition (OCR) systems. The simplicity and efficiency of Keras make it an ideal choice for exploring image classification tasks, making it accessible for both beginners and experienced machine learning practitioners.  """

        self.architecture = self.root_dir/ 'media/mnist_keras.png'
        self.cometml_url = "https://www.comet.com/wereign/solar-detection-v2/view/EjM3aobkDhccBouofxikIQtrc/panels"
        self.model = keras.models.load_model(self.root_dir / 'saved_models/mnist.keras')


    def inference(self,image,source):

        # print(image.shape)

        image = image.astype('float32') / 255.0
        image = image.reshape(-1,28,28,1)


        predictions = self.model.predict(image)
        class_label = np.argmax(predictions)

        print()
        print(source)
        print(predictions)
        print(predictions.shape)
        print(class_label)
        print()

        return class_label
