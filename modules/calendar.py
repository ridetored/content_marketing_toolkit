import pandas as pd
from datetime import datetime, timedelta

def generate_content_calendar(topics, start_date, frequency="weekly"):
    """Generate a content calendar based on topics and frequency."""
    calendar = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    delta = timedelta(weeks=1) if frequency == "weekly" else timedelta(days=1)

    for topic in topics:
        calendar.append({"Date": current_date.strftime("%Y-%m-%d"), "Topic": topic})
        current_date += delta

    # Save to CSV
    output_path = "data/calendar.csv"
    df = pd.DataFrame(calendar)
    df.to_csv(output_path, index=False)
    print(f"Content calendar saved to {output_path}")
