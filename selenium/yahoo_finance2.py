import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

def kabuka():
	code = 3323
	S_year = 5
	S_day = 1

	company_code = str(code) + '.T'
	my_share = share.Share(company_code)
	symbol_data = None

	try:
		symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR, S_year, share.FREQUENCY_TYPE_DAY, S_day)

	except YahooFinanceError as e:
		print(e.message)
		sys.exit(1)

	df_base = pd.DataFrame(symbol_data)
	df_base = pd.DataFrame(symbol_data.values(), index=symbol_data.keys()).T
	df_base.timestamp = pd.to_datetime(df_base.timestamp, unit='ms')
	df_base.index = pd.DatetimeIndex(df_base.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')

	df_base = df_base.reset_index(drop=True)

	return company_code, df_base

if __name__ == '__main__':
	result = kabuka()
	print(str(result[0]), result[1].shape)

	df_base = result[1]

	df_base.head()
