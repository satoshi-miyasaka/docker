#!/bin/python3
import sys
import pandas as pd
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

class KabukaCheck:
	def __init__(self):
		# コンストラクタ
		print("Hello!")

	def __del__(self):
		# デストラクタ
		print("Goodbye!")

	def  kabuka(self, code, sYear, sDay):
		company_code = str(code) + '.T'
		my_share = share.Share(company_code)
		symbol_data = None

		try:
			symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR, sYear, share.FREQUENCY_TYPE_DAY, sDay)

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

	code = 3323
	sYear = 5
	sDay = 1

	kabukaCheck = KabukaCheck()

	result = kabukaCheck.kabuka(code , sYear , sDay)
	print(str(result[0]), result[1].shape)

	df_base = result[1]

	df_base.head()
