# coding: utf-8
from socketIO_client import SocketIO
from lock import RPiLock
import pigpio

SERVER, PORT = '52.43.75.183', 8000


def main():
    rpi_lock = RPiLock(pigpio.pi(), SocketIO(SERVER, PORT))
    rpi_lock.listen_to_signal()
    rpi_lock.io_client.wait()

if __name__ == '__main__':
    main()
