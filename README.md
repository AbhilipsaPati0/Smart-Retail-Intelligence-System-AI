
 # Smart-Retail-Intelligence-System-AI
Smart Retail Intelligence System – Walmart Sales Analysis
📌 Project Overview

This project is an end-to-end retail analytics system built using Python, SQL, Power BI, and Machine Learning, designed to analyze Walmart sales data and extract business, performance, and external factor insights.

The goal is to simulate how a real-world retail analytics team works — from raw data to dashboards and predictive insights.

🎯 Objectives

Analyze overall and store-level Walmart sales performance

Identify top and bottom performing stores

Study the impact of holidays, temperature, and unemployment on sales

Build a sales forecasting model

Present insights through interactive Power BI dashboards

Generate rule-based + AI-generated insights (optional GenAI layer)

🗂️ Project Structure
![image](https://github.com/AbhilipsaPati0/Smart-Retail-Intelligence-System-AI/blob/0638d94a808b926360c4dc8fde90facd9815bf25/Screenshot%202026-02-07%20160426.png)

🧪 Dataset Description

The dataset contains weekly sales data for multiple Walmart stores along with external variables.

Key Columns:

Store

Date

Weekly_Sales

Holiday_Flag

Temperature

Fuel_Price

CPI

Unemployment

🔄 Data Pipeline
1️⃣ Data Loading

Loaded CSV data using Pandas

Parsed date columns

Basic validation (shape, info, head)

2️⃣ Data Cleaning

Handled missing values

Corrected data types

Removed inconsistencies

Ensured clean time-series data

3️⃣ Exploratory Data Analysis (EDA)

Sales distribution analysis

Holiday vs non-holiday sales comparison

Store-level sales behavior

Time-based trends

4️⃣ Feature Engineering

Extracted:

Year

Month

Week number

Created lag features:

Lag 1 week

Lag 2 weeks

Lag 4 weeks

🤖 Sales Forecasting (Machine Learning)

Model used: Linear Regression

Features:

Time-based features

Lagged sales values

Economic indicators

Evaluation Metrics:

RMSE

R² Score

The model demonstrates strong predictive capability for weekly sales trends.

🧠 Insights Generation
✔️ Rule-Based Insights

Sales spike during holiday periods

Certain stores consistently outperform others

External factors show correlation with sales patterns

✔️ AI-Based Insights (Optional)

Integrated OpenAI API (GenAI)

Automatically converts numerical outputs into business-friendly insights

(API key excluded from repo for security)

🗄️ SQL Analysis

Business-level queries written using MySQL:

Examples:

Top 10 stores by total sales

Bottom 10 stores by sales

Average weekly sales per store

Holiday vs non-holiday sales contribution

Time-based aggregations

All queries are stored in:

sql/walmart_business_queries.sql

📊 Power BI Dashboard
📄 Page 1 – Executive Overview

Total Sales (Card)

Average Weekly Sales (Card)

Peak Weekly Sales (Card)

Holiday vs Non-Holiday Sales (Donut)

Overall Sales Trend (Line)

📄 Page 2 – Store Performance Analysis

Top 10 Stores by Total Sales

Bottom 10 Stores by Total Sales

Average Weekly Sales by Store

📄 Page 3 – External Factors Analysis

Temperature vs Weekly Sales (Scatter)

Unemployment vs Avg Weekly Sales (Scatter)

Yearly Sales vs Temperature Trend

🛠️ Tools & Technologies

Python (Pandas, NumPy, Matplotlib, Scikit-learn)

SQL (MySQL)

Power BI

Machine Learning

Generative AI (OpenAI API)

Git & GitHub

🔐 Security & Best Practices

API keys excluded using .gitignore

Modular notebook structure

Clear separation of data, logic, and visualization layers

🚀 Key Takeaways

Combines data analytics + ML + BI + AI

Mimics real-world retail intelligence systems

Portfolio-ready and interview-ready project

Demonstrates strong understanding of business + technical analytics

👩‍💻 Author

Abhilipsa Pati
B.Tech CSE | Data Analytics & Software Development

🔗 GitHub: AbhilipsaPati0

