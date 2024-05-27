import socket
import threading
import pyaudio
import struct
import pickle
import time
import inspect
import ctypes

CHUNK = 1024
FORMAT = pyaudio.paInt16    # 格式
CHANNELS = 2    # 输入/输出通道数
RATE = 44100    # 音频数据的采样频率
RECORD_SECONDS = 0.5    # 记录秒


class Audio_Server(threading.Thread):
    def __init__(self, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = ('', port)
        self.version = version
        self.sock = None
        self.conn = None
        self.stream = None
        self.p = pyaudio.PyAudio()  # 实例化PyAudio, 并于下面设置portaudio参数
        self.setup_socket()

    def setup_socket(self):
        if self.version == 4:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __del__(self):
        self.close()

    def close(self):
        if self.conn:
            self.conn.close()
        if self.sock:
            self.sock.close()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def run(self):
        print("Audio server starts...")
        self.sock.bind(self.ADDR)
        self.sock.listen(1)
        self.conn, addr = self.sock.accept()
        print("Remote Audio client successfully connected...")
        data = b""
        payload_size = struct.calcsize("L")
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  output=True,
                                  frames_per_buffer=CHUNK)
        while True:
            try:
                while len(data) < payload_size:
                    data += self.conn.recv(81920)
                packed_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("L", packed_size)[0]
                while len(data) < msg_size:
                    data += self.conn.recv(81920)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frames = pickle.loads(frame_data)
                for frame in frames:
                    self.stream.write(frame, CHUNK)
            except Exception as e:
                print(f"Audio server error: {e}")
                break
        self.close()


class Audio_Server(threading.Thread):
    def __init__(self, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = ('', port)
        self.version = version
        self.sock = None
        self.conn = None
        self.stream = None
        self.p = pyaudio.PyAudio()  # 实例化PyAudio, 并于下面设置portaudio参数
        self.setup_socket()

    def setup_socket(self):
        if self.version == 4:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __del__(self):
        self.close()

    def close(self):
        if self.conn:
            self.conn.close()
        if self.sock:
            self.sock.close()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def run(self):
        print("Audio server starts...")
        try:
            self.sock.bind(self.ADDR)
            self.sock.listen(1)
            self.conn, addr = self.sock.accept()
            print("Remote Audio client successfully connected...")
            data = b""
            payload_size = struct.calcsize("L")
            self.stream = self.p.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      output=True,
                                      frames_per_buffer=CHUNK)
            while True:
                while len(data) < payload_size:
                    data += self.conn.recv(81920)
                packed_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("L", packed_size)[0]
                while len(data) < msg_size:
                    data += self.conn.recv(81920)
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frames = pickle.loads(frame_data)
                for frame in frames:
                    self.stream.write(frame, CHUNK)
        except Exception as e:
            print(f"Audio server error: {e}")
        finally:
            self.close()


class Audio_Client(threading.Thread):
    def __init__(self, ip, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = (ip, port)
        self.version = version
        self.sock = None
        self.stream = None
        self.p = pyaudio.PyAudio()
        self.setup_socket()
        print("Audio client starts...")

    def setup_socket(self):
        if self.version == 4:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __del__(self):
        self.close()

    def close(self):
        if self.sock:
            self.sock.close()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def run(self):
        while True:
            try:
                self.sock.connect(self.ADDR)
                break
            except Exception as e:
                print(f"Audio client connection error: {e}")
                time.sleep(3)
                continue
        print("Audio client connected...")
        try:
            self.stream = self.p.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      frames_per_buffer=CHUNK)
            while self.stream.is_active():
                frames = []
                for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = self.stream.read(CHUNK)
                    frames.append(data)
                senddata = pickle.dumps(frames)
                self.sock.sendall(struct.pack("L", len(senddata)) + senddata)
        except Exception as e:
            print(f"Audio client error: {e}")
        finally:
            self.close()

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

if __name__ == '__main__':
    au = Audio_Server(4567, 4)
    au1 = Audio_Client('192.168.31.90', 4568, 4)
    re = threading.Thread(target=au.run)
    re1 = threading.Thread(target=au1.run)
    re.start()
    re1.start()
    time.sleep(8)
    print('sleep over!')
    stop_thread(re)
    stop_thread(re1)

