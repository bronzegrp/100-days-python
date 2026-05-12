import tkinter as tk
from PIL import Image, ImageTk

import time

random_char = 'timer goes here'
time.sleep(1)


window = tk.Tk()
window.geometry('800x600')
window.title('Pomodoro Timer')

#main title below ------------>

header = tk.Label(window)

header.config(text='Pomodoro Timer',font=('arial',25))

header.pack()

# timer below ----------------->

timer = tk.Label(window)

timer.config(text=f'{random_char}',font=('georgia',20))

timer.place(x=300,y=300)


























print('window ran')


window.mainloop()
