import ctypes
import time
from PIL import Image

def set_wallpaper(color):
    img = Image.new("RGB", (1920, 1080), color)
    img_path = f"{color}.bmp"
    img.save(img_path)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 3)

colors = ["red", "yellow", "green", "blue"]

try:
    while True:
        for color in colors:
            set_wallpaper(color)
            time.sleep(1)
except KeyboardInterrupt:
    print("Приложение остановлено.")