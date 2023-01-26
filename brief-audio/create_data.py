# Import des packages nécessaires
import random
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import pickle

def create_sinus(nb, max_f0):
    duree = 2 # Durée en secondes
    fe = 44100 # Fréquence d'échatillonnage en Hertz, 44100 est très courant en audio
    amp = 0.1 # Amplitude en Pascal

    for i in range (nb):
        f0 = random.randint(1, max_f0) # Fréquence du sinus
        t = np.arange(0, duree, 1/fe) # Création du vecteur temporel (1 point pour chaque échantillon)
        sinus = amp*np.sin(2*np.pi*f0*t)

        # On peut éventuellement le sauvegarder sur disque
        fichier_sinus = open('Data/sinus' + str(i), 'wb')
        pickle.dump(sinus, fichier_sinus)
        fichier_sinus.close()

#create_sinus(8, 15000)

def create_bb(nb):
    duree = 2 # Durée en secondes
    fe = 44100 # Fréquence d'échatillonnage en Hertz, 44100 est très courant en audio
    amp = 0.1 # Amplitude en Pascal    

    for i in range(nb):
        bb = amp*np.random.randn(duree*fe)
        # Export sur disque
        fichier_bb = open('bb' + str(i), 'wb')
        pickle.dump(bb, fichier_bb)
        fichier_bb.close()

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
            label.append(rdm)
        else:
            sample = amp*np.random.randn(duree*fe)
            fichier_sample = open('Data/sample' + str(i), 'wb')
            pickle.dump(sample, fichier_sample)
            fichier_sample.close()
            bb += 1
            label.append(rdm)
    print("nb sinus: " + str(sinus), "| nb_ bb : " + str(bb))
    return label

print(create_sample(20, 18000))

