import time
from PIL import ImageGrab
from pynput.keyboard import Listener, Key
import pyautogui
import keyboard

fundo = (87, 87, 87)
branco = (255, 255, 255)
pos = (318, 623)

x, y = pyautogui.position()

def detectar_cor(screen):
  x, y = pyautogui.position()
  color = screen.getpixel((x, y))
  print(x," ", y ," - ",color, time.clock())
  screen = ImageGrab.grab()
  if(screen.getpixel(pos) == fundo):
    click()

def click():
  pyautogui.click(pos)

while True:
  detectar_cor(screen = ImageGrab.grab())
