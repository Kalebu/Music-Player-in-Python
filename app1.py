#------------Simple Music player =============
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()

root.title('Simple Music player')
root.geometry('100x80')
root.config(background = "#243")

class music_player:
    def __init__(self):
        self.time = 0
    def load_music(self):
        file = filedialog.askopenfile()
        file = file.name
        self.file = file
    def play(self):
        mixer.init()
        mixer.music.load(self.file)
        mixer.music.play(-1)
    def pause(self):
        if self.time is 0:
            print(self.file)
            mixer.music.pause()
            print("paused... please wait")
            self.time = self.time+1
        else:

            mixer.music.unpause()
            print("unpaused.... enjoy listeining")
            self.time = self.time-1

player = music_player()
load = Button(root, text = "Load Music", width=20,bg='blue', command=player.load_music)
load.pack()
play = Button(root, text = "Play", width=20,bg='green', command=player.play)
play.pack()
pause = Button(root, text = "Pause", width=20,bg='red', command=player.pause)
pause.pack()

root.mainloop()
