import pandas as pd  # install pandas module using pip3 install pandas
import alpha_vantage  # install alpha_vantage using pip3 install alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import time


api_key = ''  # Get this api_key from alphavantage.co

time_series = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = time_series.get_intraday(symbol = 'MSFT', interval = '1min', outputsize = 'full')
print(data)

# saving the data in an excel at 60 sec interval of time
path_to_save_excel_file = ""

trigger_default_value = 1
while trigger_default_value == 1:
    data.to_excel(path_to_save_excel_file+"MSFT_intraday_data.xlsx")
    time.sleep(6)
