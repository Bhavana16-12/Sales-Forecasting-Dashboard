#FUTURE_ML_01/
# Sales Forecasting Dashboard

## Dashboard Preview

![Sales Forecasting Dashboard](screenshots/dashboard.png)



---<img width="1837" height="812" alt="image" src="https://github.com/user-attachments/assets/dfe0c38c-ed8f-4a67-832e-b2c4dfbf2bf0" />


## Project Overview

The Sales Forecasting Dashboard is a Machine Learning project designed to predict future sales using historical business data. The system performs data cleaning, feature engineering, model training, forecasting, and visualization to help businesses make informed decisions.

This project demonstrates how Machine Learning can be used in real-world business scenarios to forecast demand, optimize inventory planning, estimate revenue, and support strategic decision-making.

---

## Objective

To forecast future sales and demand patterns using historical sales records and provide business-friendly insights through interactive visualizations.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* Jupyter Notebook

---

## Features

### Data Cleaning

* Duplicate record removal
* Missing value handling
* Invalid value correction
* Date standardization

### Feature Engineering

* Year
* Month
* Quarter
* Week Number
* Day of Week
* Day of Month

### Machine Learning Models

* Linear Regression
* Random Forest Regressor

### Model Evaluation

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

### Forecasting

* Future 30-Day Sales Forecast
* Category-wise Sales Prediction
* Trend Analysis

### Visualizations

* Sales Trend Analysis
* Monthly Sales Analysis
* Yearly Sales Analysis
* Actual vs Predicted Sales
* Future Forecast Visualization
* Error Analysis

---

## Project Workflow

Historical Sales Data

↓

Data Cleaning

↓

Feature Engineering

↓

Model Training

↓

Model Evaluation

↓

Future Forecast Generation

↓

Dashboard Visualization

↓

Business Insights

---

## Model Performance

| Model                   | R² Score | MAE       | RMSE      |
| ----------------------- | -------- | --------- | --------- |
| Random Forest Regressor | 0.8430   | $1,172.92 | $1,940.08 |
| Linear Regression       | 0.6709   | $1,825.38 | $2,809.02 |

### Best Model

The Random Forest Regressor achieved the highest R² Score and lowest prediction error, making it the best-performing model for sales forecasting.

---

## Results

* Compared Linear Regression and Random Forest models.
* Selected the best-performing model based on evaluation metrics.
* Generated future sales forecasts for the next 30 days.
* Created business-friendly visual dashboards for decision-making.
* Improved forecasting accuracy through feature engineering and model optimization.

---

## Business Benefits

* Better inventory planning
* Demand forecasting
* Revenue estimation
* Sales trend identification
* Resource allocation planning
* Data-driven decision making

---

## Project Structure

Sales-Forecasting-Dashboard/

├── .gitignore

├── README.md

├── main.py

├── serve_dashboard.py

├── requirements.txt

├── screenshots/

│ └── dashboard.png

└── data/

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavana16-12/Sales-Forecasting-Dashboard.git
```

### 2. Navigate to the Project Directory

```bash
cd Sales-Forecasting-Dashboard
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run serve_dashboard.py
```

---

## Future Enhancements

* Real-time forecasting
* Power BI integration
* Advanced Time Series Models (ARIMA, Prophet, LSTM)
* Cloud deployment
* Automated report generation
* API integration for live sales data

---

## Conclusion

This project demonstrates the practical application of Machine Learning in sales forecasting. By leveraging historical sales data and predictive analytics, businesses can make informed decisions, optimize inventory management, improve operational efficiency, and increase profitability.

---

## Author

Bhavana

GitHub:
GitHub: https://github.com/Bhavana16-12/FUTURE_ML_01

