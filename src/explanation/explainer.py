def explain(anomaly):
    endpoint = anomaly["endpoint"]
    client_ip = anomaly["client_ip"]
    reasons = anomaly["reasons"]
    score = anomaly["score"]

    explanation = (
        f"Anomaly detected for client {client_ip} on endpoint {endpoint}: "
        + ", ".join(reasons)
        + f" (confidence score: {score})"
    )

    return explanation