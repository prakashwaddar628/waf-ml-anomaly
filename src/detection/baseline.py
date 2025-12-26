import statistics

def compute_baseline(grouped_features):
    """
    Computes baseline per (endpoint, client_ip)
    """
    baseline = {}

    for key, records in grouped_features.items():
        response_times = [r["response_time_ms"] for r in records]
        request_sizes = [r["request_size"] for r in records]

        if len(response_times) < 2:
            continue

        baseline[key] = {
            "avg_rt": statistics.mean(response_times),
            "std_rt": statistics.stdev(response_times),
            "avg_size": statistics.mean(request_sizes),
            "std_size": statistics.stdev(request_sizes)
        }

    return baseline
