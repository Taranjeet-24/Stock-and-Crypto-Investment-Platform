# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:28:41 2021

@author: hp
"""
from nsetools import Nse
nse=Nse()
all_stock_codes = nse.get_stock_codes()
print(all_stock_codes)

top_gainers = nse.get_top_gainers()
print(top_gainers)

top_losers = nse.get_top_losers()
print(top_losers)

q= nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
print(q)

adv_dec = nse.get_advances_declines()
print(adv_dec)


nse.get_fno_lot_sizes()