-- ============================================
-- Walmart Sales Business Analysis Queries
-- ============================================

-- 1. Total sales by store
SELECT Store,
       SUM(Weekly_Sales) AS total_sales
FROM walmart_sales
GROUP BY Store
ORDER BY total_sales DESC;

-- 2. Average weekly sales across all stores
SELECT AVG(Weekly_Sales) AS avg_weekly_sales
FROM walmart_sales;

-- 3. Holiday vs Non-Holiday sales comparison
SELECT Holiday_Flag,
       AVG(Weekly_Sales) AS avg_sales
FROM walmart_sales
GROUP BY Holiday_Flag;

-- 4. Monthly sales trend
SELECT YEAR(Date) AS year,
       MONTH(Date) AS month,
       SUM(Weekly_Sales) AS monthly_sales
FROM walmart_sales
GROUP BY year, month
ORDER BY year, month;

-- 5. Top 5 highest sales weeks
SELECT Date,
       Weekly_Sales
FROM walmart_sales
ORDER BY Weekly_Sales DESC
LIMIT 5;

-- These queries analyze store performance, seasonal trends,
-- and holiday impact on weekly sales using Walmart retail data.