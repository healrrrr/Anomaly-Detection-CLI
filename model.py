import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def preprocess_logs(log_file):
    # Read and parse log file into a DataFrame
    logs = []
    try:
        with open(log_file, 'r') as file:
            for line in file:
                #  format: timestamp,level,message,ip
                parts = line.strip().split(',')
                if len(parts) == 4:
                    timestamp, level, message, ip = parts
                    logs.append({
                        'level': level,
                        'message': message,
                        'message_length': len(message),
                        'ip_first_octet': int(ip.split('.')[0]) if ip else 0,
                        'is_error': 1 if level == 'ERROR' else 0
                    })
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file '{log_file}' not found")

    df = pd.DataFrame(logs)

    df['level_code'] = df['level'].astype('category').cat.codes

    # Features for anomaly detection
    features = ['message_length', 'ip_first_octet', 'is_error', 'level_code']
    X = df[features].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return df, X_scaled

def detect_anomalies(X, contamination=0.1):
    # Train Isolation Forest model
    model = IsolationForest(contamination=contamination, random_state=42)
    predictions = model.fit_predict(X)

    # -1 indicates anomaly, 1 indicates normal
    return predictions

def get_anomalies(log_file, contamination=0.1):
    # Process logs and detect anomalies
    df, X = preprocess_logs(log_file)
    predictions = detect_anomalies(X, contamination)

    df['is_anomaly'] = predictions == -1

    # Return anomalies with original log details
    anomalies = df[df['is_anomaly']][['level', 'message', 'ip_first_octet', 'is_error']]
    return df, anomalies

def get_anomaly_counts(df):
    # Count normal vs anomalous logs for visualization
    total = len(df)
    anomalous = len(df[df['is_anomaly']])
    return total - anomalous, anomalous
