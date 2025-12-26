def recommend_rule(anomaly):
    f = anomaly["feature"]
    return {
        "action": "RATE_LIMIT",
        "endpoint": f["endpoint"],
        "confidence": "HIGH",
        "reason": "Repeated abnormal request pattern"
    }