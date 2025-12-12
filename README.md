# Ethereum Fraud Detection System

A machine learning-powered web application that analyzes Ethereum wallet addresses to detect potential fraudulent activity including phishing, Ponzi schemes, and scam wallets.

## 🎯 Overview

This project implements a Random Forest classifier to identify fraudulent Ethereum wallets by analyzing blockchain transaction data fetched in real-time from the Etherscan API. The system calculates a fraud probability score (0-1) and displays behavioral indicators through an intuitive React-based dashboard.

## ✨ Features

- **Real-time Analysis**: Fetches live blockchain data directly from Etherscan API
- **ML-Powered Detection**: Uses Random Forest algorithm trained on transactional features
- **Fraud Classification**: Identifies phishing, Ponzi schemes, and scam wallets
- **Probability Scoring**: Provides fraud likelihood score between 0 (legitimate) and 1 (fraudulent)
- **Interactive Dashboard**: Clean React interface for wallet analysis and results visualization
- **Behavioral Indicators**: Displays transaction patterns and suspicious activity markers

## 🏗️ Architecture

- **Backend**: Python Flask server handling API requests and ML predictions
- **Frontend**: React with Vite for fast development and optimized builds
- **ML Model**: Serialized Random Forest classifier (`Ethereum_Fraud_Detection.joblib`)
- **Data Source**: Etherscan API for real-time blockchain data

## 📋 Prerequisites

- Python 3.7+
- Node.js 16+
- Etherscan API key ([Get one here](https://etherscan.io/apis))

## 🚀 Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the backend folder:
```bash
my_eth_key=YOUR_ETHERSCAN_API_KEY
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

## 💻 Running the Application

### Start the Backend Server

From the backend directory:
```bash
python app.py
```

The Flask server will start on `http://localhost:5000` (or configured port).

### Start the Frontend Development Server

From the frontend directory:
```bash
npm run dev
```

The React app will be available at `http://localhost:5173` (default Vite port).

## 📁 Project Structure
```
.
├── backend/
│   ├── app.py                              # Flask server
│   ├── requirements.txt                    # Python dependencies
│   ├── Ethereum_Fraud_Detection.joblib     # Trained ML model
│   ├── X_Address.joblib                    # Training data addresses
│   └── .env                                # Environment variables
└── frontend/
    ├── src/                                # React source files
    ├── package.json                        # Node dependencies
    └── vite.config.js                      # Vite configuration
```

## 🔧 Key Components

### Machine Learning Model
- **File**: `Ethereum_Fraud_Detection.joblib`
- **Algorithm**: Random Forest Classifier
- **Input**: Transactional features from Ethereum wallets
- **Output**: Fraud probability score (0-1)

### Training Data
- **File**: `X_Address.joblib`
- **Purpose**: Contains wallet addresses used during model training
- **Note**: Currently, predictions are limited to addresses present in this dataset

## 🔑 API Configuration

The application requires an Etherscan API key to fetch blockchain data. Store it in the backend `.env` file:
```
my_eth_key=YOUR_API_KEY_HERE
```

## 🎨 Frontend Features

- Wallet address input and validation
- Real-time fraud probability display
- Behavioral indicators visualization
- Transaction pattern analysis
- Clean, responsive UI design

## ⚠️ Current Limitations

- Predictions are currently limited to wallet addresses present in `X_Address.joblib`
- Live wallet analysis for arbitrary addresses requires backend enhancement

## 🛠️ Future Enhancements

- [ ] Support for analyzing any Ethereum wallet address
- [ ] Enhanced feature engineering from live transaction data
- [ ] Additional fraud classification categories
- [ ] Historical analysis and trend visualization
- [ ] Batch wallet analysis capability

## 📊 How It Works

1. User enters an Ethereum wallet address in the frontend
2. Frontend sends the address to the Flask backend
3. Backend fetches transaction data from Etherscan API
4. Transactional features are extracted and processed
5. ML model predicts fraud probability
6. Results and behavioral indicators are returned to the dashboard
7. Frontend displays the fraud score and analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 👤 Author

[Nimesh Mali]

---

**Note**: This project is for educational and research purposes. Always perform thorough due diligence before making any decisions based on fraud detection results.
