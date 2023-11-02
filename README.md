# Ethereum-Fraud-Detection

## Installing required modules and packages.
Backend is written in python.\
**For backend** folder files, paste the following code in the terminal to automatically install all the required packages.\
`pip install -r requirements.txt`\
\
**For frontend** we are using React with vite, so just type in the following code in terminal after entering the Frontend folder.\
`npm i`   
  
  
## Run the **_server.py_** file to start a flask server.  
This file is responsible for the communication between frontend and backend.

## Start the frontend server with following command.  
`npm run dev`  

#### **_Ethereum_Fraud_Detection.joblib_** is the saved Machine Learning Model in serialized form which is loaded to predict the possible outcome in server.py file.
  
    
#### **_X_Address.joblib_** is the training X values which are saved and loaded in server.py file for getting the features because currently we dont have a proper backend.
Only the addresses listed in X_Address.joblib will be predicted for now.
