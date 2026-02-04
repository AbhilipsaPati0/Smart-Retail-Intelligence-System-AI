from openai import OpenAI

# Initialize client
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_genai_insights(rmse, r2, top_features):
    """
    Uses Generative AI to convert model metrics into business insights.
    """

    prompt = f"""
    You are a senior retail data analyst.

    Model Performance:
    - RMSE: {rmse}
    - R2 Score: {r2}

    Top Predictive Features:
    {', '.join(top_features)}

    Generate 4 concise, actionable business insights
    for a retail manager.
    Avoid technical jargon.
    Focus on decisions and strategy.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# Test run
if __name__ == "__main__":
    rmse = 106744
    r2 = 0.93
    top_features = ["Lag_1_Week", "Lag_4_Week", "Month"]

    insights = generate_genai_insights(rmse, r2, top_features)
    print("GenAI Business Insights:\n")
    print(insights)
