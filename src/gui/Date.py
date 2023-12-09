from __future__ import print_function
import ttkbootstrap as tb
import tkinter as tk
from ttkbootstrap.constants import *
import datetime
from typing import List
from src.config import *
from src.gui.Button import ClearButton
from src.data import Widget


class LabelDateEntry:
   def __init__(self, master:tb.Frame=None, 
                label_text:str="Label Date Entry", 
                row:int=0, column:int=0):
      self.master = master
      self.label = tb.Label(master, text=label_text, font=FONT)
      self.label.grid(row=row, column=column, pady=12, padx=12, sticky="nw")

      self.calender = tb.DateEntry(master, dateformat=DATE_FORMAT)
      self.calender.grid(row=row, column=column+1, pady=12, padx=12,sticky="nw")
      
      # self.string_var = tb.StringVar(value=datetime.datetime.now().strftime(DATE_FORMAT))
      self.string_var = tb.StringVar(value="")
      self.string_var.trace("w", lambda name, index, mode, sv=self.string_var: self.on_date_pick(sv))
      self.calender.entry.configure(textvariable=self.string_var)

      self.date_ref = {"Y": None, "m": None, "d": None}
      for i, element in enumerate(DATE_FORMAT_LIST):
         self.date_ref[element] = i

      self.date_frame = tb.Frame(master)
      self.date_frame.grid(row=row, column=column+1, pady=12, padx=12, sticky="nw")

      self.entry_type = DateEntryType(self.date_frame)
      self.entry_type.grid(row=0, column=0, pady=2, padx=0, sticky="nw")
      self.entry_type.set_date(self.get_text())
      for entry in self.entry_type.get_entries():
         entry.bind('<KeyRelease>', lambda e: self.on_date_type(e.widget))

   def get_label(self):
      return self.label

   def get_entry(self):
      return self.calender.entry
   
   def get_btn(self):
      return self.calender.button
   
   def get_calender(self):
      return self.calender
   
   def get_text(self):
      # print(self.calender.entry.get())
      return self.calender.entry.get()
   
   def set_date(self, text:str):
      is_real = check_real_date(text)
      if is_real:
         self.string_var.set(text)
   
   def on_date_pick(self, sv:tb.StringVar):
      date = sv.get()
      print("Date picked: ", date)
      self.entry_type.set_date(date)
   
   def on_date_type(self, widget:tk.Entry):
      ref = self.entry_type.get_entries_ref()[widget]
      date = self.entry_type.get_text()
      print("Date typed: ", date, ref)
      self.set_date(date)

   def clear_text(self):
      self.calender.entry.delete(0, tb.END)
      self.entry_type.set_date("")

   def add_clear_btn(self, row, column):
        self.clear_btn = ClearButton(self.master, self, row, column+2)


class DateEntryType(tb.Frame, Widget.Validator):
   def __init__(self, master:tb.Frame=None, **kwargs):
      tb.Frame.__init__(self, master, **kwargs)
      Widget.Validator.__init__(self, master)
      self.master = master
      self.date_format_ref = {
         "width": {"Y": 5, "m": 3, "d": 3},
         "num_char": {"Y": 4, "m": 2, "d": 2} }
      
      self.entry_1 = tb.Entry(self, width=self._get_ref("width", 0), font=FONT, justify="center", validate="key", validatecommand=(self.validate("number"), '%P'))     # year
      self.label_1 = tb.Label(self, text='-', font=(40), justify="center")
      self.entry_2 = tb.Entry(self, width=self._get_ref("width", 1), font=FONT, justify="center", validate="key", validatecommand=(self.validate("number"), '%P'))     # month
      self.label_2 = tb.Label(self, text='-', font=(40), justify="center")
      self.entry_3 = tb.Entry(self, width=self._get_ref("width", 2), font=FONT, justify="center", validate="key", validatecommand=(self.validate("number"), '%P'))     # day

      self.entry_1.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
      self.label_1.grid(row=0, column=1, padx=2, pady=0, sticky="nsew") 
      self.entry_2.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
      self.label_2.grid(row=0, column=3, padx=2, pady=0, sticky="nsew")
      self.entry_3.grid(row=0, column=4, padx=0, pady=0, sticky="nsew")

      self.entries = [self.entry_1, self.entry_2, self.entry_3]
      self.entries_ref = {}
      for i, entry in enumerate(self.entries):
         self.entries_ref[entry] = DATE_FORMAT_LIST[i]
      self.entry_1.bind('<KeyRelease>', lambda e: self._check(0))
      self.entry_2.bind('<KeyRelease>', lambda e: self._check(1, self._get_ref("num_char", 1)))
      self.entry_3.bind('<KeyRelease>', lambda e: self._check(2, self._get_ref("num_char", 2)))

   def _backspace(self, entry:tb.Entry):
      cont = entry.get()
      entry.delete(0, tb.END)
      entry.insert(0, cont[:-1])

   def _check(self, index:int, size:int):
      print("Check: ", index, size)
      entry = self.entries[index]
      next_index = index + 1
      next_entry = self.entries[next_index] if next_index < len(self.entries) else None
      data = entry.get()

      if len(data) > size or not data.isdigit():
         self._backspace(entry)
      if len(data) >= size and next_entry:
         next_entry.focus()

   def _get_ref(self, type="width", index=0):
      return self.date_format_ref[type][DATE_FORMAT_LIST[index]]

   def set_date(self, date:str):
      is_real_date = check_real_date(date)
      if is_real_date:
         date_list = date.split("/")
         # print("Set date: ", date_list)
         for i, entry in enumerate(self.entries):
            entry.delete(0, tb.END)
            if date_list == [""]:
               continue
            entry.insert(0, date_list[i])

   def get_entries(self) -> List[tb.Entry]:
      return self.entries

   def get_text(self):
      text_list = [e.get() for e in self.entries]
      text = '/'.join(text_list)
      return text
   
   def get_entries_ref(self):
      return self.entries_ref

def check_real_date(date:str):
      # yyyy/mm/dd
      date_list = date.split("/")
      if date_list == [""]:
         return True
      for i, element in enumerate(date_list):
         if not element.isdigit():
            return False
         if i == 0:
            if len(element) != 4:
               print("ERROR: Date format must be: yyyy/mm/dd")
               return False
            elif int(element) < 0 or int(element) > 9999:
               print("Year is not valid")
               return False
         if i == 1:
            if len(element) != 2:
               print("ERROR: Date format must be: yyyy/mm/dd")
               return False
            elif int(element) < 1 or int(element) > 12:
               print("Month is not valid")
               return False
         if i == 2:
            if len(element) != 2:
               print("ERROR: Date format must be: yyyy/mm/dd")
               return False
            elif int(element) < 1 or int(element) > 31:
               print("Day is not valid")
               return False
      return True

def main():
   app = tb.Window()
   app.title("Button")
   app.geometry("500x500")
   new_btn = LabelDateEntry(app, "button", 0, 0)
   app.mainloop()

if __name__ == "__main__":
   main()
   # print(check_real_date("2021/02/29"))