import numpy as np     # for manipulating 3d images
import pandas as pd    # for reading and writing tables
import h5py           # for reading the image files
# import skimage      # for image processing and visualizations
import sklearn       # for machine learning and statistical models
import os             # help us load files and deal with paths
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# from user.views import upload

#READING THE UPLOAD FILE 
def read_scan(in_filename ):
     print("from read-scan function ", in_filename)
     with h5py.File(in_filename, 'r') as h:
        print("location::",in_filename)
        return  h['image'][:][:, :, :, 0]
        
#PREDECTING  THE RESULT
def predect(c_filename):
        import tensorflow as tf
        import os
        from django.conf import settings
        from tensorflow.keras.models import load_model
        path = settings.MEDIA_ROOT + '//' + 'my_model.h5'
        print(path)
        
        model_load = load_model(filepath=path)
        pred = model_load.predict(np.expand_dims(np.expand_dims(read_scan(c_filename), axis=-1),axis=0))
        # import matplotlib.pyplot as plt
        # plt.hist(pred)
        # plt.show()
        print(pred)
        return pred