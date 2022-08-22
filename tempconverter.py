'''python program to convert temperature in celsius to kelvin usng tkinter gui''' 
from distutils.cmd import Command
import tkinter 
from tkinter import  ttk

llblue = '#00e5ff'
class Democustom:
    '''trying custom tkinter'''
    def changeText(self):
        try:
            temp = float(self.enc.get())
            val = self.combo.get()
            if val == 'kelvin': 
                temp = temp + 273.15
                self.lbk['text']= str(temp)+'*K'
            elif val == 'fahrenheit':
                temp = (9*temp)/5 + 32
                self.lbk['text']= str(temp)+'F' 
        except Exception as e:
            dis = 'Invalid Entry'
            self.lbk['text']=dis

    def clearText(self):
        self.lbk['text']=''
        self.enc.delete(0, tkinter.END)

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.geometry("500x300")
        self.window.title("converting temperatures")
        self.window.grid()
        self.lbc = tkinter.Label(self.window, text="Enter temperature( *C):", font=("arial", 10))
        self.enc = tkinter.Entry(self.window, width=40)
        self.lbk = tkinter.Label(self.window, text=" ", font=("arial", 10)) 
        self.combo = ttk.Combobox(self.window, width=35)
        self.combo['values'] = ('kelvin', 'fahrenheit')
        self.combo.current(0) 
        self.button = tkinter.Button(self.window, text="convert", width=30, bg=llblue, command=self.changeText)
        self.button_clear = tkinter.Button(self.window, text="clear", width=30, bg=llblue, command=self.clearText)
        self.lbcombo = tkinter.Label(self.window, text="Choose convertion:", font=("arial", 10))
        self.lbc.grid(row=1, column=0, padx=5, pady=5)
        self.enc.grid(row=1, column= 1, padx=5, pady=5)
        self.lbcombo.grid(row=2, column=0)
        self.combo.grid(row=2, column=1, padx=5, pady=5)
        self.button.grid(row=3, column=1, padx=5, pady=5)
        self.button_clear.grid(row=4, column=1, padx=5, pady=5)
        self.lbk.grid(row=5, column=1, padx=5, pady=5)
        self.window.mainloop()

def main():
    Democustom()

main()
