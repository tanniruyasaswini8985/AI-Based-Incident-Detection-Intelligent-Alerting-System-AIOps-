def print_summary(data):
    total = len(data)
    anomalies = len(data[data['anomaly'] == -1])

    print("\n===== SUMMARY =====")
    print(f"Total Records: {total}")
    print(f"Anomalies Detected: {anomalies}")
