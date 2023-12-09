import tkinter as tk
import ttkbootstrap as tb
from typing import Callable
import pandas as pd
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from src.config import *
from src.data import DataFrame


class Table:
   def __init__(self, master:tb.Notebook, 
                df:DataFrame.CustomerDataFrame=None,
                dbclick_callback:Callable[[pd.DataFrame], None]=None):
      self.master = master
      self.df = df
      self.master.rowconfigure(0, weight=1)
      self.master.columnconfigure(0, weight=1)

      style = Style()
      style.configure("CustomerTab.Treeview", font=FONT, rowheight=25, theme="litera")
      self.table = tb.Treeview(self.master, columns=(CUSTOMER_COLUMNS), bootstyle="primary")
      self.table['show'] = 'headings'

      self.table.heading("No.", text="No.", anchor="nw")
      self.table.column("No.", width=CUSTOMER_COLUMNS_WIDTH["No."], minwidth=CUSTOMER_COLUMNS_WIDTH["No."], anchor="nw", stretch=False)
      for i, column in enumerate(CUSTOMER_COLUMNS[1:]):
         self.table.heading(column, text=column, anchor="nw")
         self.table.column(column, width=CUSTOMER_COLUMNS_WIDTH[column], minwidth=100, anchor="nw")
      self.table.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
      self.display(self.df.get_df())

      self.scrollbar = tb.Scrollbar(self.master, orient="vertical", command=self.table.yview)
      self.scrollbar.grid(row=0, column=1, sticky="nsew")
      self.table.configure(yscrollcommand=self.scrollbar.set)

      self.table.bind("<Double-1>", self.customer_dblick)


   def customer_dblick(self, event):
      if len(self.table.selection()) == 0:
         print("Table is empty")
         return
      item = self.table.selection()[0]
      print(self.table.item(item, "values"))

   def clear(self):
      self.table.delete(*self.table.get_children())

   def display(self, df:pd.DataFrame):
      print("Displaying customer table")
      self.clear()
      for index, row in df.iterrows():
         row = row.tolist()
         row = [index+1] + row
         self.table.insert("", "end", values=list(row))


