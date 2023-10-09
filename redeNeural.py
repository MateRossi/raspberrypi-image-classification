from sklearn.neural_network import MLPClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd

def treinar(df):
    dfNew = df.values
    
    #dados
    X = dfNew[0:,0:7]
    Y = dfNew[0:,7]

    print(X.shape)
    print(Y.shape)

    X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y, test_size = 0.3, random_state=0)
    
    #print("Dados")
    #print(X_train.shape)
    #print(X_test.shape)

    #print("Classe")
    #print(Y_train.shape)
    #print(Y_test.shape)

    #print("Vetores de Classes")
    #print(Y_test)
    #print(Y_train)

    model = MLPClassifier(random_state=0, max_iter=1000, activation='relu', hidden_layer_sizes=(10), solver='lbfgs')
    #print(X_train)
    #print(Y_train)
    #print(model)
    model.fit(X_train, Y_train)
    predict = model.predict(X_test)
    mc = confusion_matrix(Y_test, predict)

    mcS = pd.DataFrame(mc)
    print(mcS)

    score = accuracy_score(Y_test, predict)
    print(score)

    return model