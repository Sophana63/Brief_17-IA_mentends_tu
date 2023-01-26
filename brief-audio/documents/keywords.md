## <span style="color:#4180df">LA FEATURE SPECTRALE</span>

La **feature spectrale** d'un son est un ensemble de caractéristiques qui décrivent sa composition en termes de fréquences et d'amplitudes. Il existe plusieurs types de features spectrales, chacun ayant une utilisation spécifique.
- **Le spectre d'amplitude** est une représentation graphique de l'intensité des fréquences d'un son. Il est généralement représenté par un histogramme ou un diagramme en barres qui montre les différentes fréquences présentes dans le son et leur amplitude respective.
- **La décomposition en ondelettes** est une technique qui permet de décomposer un signal sonore en ses différentes composantes fréquentielles. Les coefficients de décomposition en ondelettes sont souvent utilisés comme features spectrales.
- **Les coefficients de cepstre** sont un autre type de feature spectrale qui est obtenue en calculant la transformée de Fourier du logarithme de l'amplitude du signal. Il est souvent utilisé dans la reconnaissance vocale ou la reconnaissance de parole.
- **Le Mel-Frequency Cepstral Coefficients (MFCC)** est une variante des coefficients de cepstre qui tient compte de la répartition des fréquences audibles par l'oreille humaine. C'est un des feature spectral le plus utilisé pour la reconnaissance vocale et la reconnaissance de parole.
En générale, les features spectrales sont utilisées pour analyser et caractériser les propriétés acoustiques des sons, et ils sont souvent utilisés dans les systèmes de reconnaissance de la parole, la reconnaissance musicale, l'analyse de la parole, etc.

<br>

## <span style="color:#4180df">SKEWNESS</span>

**La skewness (ou asymétrie)** d'une distribution de probabilité est une mesure de la symétrie de cette distribution autour de sa moyenne. **Elle est calculée en prenant la moyenne des cubiques des écarts à la moyenne, divisée par la variance de la distribution**.

Si **la skewness est nulle**, cela signifie que la distribution est symétrique autour de sa moyenne, c'est-à-dire que les valeurs à gauche et à droite de la moyenne sont similaires. Si la skewness est positive, cela signifie que la queue de la distribution est étirée vers la droite de la moyenne, c'est-à-dire qu'il y a plus de valeurs élevées que de valeurs basses. Si **la skewness est négative**, cela signifie que la queue de la distribution est étirée vers la gauche de la moyenne, c'est-à-dire qu'il y a plus de valeurs basses que de valeurs élevées.

Il est important de noter que la skewness est une mesure relativement **sensible aux outliers (valeurs extrêmes)** dans les données et peut donc ne pas être un indicateur fiable **si les données contiennent des outliers importants**.

<br>

## <span style="color:#4180df">KURTOSIS</span>

**La kurtosis (ou aplatissement)** d'une distribution de probabilité **est une mesure de la concentration des valeurs autour de la moyenne de la distribution**. Elle est calculée en prenant la moyenne des quatrièmes des écarts à la moyenne, divisée par la variance de la distribution, et soustrayant 3.

Une distribution normale a une kurtosis égale à 3, ce qui signifie que la plupart des valeurs sont concentrées autour de la moyenne avec une répartition symétrique des valeurs élevées et basses. Une distribution avec une kurtosis supérieure à 3 a une "queue" plus épaisse que celle d'une distribution normale, c'est-à-dire qu'il y a plus de valeurs extrêmes (élevées ou basses) que prévu par rapport à une distribution normale. Une distribution avec une kurtosis inférieure à 3 a une "queue" plus mince que celle d'une distribution normale, c'est-à-dire qu'il y a moins de valeurs extrêmes que prévu par rapport à une distribution normale.

**La kurtosis est un indicateur complémentaire à celui de la skewness** pour caractériser la forme d'une distribution de probabilité, il est souvent utilisé en statistique pour décrire les propriétés d'une population ou d'un échantillon.

<br>

## <span style="color:#4180df">SHANNON</span>

**Le signal de Shannon** est un concept de la théorie de l'information qui **décrit la capacité d'un canal de communication à transmettre de l'information**. Il est défini comme la limite supérieure de la quantité d'information qui peut être transmise par un canal par unité de temps, en utilisant une certaine technique de codage.

Le signal de Shannon est lié à la densité spectrale de puissance du signal, qui mesure la distribution de l'énergie du signal sur les différentes fréquences. **Plus la densité spectrale de puissance est élevée, plus le signal contient d'informations différentes et plus grande est la capacité de transmission de l'information.**

La capacité de Shannon d'un canal est également liée au taux d'erreur toléré par le système de communication. **Plus le taux d'erreur est faible, plus grande est la capacité de Shannon.**

Le concept de signal de Shannon est largement utilisé dans les systèmes de communication pour optimiser la performance et maximiser la capacité de transmission d'information. Il est également utilisé dans la compression de données pour trouver les codes les plus efficaces pour représenter les données.

<br>

## <span style="color:#4180df">RENYI</span>

**Le signal de Renyi** est un concept de la théorie de l'information qui **dévalue la diversité d'un signal ou d'une série de données en utilisant une mesure de similarité** basée sur la théorie de Renyi. La mesure de Renyi est basée sur la notion de la "diversité relative", qui est une mesure de la similitude entre les différents éléments d'un ensemble.

La mesure de Renyi est définie comme étant la **somme pondérée des probabilités des éléments d'un ensemble, où la pondération est donnée par une fonction de similarité définie par un paramètre alpha**. Pour alpha =1, la mesure de Renyi correspond à l'entropie de Shannon, qui est une mesure classique de l'information d'un signal. Pour alpha >1, la mesure de Renyi met l'accent sur les éléments les plus probables du signal, tandis qu'une valeur alpha <1 met l'accent sur les éléments les moins probables.

La mesure de Renyi est utilisée pour évaluer la diversité d'un signal dans différents domaines tels que la reconnaissance de la parole, l'analyse de données, la compression de données, la classification de données, et la segmentation de données. Elle est souvent utilisée pour évaluer la performance des systèmes de classification automatique en comparant les résultats obtenus avec une classification humaine.
