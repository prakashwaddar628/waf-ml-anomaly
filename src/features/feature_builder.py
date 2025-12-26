from collections import defaultdict

def build_features(logs):
    """
    Groups records by (endpoint, client_ip) for client-aware baselining
    """
    grouped = defaultdict(list)

    for log in logs:
        key = (log["endpoint"], log["client_ip"])
        grouped[key].append({
            "response_time_ms": log["response_time_ms"],
            "request_size": log["request_size"],
            "status": log["status"]
        })

    return grouped