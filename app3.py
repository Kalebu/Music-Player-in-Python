#------------Simple Music player =============
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from pygame import mixer
import time
import threading

root = Tk()
root.title('Simple Music player')
root.geometry('400x400')
root.config(background = "#243")
root.resizable(False, False)
root.iconbitmap('play.ico')




class music_player:
    level = 50
    load_times = 0
    def __init__(self):
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

    def color_picker(self):
        color = colorchooser.askcolor()
        color = color[1]
        root.config(bg=color)


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
        mixer.music.load(self.file)
        song_file = self.file.split('/')
        song_name = song_file[-1]
        print(song_name)
        mixer.music.play(-1)

    def pause(self):
        if self.time is 0:
            playing = mixer.music.get_busy()
            if playing is 1:
                mixer.music.pause()
                print('pause please wait')
                print(".................")
                self.time = self.time+1
        else:
            mixer.music.unpause()
            print("enjoy listeining")
            self.time = self.time-1

    def adjust_volume(self, level):
        if level:
            vlm = mixer.music.get_volume()
            if vlm>=0:
                scroll = int(level)
                print(scroll)
                if scroll<=9:
                    volume_color = '#'+str(level)+'00'
                    print(volume_color)
                elif scroll==100:
                    volume_color="#111"
                    print(volume_color)
                else:
                    volume_color = '#'+str(level)+'0'
                    print(volume_color)
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
t3.start()



if player.load_times == 0:
    load = Button(root, text = "Load Music", width=15,bg='blue', command=player.load_music)
else:
    load = Button(root, text = "Load Music", width=15,bg='blue', command=player.open_file)
play = Button(root, text = "play",width=15, command=player.play)
playi = Button(root, text = "inifinitely", width=15,bg='green', command=player.playi)
pause = Button(root, text = "Pause", width=15,bg='red', command=player.pause)
next_ = Button(root, text = "Next", width=15,bg='red', command=player.next_)
back = Button(root, text='Back', width=15, bg='#345', command=player.back)
volume = Scale(bg='#675', width=18, from_=0, to=100, orient = "vertical",command=player.adjust_volume)
volume.set(50)

class music(music_player):
    def __init__(self):
        load.pack()
        play.place(x=150, y=350)
        playi.pack()
        pause.pack()
        volume.place(x=0, y = 275)
        next_.place(x = 250, y= 350)
        back.place(x = 50, y = 350)

player1 = music()



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Choose songs to play', command=player.open_file)
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='background', command=player.color_picker)
root.config(menu=menubar)


root.mainloop()

#Iris Coders