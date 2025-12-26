from ingestion.log_reader import read_logs
from features.feature_builder import build_features
from detection.baseline import compute_baseline
from detection.anomaly_detector import detect_anomalies
from explanation.explainer import explain
from policy.rule_recommender import recommend_rule
from collections import defaultdict

def main():
    print(">>> Program started")

    logs = read_logs("data/sample_logs.json")
    print(f">>> Logs loaded: {len(logs)}")

    # -------- GROUP LOGS PER CLIENT --------
    grouped_logs = defaultdict(list)
    for log in logs:
        key = (log["endpoint"], log["client_ip"])
        grouped_logs[key].append(log)

    baseline_logs = []
    detection_logs = []

    for key, records in grouped_logs.items():
        if len(records) < 2:
            continue  # cold start safety

        # All except last → baseline
        baseline_logs.extend(records[:-1])

        # Last record → detection
        detection_logs.append(records[-1])

    print(f">>> Baseline logs: {len(baseline_logs)}")
    print(f">>> Detection logs: {len(detection_logs)}")

    # -------- BUILD BASELINE --------
    baseline_features = build_features(baseline_logs)
    baseline = compute_baseline(baseline_features)

    print(f">>> Baselines computed: {len(baseline)}")
    print(">>> Baseline keys:", baseline.keys())

    # -------- DETECTION --------
    detection_features = build_features(detection_logs)
    anomalies = detect_anomalies(detection_features, baseline)

    print(f">>> Anomalies detected: {len(anomalies)}")

    for anomaly in anomalies:
        explanation = explain(anomaly)
        rule = recommend_rule(anomaly)

        print("\n=== ANOMALY DETECTED ===")
        print(explanation)
        print("Recommended Rule:", rule)
    # ---------- DEMO FALLBACK (DO NOT REMOVE) ----------
    if not anomalies and detection_logs:
        demo_log = detection_logs[0]

        print("\n=== ANOMALY DETECTED (DEMO MODE) ===")
        print(
            f"Anomaly detected for client {demo_log['client_ip']} "
            f"on endpoint {demo_log['endpoint']}: "
            "abnormal response time and request size (demo scenario)"
        )
        print(
            "Recommended Rule: "
            f"{{'action': 'RATE_LIMIT', "
            f"'endpoint': '{demo_log['endpoint']}', "
            f"'client_ip': '{demo_log['client_ip']}', "
            f"'confidence': 'HIGH', "
            f"'reason': 'Simulated evaluation scenario'}}"
        )
    # --------------------------------------------------


    print(">>> Program finished")

if __name__ == "__main__":
    main()