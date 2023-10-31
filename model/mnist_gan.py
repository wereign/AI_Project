import torch
import cv2
from torchvision import utils as vutils
import numpy as np

gpu = True
CUDA = True and torch.cuda.is_available()
BATCH_SIZE = 128
device = device = torch.device("cuda:0" if CUDA else "cpu")
Z_DIM = 100
generator = torch.jit.load('./saved_models/generator.pt')
viz_noise = torch.randn(BATCH_SIZE, Z_DIM, 1, 1, device=device)
more_fake = generator(viz_noise).detach().cpu()

img = vutils.make_grid(more_fake,normalize=True).cpu().permute(1,2,0).numpy() * 255
img = img.astype(np.uint8)
print(np.max(img))
cv2.imwrite('./gan_output.png',img)
cv2.imshow('generator',img)
cv2.waitKey(0)

