def detect_anomalies(grouped_features, baseline):
    anomalies = []

    for key, records in grouped_features.items():
        if key not in baseline:
            continue

        endpoint, client_ip = key
        base = baseline[key]

        for r in records:
            score = 0
            reasons = []

            # Dynamic thresholding
            rt_threshold = (
                base["avg_rt"] + 2 * base["std_rt"]
                if base["std_rt"] > 0
                else base["avg_rt"] * 1.5
            )

            size_threshold = (
                base["avg_size"] + 2 * base["std_size"]
                if base["std_size"] > 0
                else base["avg_size"] * 1.5
            )

            if r["response_time_ms"] > rt_threshold:
                score += 0.5
                reasons.append("response time unusually high")

            if r["request_size"] > size_threshold:
                score += 0.5
                reasons.append("request size unusually large")

            if score >= 0.5:
                anomalies.append({
                    "endpoint": endpoint,
                    "client_ip": client_ip,
                    "record": r,
                    "score": score,
                    "reasons": reasons
                })

    return anomalies