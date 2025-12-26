def explain(anomaly):
    f = anomaly["feature"]
    explanation = (
        f"Unusual behavior detected on endpoint {f['endpoint']}: "
        f"response time {f['response_time_ms']}ms "
        f"and request size {f['request_size']} bytes exceed normal baseline."
    )
    return explanation