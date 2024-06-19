import pandas as pd

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #creando un dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna","id","ica","fecha"])
    dataFrameICA.to_csv("datosica.csv",index=False)
    print(dataFrameICA)

construirDataICA()