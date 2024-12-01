from tkinter import *
from tkinter import messagebox

def volumeUp():
   if root.volume_level >= 60:
      messagebox.showwarning("Error", "Max volume") 
   else:
      root.volume_level += 1
      print("Volume increase: ", root.volume_level)

def volumeDown():
   if root.volume_level <= 0:
      messagebox.showwarning("Error", "Min volume")
   else:
      root.volume_level -= 1
      print("Volume decrease: ", root.volume_level)

def turnOn():
   if root.device_state == "off":
      root.device_state = "on"
   else:
      root.device_state = "off"
   print("Device turned", root.device_state)

root = Tk()
root.volume_level = 50
root.device_state = "off"

on_button_photo = PhotoImage(file="turn.png")
photo = on_button_photo.subsample(10, 10)
turn_on = Button(root, image=photo, command=lambda: turnOn())
turn_on.pack()

turn_off = Button(root, text="OFF", command=root.quit)
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

vol_up = Button(root, text="+", command=lambda: volumeUp())
vol_up.pack()

vol_down = Button(root, text="-", command=lambda: volumeDown())
vol_down.pack()

root.mainloop()
