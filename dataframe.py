import datetime
import pandas as pd
import db


def get_data(uploaded_file,name): 
    type = name.split(".")
    if type[-1] == "xlsx":
        # name = type[0] 
        dataframe = pd.read_excel(uploaded_file, engine = 'openpyxl')
        return dataframe
    elif type[-1] == "xls":
        # name = type[0] 
        dataframe = pd.read_excel(uploaded_file)
        return dataframe
    elif type[-1] == "csv":
        # name = type[0] 
        dataframe = pd.read_csv(uploaded_file, parse_dates = ["Date"])
        return dataframe