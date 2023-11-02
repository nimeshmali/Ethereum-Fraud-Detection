import json
import pickle
from flask import  jsonify


with open('X_Address_pickle', 'rb') as f:
    X_Address =pickle.load(f)
 
with open('model_pickle', 'rb') as f:
    clf =pickle.load(f)   
    
data = {0:"0x00009277775ac7d0d59eaad8fee3d10ac6c805e8"}
print(data[0])
temp = X_Address.where(X_Address['Address'] == data[0])
X_info = temp.dropna().iloc[:,0:44]
 # X_info = np.array(X_info).reshape(1,-1) 
print(X_info)
        
prediction = clf.predict(X_info)

print(prediction)