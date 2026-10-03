\# Stock Market Prediction and Analysis Using LSTM and ARIMA



\## About the Project



This project is based on stock price prediction using LSTM and ARIMA models. Historical stock data of Amazon, Apple, and Microsoft was collected using Yahoo Finance.



The main goal of the project is to analyze the stock data, build both models, compare their performance, and use the better performing model for future price prediction.



\## Stocks Used



\- Amazon (AMZN)

\- Apple (AAPL)

\- Microsoft (MSFT)



\## Tools and Technologies



\- Python

\- Jupyter Notebook

\- Pandas

\- NumPy

\- Matplotlib

\- yfinance

\- TensorFlow / Keras

\- Scikit-learn

\- Statsmodels

\- Flask

\- HTML

\- CSS



\## Models Used



\### LSTM



LSTM was used to predict stock prices based on patterns in the historical data. The data was scaled and divided into training, validation, and testing sets before training the model.



\### ARIMA



ARIMA was also used for stock price prediction. The model was tested using rolling predictions and its performance was compared with LSTM.



\## Model Results



| Company | LSTM MAE | LSTM Accuracy | ARIMA MAE | ARIMA Accuracy |

| --- | ---: | ---: | ---: | ---: |

| Amazon | 2.1930 | 98.31% | 1.8985 | 98.53% |

| Apple | 2.6471 | 98.55% | 1.6355 | 99.09% |

| Microsoft | 5.1816 | 98.43% | 3.6247 | 98.92% |



Both models gave good results for the three stocks. In this project, ARIMA had lower MAE and slightly higher accuracy than LSTM.



\## Web Application



A simple Flask web application was created for stock price prediction.



The user can select:



\- Amazon

\- Apple

\- Microsoft



The user can also enter the number of days to predict. The application then uses the ARIMA model to display the predicted stock prices for those days.



\## Project Files



The project contains the following folders:



\- `data` - folder for project data

\- `python` - contains the Jupyter Notebook

\- `results` - contains the model graphs and comparison graphs

\- `website` - contains the Flask web application

\- `README.md` - project information



The `results` folder contains separate folders for LSTM, ARIMA, and model comparison.



\## Results



The following graphs are included in the project:



\- Amazon, Apple, and Microsoft LSTM prediction graphs

\- Amazon, Apple, and Microsoft ARIMA prediction graphs

\- LSTM vs ARIMA accuracy comparison

\- LSTM vs ARIMA MAE comparison



\## How to Run the Website



Activate the environment:



&#x20;   conda activate stockmarket



Go to the website folder:



&#x20;   cd "C:\\Users\\aksha\\Documents\\Prediction and Analysis of Stock Market Using ARIMA Models\\website"



Run the application:



&#x20;   python app.py



Open the local address shown in the terminal to view the website.



\## Note



The predictions in this project are based on the historical data period used for the analysis. They are created for project and learning purposes.

