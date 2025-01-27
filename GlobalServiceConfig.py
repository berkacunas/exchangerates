from enum import Enum

# enumerators
class ExecMachine(Enum):
	PC_Windows = 1
	PC_Ubuntu = 2
	Laptop_Windows = 3
	Laptop_Ubuntu = 4
	Remote_Arman = 5
	Reserved_Machine_0 = 6
	Reserved_Machine_1 = 7
	Reserved_Machine_2 = 8
	Reserved_Machine_3 = 9

class GlobalServiceConfig:

	def __init__(self):

		self.machine_dict = {}  # data structure for machine-specific settings
		self.city_names_json_db_diff = {}
		
		self.add_machine(ExecMachine.PC_Windows, 
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')

		self.add_machine(ExecMachine.PC_Ubuntu,
					root_dir='/home/berk/Documents/Services/ExchangeRates',
					sqlite_on=True,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=True,
					raw_data_dir='',
					sqlitedb_filepath='/home/berk/Documents/Databases/ExchangeRates/sqlite/ExchangeRates.db',
					csv_dir='',					
					log_dir='/home/berk/Documents/Services/ExchangeRates/Logs',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')

		self.add_machine(ExecMachine.Laptop_Windows,
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')

		self.add_machine(ExecMachine.Laptop_Ubuntu,
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')

		self.add_machine(ExecMachine.Remote_Arman,
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')
						
		self.add_machine(ExecMachine.Reserved_Machine_1,
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')

		self.add_machine(ExecMachine.Reserved_Machine_2,
					root_dir='',
					sqlite_on=False,
					mysql_on=False,
					postgresql_on=False,
					csv_on=False,
					log_on=False,
					raw_data_dir='',
					sqlitedb_filepath='',
					csv_dir='',					
					log_dir='',
					mysql_db_name='',
					mysql_user='',
					mysql_pass='',
					mysql_host='',
					postgresql_db_name='',
					postgresql_user='',
					postgresql_pass='',
					postgresql_host='',
					postgresql_port='')


	def add_machine(self, execMachine, root_dir, sqlite_on=False, mysql_on=False, postgresql_on=False,
						csv_on=False, log_on=False, raw_data_dir=None, sqlitedb_filepath=None, 
						csv_dir=None, log_dir=None, backup_dir=None,
						mysql_db_name=None, mysql_user=None, mysql_pass=None, mysql_host=None, 
						postgresql_db_name=None, postgresql_user=None, postgresql_pass=None, postgresql_host=None, postgresql_port=None):
	
		self.machine_dict[execMachine] = {
			'ROOT_DIR': root_dir,

			'SQLITE_ON': sqlite_on,
			'MYSQL_ON': mysql_on,
			'POSTGRESQL_ON': postgresql_on,
			'CSV_ON': csv_on,
			'LOG_ON': log_on,

			'SQLITEDB_FILEPATH': sqlitedb_filepath,

			'RAW_DATA_DIR': raw_data_dir,
			'BACKUP_DIR': backup_dir,
			'CSV_DIR': csv_dir,
			'LOG_DIR': log_dir,

			'MYSQL_DATABASE_NAME': mysql_db_name,
			'MYSQL_USERNAME': mysql_user,
			'MYSQL_PASSWORD': mysql_pass,
			'MYSQL_HOST': mysql_host,

			'POSTGRESQL_DATABASE_NAME': postgresql_db_name,
			'POSTGRESQL_USERNAME': postgresql_user,
			'POSTGRESQL_PASSWORD': postgresql_pass,
			'POSTGRESQL_HOST': postgresql_host,
			'POSTGRESQL_PORT': postgresql_port,
		}

	def load_machine(self, execMachine):

		self.root_dir = self.machine_dict[execMachine]['ROOT_DIR']
		self.sqlite_on = self.machine_dict[execMachine]['SQLITE_ON']
		self.mysql_on = self.machine_dict[execMachine]['MYSQL_ON']
		self.postgresql_on = self.machine_dict[execMachine]['POSTGRESQL_ON']
		self.csv_on = self.machine_dict[execMachine]['CSV_ON']
		self.log_on = self.machine_dict[execMachine]['LOG_ON']

		if self.sqlite_on:
			self.sqlite_db_path = self.machine_dict[execMachine]['SQLITEDB_FILEPATH']

		if self.mysql_on:
			self.mysql_db_name = self.machine_dict[execMachine]['MYSQL_DATABASE_NAME']
			self.mysql_user = self.machine_dict[execMachine]['MYSQL_USERNAME']
			self.mysql_pass = self.machine_dict[execMachine]['MYSQL_PASSWORD']
			self.mysql_host = self.machine_dict[execMachine]['MYSQL_HOST']

		if self.postgresql_on:
			self.postgresql_db_name = self.machine_dict[execMachine]['POSTGRESQL_DATABASE_NAME']
			self.postgresql_user = self.machine_dict[execMachine]['POSTGRESQL_USERNAME']
			self.postgresql_pass = self.machine_dict[execMachine]['POSTGRESQL_PASSWORD']
			self.postgresql_host = self.machine_dict[execMachine]['POSTGRESQL_HOST']
			self.postgresql_port = self.machine_dict[execMachine]['POSTGRESQL_PORT']

		self.RAW_DATA_DIR = self.machine_dict[execMachine]['RAW_DATA_DIR']
		if self.csv_on:
			self.CSV_DIR = self.machine_dict[execMachine]['CSV_DIR']

		if self.log_on:
			self.LOG_DIR = self.machine_dict[execMachine]['LOG_DIR']

		self.BACKUP_DIR = self.machine_dict[execMachine]['BACKUP_DIR']

import os
from datetime import datetime

from GlobalServiceConfig import GlobalServiceConfig
from LogMe import LogMe, error_message
from DBConnection import DBConnection



class GlobalServiceOptions:

	def __init__(self, execMachine):
		
		# get current date
		self.GLOBAL_NOW = datetime.now()
		self.CURRENT_DATE = self.GLOBAL_NOW.date()   # %Y.%m.%d
		self.CURRENT_TIME = self.GLOBAL_NOW.time()   # %H:%M.%S

		self.PROGRAMMERS_TIMEZONE = 3
		self.KELVIN_TO_CELCIUS = 273.15

		self.FILENAME_WITHOUT_EXT = f'{self.GLOBAL_NOW.strftime("%Y.%m.%d %H%M%S")}_openweather'

		self.JSON_FILE_PATH = 'resources/city.list.json'
		self.MAX_GROUP_QUERY_LIMIT = 20

		self.g_service_config = GlobalServiceConfig()
		self.g_service_config.load_machine(execMachine)

		self.db_Conn = DBConnection(execMachine)
		self.logMe = LogMe(self.g_service_config.LOG_DIR, self.FILENAME_WITHOUT_EXT)

		self.create_backup_dir_if_not_exists()
		self.create_log_dir_if_not_exists()
		self.create_csv_dir_if_not_exists()
		self.create_raw_data_dir_if_not_exists()
	
	
	@staticmethod
	def create_dir_if_not_exists(DIR_NAME):

		try:
			if not os.path.exists(DIR_NAME):
				os.makedirs(DIR_NAME)

		except:
			raise Exception

	def create_backup_dir_if_not_exists(self):

		try:
			GlobalServiceOptions.create_dir_if_not_exists(self.g_service_config.BACKUP_DIR)

		except Exception as error:
			print(error_message('GlobalServiceOptions.create_backup_dir_if_not_exists(self)', error))
			self.logMe.logs.append(error_message('GlobalServiceOptions.create_backup_dir_if_not_exists(self)', error))

	def create_log_dir_if_not_exists(self):

		if self.g_service_config.log_on:
			try:
				GlobalServiceOptions.create_dir_if_not_exists(self.g_service_config.LOG_DIR)

			except Exception as error:
				print(error_message('GlobalServiceOptions.create_log_dir_if_not_exists(self)', error))
				self.logMe.logs.append(error_message('GlobalServiceOptions.create_log_dir_if_not_exists(self)', error))

	def create_csv_dir_if_not_exists(self):

		if self.g_service_config.log_on:
			try:
				GlobalServiceOptions.create_dir_if_not_exists(self.g_service_config.CSV_DIR)

			except Exception as error:
				print(error_message('GlobalServiceOptions.create_csv_dir_if_not_exists(self)', error))
				self.logMe.logs.append(error_message('GlobalServiceOptions.create_csv_dir_if_not_exists(self)', error))

	def create_raw_data_dir_if_not_exists(self):

		try:
			GlobalServiceOptions.create_dir_if_not_exists(self.g_service_config.RAW_DATA_DIR)

		except Exception as error:
			print(error_message('GlobalServiceOptions.create_raw_data_dir_if_not_exists(self)', error))
			self.logMe.logs.append(error_message('GlobalServiceOptions.create_raw_data_dir_if_not_exists(self)', error))
