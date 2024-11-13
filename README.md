# Forest-cover-type

## Description

On s’intéresse ici à prédire la type de couverture végétale de parcelles de 900m^2 situées dans le parc
national Roosevelt, au Colorado. Pour cela, nous avons accès à 100000 données labélisées d’autres parcelles
de même dimension. Les données de test et d'entrainement se trouvent à l'adresse suivante :https://www.kaggle.com/competitions/forest-cover-type-orsay.

Ce repo contient une analyse de données ainsi que trois modèles de prédiction. La démarche employée est expliquée dans le fichier Kaggle_supervise_MONDELICE_BENBALIT_DUGUERNE.pdf, et les étapes clés sont rappelées dans les notebooks.


## Installation

Les packages suivants sont à installer
```{C}
pip install scikit-learn
pip install imbalanced-learn
pip install lightgbm
pip install joblib
```

Les données train.csv et test.csv doivent se trouver dans le dossier data. Le notebook FCT_data_analysis présente l'analyse des données et l'ensemble des transformations nécéssaires avant d'appliquer les modèles. A la fin de l'exécution du notebook FCT_data_analysis, deux nouveaux fichiers au format csv seront enregistrés dans le dossier data : train_nettoye et test_nettoye. 
Ensuite, les notebooks FCT_knn, FCT_lightgbm et FCT_rf_smote permettent d'appliquer les trois modèles retenus pour ce problème de classification, et enregistrent chacun, dans le dossier output, une prédiction réalisée à partir des données de test. Nous n'avons malheureusement pas retenu le fichier `train_nettoye.csv`, obtenu par le feature engineering.
Après plusieurs phases de validation, cela ne nous a pas permis d'obtenir des meilleurs scores de prédiction sur aucune de nos méthodes.



## Description des fichiers et dossiers

| file/folder | description |
|-----------|-----------|
| data  | dossier contenant les données train et test, puis les données train_nettoye et test_nettoye après la première exécution de FCT_data_analysis |
| output | dossier qui va contenir les predictions pour chacun des trois modèles retenus|
| `FCT_data_analysis.ipynb` | notebook jupyter présentant l'analyse des données et les transformations à appliquer. Ce notebook doit être exécuté avant les trois notebook contenant les modèles |
| `FCT_knn.ipynb` | notebook jupyter contenant le modèle des k plus proches voisins |
| `FCT_lightgbm.ipynb` | notebook jupyter contenant le modèle LightGBM |
| `FCT_rf_smote.ipynb` | notebook jupyter contenant le modèle des random forest |
