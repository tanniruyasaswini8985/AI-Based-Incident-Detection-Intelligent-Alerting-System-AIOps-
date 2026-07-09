from src.data_preprocessing import load_data
from src.anomaly_detection import detect_anomalies
from src.alerting import generate_alerts
from src.utils import print_summary

def main():
    print("🔍 Loading data...")
    data = load_data("data/metrics_data.csv")

    print("🤖 Detecting anomalies...")
    result = detect_anomalies(data)

    print("🚨 Generating alerts...")
    alerts = generate_alerts(result)

    print_summary(result)

    print("\n===== ALERTS =====")
    for alert in alerts:
        print(alert)

    print("\n✅ Process completed successfully!")

if __name__ == "__main__":
    main()
