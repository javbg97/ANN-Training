#Developed by Bernabe Garcia Javier and Maldonado Lozano Juan Carlos
#Fall 2021

import pandas as pd
import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
#Lectura del dataset de entrenamiento y de prueba
dataTest = pd.read_csv("P5.csv")
dataTrain = pd.read_csv("P5_Training.csv")
#Division del dataset en X y Y
X_train = dataTrain.iloc[:,:-1].values
y_train = dataTrain.iloc[:,-1].values
X_test = dataTest.iloc[:,:-1].values
y_test = dataTest.iloc[:,-1].values
#Escalado de datos
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#Se establece una lista con las neuronas y sus respectivas capas que obtuvieron los mejores resultados
numeroCapas =[[5,5],[6,6],[14,14],[15],[16,16],[17],[23,23],[24,24],[25,25],[26,26],[27,27]]
#Con su respectivo numero de epocas
iteraciones=[850,1050,950,1150,950,950,950,750,1050,1150,1050]
learningRate=[0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20]
#Se entrena a la RNA con dichas neuronas iterando sobre un rango de learning rate
for capa,ite in zip(numeroCapas,iteraciones):
    print(capa,ite)
    for lt in learningRate:
        clf = MLPClassifier(random_state=1, max_iter=ite, activation="logistic", hidden_layer_sizes=capa,learning_rate="constant",learning_rate_init=lt,momentum=0.15,solver="sgd",n_iter_no_change=1150)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=ConvergenceWarning,module="sklearn")
            clf.fit(X_train,y_train)
            print(lt,clf.score(X_test,y_test))
