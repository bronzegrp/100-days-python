import tkinter as tk
import time

random_char = input('test: ') #will display input in label below
time.sleep(1)


window = tk.Tk()
window.geometry('800x600')
window.title('Pomodoro Timer')

#main title below ------------>

header = tk.Label(window)

header.config(text='pomodoro',font=('arial',25))

header.pack()

# timer below ----------------->

timer = tk.Label(window)

timer.config(text=f'{random_char}',font=('georgia',20))

timer.pack()


























print('window ran')


window.mainloop()
