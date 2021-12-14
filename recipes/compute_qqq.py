# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
web_history_prepared = dataiku.Dataset("web_history_prepared")
web_history_prepared_df = web_history_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

qqq_df = web_history_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
qqq = dataiku.Dataset("qqq")
qqq.write_with_schema(qqq_df)
