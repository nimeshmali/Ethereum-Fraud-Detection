from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from joblib import load
from web3 import Web3
import requests
import pandas as pd
import myKey as k
# from ethereum_address import is_address
# Initializing flask app
app = Flask(__name__)
CORS(app) 

api_key = k.my_eth_key
url = "https://api.etherscan.io/api"

features = {
        "avgMinSentTnx":[0],
        "avgMinRecTnx":[0],
        "timeFirstLastTnx":[0],
        "transFrom":[0],
        "transTo":[0],
        "createdCont":[0],
        "uniqRecAdd":[0],
        "uniqSentAdd":[0],
        "minValRec":[0],
        "maxValRec":[0],
        "avgValRec":[0],
        "minValSent":[0],
        "maxValSent":[0],
        "avgValSent":[0],
        "minSentToCont":[0],
        "maxSentToCont":[0],
        "avgSentToCont":[0],
        "totalTnx":[0],
        'totalEtherSent':[0],
        "totalEtherRec":[0],
        "totalEtherSentcCont":[0],
        "totalEtherBal":[0],
        "totalErcTrans":[0],
        "totalErcEtherRec":[0],
        "totalErcEtherSent":[0],
        "totalErcEtherSentCont":[0],
        "ercUniqSentAddr":[0],
        "ercUniqRecAddr":[0],
        "ercUniqSentAddr1":[0],
        "ercUniqRecCont":[0],
        "ercAvgTimeSentTnx":[0],
        "ercAvgTimeRecTnx":[0],
        "ercAvgTimeRec2Tnx":[0],
        "ercAvgTimeContTnx":[0],
        "ercMinRec":[0],
        "ercMaxRec":[0],
        "ercAvgRec":[0],
        "ercMinSent":[0],
        "ercMaxSent":[0],
        "ercAvgSent":[0],
        "ercMinValSentCont":[0],
        "ercMaxValSentCont":[0],
        "ercAvgValSentCont":[0],
        "ercUniqSentToken":[0],

}


def getErc(addr,features):

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
                b=0
                features["totalErcTrans"][0]=len(dict["result"])
                for i in range(len(dict["result"])):
                        if dict["result"][i]["from"]==addr:
                                c=c+1

                                # print(int(dict["result"][i]["value"]))
                                if int(dict["result"][i]["value"]) < features["ercMinSent"][0]:
                                        features["ercMinSent"][0]=int(dict["result"][i]["value"])
                                
                                if int(dict["result"][i]["value"]) > features["ercMaxSent"][0]:
                                        features["ercMaxSent"][0]=int(dict["result"][i]["value"])
                                
                                features["ercAvgSent"][0]=features["ercAvgSent"][0]+int(dict["result"][i]["value"])
                        else:
                                b=b+1
                                if int(dict["result"][i]["value"]) < features["ercMinRec"][0]:
                                        features["ercMinRec"][0]=int(dict["result"][i]["value"])
                                
                                if int(dict["result"][i]["value"]) > features["ercMaxRec"][0]:
                                        features["ercMaxRec"][0]=int(dict["result"][i]["value"])
                                
                                features["ercAvgRec"][0]=features["ercAvgRec"][0]+int(dict["result"][i]["value"])
                                

                                
                if c>0:
                        features["ercAvgSent"][0]=features["ercAvgSent"][0]/c
                if b>0:
                        features["ercAvgRec"][0]=features["ercAvgRec"][0]/b

                print(features["ercMinSent"][0])
                print(features["ercMaxSent"][0])
                print(features["ercAvgSent"][0])
                print(features["ercMinRec"][0])
                print(features["ercMaxRec"][0])
                print(features["ercAvgRec"][0])
                print(features["totalErcTrans"][0])
                                

        else:
                print("error occured")

def trans(addr,features):
        valuesErc = f'{url}?module=account&action=txlist&address={addr}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={api_key}'
        # print(valuesErc)
        print("transactionn related info below")
        print("addr",(addr))
        response=requests.get(valuesErc)
        if response.status_code==200:
                print("ho gyis two")
                print(type(response.json()))
                dict = response.json()
                print("length of result ",len(dict["result"]))
                features["totalTnx"][0]=len(dict["result"])        
                print("type of result ",type(dict["result"]))
                b=0
                c=0
                for i in range(len(dict["result"])):
                        if dict["result"][i]["from"]==addr:
                                c=c+1
                                features["transFrom"][0]=features["transFrom"][0]+1
                                if int(dict["result"][i]["value"]) < features["minValSent"][0]:
                                        features["minValSent"][0]=int(dict["result"][i]["value"])
                                
                                if int(dict["result"][i]["value"]) > features["maxValSent"][0]:
                                        features["maxValSent"][0]=int(dict["result"][i]["value"])
                                
                                features["avgValSent"][0]=features["avgValSent"][0]+int(dict["result"][i]["value"])
                        else:
                                b=b+1
                                features["transTo"][0]=features["transTo"][0]+1
                                if int(dict["result"][i]["value"]) < features["minValRec"][0]:
                                        features["minValRec"][0]=int(dict["result"][i]["value"])
                                
                                if int(dict["result"][i]["value"]) > features["maxValRec"][0]:
                                        features["maxValRec"][0]=int(dict["result"][i]["value"])
                                
                                features["avgValRec"][0]=features["avgValRec"][0]+int(dict["result"][i]["value"])
                if c>0:
                        features["avgValSent"][0]=features["avgValSent"][0]/c
                if b>0:
                        features["avgValRec"][0]=features["avgValRec"][0]/b
                        

                print(features["transFrom"][0])
                print(features["transTo"][0])
                print(features["minValSent"][0])
                print(features["maxValSent"][0])
                print(features["avgValSent"][0])
                print(features["minValRec"][0])
                print(features["maxValRec"][0])
                print(features["avgValRec"][0])
        else:
                print("error occured")


def giveEther(addr,features):
        values = f"{url}?module=account&action=balancemulti&address={addr}&tag=latest&apikey={api_key}"  
        response = requests.get(values)
        if response.status_code == 200:
                dict=response.json()
                features["totalEtherBal"][0]=int(dict["result"][0]["balance"]) 
                print("total ether balence ",features["totalEtherBal"][0])




def isValidAddress(add):
  if(Web3.is_address(add)):
    return True

  else:
    return False


def getData(data, X_Address, X_info, features):
        print("aa gaya")
        print(X_Address)
        temp = pd.DataFrame()
        temp = X_Address.where(X_Address['Address'] == data)
        # print(temp.isna().sum())
        print(temp)
        if temp.iloc[:, 0].isna().sum()==9840:
                # X_info = temp.dropna().iloc[:,0:44]
                # print("jojo")
                # temp = X_Address.where(X_Address['Address'] == data[1:-1])
                X_info = temp.dropna().iloc[:,0:44]
        elif temp.shape == (9841,45):
                # print("ha bhai empty hai")
                temp = pd.DataFrame.from_dict(features)
                X_info=temp
           
        print(X_info)
        print(type(X_info))
        return X_info



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
                        getErc(data[1:-1],features)   
                        trans(data[1:-1],features)  
                        giveEther(data[1:-1],features)
                        X_info=pd.DataFrame()

                        Z_info=getData(data[1:-1],X_Address,X_info,features)
                        print("********")
                        print(Z_info)
                        
                        # print(X_info) #get information related to that data point 
                        prediction = clf.predict_proba(Z_info)
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