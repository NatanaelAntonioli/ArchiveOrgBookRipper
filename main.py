import time
import pyautogui
from PIL import Image
from pynput.keyboard import Key, Controller
import os

def make_photos():
    kb = Controller()
    time.sleep(5)

    for i in range (324):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(str(i) + ".png")
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(2)

def cut():
    vetor_arquivos = []

    for i in range(163):
        vetor_arquivos.append(i)

    for filename in os.listdir("fotos"):
        num = filename.replace(".png","")
        num = int(num)
        vetor_arquivos[num] = filename

    for i in vetor_arquivos:
        im = Image.open('fotos/' + i).convert('L')
        im = im.crop((377, 126, 1026, 663))
        im.save('cortado/' + str(i))

def merge():
    vetor_arquivos = []
    image_list = []
    capa = "nada"

    for i in range(163):
        vetor_arquivos.append(i)

    for filename in os.listdir("cortado"):
        num = filename.replace(".png","")
        num = int(num)
        vetor_arquivos[num] = filename

    for i in vetor_arquivos:
        im = Image.open('cortado/' + i)
        if i == "0.png":
            capa = im
        else:
            image_list.append(im)

    capa.save('livro.pdf', save_all=True, append_images=image_list)


merge()