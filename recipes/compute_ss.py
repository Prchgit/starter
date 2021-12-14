# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import time

# Read recipe inputs
revenue_prediction = dataiku.Dataset("revenue_prediction")
revenue_prediction_df = revenue_prediction.get_dataframe()
time.sleep(300)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

ss_df = revenue_prediction_df # For this sample code, simply copy input to output


# Write recipe outputs
ss = dataiku.Dataset("ss")
ss.write_with_schema(ss_df)
