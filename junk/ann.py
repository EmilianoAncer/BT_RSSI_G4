# tensorflow ann

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # turn off errors log

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

directory_path = '../Processed/'

for filename in os.listdir(directory_path):
    f = open(directory_path + filename, 'r')
    txt = f.read()
    print(txt)


# f = open('../Processed/x0y25.txt', 'r')
# lines = f.read()
# f.close()
# print(lines)



