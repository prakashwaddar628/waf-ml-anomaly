def recommend_rule(anomaly):
    endpoint = anomaly["endpoint"]
    score = anomaly["score"]

    if score >= 1.0:
        action = "RATE_LIMIT"
        confidence = "HIGH"
    else:
        action = "MONITOR"
        confidence = "MEDIUM"

    return {
        "action": action,
        "endpoint": endpoint,
        "confidence": confidence,
        "reason": "Behavior deviates significantly from learned baseline"
    }
