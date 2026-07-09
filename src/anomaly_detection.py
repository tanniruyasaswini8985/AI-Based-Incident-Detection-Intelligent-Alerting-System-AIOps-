from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest(contamination=0.2, random_state=42)

    features = data[['cpu_usage', 'memory_usage']]
    model.fit(features)

    data['anomaly'] = model.predict(features)

    data['anomaly_label'] = data['anomaly'].apply(
        lambda x: 'Anomaly' if x == -1 else 'Normal'
    )

    return data
