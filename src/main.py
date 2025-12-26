from ingestion.log_reader import read_logs
from features.feature_builder import build_features
from detection.anomaly_detector import detect_anomalies
from explanation.explainer import explain
from policy.rule_recommender import recommend_rule

def main():
    logs = read_logs("data/sample_logs.json")
    features = build_features(logs)
    anomalies = detect_anomalies(features)

    for anomaly in anomalies:
        explanation = explain(anomaly)
        rule = recommend_rule(anomaly)

        print("\n=== ANOMALY DETECTED ===")
        print(explanation)
        print("Recommended Rule:", rule)

if __name__ == "__main__":
    main()
