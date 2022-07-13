from pymem import *
from pymem.process import *
from tkinter import *
import keyboard

name = 'Venom AssaultCube'
win = Tk()
win.geometry('400x200')
win.wm_attributes('-alpha',0.5)
win.configure(bg='black')
win.overrideredirect(1)
win.wm_attributes('-topmost',1)
def move(event):
    x,y = win.winfo_pointerxy()
    win.geometry(f'+{x}+{y}')
win.bind('<B1-Motion>',move)
title = Label(win,text=name,font=('Josefin Sans',20),fg='purple',bg='black').pack()
mem = Pymem('ac_client.exe')
module = module_from_name(mem.process_handle, "ac_client.exe").lpBaseOfDll

def getPointerAddr(base,offsets):
    addr = mem.read_int(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr

def Ammo():
    ammooffsets = [0x34C, 0x14, 0x218, 0x14, 0x4]
    mem.write_int(getPointerAddr(module + 0x00192414, ammooffsets), 180000)

def Health():
    healthoffsets = [0x54, 0x468, 0x9C, 0x134, 0x688]
    mem.write_int(getPointerAddr(module + 0x0017A85C, healthoffsets), 180000)


ammohack = Button(win,text='Ammo Hack',font=('Josefin Sans',10),fg='purple',bg='black',command=Ammo).pack()
healthhack = Button(win,text='Health Hack',font=('Josefin Sans',10),fg='purple',bg='black',command=Health).pack()
win.mainloop()
