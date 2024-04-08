import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def preview_gif():
    root = tk.Tk()

    
    root.title("My AI Assistant")

    
    icon_path = "E:\AI ASSISTANT\logo.ico"  
    root.iconbitmap(icon_path)

    
    canvas = tk.Canvas(root, width=400, height=300, bg="black")
    canvas.pack()

    
    gif_path = "E:/AI ASSISTANT/orb.gif" 
    gif = Image.open(gif_path)
    photo = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]


    label = tk.Label(canvas, bg="black")
    label.pack()

    def update_frame(frame):
        label.config(image=photo[frame])
        label.image = photo[frame]
        root.after(100, update_frame, (frame + 1) % len(photo))

    update_frame(0)


    text_label = tk.Label(canvas, text="Desktop AI Assistant", bg="black", fg="white", font=("Times New Roman", 48))
    text_label.pack()

    root.mainloop()

if __name__ == "__main__":
    preview_gif()
