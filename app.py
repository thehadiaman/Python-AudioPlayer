from pygame import mixer
from tkinter import *
from tkinter import filedialog

app = Tk()
app.title('Audio Player')
app.geometry('100x100+570+200')
app.maxsize(height=120, width=230)
app.minsize(height=120, width=230)


def selectFile():
    file = filedialog.askopenfile(mode='r', filetypes=[('AudioFile', '*.mp3')])
    global filePath
    filePath = str(file).split("'")[1]
    try:
        playAudio()
    except:
        pass


def changeText(text):
    if text == 'play':
        return 'pause'
    if text == 'pause':
        return 'play'


def playStop():
    playBtn.config(text=changeText(playBtn.config('text')[4]))
    if playBtn.config('text')[4] == 'pause':
        mixer.music.unpause()
    else:
        if playBtn.config('text')[4] == 'play':
            mixer.music.pause()


x = 0.5


def audioINC(y):
    mixer.music.set_volume(y + 0.1)
    global x
    x += 0.1


def audioDEC(y):
    mixer.music.set_volume(y - 0.1)
    global x
    x -= 0.1


def playAudio():
    try:
        mixer.init()
        mixer.music.load(filePath)
        mixer.music.set_volume(x)
        playBtn.config(text='pause')
        mixer.music.play()
    except:
        pass


frame = Frame(app)
frame.place(x=35, y=20)

openBtn = Button(frame, text='OpenFile', command=selectFile, width=8).grid(row=0, column=1)

audioDec = Button(frame, text='-', command=lambda: audioDEC(x)).grid(row=1, column=0)
playBtn = Button(frame, text='...', command=playStop, width=8)
playBtn.grid(row=1, column=1)
audioInc = Button(frame, text='+', command=lambda: audioINC(x)).grid(row=1, column=2)
restartBtn = Button(frame, text='Restart', command=playAudio, width=8).grid(row=2, column=1)

app.mainloop()
