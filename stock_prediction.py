from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta

app = Flask(__name__)

# Loading dataset
stock_data = pd.read_csv("stock.csv")

# Converting 'Date' to datetime 
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.sort_values('Date', inplace=True) #sorting the dataset by date 

# Variables (X) and target variable (y)
X = stock_data[['Open', 'High', 'Low', 'Volume']]
y = stock_data['Close']

# creating and training the model using random forest ml algo
model = RandomForestRegressor()
model.fit(X, y)


#routes to different applications created 
@app.route('/')
def index():
    return render_template('index.html')



#prediction model 

@app.route('/predict', methods=['POST'])
def predict():
    global stock_data #declaring the stock data as a global variable 
    if request.method == 'POST':
        open_price = float(request.form['open_price'])
        high_price = float(request.form['high_price'])
        low_price = float(request.form['low_price'])
        volume = float(request.form['volume']) # assigning input values to variables



#creating new input for prediction
        current_date = datetime.now().strftime('%Y-%m-%d')

        input_data = pd.DataFrame({
            'Date': [current_date],
            'Open': [open_price],
            'High': [high_price],
            'Low': [low_price],
            'Volume': [volume]
        })

        input_data['Date'] = pd.to_datetime(input_data['Date'])

        # Adding user input to the dataset using concatenation 
        stock_data = pd.concat([stock_data, input_data], ignore_index=True)

        

        # Making prediction for the new input
        next_day = stock_data.tail(1).copy()
        next_day['Date'] = next_day['Date'] + timedelta(days=1)
        next_day.drop(columns=['Close'], inplace=True)

        prediction = model.predict(next_day[['Open', 'High', 'Low', 'Volume']])

        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
