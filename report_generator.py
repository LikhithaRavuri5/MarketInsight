from openai import OpenAI
from config import OPENROUTER_API_KEY, COMPANY_NAME
import datetime

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def generate_report(headlines, sentiment_result):
    print("Generating final report using AI...")

    headlines_text = "\n".join(headlines)
    today = datetime.date.today()

    prompt = f"""
    You are a professional business intelligence report writer.
    
    Company: {COMPANY_NAME}
    Date: {today}
    
    News Headlines:
    {headlines_text}
    
    Sentiment Analysis:
    {sentiment_result}
    
    Based on the above, write a complete Market Insight Report with these sections:
    1. Executive Summary
    2. Recent News Overview
    3. Sentiment Analysis Summary
    4. Key Opportunities
    5. Key Risks
    6. Final Recommendation (Buy / Hold / Watch)
    
    Write in professional business language. Keep it clear and structured.
    """

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    report = response.choices[0].message.content
    print("Report generation complete!")
    return report

def save_report(report):
    today = datetime.date.today()
    filename = f"{COMPANY_NAME}_Market_Report_{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"MARKET INSIGHT REPORT\n")
        file.write(f"{'='*50}\n")
        file.write(f"Company: {COMPANY_NAME}\n")
        file.write(f"Date: {today}\n")
        file.write(f"{'='*50}\n\n")
        file.write(report)

    print(f"Report saved as: {filename}")
    return filename

if __name__ == "__main__":
    sample_headlines = [
        f"{COMPANY_NAME} reports record quarterly profits",
        f"{COMPANY_NAME} expands operations to 5 new countries",
        f"{COMPANY_NAME} wins major government contract"
    ]
    sample_sentiment = "Overall Sentiment: Positive. Score: 8/10. Strong financial performance."

    report = generate_report(sample_headlines, sample_sentiment)
    print(report)
    save_report(report)