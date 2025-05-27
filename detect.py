import argparse
from model import get_anomalies, get_anomaly_counts

def main():
    # Set up CLI arguments
    parser = argparse.ArgumentParser(description="CLI Anomaly Detection Tool for System Logs")
    parser.add_argument("log_file", type=str, help="Path to log file")
    parser.add_argument("--contamination", type=float, default=0.1,
                       help="Anomaly threshold (0.0 to 0.5)", choices=[x/100 for x in range(1, 51)])
    args = parser.parse_args()

    try:
        # Detect anomalies
        df, anomalies = get_anomalies(args.log_file, args.contamination)

        # Display results
        if anomalies.empty:
            print("No anomalies detected.")
        else:
            print("\nDetected Anomalies:")
            for _, row in anomalies.iterrows():
                print(f"- Level: {row['level']} | Message: {row['message']} | IP starts with: {row['ip_first_octet']}.x.x.x")

        # Display simple stats
        normal_count, anomaly_count = get_anomaly_counts(df)
        print(f"\nSummary: {normal_count} normal logs, {anomaly_count} anomalies detected")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
