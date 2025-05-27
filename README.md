# CLI Anomaly Detection Tool for System Logs

A Python-based command-line tool for detecting anomalies in system log files using the Isolation Forest algorithm. It helps identify unusual patterns—such as unauthorized access attempts or suspicious IP addresses—making it useful for IT operations, DevOps, and cybersecurity monitoring.

## Features

* Analyzes log files for anomalies based on message length, log level, and IP address.
* Uses scikit-learn's Isolation Forest for unsupervised anomaly detection.
* Supports customizable anomaly thresholds via the CLI (e.g., `--contamination 0.2`).
* Displays results for easy visualization.

## Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/healrrrr/Anomaly-Detection-CLI.git>
   cd log_anomaly_detector
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Make sure Python 3.7 or higher is installed.

## Usage

Run the tool with a log file:

```bash
python anomaly_detector.py sample_log.txt
```

Customize the anomaly threshold (recommended range: 0.01–0.5):

```bash
python anomaly_detector.py sample_log.txt --contamination 0.2
```

## Example Output

```bash
Detected Anomalies:
- Level: ERROR | Message: Unauthorized access | IP starts with: 10.x.x.x

Summary: 6 normal logs, 1 anomaly detected

Anomaly Distribution Chart:
Normal   : #################### (6)
Anomalies: ### (1)
```

## Expected Log Format

Logs should be in the following comma-separated format:

```
timestamp,level,message,ip
```

Example (`sample_log.txt`):

```
2025-05-23 08:00:01,INFO,User login,192.168.1.1
2025-05-23 08:00:02,ERROR,Failed login attempt,192.168.1.2
```

## Project Structure

* `detect.py` – CLI interface and entry point.
* `model.py` – Core logic for log parsing and anomaly detection.
* `sample_log.txt` – Sample input log file.
* `requirements.txt` – Python dependency list.


## License

This project is licensed under the MIT License.
