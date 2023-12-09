from typing import Any
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Validator():
   def __init__(self, master:tb.Frame=None):
      self.master = master
      self.number_func = self.master.register(self.validate_number)
      self.alpha_func = self.master.register(self.validate_str)

   def validate_number(self, x, size=-1) -> bool:
      """Validates that the input is a number"""
      if x.isdigit() or x == "":
         if size != -1 and len(x) > size:
               return False
         return True
      else:
         return False

   def validate_str(self, x, size=-1) -> bool:
      """Validates that the input is string"""
      if size != -1 and len(x) > size:
            return False
      return True
      
   def validate(self, dtype:str):
      func = {
         "number": self.number_func,
         "str": self.alpha_func
      }
      return func.get(dtype, None)