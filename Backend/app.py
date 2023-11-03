from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from joblib import load
from web3 import Web3
import requests
import sys
import myKey as k
# from ethereum_address import is_address
# Initializing flask app
app = Flask(__name__)
CORS(app) 

api_key = k.my_eth_key
url = "https://api.etherscan.io/api"
tempAdd = "0x4e83362442b8d1bec281594cea3050c8eb01311c"
transFromAccount = 0

ercMin=0
ercMax=0
ercAvg=0

def getErc(addr,ercMin,ercMax,ercAvg):

        valuesErc = f'{url}?module=account&action=tokentx&address={addr}&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey={api_key}'
        print(valuesErc)
        print("addr",(addr))
        response=requests.get(valuesErc)
        if response.status_code==200:
                print("ho gyis")
                print(type(response.json()))
                dict = response.json()
                print("length of result ",len(dict["result"]))
                print("type of result ",type(dict["result"]))
                c=0
                for i in range(len(dict["result"])):
                        c=c+1
                        if dict["result"][i]["from"]==addr:
                                # print(int(dict["result"][i]["value"]))
                                if int(dict["result"][i]["value"]) < ercMin:
                                        ercMin=int(dict["result"][i]["value"])
                                
                                if int(dict["result"][i]["value"]) > ercMax:
                                        ercMax=int(dict["result"][i]["value"])
                                
                                ercAvg=ercAvg+int(dict["result"][i]["value"])
                                

                                
                ercAvg=ercAvg/c

                print(ercMin)
                print(ercMax)
                print(ercAvg)
                                

        else:
                print("gg krdis")
        



# def transDetails(addr):
#         w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/1bfa363ce82540c99d1097ed2db155e3'))
#         if w3.is_connected():
#                 transFromAccount=w3.eth.get_transaction_count(addr)
#                 print(transFromAccount)
#                 print("connected")


def isValidAddress(add):
  if(Web3.is_address(add)):
    return True

  else:
    return False




clf = load('D:\eth_fraud_detect\Ethereum-Fraud-Detection\Backend\Ethereum_Fraud_Detection.joblib')
X_Address = load('D:\eth_fraud_detect\Ethereum-Fraud-Detection\Backend\X_Address.joblib')
# file = open('model_pickle', 'rb')
# clf = pickle.load(file)



@app.route('/predict', methods=["POST"])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])

# #Sample Address = 0x00009277775ac7d0d59eaad8fee3d10ac6c805e8
# 0x0d979f9ffdd579d67c29531cccba568d2172d0b0

def prediction_func():
        print(request.json)
        if(request.json):
                data = request.json
                if(isValidAddress(data[1:-1])):
                        getErc(data[1:-1],ercMin,ercMax,ercAvg)              
                        # transDetails(data[1:-1])
                        temp = X_Address.where(X_Address['Address'] == data[1:-1])
                        X_info = temp.dropna().iloc[:,0:44]
                        # print(X_info) #get information related to that data point 
                        prediction = clf.predict_proba(X_info)
                        response = jsonify({"result": str(prediction[0][0])})
                        print("preiction[0][0] ",prediction[0][0])
                        print(response, "  response is given")
                        return response 
                else:
                        response = jsonify({"result": str(-1)})
                        print(response, "  response is given")
                        return response   
                
        else:
                response = jsonify({"result": str(-1)})
                print(response, "  response is given")
                return response      
    
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)