import pandas as pd
import numpy as np
import pickle

data = pd.read_csv("Earthquake_over_sampled ffill Dead.csv")

X = data.drop(['Dead'],axis=1)
y = data['Dead']

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rfc.fit(X,y)

pickle.dump(rfc, open("EdeathModel.sav", "wb"))

