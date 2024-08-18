#from nselib import *
from nselib import capital_market
from nselib import derivatives
import datetime


#shows all the block deals data
block_deals = capital_market.block_deals_data(period = '1M')
print(block_deals)

#shows the volatility of the overall market 
market_volatility = capital_market.india_vix_data(period='1M')
print(market_volatility)

#short selling data 
short_selling_data = capital_market.short_selling_data(period='1M')
print(short_selling_data)

#expiry dates for option cjain index
options_expiry = derivatives.expiry_dates_option_index()

#foreign institutional investors
#foreign_investors = derivatives.fii_derivatives_statistics('22-12-2023')






