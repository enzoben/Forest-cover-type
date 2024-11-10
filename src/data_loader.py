import pandas as pd


def load_data(path):
    """
    Fonction pour extraire les données d'un fichier .csv afin de les stockées dans un DataFrame.

    Args:
        path : Chemin vers le fichier .csv
    """
    
    data = pd.read_csv(path, index_col=0)
    
    return encoding_ELU(data)
    
    
def encoding_ELU(dataFrame : pd.DataFrame):
    """
    On trouve le numéro ELU en fonction du Soil_Type et on l'encode dans le dataframe

    Args:
        dataFrame (pd.DataFrame): DataFrame contenant seulement les Soil_Type
    """
    
    soil_type = [f"Soil_Type{i}" for i in range(1,41)]
    
    climatic_zone = []
    geologic_zone = []
    
    # dictionnaire qui associe à chaque Soil_Type les deux premiers chiffres du code ELU correspondant
    number_ELU = {
        'Soil_Type1':"27",
        'Soil_Type2':"27",
        'Soil_Type3':"27",
        'Soil_Type4':"27",
        'Soil_Type5':"27",
        'Soil_Type6':"27",
        'Soil_Type7':"35",
        'Soil_Type8':"35",
        'Soil_Type9':"42",
        'Soil_Type10':"47",
        'Soil_Type11':"47",
        'Soil_Type12':"47",
        'Soil_Type13':"47",
        'Soil_Type14':"51",
        'Soil_Type15':"51",
        'Soil_Type16':"61",
        'Soil_Type17':"61",
        'Soil_Type18':"67",
        'Soil_Type19':"71",
        'Soil_Type20':"71",
        'Soil_Type21':"71",
        'Soil_Type22':"72",
        'Soil_Type23':"72",
        'Soil_Type24':"77",
        'Soil_Type25':"77",
        'Soil_Type26':"77",
        'Soil_Type27':"77",
        'Soil_Type28':"77",
        'Soil_Type29':"77",
        'Soil_Type30':"77",
        'Soil_Type31':"77",
        'Soil_Type32':"77",
        'Soil_Type33':"77",
        'Soil_Type34':"77",
        'Soil_Type35':"87",
        'Soil_Type36':"87",
        'Soil_Type37':"87",
        'Soil_Type38':"87",
        'Soil_Type39':"87",
        'Soil_Type40':"87"
    }
    
    # On regarde le dataframe sur les Soil_Type
    df = dataFrame[soil_type]
    
    for index, individu in df.iterrows():
        # On reagrde individu par individu pour retrouver le code ELU associé à la parcelle
        
        # On prend l'indice de colonne associé au Soil_Type
        ind_soil_type = list(df.columns[df.iloc[index] == 1])
        
        # On prend la valeur du numéro ELU associé à la clé Soil_type correspondante
        elu = number_ELU[ind_soil_type[0]]
        
        # On ajout aux list climatic_zone et geologic_zone la bon numéro du code ELU
        climatic_zone.append(int(elu[0]))
        geologic_zone.append(int(elu[1]))
    
    # On encode les tableaux précedent en one-hot
    climatic_one_hot = pd.get_dummies(climatic_zone, prefix = 'Climatic_Zone')
    geologic_one_hot = pd.get_dummies(geologic_zone, prefix = 'Geologic_Zone')
    
    # liste de 1 à 8 pour connaitre les zones climatiques et géologiques non citées
    ind = [i for i in range(1,9)]
    
    # On retrouve les zones non citées
    no_climat = list(set(ind).difference(list(set(climatic_zone))))
    no_geo = list(set(ind).difference(list(set(geologic_zone))))
    
    # on fixe à 0 les zones non citées 
    if len(no_climat) !=0:
        for i in no_climat:
            dataFrame[f"Climatic_Zone_{i}"] = 0
    
    if len(no_geo) != 0:
        for i in no_geo:
            dataFrame[f"Geologic_Zone_{i}"] = 0
        
    return pd.concat([dataFrame, climatic_one_hot, geologic_one_hot], axis=1)