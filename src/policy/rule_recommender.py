def recommend_rule(anomaly):
    endpoint = anomaly["endpoint"]
    client_ip = anomaly["client_ip"]
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
        "client_ip": client_ip,
        "confidence": confidence,
        "reason": "Client behavior deviates from its historical baseline"
    }