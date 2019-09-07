#------------Simple Music player =============
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Simple Music player')
root.geometry('150x110')
root.config(background = "#243")

def open_file():
    songs = ""
    real_songs = []
    songs = filedialog.askopenfilenames()
    songs = list(songs)
    for song in songs:
        if song.endswith('.mp3'):
            real_songs.append(song)
        else:
            continue
        for song in real_songs:
            print(song)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)
root.config(menu=menubar)


class music_player:
    def __init__(self):
        self.time = 0
        self.volume = 0.5
    def load_music(self):
        file = filedialog.askopenfile()
        file = file.name
        self.file = file
    def play(self):
        mixer.init()
        mixer.music.load(self.file)
        mixer.music.set_volume(0.5)
        mixer.music.play(1)
    def playi(self):
        mixer.init()
        mixer.music.load(self.file)
        mixer.music.set_volume(0.5)
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
    def vplus(self):
        vminus.config(bg='#111')
        vminus.pack()
        volume = mixer.music.get_volume()
        if volume<1:
            volume = volume + 0.1
            mixer.music.set_volume(volume)
        else:
            vplus.config(bg='red')
            vplus.pack()
    def vminus(self):
        vplus.config(bg='orange')
        vplus.pack()
        volume = mixer.music.get_volume()
        if volume>0:
            volume = volume - 0.1
            if volume>0:
                mixer.music.set_volume(volume)
            else:
                   vminus.config(bg='red')
                   vminus.pack()
         
        
player = music_player()
load = Button(root, text = "Load Music", width=20,bg='blue', command=player.load_music)
play = Button(root, text = "play",width=10, command=player.play)
playi = Button(root, text = "inifinitely", width=10,bg='green', command=player.playi)
pause = Button(root, text = "Pause", width=20,bg='red', command=player.pause)
vplus = Button(root, text = "V+", width=10,bg='orange', command=player.vplus)
vminus = Button(root, text = "V-", width=10,bg='#111' ,command=player.vminus)

class music(music_player):
    def __init__(self):
        load.pack()
        play.pack(side=LEFT)
        playi.pack(side=RIGHT)
        pause.pack()
        vplus.pack(side=LEFT)
        vminus.pack(side=RIGHT)

player1 = music()

root.mainloop()

#Iris Coders