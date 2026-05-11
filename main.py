from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment
from report_generator import generate_report, save_report
from config import COMPANY_NAME

def run_market_insight():
    print("\n" + "="*50)
    print(f"  MARKET INSIGHT AGENT STARTING...")
    print(f"  Analyzing: {COMPANY_NAME}")
    print("="*50 + "\n")

    print("STEP 1: Fetching latest news...")
    headlines = fetch_news()
    print(f"✓ Got {len(headlines)} headlines\n")

    print("STEP 2: Analyzing sentiment...")
    sentiment = analyze_sentiment(headlines)
    print("✓ Sentiment analysis done\n")

    print("STEP 3: Generating report...")
    report = generate_report(headlines, sentiment)
    filename = save_report(report)
    print("✓ Report saved\n")

    print("="*50)
    print(f"  DONE! Report saved as: {filename}")
    print("="*50 + "\n")

    print(report)

if __name__ == "__main__":
    run_market_insight()