# Stock Price Predictor

This repository contains a Flask-based web application that predicts stock prices using historical data and a Random Forest regression model. The application is designed to provide next-day closing price predictions based on user-provided stock metrics such as opening price, high price, low price, and trading volume.

---

## Features

- **Stock Data Analysis**: Uses historical stock data for model training and prediction.
- **Machine Learning Model**: Utilizes a Random Forest Regressor for accurate stock price predictions.
- **User-Friendly Interface**: Provides a simple and intuitive web interface for entering stock metrics and viewing predictions.
- **Dynamic Updates**: Appends user inputs to the dataset for enhanced predictions over time.

---

## How It Works

1. **Input Stock Data**: Users input stock metrics including:
   - Open Price
   - High Price
   - Low Price
   - Volume
2. **Predict Next-Day Closing Price**: The app predicts the stock's closing price for the next trading day.
3. **Machine Learning Pipeline**:
   - Dataset preprocessing (e.g., sorting by date, handling datetime format).
   - Training a Random Forest Regressor model using historical data.
   - Predicting new closing prices based on user input.

---


## Project Structure

```
.
|-- stock.csv                 # Historical stock data file
|-- stock_prediction.py       # Main Flask application and prediction logic
|-- templates/
|   |-- index.html            # Home page
|   |-- result.html           # Prediction result page
|-- static/
|   |-- (Optional CSS/JS files for styling and interactivity)
|-- README.md                 # Project documentation (this file)
```

---

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning**: scikit-learn (Random Forest Regressor)
- **Data Handling**: pandas

---

## Usage

1. Start the Flask application by running `stock_prediction.py`.
2. Enter stock details in the web form.
3. View the predicted closing price on the results page.

---

## Dataset

The app uses a historical stock dataset (`stock.csv`) that includes the following columns:
- `Date`: Date of stock data
- `Open`: Opening price
- `High`: Highest price during the trading day
- `Low`: Lowest price during the trading day
- `Close`: Closing price (target variable)
- `Volume`: Volume of stocks traded

Ensure the dataset is properly formatted for seamless operation.

---

## Future Improvements

- Enhance the model by incorporating additional features like moving averages, RSI, etc.
- Implement real-time data fetching from stock APIs.
- Add visualization tools to show trends and predictions.
- Deploy the application using cloud platforms like AWS or Heroku.

---

## Contributing

Feel free to fork this repository and make pull requests for enhancements or bug fixes. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

