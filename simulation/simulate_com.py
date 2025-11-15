from queue import Queue
import time
from readers.interfaces import SerialReaderInterface

class SerialReaderMock(SerialReaderInterface):
    def __init__(self, queue: Queue):
        self.queue = queue

    def read_line(self) -> str:
        if not self.queue.empty():
            return self.queue.get()
        return None

    def close(self) -> None:
        print("Simulation closed")

def simulate_logs(queue: Queue):
    simulated_logs = [
        "[INFO] System initialized successfully",
        "[DEBUG] Reading sensor data: temperature=23.5C, humidity=45%",
        "[WARN] Sensor 2 response delayed",
        "[INFO] Sensor 1 data processed",
        "[ERROR] Failed to read sensor 3: timeout",
        "[DEBUG] Retry reading sensor 3",
        "[INFO] Sensor 3 data received: 19.8C",
        "[INFO] All sensors updated",
        "[WARN] High temperature detected: 75C",
        "[DEBUG] Activating cooling system",
        "[INFO] Cooling system activated",
        "[ERROR] Cooling system fan error",
        "[INFO] Attempting fan reset",
        "[INFO] Fan reset successful",
        "[DEBUG] Monitoring sensors..."
    ]

    while True:
        for line in simulated_logs:
            queue.put(line)
            print(f"Sent: {line}")
            time.sleep(1)   # Simulate delay between log entries
        time.sleep(5)  # Pause before repeating the logs
