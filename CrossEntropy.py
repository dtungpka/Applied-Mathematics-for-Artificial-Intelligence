import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pickle
import random
#load the cirfar10 dataset at D:\2021-2022\Research\Dataset\CIFAR-10
def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
#load the data
def load_data():
    data = []
    labels = []
    for i in range(1, 6):
        data_dict = unpickle('D:\\2021-2022\\Research\\Dataset\\CIFAR-10\\data_batch_' + str(i))
        data.append(data_dict[b'data'])
        labels.append(data_dict[b'labels'])
    data = np.concatenate(data)
    labels = np.concatenate(labels)
    return data, labels
def load_label_names():
    label_names_dict = unpickle('D:\\2021-2022\\Research\\Dataset\\CIFAR-10\\batches.meta')
    label_names = label_names_dict[b'label_names']
    return label_names
#load the test data
def load_test_data():
    test_data_dict = unpickle('D:\\2021-2022\\Research\\Dataset\\CIFAR-10\\test_batch')
    test_data = test_data_dict[b'data']
    test_labels = test_data_dict[b'labels']
    return test_data, test_labels


#load the data
data, labels = load_data()
label_names = load_label_names()
test_data, test_labels = load_test_data()


#filter the data
def filter_data(data, labels, class1, class2):
    data = data[(labels == class1) | (labels == class2)]
    labels = labels[(labels == class1) | (labels == class2)]
    return data, labels
data, labels = filter_data(data, labels, 4, 8)

#normalize the data
def normalize_data(data):
    data = data / 255
    return data







t0 = time.time()
X = data
print(X.shape)
w = np.random.randint(1,X.shape[1])
w2 = np.where()
def h(w,x):
    return  w.T @ X
H = h(w,_X)
Y = np.dot(H,w2);
print(Y)
Z = np.exp(Y)/np.sum(np.exp(Y))
print(Z)

