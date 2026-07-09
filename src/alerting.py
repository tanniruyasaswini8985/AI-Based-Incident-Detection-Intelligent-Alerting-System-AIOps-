def generate_alerts(data):
    alerts = []

    for _, row in data.iterrows():
        if row['anomaly'] == -1:
            alert_message = (
                f"[ALERT] High resource usage detected at {row['timestamp']} "
                f"(CPU: {row['cpu_usage']}%, Memory: {row['memory_usage']}%)"
            )
            alerts.append(alert_message)

    return alerts
