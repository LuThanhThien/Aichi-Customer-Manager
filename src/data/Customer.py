from typing import List
from datetime import datetime
from src.config import *

class Customer:
   def __init__(self, name: str, cert_type: str, doc_id: str, phone_no: str, fb_account: str, 
             entry_date: datetime, theory_date: datetime, test_date: List[datetime]) -> None:
      self.name = name
      self.cert_type = cert_type
      self.doc_id = doc_id
      self.phone_no = phone_no
      self.fb_account = fb_account
      self.entry_date = entry_date
      self.theory_date = theory_date
      self.test_date = test_date

   def get_name(self) -> str:
      return self.name

   def get_cert_type(self) -> str:
      return self.cert_type

   def get_doc_id(self) -> str:
      return self.doc_id

   def get_phone_no(self) -> str:
      return self.phone_no

   def get_fb_account(self) -> str:
      return self.fb_account

   def get_entry_date(self) -> datetime:
      return self.entry_date

   def get_theory_date(self) -> datetime:
      return self.theory_date

   def get_test_date(self) -> List[datetime]:
      return self.test_date

   def set_name(self, name: str) -> None:
      self.name = name

   def set_cert_type(self, cert_type: str) -> None:
      self.cert_type = cert_type

   def set_doc_id(self, doc_id: str) -> None:
      self.doc_id = doc_id

   def set_phone_no(self, phone_no: str) -> None:
      self.phone_no = phone_no

   def set_fb_account(self, fb_account: str) -> None:
      self.fb_account = fb_account

   def set_entry_date(self, entry_date: datetime) -> None:
      self.entry_date = entry_date

   def set_theory_date(self, theory_date: datetime) -> None:
      self.theory_date = theory_date

   def set_test_date(self, test_date: List[datetime]) -> None:
      self.test_date = test_date



# Tên : 
# Loại bằng
# Mã số hồ sơ
# Sđt
# Tên Facebook
# Ngày nộp hsơ
# Ngày thi LT
# Ngày thi thực hành
# Lần 1
# 2
# 3
# 4 ....