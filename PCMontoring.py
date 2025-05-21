import psutil
import time
import logging
import os

# --- Configuration ---
LOG_FILE = "system_performance.log"
MONITOR_INTERVAL_SECONDS = 5  # How often to log data (in seconds)
LOG_LEVEL = logging.INFO    # Set to logging.DEBUG for more detailed messages

# --- Setup Logging ---
# Ensure the log directory exists if you want to put it in a subdirectory
# For simplicity, we'll log to the current directory.
logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print(f"Starting system performance monitoring. Data will be logged to '{LOG_FILE}' every {MONITOR_INTERVAL_SECONDS} seconds.")
print("Press Ctrl+C to stop the monitoring.")

def get_system_metrics():
    """
    Fetches the current CPU and memory usage.
    Returns a dictionary containing 'cpu_percent' and 'memory_percent'.
    """
    try:
        cpu_percent = psutil.cpu_percent(interval=1) # interval=1 blocks for 1 second to get a meaningful CPU percentage
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        return {"cpu_percent": cpu_percent, "memory_percent": memory_percent}
    except Exception as e:
        logging.error(f"Error fetching system metrics: {e}")
        return None

def monitor_and_log():
    """
    Continuously monitors system performance and logs the data.
    """
    try:
        while True:
            metrics = get_system_metrics()
            if metrics:
                log_message = (
                    f"CPU Usage: {metrics['cpu_percent']:.2f}% | "
                    f"Memory Usage: {metrics['memory_percent']:.2f}%"
                )
                logging.info(log_message)
                # print(log_message) # Uncomment to also print to console
            time.sleep(MONITOR_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        logging.info("System performance monitoring stopped.")
    except Exception as e:
        logging.critical(f"An unhandled error occurred: {e}")

if __name__ == "__main__":
    # Check if psutil is installed
    try:
        import psutil
    except ImportError:
        print("The 'psutil' library is not installed.")
        print("Please install it using: pip install psutil")
        exit(1)

    monitor_and_log()
