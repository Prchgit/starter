# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
py_out_copy = dataiku.Dataset("py_out_copy")
py_out_copy_df = py_out_copy.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_1_df = py_out_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
python_1 = dataiku.Dataset("python_1")
python_1.write_with_schema(python_1_df)
