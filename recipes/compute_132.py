# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
py_out = dataiku.Dataset("py_out")
py_out_df = py_out.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

v132_df = py_out_df # For this sample code, simply copy input to output


# Write recipe outputs
v132 = dataiku.Dataset("132")
v132.write_with_schema(v132_df)
