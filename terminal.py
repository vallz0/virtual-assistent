import os
import ctypes

class Terminal:
    @staticmethod
    def resize(width: int, height: int) -> None:
        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        class SMALL_RECT(ctypes.Structure):
            _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
                        ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        buffer_size = COORD(width, height)
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, buffer_size)
        window_size = SMALL_RECT(0, 0, width - 1, height - 1)
        ctypes.windll.kernel32.SetConsoleWindowInfo(handle, ctypes.c_bool(True), ctypes.byref(window_size))

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
