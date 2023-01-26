# -*- coding: utf-8 -*-
"""
Script to learn a model with Scikit-learn.

Created on Mon Oct 24 20:51:47 2022

@author: ValBaron10
"""

import numpy as np
from sklearn import preprocessing
from sklearn import svm
import pickle
from joblib import dump
from sklearn.model_selection import train_test_split
from features_functions import compute_features
import random
from numpy import inf

### création des échantillons (aléatoire)
def create_sample(nb, max_f0):
    duree = 2 # Durée en secondes
    fe = 44100 # Fréquence d'échatillonnage en Hertz, 44100 est très courant en audio
    amp = 0.1 # Amplitude en Pascal  
    sinus = 0
    bb = 0
    label = []
    for i in range (nb):
        rdm = random.randint(0, 1)       
        
        if rdm == 0:
            f0 = random.randint(1, max_f0) 
            t = np.arange(0, duree, 1/fe) 
            sample = amp*np.sin(2*np.pi*f0*t)
            fichier_sample = open('Data/sample' + str(i), 'wb')
            pickle.dump(sample, fichier_sample)
            fichier_sample.close()
            sinus += 1
            rdm_array = np.array(rdm)
            label = np.append(label, rdm_array)            
        else:
            sample = amp*np.random.randn(duree*fe)
            fichier_sample = open('Data/sample' + str(i), 'wb')
            pickle.dump(sample, fichier_sample)
            fichier_sample.close()
            bb += 1
            rdm_array = np.array(rdm)
            label = np.append(label, rdm_array) 
    print("nb sinus: " + str(sinus), "| nb_ bb : " + str(bb))
    print(label)
    return label

labels = create_sample(20, 18000)

# LOOP OVER THE SIGNALS
learningFeatures = []
for i in range (20):
    # Get an input signal
    FILENAME = 'sample' + str(i)
    file = open("Data/{}".format(FILENAME), 'rb')
    #file = open("Data/{}".format(FILENAME), 'rb')
    input_sig = pickle.load(file)
    # Compute the signal in three domains
    sig_sq = input_sig**2
    sig_t = input_sig / np.sqrt(sig_sq.sum())
    sig_f = np.absolute(np.fft.fft(sig_t))
    sig_c = np.absolute(np.fft.fft(sig_f))

    # Compute the features and store them
    features_list = []
    N_feat, features_list = compute_features(sig_t, sig_f[:sig_t.shape[0]//2], sig_c[:sig_t.shape[0]//2])
    features_vector = np.array(features_list)[np.newaxis,:]    
    features_vector[features_vector == -inf] = 0
    features_vector[features_vector == inf] = 0
    features_vector = np.nan_to_num(features_vector, nan=0)
    features_vector = features_vector.reshape(-1)
    learningFeatures.append(features_vector)
    
    learningLabels = labels

X_train, X_test, y_train, y_test = train_test_split(learningFeatures, learningLabels, test_size=0.3, random_state=0)

# Encode the class names

labelEncoder = preprocessing.LabelEncoder().fit(y_test)
learningLabelsStd = labelEncoder.transform(y_test)

# Learn the model
model = svm.SVC(C=10, kernel='linear', class_weight=None, probability=False)

scaler = preprocessing.StandardScaler(with_mean=True).fit(X_test)
learningFeatures_scaled = scaler.transform(X_test)

model.fit(learningFeatures_scaled, learningLabelsStd)

print("------------------------------------")
print("Jeux de validation: ", y_test)
print("Prédiction : ", model.predict(X_test))
print("Score :" , model.score(X_test, y_test))
print("------------------------------------")

# Export the scaler and model on disk
dump(scaler, "SCALER")
dump(model, "SVM_MODEL")

