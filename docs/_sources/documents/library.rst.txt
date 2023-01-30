Librairies les plus utilisées
=============================

Numpy
-----

NumPy est une bibliothèque pour langage de programmation Python, destinée à manipuler des matrices ou tableaux multidimensionnels ainsi que des fonctions mathématiques opérant sur ces tableaux.

.. code-block:: bash

    $ pip install numpy

----

Pickle
------

Le module pickle permet de sauvegarder dans un fichier, au format binaire,  n'importe quel objet Python.

.. code-block:: bash

    $ pip install pickel


----

sk-learn
--------

Scikit-learn est une bibliothèque libre Python destinée à l'apprentissage automatique. Elle est développée par de nombreux contributeurs notamment dans le monde académique par des instituts français d'enseignement supérieur et de recherche comme Inria.

.. code-block:: bash

    $ pip install -U scikit-learn


Sphinx 
------

Sphinx est un générateur de documentation libre. Il a été développé par Georg Brandl pour la communauté Python en 2008, et est le générateur de la documentation officielle de projets tels que Python, Django, Selenium, Urwid, ou encore Bazaar.

    .. code-block:: bash

        $ pip install -U sphinx

        # quelques commandes utiles
        $ sphinx-quickstart  # création rapide des fichiers Sphinx
        # permet de visualiser les fichiers de code 
        $ sphinx-apidoc -o dossier_sortant dossier_entrant_des_sources   
        $ make html  # créer les fichiers HTML
        $ make clean  # supprime le dossier _build/html

