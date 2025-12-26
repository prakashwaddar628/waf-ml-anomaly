from collections import defaultdict

def build_features(logs):
    grouped = defaultdict(list)

    for log in logs:
        endpoint = log["endpoint"]
        grouped[endpoint].append({
            "response_time_ms": log["response_time_ms"],
            "request_size": log["request_size"],
            "status": log["status"]
        })

    return grouped
