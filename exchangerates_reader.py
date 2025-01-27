"""
Created on Wed Jul 14 10:27:47 2021
Completed on Wed Jul 14 12:54:47 2021

@author: Berk Acunaş
"""
import os
from datetime import datetime

import csv
import requests
import xml.etree.ElementTree as elemTree

import sqlite3

home_dir = r'C://berk' # os.path.expanduser("~")
print(f'Home Directory is: {home_dir}')

documents_dir = f'{home_dir}/Documents'

# Global Variables
XML_DIR = f'{documents_dir}/Databases/tcmbDailyRates/xml'
CSV_DIR = f'{documents_dir}/Databases/tcmbDailyRates/csv'
LOG_DIR = f'{documents_dir}/Databases/tcmbDailyRates/log'
DB_FILE = f'{documents_dir}/Databases/ExchangeRates/sqlite/ExchangeRates.db'

print(f'XML_DIR Directory is: {XML_DIR}')
print(f'CSV_DIR Directory is: {CSV_DIR}')
print(f'LOG_DIR Directory is: {LOG_DIR}')
print(f'DB is at: {DB_FILE}')


TCMB_URL = 'http://www.tcmb.gov.tr/kurlar/today.xml'

NOW = datetime.now()
CURRENT_DATE = NOW.date()   # %Y.%m.%d
CURRENT_TIME = NOW.time()   # %H:%M.%S

FILENAME_WITHOUT_EXT = f'{NOW.strftime("%Y.%m.%d %H%M%S")}_exchangerates'

log_dict = { }

tags_dict = {
    'Unit': 1,
    'CurrencyName': 2,
    'ForexBuying': 3,
    'ForexSelling': 4,
    'BanknoteBuying': 5,
    'BanknoteSelling': 6,
    'CrossRateUSD': 7,
    'CrossRateOther': 8
}

def error_message(func_name, error):

    return f'Exception at function: {func_name}\nError message: {error}'

def fetch_xml_from_webservice():

    try:
        xml_filename = os.path.join(XML_DIR, f'{FILENAME_WITHOUT_EXT}.xml')

        # creating HTTP response object from given url
        resp = requests.get(TCMB_URL)

        # saving the xml file
        with open(xml_filename, 'wb') as f:
            f.write(resp.content)

        return xml_filename

    except Exception as error:
        print(error_message('fetch_xml_from_webservice', error))
        log_dict['XML ERROR'] = error


def parse_xml(xml_filename):

    try:

        tree = elemTree.parse(xml_filename)
        root = tree.getroot()

        exchange_rates_items = []
        for child in root:

            exchange_rates = {
                'date': CURRENT_DATE.strftime('%Y.%m.%d'),
                'time': CURRENT_TIME.strftime('%H:%M.%S'),
                'currency': child.attrib['CurrencyCode'],
                'currency_name': child[tags_dict['CurrencyName']].text,
                'forex_buying': child[tags_dict['ForexBuying']].text,
                'forex_selling': child[tags_dict['ForexSelling']].text,
                'banknote_buying': child[tags_dict['BanknoteBuying']].text,
                'banknote_selling': child[tags_dict['BanknoteSelling']].text,
                'crossrate_usd': child[tags_dict['CrossRateUSD']].text,
                'crossrate_other': child[tags_dict['CrossRateOther']].text
            }

            print(exchange_rates)
            exchange_rates_items.append(exchange_rates)

        return exchange_rates_items
    
    except Exception as error:
        print(error_message('parse_xml', error))


def save_to_csv(exchange_rates_items):

    try:
        # specifying the fields for csv file
        fields = ['currency', 'currency_name', 'forex_buying', 'forex_selling',
                'banknote_buying', 'banknote_selling', 'crossrate_usd', 'crossrate_other', 'date', 'time']

        csv_filename = os.path.join(CSV_DIR, f'{FILENAME_WITHOUT_EXT}.csv')

        with open(csv_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(exchange_rates_items)

    except Exception as error:
        print(error_message('save_to_csv', error))
        log_dict['CSV ERROR'] = error


def insert_into_sqlite(exchange_rates_items):

    try:
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()

        for item in exchange_rates_items:
            date = item['date']
            time = item['time']
            currency = item['currency']
            currency_name = item['currency_name']
            forex_buying = item['forex_buying']
            forex_selling = item['forex_selling']
            banknote_buying = item['banknote_buying']
            banknote_selling = item['banknote_selling']
            crossrate_usd = item['crossrate_usd']
            crossrate_other = item['crossrate_other']

            # qmark style:
            sql = 'INSERT INTO Currency VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

            cur.execute(sql,
                        (currency, currency_name, forex_buying, forex_selling,
                        banknote_buying, banknote_selling, crossrate_usd, crossrate_other, date, time, )
                        )
        cur.close()

        conn.commit()

    except Exception as error:
        print(error_message('insert_into_sqlite', error))
        log_dict['SQLITE ERROR'] = error

    finally:
        conn.close()


def create_log_text(operation):

    text = ''
    operation_name = f"{operation} ERROR"
    if operation_name in log_dict:
        text = f'{operation} ERROR: {log_dict[operation_name]}\n'
    else:
        text = f'{operation} SUCCESS !\n'

    return text


def log_file():

    try:
        log_filename = os.path.join(LOG_DIR, f'{FILENAME_WITHOUT_EXT}.log') 
        log_text = ''
        
        if not os.path.exists(log_filename):
            f = open(log_filename, "x")
            f.close()

        if os.path.exists(log_filename):
            with open(log_filename, 'w') as f:

                log_text = create_log_text('MYSQL')
                log_text += create_log_text('SQLITE')
                log_text += create_log_text('XML')
                log_text += create_log_text('CSV')
            
                f.write(log_text)
    except Exception as error:
        print(error)


def main():

    try:
        xml_filename = fetch_xml_from_webservice()
        exchange_rates_items = parse_xml(xml_filename)
        insert_into_sqlite(exchange_rates_items)
        save_to_csv(exchange_rates_items)
    except:
        pass

    log_file()


if __name__ == "__main__":
    main()

