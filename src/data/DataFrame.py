import pandas as pd
from typing import Dict, Union
from src.config import *
from src.data import Customer


class CustomerDataFrame:
   def __init__(self) -> None:
      self.df:pd.DataFrame = CUSTOMER_DF.sort_index(ascending=False)
      self.df.columns:list = CUSTOMER_COLUMNS[1:]
      self.columns = CUSTOMER_COLUMNS
      self.dtype = SETTING["dtype"]


   def get_df(self) -> pd.DataFrame:
      return self.df
   
   def get_customer(self, index:int) -> Customer:
      row = self.df.iloc[index]
      components = row.tolist()
      return Customer(*components)
   
   def search(self, search_dict:Dict[str, Union[str, list]]) -> pd.DataFrame:
      df = self.df.dropna()
      for key in search_dict:
         if key in self.columns:
            # print("Searching by", key)
            df = self.search_by_dtype(df, key, search_dict[key])
      print("Searched df.head(10): ")
      print(df.head(10))
      return df
   
   def search_by_dtype(self, df:pd.DataFrame, col:str, search_input:Union[str, list]) -> pd.DataFrame:
      dtype = self.dtype[col]
      search_func = {
         "str": self.search_str,
         "opt": self.search_opt,
         "date": self.search_date,
         "number": self.search_number
      }
      search_result = search_func.get(dtype, None)
      if search_result:
         return search_result(df, col, search_input)
      else:
         print("Error: dtype not found")
         return self.df


   def search_str(self, df:pd.DataFrame, col:str, search_str:str) -> pd.DataFrame:
      search_str = search_str.strip()
      search_str = search_str.lower()
      if search_str == "":
         return df
      search_df = df[df[col].str.lower().str.contains(search_str)]
      return search_df
   
   def search_opt(self, df:pd.DataFrame, col:str, search_list:list) -> pd.DataFrame:
      if search_list == []:
         return df
      search_df = pd.DataFrame(columns=self.df.columns)
      for entry in search_list:
         search_df = pd.concat([df[df[col] == entry], search_df]) 
      return search_df
   
   def search_date(self, df:pd.DataFrame, col:str, search_str:str) -> pd.DataFrame:
      search_str = search_str.strip()
      if search_str == "":
         return df
      df = self.df
      search_df = df[df[col] == search_str]
      return search_df
   
   def search_number(self, df:pd.DataFrame, col:str, search_str:str) -> pd.DataFrame:
      search_str = search_str.replace(" ", "")
      print("Searching number:", search_str)
      if search_str == "":
         return df
      search_df = df[df[col].str.replace("-", "").replace(" ", "") == search_str]
      return search_df


if __name__=="__main__":
   cdf = CustomerDataFrame()
   # cdf.search({"Name": "Nguyễn"})

   df = cdf.get_df()
   filter_df = df[df["Name"].str.contains("John")]
   print(filter_df.head(10))

