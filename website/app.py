from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)

tickers = {
    "AMZN": "Amazon",
    "AAPL": "Apple",
    "MSFT": "Microsoft"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    prediction_data = None
    selected_ticker = None
    company_name = None
    days = None
    current_price = None
    error = None

    if request.method == "POST":

        try:
            selected_ticker = request.form.get("ticker")
            days = int(request.form.get("days"))

            if selected_ticker not in tickers:
                raise ValueError("Please select a valid stock.")

            if days < 1 or days > 30:
                raise ValueError(
                    "Prediction days must be between 1 and 30."
                )

            company_name = tickers[selected_ticker]

            # Download the same historical data used in the notebook
            data = yf.download(
                selected_ticker,
                start="2018-01-01",
                end="2023-12-01",
                auto_adjust=False,
                progress=False
            )

            if data.empty:
                raise ValueError(
                    "Stock data could not be downloaded."
                )

            # Extract closing prices
            close_data = data["Close"].dropna()

            if isinstance(close_data, pd.DataFrame):
                close_data = close_data.iloc[:, 0]

            # Save the final historical date before removing the index
            last_date = pd.to_datetime(close_data.index[-1])

            # Convert prices to a simple numeric array for ARIMA
            close_prices = np.asarray(
                close_data,
                dtype=float
            ).reshape(-1)

            current_price = float(close_prices[-1])

            # Train ARIMA
            model = ARIMA(
                close_prices,
                order=(5, 1, 0)
            )

            model_fit = model.fit()

            # Forecast future prices
            forecast = model_fit.forecast(
                steps=days
            )

            forecast = np.asarray(
                forecast,
                dtype=float
            ).reshape(-1)

            # Generate future business dates
            future_dates = pd.bdate_range(
                start=last_date + pd.Timedelta(days=1),
                periods=days
            )

            prediction_data = []

            for date, price in zip(
                future_dates,
                forecast
            ):
                prediction_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "price": round(float(price), 2)
                })

        except Exception as e:
            error = str(e)

    return render_template(
        "predict.html",
        prediction_data=prediction_data,
        selected_ticker=selected_ticker,
        company_name=company_name,
        days=days,
        current_price=current_price,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)