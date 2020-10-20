# import statements
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

df = pd.DataFrame(cg.get_price(ids='bitcoin', vs_currencies='usd'))
df.head()

# print(cg.ping())
# print(cg.get_search_trending())






