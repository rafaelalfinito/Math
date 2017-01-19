import pandas as pd
import os
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt


colNames = ["Session Date", "Instrument Symbol", "Trade Number", "Trade Price", "Traded Quantity", "Trade Time", "Trade Indicator", "Buy Order Date", "Sequential Buy Order Number", "Secondary Order ID - Buy Order", "Aggressor Buy Order Indicator", "Sell Order Date", "Sequential Sell Order Number", "Secondary Order ID - Sell Order", "Aggressor Sell Order Indicator", "Cross Trade Indicator", "Buy Member", "Sell Member"]

FileFolder = 'C:\\Users\\alfinira\\PycharmProjects\\Math\\BMFData\\zip\\extract\\apphmb\\intraday\\'

for item in os.listdir(FileFolder):
    if item.endswith('.TXT'):
        file_name = FileFolder + '\\' + os.path.relpath(item)  # get full path of files
        data = pd.read_csv(file_name, sep  = ';', names = colNames, low_memory=False, index_col = False, skiprows = 1)
        dataDOL = data[data['Instrument Symbol'] == 'DOLG16                                            ']
        dataDOLClean = dataDOL[dataDOL['Trade Price'] > 1000]
        ts = pd.Series(dataDOLClean['Trade Price'].values, index=dataDOLClean['Trade Time'])
        ts.plot()
        plt.show()




9

