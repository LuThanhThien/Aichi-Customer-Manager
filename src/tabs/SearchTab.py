from typing import Callable
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from src.config import *
from src.gui import Button, Date, Entry
from src.data import DataFrame

class Search():
   def __init__(self, master: tb.Frame, 
                search_callback:Callable[[pd.DataFrame], None]=None,
                add_callback:Callable[[pd.DataFrame], None]=None):
      # master.rowconfigure(0, weight=1)
      # master.columnconfigure(0, weight=1)
      self.master = master
      self.search_callback = search_callback
      self.dtype = SETTING["dtype"]
      self.customer_frame = DataFrame.CustomerDataFrame()
      self.entries = {}

      # Create search entries
      for i, entry_name in enumerate(SEARCH_ENTRIES):
         if entry_name.lower() == "no.":
            continue
         elif "date" in entry_name.lower() or "birthday" in entry_name.lower():
            label_widget = Date.LabelDateEntry(master, entry_name+":", i, 0)
         elif entry_name.lower() == "gender":
            label_widget = Button.LabelCheckButton(master, entry_name+":", GENDER_OPT, i, 0)
         elif entry_name.lower() == "certificate type":
            label_widget = Button.LabelCheckButton(master, entry_name+":", CERT_OPT, i, 0, 1)
         else:
            label_widget = Entry.LabelEntry(master, entry_name+":", i, 0, self.dtype[entry_name])
         label_widget.add_clear_btn(row=i, column=0)
         
         # Add entry to entries dict
         entry_att = entry_name.lower().replace(" ", "_") + "_widget"
         self.entries[entry_name] = entry_att
         setattr(self, entry_att, label_widget)

         # Bind enter key to search
         entry_widget = getattr(self, self.entries[entry_name])
         if (not isinstance(entry_widget, Button.LabelCheckButton) and 
             not isinstance(entry_widget, Button.LabelRadioButton)):
            entry_widget.get_entry().bind("<Return>", lambda event: self.search())

      # Create Buttons
      self.btn_frame = tb.Frame(master)
      self.btn_frame.grid(row=len(SEARCH_ENTRIES), column=0, pady=10, padx=10, sticky="nsew", columnspan=3)
      # self.btn_frame.grid_propagate(False)
      self.btn_frame.columnconfigure(0, weight=1)
      self.btn_frame.columnconfigure(1, weight=1)
      self.btn_frame.columnconfigure(2, weight=1)
      # Create search button   
      self.search_button = tb.Button(self.btn_frame, text="Search", command=self.search, bootstyle="primary")
      self.search_button.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")  
      # Create add button
      self.add_button = tb.Button(self.btn_frame, text="Add", command=self.add, bootstyle="success")
      self.add_button.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")
      # Create clear all button
      self.clear_button = tb.Button(self.btn_frame, text="Clear All", command=self.clear, bootstyle="danger")
      self.clear_button.grid(row=0, column=2, pady=5, padx=5, sticky="nsew")  
      


   def get_entries(self):
      return self.entries

   def search(self):
      search_dict = {}
      print("---------------------------")
      print("Search button clicked:")
      for entry_name in SEARCH_ENTRIES[1:]:
         entry_widget = getattr(self, self.entries[entry_name])
         entry_text = entry_widget.get_text()
         search_dict[entry_name] = entry_text
         print(entry_name, ":", entry_text)
      print("---------------------------")
      search_df = self.customer_frame.search(search_dict)
      self.search_callback(search_df)
   
   def clear(self):
      print("Clear button clicked")
      for entry_name in SEARCH_ENTRIES[1:]:
         entry_widget = getattr(self, self.entries[entry_name])
         entry_widget.clear_text()

   def add(self):
      pass
      