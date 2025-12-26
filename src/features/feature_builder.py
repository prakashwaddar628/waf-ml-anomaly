def build_features(logs):
    features = []
    for log in logs:
        feature = {
            "endpoint" : log['endpoint'],
            "method" : log['method'],
            "status" : log['status'],
            "request_size" : log['request_size'],
            "response_time_ms" : log['response_time_ms'],
        }
        features.append(feature)
    return features