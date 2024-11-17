import pandas as pd
import matplotlib.pyplot as plt

def analyze_performance(data_file="data/performance.csv"):
    """Analyze content performance from a CSV file."""
    df = pd.read_csv(data_file)
    metrics = ["Traffic", "Bounce Rate", "Engagement"]

    for metric in metrics:
        plt.figure()
        plt.plot(df["Date"], df[metric], marker="o")
        plt.title(f"{metric} Over Time")
        plt.xlabel("Date")
        plt.ylabel(metric)
        plt.grid(True)
        output_path = f"data/{metric.lower()}_trend.png"
        plt.savefig(output_path)
        print(f"{metric} trend saved to {output_path}")
