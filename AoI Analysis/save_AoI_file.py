import pandas as pd

def saveAoIFile(arr,path= 'AoI.csv'):

     df_to_save = pd.DataFrame(arr, columns=['AoI'])
     df_to_save.to_csv(path, index=False)
