from openai import OpenAI
from config import OPENROUTER_API_KEY, COMPANY_NAME

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

def analyze_sentiment(headlines):
    print("Analyzing sentiment using AI...")

    headlines_text = "\n".join(headlines)

    prompt = f"""
    You are a financial analyst AI.
    
    Below are recent news headlines about {COMPANY_NAME}:
    {headlines_text}
    
    Analyze these headlines and provide:
    1. Overall Sentiment: (Positive / Negative / Neutral)
    2. Sentiment Score: (give a score from 1 to 10, where 1 is very negative and 10 is very positive)
    3. Key Reasons: (3 bullet points explaining why)
    4. Market Outlook: (1 paragraph about what this means for the company)
    
    Be professional and concise.
    """

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sentiment_result = response.choices[0].message.content

    print("Sentiment analysis complete!")
    return sentiment_result

if __name__ == "__main__":
    sample_headlines = [
        f"{COMPANY_NAME} reports record quarterly profits",
        f"{COMPANY_NAME} expands operations to 5 new countries",
        f"{COMPANY_NAME} wins major government contract"
    ]
    result = analyze_sentiment(sample_headlines)
    print(result)