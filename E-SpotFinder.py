import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import pickle
import sys


fname = sys.argv[1]
print("Start run E-SpotFinder\n")
dat=pd.read_table(fname)
X= dat.iloc[:,1:407]
model = pickle.load(open("E-SpotFinder.dat", "rb"))
Y_pred=model.predict(X)
dat['predict_class']=Y_pred
output_key = 'E-SpotFinder_output.txt.gz'
key_info = dat.loc[:, ['hotspot','predict_class']]
key_info.to_csv(output_key,sep="\t",compression='gzip',index=None)
print("Finish\n")