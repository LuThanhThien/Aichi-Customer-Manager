import ttkbootstrap as tb
from ttkbootstrap.constants import *
from typing import List, Any
from src.config import *

class ClearButton(tb.Button):
    def __init__(self, master:tb.Frame=None,
                 label_widget:Any=None,
                 row:int=0, column:int=0,
                 bootstyle="danger.link.TButton",
                 **kwargs):
        self.master =  master
        self.label_widget = label_widget
        self.clear_frame = tb.Frame(master)
        super().__init__(self.clear_frame, **kwargs)
        self.clear_frame.grid(row=row, column=column, pady=12, padx=0, sticky="nw")
        self.config(text="Clear", bootstyle=bootstyle, command=self.on_clear)
        self.grid(row=0, column=0, pady=0, padx=0, sticky="ne")
        self.master.rowconfigure(row, weight=1)
        
        # Bind events to show and hide the button
        # self.master.bind("<Enter>", self.show_button)
        # self.master.bind("<Leave>", self.hide_button)

    def show_button(self, event):
        self.config(text="Clear")

    def hide_button(self, event):
        self.config(text="         ")

    def on_clear(self):
        print("Clear button clicked")
        self.label_widget.clear_text()


class LabelRadioButton(tb.Radiobutton):
    def __init__(self, master:tb.Frame=None, 
                 label_text:str="Label Radio Button", 
                 buttons:List[str]=[], 
                 row:int=0, column:int=0, bpr:int=2, 
                 bootstyle:str="success", 
                 **kwargs):
        super().__init__(master, **kwargs)  
        self.master = master
        self.label = tb.Label(master, text=label_text, font=FONT)
        self.label.grid(row=row, column=column, pady=12, padx=12, sticky="nw")
        self.btn_frame = tb.Frame(master)
        self.btn_frame.grid(row=row, column=column+1, pady=5, padx=5, sticky="nw")
        self.btn_list = [None] * len(buttons)
        self.var_list = [tb.StringVar()] * len(buttons)
        radio_style = tb.Style()
        radio_style.configure("TRadiobutton", font=FONT)

        for i, b in enumerate(buttons):
            self.btn_list[i] = tb.Radiobutton(self.btn_frame, variable=self.var_list[i], bootstyle=bootstyle, text=b, value=b, style="TRadiobutton")
            self.btn_list[i].config(command=lambda text=b, var=self.var_list[i]: self.on_btn_click(text, var))
            self.btn_list[i].grid(row=i//bpr, column=i%bpr, pady=12, padx=12, sticky="nsew")
        self.clicked_btn = None # contains clicked button text        

    def on_btn_click(self, text:str, var:tb.StringVar):
        print("Clicked button: ", text)
        # if btn is in clicked_btn, deselect it
        if text == self.clicked_btn:
            self.clear_text()
        else:
            self.clicked_btn = text
        # print(self.clicked_btn)
        return self.clicked_btn

    def get_label(self):
        return self.label

    def get_btn(self):
        return self.btn_list
    
    def get_var(self):
        return self.var_list
    
    def get_text(self):
        # print("Clicked buttons: ", self.clicked_btn)
        return self.clicked_btn

    def clear_text(self):
        for var in self.var_list:
            var.set(None)
        self.clicked_btn = None

    def add_clear_btn(self, row, column):
        self.clear_btn = ClearButton(self.master, self, row, column+2)

class LabelCheckButton(tb.Checkbutton):
    def __init__(self, master:tb.Frame=None, 
                 label_text:str="Label Radio Button", 
                 buttons:List[str]=[], 
                 row:int=0, column:int=0, bpr:int=2, 
                 bootstyle:str="success", 
                 **kwargs):
        super().__init__(master, **kwargs)  
        self.master = master
        self.label = tb.Label(master, text=label_text, font=FONT)
        self.label.grid(row=row, column=column, pady=12, padx=12, sticky="nw")
        self.btn_frame = tb.Frame(master)
        self.btn_frame.grid(row=row, column=column+1, pady=5, padx=5, sticky="nw")
        self.btn_list = [None] * len(buttons)
        self.var_list = [None] * len(buttons)
        radio_style = tb.Style()
        radio_style.configure("TCheckbutton", font=FONT)

        for i, b in enumerate(buttons):
            self.var_list[i] = tb.IntVar()
            self.btn_list[i] = tb.Checkbutton(self.btn_frame, variable=self.var_list[i], bootstyle=bootstyle, text=b, style="TCheckbutton")
            self.btn_list[i].config(command=lambda text=b, var=self.var_list[i]: self.on_btn_click(text, var))
            self.btn_list[i].grid(row=i//bpr, column=i%bpr, pady=12, padx=12, sticky="nsew")
        self.clicked_list = [] # contains clicked buttons texts

    def on_btn_click(self, text, var):
        # print("Clicked button: ", text)
        # append to clicked_list 
        if var.get() == 0:
            self.clicked_list.remove(text)
        elif text not in self.clicked_list:
            self.clicked_list.append(text)
        # print(self.clicked_list)
        return self.clicked_list

    def get_label(self):
        return self.label

    def get_btn(self):
        return self.btn_list
    
    def get_var(self):
        return self.var_list
    
    def get_text(self):
        # print("Clicked buttons: ", self.clicked_list)
        return self.clicked_list

    def clear_text(self):
        for var in self.var_list:
            var.set(0)
        self.clicked_list = []

    def add_clear_btn(self, row, column):
        self.clear_btn = ClearButton(self.master, self, row, column+2)

def main() :
    app = tb.Window()
    app.title("Button")
    app.geometry("500x500")
    new_btn = LabelRadioButton(app, "button", ["Male", "Female"], 0, 0)
    var = new_btn.get_var()
    print(var)
    for v in var:
        print(v.get())
    btn = new_btn.get_btn()
    print(btn)
    label = new_btn.get_label()
    print(label)
    app.mainloop()

if __name__=="__main__":
    main()