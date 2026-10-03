\# Stock Market Prediction and Analysis Using LSTM and ARIMA



\## About the Project



This project focuses on stock price prediction using LSTM and ARIMA models. Historical stock data for Amazon, Apple, and Microsoft was collected using Yahoo Finance.



The main goal of the project is to analyze historical stock prices, build prediction models, compare their performance, and use ARIMA to generate future stock price forecasts through a simple web application.



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



LSTM was used to learn patterns from historical stock prices and generate predictions. The data was scaled and divided into training, validation, and testing sets before training the model.



\### ARIMA



ARIMA was used as a time-series forecasting model. Rolling predictions were generated on the test data and compared with the actual stock prices.



\## Model Results



| Company | LSTM MAE | LSTM MAPE-based Accuracy | ARIMA MAE | ARIMA MAPE-based Accuracy |

| --- | ---: | ---: | ---: | ---: |

| Amazon | 2.1930 | 98.31% | 1.8985 | 98.53% |

| Apple | 2.6471 | 98.55% | 1.6355 | 99.09% |

| Microsoft | 5.1816 | 98.43% | 3.6247 | 98.92% |



Both models performed well on the selected historical stock data. In this project, ARIMA produced lower MAE and slightly higher MAPE-based accuracy than LSTM for all three stocks.



\## Web Application



A simple Flask web application was created for stock price forecasting.



The user can:



\- Select Amazon, Apple, or Microsoft

\- Enter a forecast period from 1 to 30 business days

\- Generate future stock price forecasts using ARIMA

\- View the predicted stock prices by date



\## Project Files



The project contains the following folders:



\- `python` - contains the Jupyter Notebook used for data analysis and model development

\- `results` - contains LSTM, ARIMA, and model comparison graphs

\- `website` - contains the Flask web application

\- `README.md` - contains the project details



The stock data is downloaded directly from Yahoo Finance using the `yfinance` library, so a separate dataset is not required.



\## Results



The project includes the following visualizations:



\- Amazon, Apple, and Microsoft LSTM prediction graphs

\- Amazon, Apple, and Microsoft ARIMA prediction graphs

\- LSTM vs ARIMA accuracy comparison

\- LSTM vs ARIMA MAE comparison



The comparison results show that ARIMA had lower prediction error than LSTM for the three stocks used in this project.



\## How to Run the Project



Install the required Python packages:



&#x20;   pip install -r requirements.txt



Activate the project environment if needed:



&#x20;   conda activate stockmarket



Go to the website folder:



&#x20;   cd website



Run the Flask application:



&#x20;   python app.py



Open the local address shown in the terminal to view the website.



\## Note



The predictions in this project are based on the historical data period used for the analysis. They are created for project and learning purposes and should not be considered financial advice.

