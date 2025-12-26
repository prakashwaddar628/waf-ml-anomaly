def explain(anomaly, baseline):
    endpoint = anomaly["endpoint"]
    r = anomaly["record"]
    base = baseline[endpoint]

    reasons = []

    if r["response_time_ms"] > base["avg_rt"] + 2 * base["std_rt"]:
        reasons.append("response time unusually high")

    if r["request_size"] > base["avg_size"] + 2 * base["std_size"]:
        reasons.append("request size unusually large")

    explanation = (
        f"Anomaly detected on {endpoint}: "
        + ", ".join(reasons)
        + f" (confidence score: {anomaly['score']})"
    )

    return explanation
