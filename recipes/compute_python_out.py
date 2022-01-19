# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
web_last_month_enriched_copy = dataiku.Dataset("web_last_month_enriched_copy")
web_last_month_enriched_copy_df = web_last_month_enriched_copy.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_out_df = web_last_month_enriched_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
python_out = dataiku.Dataset("python_out")
python_out.write_with_schema(python_out_df)
