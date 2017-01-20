import pandas as pd
import numpy as np
import BMF_treatdata



assetname = 'DOLF17'
data_frame = BMF_treatdata.data_into_dataframe(2016, 12, 1, assetname)
print(data_frame.head())

