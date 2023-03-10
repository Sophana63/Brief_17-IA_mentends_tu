Voitures ou camions ?
=====================


1. Introduction
---------------

Pour cette partie 2, Valentin nous a quasi maché le travail avec un live coding. Nous avons récupérer son code et modifier quelques lignes.  

Dans un premier temps, nous avons nettoyé un jeu de données. Des sons de voitures et de camions. Nous avons isolé certains sur ces défauts: 

1. bruits très faibles
2. si des personnes discutent
3. bruits d'animaux tel que les oiseaux, chiens, ect...
4. bruits ressemblant pas à une voiture ou camion (comme les bruits moteurs d'avions)

Nous avons rassenbler en tout 14 échantillons de sons de voiture. Idem pour les camions. Soit un total de 28 échantillons.

Maintenant que nous avons nos jeux de données, nous avons juste modifié les variables de son code. 

.. code-block:: bash

    nbr_of_obs = 28

Et voici notre résultat :

.. code-block:: bash

    ------------------------------------
    Jeux de validation:  [0 1 0 1 0 0 1 1 0 0]
    Prédiction :  [1 1 0 1 1 0 1 1 1 0]
    Score : 0.7
    ------------------------------------


.. image:: img/matrix_conf.png
   :width: 629px
   :height: 670px
   :scale: 50 %
   :alt: alternate text
----

2. Source
---------

.. code-block:: python

    # -*- coding: utf-8 -*-
    """
    Example script

    Script to perform some corrections in the brief audio project

    Created on Fri Jan 27 09:08:40 2023

    @author: ValBaron10
    """

    # Import
    import numpy as np
    import scipy.io as sio
    import matplotlib.pyplot as plt
    from features_functions import compute_features

    from sklearn import preprocessing
    from sklearn import svm
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import plot_confusion_matrix

    # Set the paths to the files 
    data_path = "Data/"

    # Names of the classes
    classes_paths = ["cars/", "trucks/"]
    classes_names = ["car", "truck"]
    nbr_of_obs = 28

    # Go to search for the files
    learning_labels = []
    for i in range(nbr_of_obs):
        if i < nbr_of_obs//2:
            name = f"{classes_names[0]}{i}.wav"
            learning_labels.append(classes_names[0])
            class_path = classes_paths[0]
        else:
            name = f"{classes_names[1]}{i - nbr_of_obs//2}.wav"
            learning_labels.append(classes_names[1])
            class_path = classes_paths[1]

        fs, data = sio.wavfile.read(data_path + class_path + name)
        data = data.astype(float)
        data = data/32768

        # Compute the signal in three domains
        sig_sq = data**2
        sig_t = data / np.sqrt(sig_sq.sum())
        sig_f = np.absolute(np.fft.fft(sig_t))
        sig_c = np.absolute(np.fft.fft(sig_f))

        # Compute the features and store them
        features_list = []
        N_feat, features_list = compute_features(sig_t, sig_f[:sig_t.shape[0]//2], sig_c[:sig_t.shape[0]//2], fs)
        features_vector = np.array(features_list)[np.newaxis,:]

        if i == 0:
            learning_features = features_vector
        else:
            learning_features = np.vstack((learning_features, features_vector))

    # Separate data in train and test
    X_train, X_test, y_train, y_test = train_test_split(learning_features, learning_labels, test_size=0.33, random_state=42)

    # Standardize the labels
    labelEncoder = preprocessing.LabelEncoder().fit(y_train)
    learningLabelsStd = labelEncoder.transform(y_train)
    testLabelsStd = labelEncoder.transform(y_test)

    # Learn the model
    model = svm.SVC(C=10, kernel='linear', class_weight=None, probability=False)
    scaler = preprocessing.StandardScaler(with_mean=True).fit(X_train)
    learningFeatures_scaled = scaler.transform(X_train)
    #learningLabels_scaled = scaler.transform(y_test)

    model.fit(learningFeatures_scaled, learningLabelsStd)

    # Test the model
    testFeatures_scaled = scaler.transform(X_test)

    print("------------------------------------")
    print("Jeux de validation: ", testLabelsStd)
    print("Prédiction : ", model.predict(testFeatures_scaled))
    print("Score :" , model.score(testFeatures_scaled, testLabelsStd))
    print("------------------------------------")

    # Matrix confusion
    plot_confusion_matrix(model, testFeatures_scaled, testLabelsStd) 
    plt.show()