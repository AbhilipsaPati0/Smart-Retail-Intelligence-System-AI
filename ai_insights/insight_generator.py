# ai_insights/insight_generator.py

def generate_business_insights(rmse, r2, top_features):
    insights = []

    insights.append(
        f"The sales forecasting model achieved strong performance with an R² score of {r2:.2f}, "
        f"indicating that approximately {r2*100:.0f}% of weekly sales variability is explained by the model."
    )

    insights.append(
        f"The average prediction error (RMSE) is around {rmse:,.0f}, "
        "which is reasonable given the scale of weekly sales."
    )

    insights.append(
        "Historical sales patterns emerged as the most influential predictors, "
        "highlighting strong demand persistence and seasonality in customer purchasing behavior."
    )

    insights.append(
        "External economic factors such as fuel price, inflation, and unemployment showed relatively weaker influence, "
        "suggesting that Walmart sales are resilient to short-term economic fluctuations."
    )

    insights.append(
        f"Key drivers of sales identified by the model include: {', '.join(top_features)}."
    )

    insights.append(
        "Based on these insights, business strategies should focus on leveraging seasonal trends, "
        "optimizing inventory planning around high-demand periods, and monitoring store-level performance."
    )

    return "\n\n".join(insights)


# Example usage
if __name__ == "__main__":
    rmse = 106744
    r2 = 0.93
    top_features = ["Lag_1_Week", "Lag_4_Week", "Month"]

    summary = generate_business_insights(rmse, r2, top_features)
    print("AI-Generated Business Insights:\n")
    print(summary)
