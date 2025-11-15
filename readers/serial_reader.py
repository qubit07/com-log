
import serial
from readers.interfaces import SerialReaderInterface

class SerialReader(SerialReaderInterface):
    def __init__(self, port, baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def read_line(self):
        if self.ser.is_open:
            return self.ser.readline().decode('utf-8').strip()
        else:
            raise ConnectionError("Serial port is not open.")

    def close(self):
        if self.ser.is_open:
            self.ser.close()