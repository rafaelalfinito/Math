import pandas as pd
import os
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt
import numpy as np


def data_into_dataframe(year, month, day, assetname):
    colNames = ["Session Date", "Instrument Symbol", "Trade Number", "Trade Price", "Traded Quantity", "Trade Time", "Trade Indicator", "Buy Order Date", "Sequential Buy Order Number", "Secondary Order ID - Buy Order", "Aggressor Buy Order Indicator", "Sell Order Date", "Sequential Sell Order Number", "Secondary Order ID - Sell Order", "Aggressor Sell Order Indicator", "Cross Trade Indicator", "Buy Member", "Sell Member"]
    FileFolder_root = 'C:\\Users\\alfinira\\PycharmProjects\\Math\\BMFData\\zip\\extract\\apphmb\\intraday\\'
    FileFolder_sub = str(year)+('0'+str(month))[-2:] + '\\'
    FileFolder = FileFolder_root + FileFolder_sub


    file_name = FileFolder + 'NEG_BMF_201612' + ('0'+str(month))[-2:] + '.TXT'

    data = pd.read_csv(file_name, sep  = ';', names = colNames, low_memory=False, index_col = False, skiprows = 1)

    for col in data.columns:
        if data[col].dtype == np.object:
            data[col] = data[col].str.strip()


    data_asset = data[data['Instrument Symbol'] == assetname]
    data_asset = data_asset[data_asset['Trade Price'] > 1000]
    if not data_asset.empty:
        data_asset['Trade Time'] = pd.to_datetime(data_asset['Trade Time'], infer_datetime_format=True)
        data_asset.sort_values(by='Trade Time')
        ts = pd.Series(data_asset['Trade Price'].values, index=data_asset['Trade Time'])
        ts.plot()
        plt.show()

    return data_asset



