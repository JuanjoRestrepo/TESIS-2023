import pygsheets
import pandas as pd

class dashboard():

    def __init__(self):
        #authorization
        self.Path = "OneDrive\Desktop\credentials.json"
        self.Key = '1FG65WfkqVTcV38nBV5GGBlrH4ZFhSjjzAsvYMbKzCQM'
        

    def Upload_Sheet_Complete(self,data,SheetName): # Update and change all the sheet information
        #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
        gc = pygsheets.authorize(service_file=self.Path)
        sh = gc.open_by_key(self.Key)

        # Open the Worksheet that you want to update
        wks = sh.worksheet_by_title(SheetName)

        #update the first sheet with df, starting at cell B2. 
        wks.clear(start='A2', end=None, fields='userEnteredValue')
        wks.set_dataframe(data,(2,1))


    def Add_End(self,data,SheetName):  # Add a new data in the end
        #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
        gc = pygsheets.authorize(service_file=self.Path)
        sh = gc.open_by_key(self.Key)

        # Open the Worksheet that you want to update
        wks = sh.worksheet_by_title(SheetName)
        index = wks.find("",matchEntireCell=True,cols=[1,1])
        wks.insert_rows((index[0].row)-1, number=1, values=data) 

    def Modified_Row(self,ID,data,SheetName,case,col):  # Modificar un dato en específico
        #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
        gc = pygsheets.authorize(service_file=self.Path)
        sh = gc.open_by_key(self.Key)

        # Open the Worksheet that you want to update
        wks = sh.worksheet_by_title(SheetName)

        cell = wks.find(ID,matchEntireCell=True)

        if case == 1: # Replace one cell
            wks.update_value((cell[0].row,col),data)
        
        else: # Replace all row
            wks.update_row(cell[0].row,values=data)

    def Delete_Row(self,ID,SheetName): # Delete a specific row
        #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
        gc = pygsheets.authorize(service_file=self.Path)
        sh = gc.open_by_key(self.Key)

        # Open the Worksheet that you want to update
        wks = sh.worksheet_by_title(SheetName)

        #delete_rows(index, number=1)
        cell = wks.find(ID,matchEntireCell=True)
        wks.delete_rows(cell[0].row, number=1)

#dash = dashboard()
#data =[1,2,3,4,5,'peep']
#dash.Add_End(data,'Ordenes')