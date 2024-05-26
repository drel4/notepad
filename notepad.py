import tkinter as tk
from tkinter import filedialog
import pygame
import threading
import sys
import os
import random

os.system('cls')


freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.music.set_volume(1.0)

audiodata = './notepad.xm'

class NotepadApp:
    def __init__(self, root, file_path=None):
        self.root = root
        self.root.title("Блокнот для чайников")
        
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Выход", command=self.exit_app)
        
        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Редактировать", menu=self.edit_menu)
        self.edit_menu.add_command(label="Копировать", command=self.copy_text)
        self.edit_menu.add_command(label="Вырезать", command=self.cut_text)
        self.edit_menu.add_command(label="Вставить", command=self.paste_text)
        self.edit_menu.add_command(label='Вставить "uwu"', command=self.uwu)
        self.edit_menu.add_command(label='Вставить "owo"', command=self.owo)
        self.edit_menu.add_command(label='Вставить ":3"', command=self.idkhowicannamethisfunction)
        
        self.fun_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Забавная менюшка", menu=self.fun_menu)
        self.fun_menu.add_command(label="Телеграм канал холиним шп (Спонсор)", command=self.sponsora)
        self.fun_menu.add_command(label="Doom в qiwi терминале", command=self.videoa)
        self.fun_menu.add_command(label="новый сереал шкебеде туалетов смотреть онлайн без смс и регистраций в 21337 году бесплатно платно 1488 9/11", command=self.videob)
        self.fun_menu.add_command(label=":3 (Отключено)", command=self.donothing) # self.openrandompica
        self.fun_menu.add_command(label="Замутить музыку", command=self.sndvol)
        self.fun_menu.add_command(label="Сменить музыку", command=self.custommusic)
        
        self.about_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Об блокноте", menu=self.about_menu)
        self.about_menu.add_command(label="Блокнот для чайников", command=self.donothing)
        self.about_menu.add_command(label="Версия: 1.1.1-git", command=self.donothing)
        self.about_menu.add_command(label="Сделал Drel4", command=self.donothing)
        self.about_menu.add_command(label="drel@zonerkin.xyz", command=self.donothing)
        self.about_menu.add_command(label="Дата последнего обновления блокнота: 26.05.2024", command=self.donothing)
        self.about_menu.add_command(label="Время последнего обновления блокнота: 20:40", command=self.donothing)

        # Если передан путь к файлу, открой его
        if file_path:
            self.open_file(file_path)
        
    def open_file(self, file_path=None):
        if not file_path:
            file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", text)
                
    def custommusic(self, music_path=None):
        if not music_path:
            music_path = filedialog.askopenfilename()
        if music_path:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)
        
    def donothing(self):
        asdasda = 123132
                
    def sponsora(self):
        os.system('start https://t.me/holinimshitpost')
        
    def videoa(self):
        os.system('start https://www.youtube.com/watch?v=ojZBKdp4nno')
       
    def videob(self):
        os.system('start https://www.youtube.com/watch?v=zlsM5u5ZkMw')
                
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                text = self.text_area.get("1.0", "end-1c")
                file.write(text)
                
    def exit_app(self):
        self.root.quit()
        
    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        
    def uwu(self):
        self.text_area.insert("insert", 'uwu')
        
    def sndvol(self):
        os.system('start sndvol')
        
    def owo(self):
        self.text_area.insert("insert", 'owo')
        
    def idkhowicannamethisfunction(self):
        self.text_area.insert("insert", ':3')

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first", "sel.last")

    def paste_text(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())
        
try:
    # Проверка, был ли передан путь к файлу через аргумент командной строки
    file_path = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    musicdatatest = open('./notepad.xm', 'r')
except FileNotFoundError:
    os.system('start https://www.youtube.com/watch?v=VGSDYK2fBQE')
    sys.exit()
except Exception as e:
    print(f"Ошибка: {e}")
else:
    musicdatatest.close()

pygame.mixer.music.load(audiodata)
pygame.mixer.music.play(-1)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root, file_path)
    root.mainloop()
