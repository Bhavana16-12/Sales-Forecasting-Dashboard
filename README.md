.
# Sales Forecasting Dashboard

## Project Overview

The Sales Forecasting Dashboard is a Machine Learning project designed to predict future sales using historical business data. The system performs data cleaning, feature engineering, model training, forecasting, and visualization to help businesses make informed decisions.

## Objective

To forecast future sales and demand patterns using historical sales records and provide business-friendly insights through interactive visualizations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* Jupyter Notebook

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
* Day Of Week
* Day Of Month

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

## Project Workflow

Historical Sales Data
→ Data Cleaning
→ Feature Engineering
→ Model Training
→ Model Evaluation
→ Future Forecast Generation
→ Dashboard Visualization
→ Business Insights

## Results

* Compared Linear Regression and Random Forest models.
* Selected the best-performing model based on evaluation metrics.
* Generated future sales forecasts for the next 30 days.
* Created business-friendly visual dashboards for decision-making.

## Business Benefits

* Better inventory planning
* Demand forecasting
* Revenue estimation
* Sales trend identification
* Data-driven decision making

## How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the dashboard

```bash
streamlit run app.py
```

## Future Enhancements

* Real-time forecasting
* Power BI integration
* Advanced time-series models
* Cloud deployment
* Automated report generation


