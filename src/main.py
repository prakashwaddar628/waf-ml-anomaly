from ingestion.log_reader import read_logs
from features.feature_builder import build_features
from detection.baseline import compute_baseline
from detection.anomaly_detector import detect_anomalies
from explanation.explainer import explain
from policy.rule_recommender import recommend_rule

def main():
    print(">>> Program started")

    logs = read_logs("data/sample_logs.json")
    print(f">>> Logs loaded: {len(logs)}")

    grouped_features = build_features(logs)
    print(f">>> Groups created: {len(grouped_features)}")
    print(">>> Group keys:", grouped_features.keys())

    baseline = compute_baseline(grouped_features)
    print(f">>> Baselines computed: {len(baseline)}")
    print(">>> Baseline keys:", baseline.keys())

    anomalies = detect_anomalies(grouped_features, baseline)
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
