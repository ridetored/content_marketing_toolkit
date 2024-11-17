import argparse
from modules import calendar, keyword_research, performance, ai_suggestions

def main():
    """
    Main entry point for the Content Marketing Toolkit.
    """
    parser = argparse.ArgumentParser(description="Content Marketing Toolkit")

    parser.add_argument("--generate-calendar", nargs="+", help="Generate a content calendar. Provide topics.")
    parser.add_argument("--start-date", help="Start date for the calendar (YYYY-MM-DD).")
    parser.add_argument("--keyword-research", help="Perform keyword research for a topic.")
    parser.add_argument("--analyze-performance", action="store_true", help="Analyze content performance.")
    parser.add_argument("--ai-suggestions", help="Generate content ideas using AI. Provide a topic or idea.")

    args = parser.parse_args()

    if args.generate_calendar and args.start_date:
        calendar.generate_content_calendar(args.generate_calendar, args.start_date)

    if args.keyword_research:
        keyword_research.fetch_keywords(args.keyword_research)

    if args.analyze_performance:
        performance.analyze_performance()

    if args.ai_suggestions:
        ai_suggestions.generate_content_idea(args.ai_suggestions)

if __name__ == "__main__":
    main()
