from  PIL import Image
import matplotlib.pyplot as plt
import numpy as np

pattern = Image.open('./pattern_h.tif')

mask_a = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
mask_b = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 1]])
mask_d = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
mask_c = mask_d * -1
