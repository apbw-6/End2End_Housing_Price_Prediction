import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv("housing.csv")
data 

#Exploring data
data.info()

#So we have mostly non-null data. Just few null data in total_bedrooms section, so we clear these out.
# We get rid of NAN: Not a number data 
data.dropna(inplace= True) #inplace just replaces the data
data.info()

from sklearn.model_selection import train_test_split

# Now we decide what X, Y is and then portion of split for training data
X = data.drop('median_house_value', axis=1)
y = data['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)