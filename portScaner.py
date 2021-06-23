import socket
from threading import Thread, Lock
from queue import Queue
import argparse

N_THREADS = 100

q = Queue()

print_lock = Lock()


def port_scan(port):
    """
    Сканируйте порт по глобальной переменной `host`
    """
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{host:15}:{port:5} is closed  ", end='\r')
    else:
        with print_lock:
            print(f"{host:15}:{port:5} is open    ")
    finally:
        s.close()


def scan_thread():
    global q
    while True:
        # получаем номер порта из очереди
        worker = q.get()
        # сканировать этого порта
        port_scan(worker)
        # сообщает очереди, что сканирование этого порта
        # сделано
        q.task_done()


def main(host, ports):
    global q
    for t in range(N_THREADS):
        # для каждого потока запускаем его
        t = Thread(target=scan_thread)
        # когда мы устанавливаем daemon в true, этот поток завершится, когда закончится основной поток
        t.daemon = True
        # запускаем поток демона
        t.start()
    for worker in ports:
        # для каждого порта поместить этот порт в очередь
        # чтобы начать сканирование
        q.put(worker)
    # ждем завершения потоков (сканеров портов)
    q.join()


if __name__ == "__main__":
    # разбираем некоторые переданные параметры
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535",
                        help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range
    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)
    ports = [ p for p in range(start_port, end_port) ]
    main(host, ports)
