import pandas as pd

songDataset = pd.read_csv("https://raw.githubusercontent.com/oscar-jiang/playlist-creator/refs/heads/main/backend/dataset/tcc_ceds_music.csv") #reads data from url

pd.set_option("display.max_colwidth", 15) #configures the output dataframe in terminal


songDataset.dropna(inplace = True) #drops NA values
songDataset.drop_duplicates(inplace = True) #drops duplicate observations
songDataset.drop(songDataset.columns[0], axis = 1, inplace = True) #drops the first column

print(songDataset.tail(3)) #prints the last 3 observations of the dataframe


