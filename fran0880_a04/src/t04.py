"""
-------------------------------------------------------
Fall 2020
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880
Email:   fran0880@mylaurier.ca
__updated__ = "2020-11-14"
-------------------------------------------------------
""" 
from functions import foreign_key_info
from Connect import Connect

conn = Connect("dcris.txt")
temp_cursor = conn.cursor;

#rows = foreign_key_info(temp_cursor,'dcris')
#rows = foreign_key_info(temp_cursor,'dcris', None, 'keyword')
#rows = foreign_key_info(temp_cursor,'dcris', 'pub', None)
print("table name and ref table name provided:")
rows = foreign_key_info(temp_cursor,'dcris', 'pub', 'pub_type')
print("COLUMNS:")
print(temp_cursor.column_names)
print("DATA:")

for row in rows:
    print(row)
    
conn.close()