import pytest
from readers.serial_reader import SerialReader
from unittest.mock import patch



@patch('readers.serial_reader.serial.Serial')
def test_serial_reader_read_line(mock_serial):
    instance = mock_serial.return_value
    instance.is_open = True
    instance.readline.return_value = b'Test Line\n'

    reader = SerialReader(port='COM3')
    line = reader.read_line()

    assert line == 'Test Line'


@patch('readers.serial_reader.serial.Serial')
def test_serial_reader_close(mock_serial):
    instance = mock_serial.return_value
    instance.is_open = True

    reader = SerialReader(port='COM3')
    reader.close()

    instance.close.assert_called_once()