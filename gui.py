import tkinter as tk
from PIL import Image 

anim = None
root = tk.Tk()

file="E:\AI ASSISTANT\orb.gif"
info = Image.open(file)
frames= info.n_frames
print(frames)
im = [tk.PhotoImage(file=file, format=f"gif-index{i}" ) for i in range(frames)]

count = 0

def animation(count):
    global anim 
    im2 =im[count]
    gif_label.configure(image=im2)
    count +=1
    if count == frames:
        count = 0
    
    anim = root.after(50,animation(count))

def stop_animation():
    global anim
    root.after_cancel(anim)



gif_label = tk.Label(image="")
gif_label.pack()


start = tk.Button(text = "Start", command=lambda:animation(count))
start.pack()

stop = tk.Button(text= "Stop", command= stop_animation)
stop.pack()
