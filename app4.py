#------------Simple Music player =============
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from pygame import mixer
import time
import threading
from random import randrange
import os

root = Tk()
root.title('Simple Music player')
root.geometry('400x400')
root.config(background = "#243")
root.resizable(False, False)
#root.iconbitmap('play.ico')




class music_player:
    level = 50
    load_times = 0
    def __init__(self):
        c_dir = os.getcwd()
        self.c_dir=c_dir
        os.system('cd / && cd %%temp%%')
        print(os.getcwd())
        temp_dir = os.getcwd()
        self.temp_dir= temp_dir
        os.chdir(c_dir)
        self.time = 0
        self.volume = 0.5
        self.real_songs = []
        self.shift =0
        file = None
        self.file = file
        self.ptimes=0
        mixer.init()
        mixer.music.set_volume(0.5)
        self.playing = 1
        self.infinity = 0
        self.search_music = "dir /a/b/s *.mp3 "
        self.store_search = ">>c:u"

    def color_picker(self):
        color = colorchooser.askcolor()
        color = color[1]
        root.config(bg=color)

    def load_folder(self):
        print(self.temp_dir)
        print(os.getcwd())
        Folder = filedialog.askdirectory()
        os.chdir('/')
        os.chdir(Folder)
        current = os.getcwd()
        print(current)



    def open_file(self):
        self.load_times+=1
        songs = filedialog.askopenfilenames()
        self.real_songs = []
        songs = list(songs)
        for song in songs:
            if song.endswith('.mp3') or song.endswith('.wav'):
                self.real_songs.append(song)
            else:
                continue
        for song in self.real_songs:
            print(song)

    def load_music(self):
        file = filedialog.askopenfile()
        file = file.name
        self.file = file

    def check_playing(self):
        playing = mixer.music.get_busy()
        while playing==1:
            time.sleep(1)
            playing =mixer.music.get_busy()
        return 'done'

    def play(self):
        if self.real_songs:
            for i in  range(len(self.real_songs)):
                mixer.music.load(self.real_songs[self.ptimes])
                song_name = self.real_songs[self.ptimes]
                song_name = song_name.split('/')
                song_name = song_name[-1]
                song_name = song_name.split('.')
                song_name = song_name[0]
                if self.ptimes==0:
                    print(song_name)
                    mixer.music.play()
                    playing = mixer.music.get_busy() 
                    play().check_playing(playing) 
                    self.playing = playing 
                    print('Song finished playing')
   
                if self.ptimes>=1:
                    print(song_name)
                    mixer.music.play()
                    playing = mixer.music.get_busy()  
                    play().check_playing(playing) 
                    print('Song finished playing')
                self.ptimes = self.ptimes+1
        else:
            if self.file:
                mixer.music.load(self.file)
                song_file = self.file.split('/')
                song_name = song_file[-1]
                song_name = song_name.split('.')
                song_name = song_name[0]
                print(song_name)
                mixer.music.play(-1)
            else:
                print("Ooops there is no song to play\n\nPlease load a new music \nor\n\nCreate a new playlist")

    def playi(self):
        if self.infinity==0:   
            mixer.music.load(self.file)
            song_file = self.file.split('/')
            song_name = song_file[-1]
            print(song_name)
            mixer.music.play(-1)
            playi.config(bg='red')
            self.infinity+=1
        else:
            playi.config(bg='blue')
            self.infinity-=1
            mixer.music.play(0)

    def pause(self):
        if self.time is 0:
            playing = mixer.music.get_busy()
            if playing is 1:
                mixer.music.pause()
                pause.config(bg='red')
                print('pause please wait')
                print(".................")
                self.time = self.time+1
        else:
            mixer.music.unpause()
            pause.config(bg='green')
            print("enjoy listeining")
            self.time = self.time-1

    def adjust_volume(self, level):
        if level:
            vlm = mixer.music.get_volume()
            if vlm>=0:
                volume_color = randrange(100, 999)
                volume_color = '#'+str(volume_color)
                volume.config(bg=volume_color)
                level = float(level)
                level = level/100
                mixer.music.set_volume(level)

    def next_(self):
        total = len(self.real_songs)
        if self.ptimes<total-1:
            self.ptimes=self.ptimes + 1
            mixer.music.stop()
            mixer.music.load(self.real_songs[self.ptimes])
            song_file = self.real_songs[self.ptimes].split('/')
            song_name = song_file[-1]
            song_name = song_name.split('.')
            song_name = song_name[0]
            print(song_name)
            mixer.music.play(-1)
            
    def back(self):
        if self.ptimes!=0:
            self.ptimes=self.ptimes - 1
            mixer.music.stop()
            mixer.music.load(self.real_songs[self.ptimes])
            song_file = self.real_songs[self.ptimes].split('/')
            song_name = song_file[-1]
            song_name = song_name.split('.')
            song_name = song_name[0]
            print(song_name)
            mixer.music.play(-1)
player = music_player()

t3 = threading.Thread(target=player.check_playing)


play = Button(root, text = "play",width=15, command=player.play)
playi = Button(root, text = "O", width=5,bg='green', command=player.playi)
pause = Button(root, text = "Pause", width=12,bg='green', command=player.pause)
next_ = Button(root, text = "Next", width=15,bg='red', command=player.next_)
back = Button(root, text='Back', width=15, bg='#345', command=player.back)
volume = Scale(bg='#675', width=20, from_=0, to=100, orient = "vertical",command=player.adjust_volume)
volume.set(50)

class music(music_player):
    def __init__(self):
        play.place(x=150, y=355)
        playi.place(x=355, y=355)
        pause.place(x=160,y=330)
        volume.place(x=0, y = 275)
        next_.place(x = 250, y= 355)
        back.place(x = 50, y = 355)

player1 = music()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar)
filemenu2.add_command(label="Load Music", command=player.load_music)
filemenu2.add_command(label="Load playlist", command=player.open_file)
filemenu2.add_command(label="Load Folder with music",command= player.load_folder)
filemenu.add_command(label='Choose songs to play', command=player.open_file)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='background', command=player.color_picker)
menubar.add_cascade(label="Load", menu=filemenu2)
root.config(menu=menubar)


root.mainloop()

#Iris Coders
