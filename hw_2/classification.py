from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

means = {
        "r": [],
        "g": [],
        "b": []
        }

results = []

teach_base_dir = "./MISC/teach/"
test_base_dir = "./MISC/test/"

teach_directory = os.listdir(teach_base_dir)
test_directory = os.listdir(test_base_dir)

for file in teach_directory:
    im_arr = np.array(Image.open(teach_base_dir + file))
    means['r'].append(im_arr[:,:,0].mean())
    means['g'].append(im_arr[:,:,1].mean())
    means['b'].append(im_arr[:,:,2].mean())
    results.append(1 if file.startswith('12_') else 0)


plt.figure()
plt.scatter(means["b"], means["r"], c=results)
plt.xlabel('green')
plt.ylabel('blue')

plt.show()

from sklearn import neighbors

knn = neighbors.KNeighborsClassifier(n_neighbors = 1)

param = np.transpose(np.array([means['r'], means['g'], means['b']]))
knn.fit(param, results)

for file in test_directory:
    im_arr = np.array(Image.open(test_base_dir + file))
    r = im_arr[:,:,0].mean()
    g = im_arr[:,:,1].mean()
    b = im_arr[:,:,2].mean()
    prediction = knn.predict(np.array([[r,g,b]]))
    print(file, "is" if prediction else "is not", "a match")
