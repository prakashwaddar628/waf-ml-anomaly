def detect_anomalies(features):
    anomalies = []
    for f in features:
        if f['response_time_ms'] > 250 or f['request_size'] > 800:
            anomalies.append({
                "feature" : f,
                "score" : 0.8
            })
    return anomalies