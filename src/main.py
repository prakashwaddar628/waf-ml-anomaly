from ingestion.log_reader import read_logs
from features.feature_builder import build_features
from detection.baseline import compute_baseline
from detection.anomaly_detector import detect_anomalies
from explanation.explainer import explain
from policy.rule_recommender import recommend_rule
import math

def main():
    print(">>> Program started")

    logs = read_logs("data/sample_logs.json")
    print(f">>> Logs loaded: {len(logs)}")

    # -------- SPLIT DATA --------
    split_index = math.floor(len(logs) * 0.7)
    baseline_logs = logs[:split_index]
    detection_logs = logs[split_index:]

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

    print(">>> Program finished")

if __name__ == "__main__":
    main()