import tkinter as tk
import ttkbootstrap as tb  
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from src.config import *
from src.gui.Button import ClearButton
from src.data import Widget

class LabelEntry(Widget.Validator):
   def __init__(self, master:tb.Frame=None, 
                label_text:str="Label Entry",
                row:int=0, column:int=0,
                dtype:str="str",
                **kwargs):
      Widget.Validator.__init__(self, master, **kwargs)
      self.master = master
      self.dtype = dtype
      self.label = tb.Label(master, text=label_text, font=FONT)
      self.label.grid(row=row, column=column, pady=12, padx=12, sticky="nw")

      self.entry_frame = tb.Frame(master)
      self.entry_frame.grid(row=row, column=column+1, pady=12, padx=0, sticky="nw")
      self.entry = tb.Entry(self.entry_frame, font=FONT, validate="key", validatecommand=(self.validate(dtype), "%P"))   
      self.entry.grid(row=0, column=0, pady=2, padx=0, sticky="nw")
      # self.entry.bind("<KeyRelease>", self.on_entry_change)
      
   def get_label(self):
      return self.label
   
   def get_entry(self):
      return self.entry
   
   def get_text(self):
      # print(self.entry.get())
      return self.entry.get()
   
   def on_entry_change(self, event):
      print(f"At [{self.label['text']}] entry: ", self.entry.get())
      # return self.entry.get()

   def clear_text(self):
      self.entry.delete(0, tk.END)

   def add_clear_btn(self, row, column):
        self.clear_btn = ClearButton(self.master, self, row, column+2)

def main():
   app = tb.Window()
   app.title("Button")
   app.geometry("500x500")
   new_btn = LabelEntry(app, "button", 0, 0)
   app.mainloop()

if __name__ == "__main__":
   main()