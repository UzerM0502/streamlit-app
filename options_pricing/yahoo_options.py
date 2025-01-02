import pandas as pd
import pandas_datareader.data as web
import numpy as np

FB = web.YahooOptions('FB')

print(FB)
calls = FB.get_call_data()
print(calls)