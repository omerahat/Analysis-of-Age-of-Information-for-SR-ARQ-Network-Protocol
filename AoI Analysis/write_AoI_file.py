import pandas as pd
def writeAoIFile(arr,path):

     # Convert the data to a DataFrame
     df_to_save = pd.DataFrame(arr, columns=['AoI'])
     df_to_save.to_csv(path, index=False)
