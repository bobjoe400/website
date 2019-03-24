#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

def generate_html_with_table(data, columns_or_rows = 1,                              column_name_prefix = 'Column',                              span_axis = 1,                              showOutput = True):
    """
    This function returns a pandas.DataFrame object and a 
    generated html from the data based on user specifications.
    
    #Example:
      data_html, data_df = generate_html_with_table(data, columns_or_rows, column_name_prefix, span_axis, showOutput)
      # To suppress output and skip the DataFrame:
      # span data along a row first
        columns = 4
        columns_or_rows = columns
        data_html, _ = generate_html_with_table(data, columns_or_rows, column_name_prefix, 1, False)  
      # span data along a column first
        rows = 4
        columns_or_rows = rows
        data_html, _ = generate_html_with_table(data, columns_or_rows, column_name_prefix, 0, False)   
      
    # Inputs: 
        1. data:               Data
           (dtype: list)
           
      **Optional Input Parameters:**
        2. columns_or_rows:            Number of Columns or rows
           (dtype: int)                columns: span_axis = 1
           (DEFAULT: 1)                rows:    span_axis = 0
        3. column_name_prefix: The Prefix for Column headers
           (dtype: string)
           (DEFAULT: 'Column')
        4. span_axis:          The direction along which the elements span.
           (dtype: int)        span_axis = 0 (span along 1st column, then 2nd column and so on)
           (DEFAULT: 1)        span_axis = 1 (span along 1st row, then 2nd row and so on)
        5. showOutput:         (True/False) Whether to show output or not. Use 
           (dtype: boolean)                   False to suppress printing output.
           (DEFAULT: True)
                                                              
    # Outputs:
        data_html: generated html
        data_df:   generated pandas.DataFrame object
        
    # Author: Sugato Ray 
    Github: https://github.com/sugatoray
    Repository/Project: CodeSnippets
    
    """
    # Calculate number of elements in the list: data
    elements = len(data)
    # Calculate the number of rows/columns needed
    if (span_axis == 0): # if spanning along a column
      rows = columns_or_rows
      columns = int(np.ceil(elements/rows))    
    else: #(span_axis = 1)
      columns = columns_or_rows
      rows = int(np.ceil(elements/columns))
    # Generate Column Names
    column_names = [column_name_prefix + '_{}'.format(i)                     for i in np.arange(columns)]    
    # Convert the data into a numpy array    
    data_array = np.array(data + ['']*(columns*rows - elements))
    if (span_axis == 0):
      data_array = data_array.reshape(columns,rows).T  
    else: #(span_axis == 0)
      data_array = data_array.reshape(rows,columns)  
    
    # Convert the numpy array into a pandas DataFrame
    data_df = pd.DataFrame(data_array, columns = column_names)    
    # Create HTML from the DataFrame
    data_html = data_df.to_html()
    if showOutput:
        print('Elements: {}\nColumns: {}\nRows: {}'.format(elements,                                                            columns,                                                            rows))
        print('Column Names: {}'.format(column_names))
        print('\nPandas DataFrame: ')
        display(data_df)
        print('\nHTML Generated: \n\n' + data_html)
        
    return (data_html, data_df)


  
#data_html, data_df = generate_html_with_table(data, columns_or_rows, column_name_prefix, span_axis, showOutput)
print(generate_html_with_table.__doc__)

