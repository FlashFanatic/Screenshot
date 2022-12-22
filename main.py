import sys
import time
import win32gui
from PIL import ImageGrab
from pytesseract import image_to_string, pytesseract

hwnd = win32gui.FindWindow(None, r'ninite')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)
time.sleep(0.1)
image = ImageGrab.grab(dimensions)
path_to_tesseract = r'tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
text = image_to_string(image)
print(text)
time.sleep(0.1)
sys.exit()
