import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from src.utils import *
from src.tabs import SearchTab, CustomerTab
from src.data import DataFrame


class App(tb.Window):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.title("Customer Management System")
      width, height = self.winfo_screenwidth(), self.winfo_screenheight()
      self.geometry("%dx%d+0+0" % (width, height))  
      self.state("zoomed")
      self.rowconfigure(0, weight=1)
      self.columnconfigure(1, weight=1)

      self.customer_df = DataFrame.CustomerDataFrame()

      self.search_frame = tb.Labelframe(self, bootstyle="primary", text="Search box")
      self.search_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
      self.search_tab = SearchTab.Search(self.search_frame, self.update_table_callback)

      self.filter_frame = tb.Labelframe(self, bootstyle="primary", text="Filter box")
      self.filter_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
      # self.filter_tab = SearchTab.Filter(self.filter_frame)
      
      self.customer_frame = tb.Labelframe(self, bootstyle="primary", text="Customer table")
      self.customer_frame.grid(row=0, column=1, rowspan=2, pady=10, padx=10, sticky="nsew")
      self.customer_table = CustomerTab.Table(self.customer_frame, self.customer_df)


   def update_table_callback(self, df):
      self.customer_table.display(df)
         


def main(*args, **kwargs):
   gui = App(*args, **kwargs)
   gui.mainloop()

if __name__ == "__main__":
   main()

   
