def detect_anomalies(endpoint_features, baseline):
    anomalies = []

    for endpoint, records in endpoint_features.items():
        if endpoint not in baseline:
            continue

        base = baseline[endpoint]

        for r in records:
            score = 0

            if r["response_time_ms"] > base["avg_rt"] + 2 * base["std_rt"]:
                score += 0.5

            if r["request_size"] > base["avg_size"] + 2 * base["std_size"]:
                score += 0.5

            if score >= 0.5:
                anomalies.append({
                    "endpoint": endpoint,
                    "record": r,
                    "score": score
                })

    return anomalies