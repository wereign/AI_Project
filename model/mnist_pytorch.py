from PIL import Image
from pathlib import Path

class MNISTPyTorch:
    def __init__(self,root_dir:Path):

        self.root_dir = root_dir

        self.type = 'cv' # allowed types = "cv" or "tabular"
        self.model_name = 'MNIST CNN PyTorch'
        self.short_description = "MNIST Classification using convolution in PyTorch"
        self.description = """
This PyTorch Convolutional Neural Network (CNN) model is designed to classify handwritten digits from the MNIST dataset. MNIST is a popular benchmark dataset containing 28x28 pixel grayscale images of handwritten digits from 0 to 9. The goal of this model is to accurately predict the digit in each image.

### Model Architecture

The CNN architecture consists of multiple convolutional layers followed by max-pooling layers to extract relevant features from the input images. This is followed by fully connected layers to make the final predictions. It leverages convolutional filters and non-linear activation functions to learn hierarchical representations of the input images.

### Training

The model is trained using backpropagation and stochastic gradient descent (SGD) to minimize the cross-entropy loss. The training dataset is split into training and validation sets to monitor the model's performance and prevent overfitting. Data augmentation techniques, such as random rotations and translations, are often used to enhance the model's generalization capabilities.

### Evaluation

The model's performance is evaluated using metrics such as accuracy and confusion matrices. The ultimate goal is to achieve high accuracy on the MNIST test dataset, demonstrating the model's ability to correctly classify handwritten digits.

### Use Cases

This model can be used in a wide range of applications, including automated mail sorting, digit recognition in forms, and even as a component of more complex optical character recognition (OCR) systems. It serves as a foundational example of image classification with deep learning in the context of computer vision tasks.

        """
        self.architecture = self.root_dir / 'media/pytorch_mnist_cnn.png'
        self.cometml_url = "https://www.comet.com/wereign/solar-detection-v2/view/EjM3aobkDhccBouofxikIQtrc/panels"

    def inference(self,image):
        return image.size
 