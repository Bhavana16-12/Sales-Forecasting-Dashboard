import os
import pandas as pd
from src.data_cleaning import load_data, clean_data
from src.eda import perform_eda
from src.feature_engineering import create_time_features
from src.forecasting_model import train_and_evaluate

def run_pipeline():
    print("==========================================================")
    print("          SALES FORECASTING PROJECT PIPELINE              ")
    print("==========================================================")
    
    # Paths definition
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(base_dir, 'data', 'raw_sales_data.csv')
    cleaned_data_path = os.path.join(base_dir, 'data', 'cleaned_sales_data.csv')
    vis_dir = os.path.join(base_dir, 'visualizations')
    
    # Ensure directories exist
    os.makedirs(os.path.join(base_dir, 'data'), exist_ok=True)
    os.makedirs(vis_dir, exist_ok=True)
    
    # 1. Dataset Generation Check
    if not os.path.exists(raw_data_path):
        print("Raw dataset not found. Running synthetic data generator first...")
        from data.generate_raw_data import generate_synthetic_data
        generate_synthetic_data(raw_data_path)
    
    # 2. Data Loading & Understanding
    df_raw = load_data(raw_data_path)
    
    # 3. Data Cleaning
    df_cleaned = clean_data(df_raw)
    df_cleaned.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned dataset saved successfully to: {cleaned_data_path}")
    
    # 4. Exploratory Data Analysis (EDA)
    perform_eda(df_cleaned, vis_dir)
    
    # 5. Feature Engineering
    df_feat = create_time_features(df_cleaned)
    
    # 6. Model Training, Evaluation, Future Forecasting, & Error Analysis
    best_model, model_name, metrics = train_and_evaluate(df_feat, vis_dir)
    
    print("\n==========================================================")
    print("       PIPELINE EXECUTION COMPLETED SUCCESSFULLY!        ")
    print("==========================================================")
    print(f"All outputs, forecasts, and visualizations are ready.")
    print(f" - Cleaned Data: data/cleaned_sales_data.csv")
    print(f" - 30-Day Forecast: data/future_forecast_30_days.csv")
    print(f" - Visualizations: visualizations/")
    print(f"   * sales_trend.png (Daily sales & 30-day moving average)")
    print(f"   * monthly_analysis.png (Sales seasonality by category)")
    print(f"   * yearly_analysis.png (Annual revenue comparison)")
    print(f"   * sales_distribution.png (Sales transaction skewness)")
    print(f"   * actual_vs_predicted.png (Model predictions on test set)")
    print(f"   * future_forecast.png (30-day forecasted stacked area chart)")
    print(f"   * error_analysis.png (Forecasting residuals distribution)")
    print("==========================================================")

if __name__ == '__main__':
    run_pipeline()
