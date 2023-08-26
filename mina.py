import tkinter as tk
import time
import colorsys
def rainbow_text():
    global current_color_index
    hue = current_color_index / 60.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color_code = "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))
    label.config(fg=color_code)
    current_color_index = (current_color_index + 1) % 360
    root.after(50, rainbow_text)
root = tk.Tk()
root.geometry('1920x1080')
root.overrideredirect(True)
root.config(bg='#000000')
root.attributes("-alpha", 1)
root.wm_attributes("-topmost", 1)
root.attributes('-transparentcolor', '#000000', '-topmost', 1)
root.resizable(False, False)
label = tk.Label(root, text="AutoClicker\nAimAssist\nReach\nSprint", bg="black", fg="#FFFFFF", font=("Arial", 15), bd=0, justify='left')
label.place(x=0, y=0)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = screen_width // 2
center_y = screen_height // 2
current_color_index = 0
rainbow_text()
root.mainloop()
