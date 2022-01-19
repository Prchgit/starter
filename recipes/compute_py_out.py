# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
python_out = dataiku.Dataset("python_out")
python_out_df = python_out.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

py_out_df = python_out_df # For this sample code, simply copy input to output


# Write recipe outputs
py_out = dataiku.Dataset("py_out")
py_out.write_with_schema(py_out_df)
