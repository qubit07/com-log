from abc import ABC, abstractmethod

class SerialReaderInterface(ABC):

    @abstractmethod
    def read_line(self) -> str:
        """Read a line from the serial interface."""
        raise NotImplementedError
    
    @abstractmethod
    def close(self) -> None:
        """Close the serial interface."""
        raise NotImplementedError