import os
import glob
from datetime import datetime

# importing the required modules
import csv
import requests
import xml.etree.ElementTree as elemTree

# database
import sqlite3


NOW = datetime.now()
CURRENT_DATE = NOW.date()   # %Y.%m.%d
CURRENT_TIME = NOW.time()   # %H:%M.%S


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


def parse_xml(xml_filename, xml_datetime=None):

    # create element tree object
    tree = elemTree.parse(xml_filename)

    # get root element
    root = tree.getroot()

    # empty list exchange rates dictionaries
    exchange_rates_items = []

    for child in root:

        if xml_datetime:
            file_date = xml_datetime
            file_time = xml_datetime
        else:
            file_date = CURRENT_DATE
            file_time = CURRENT_TIME

        # empty exchange rates dictionary
        exchange_rates = {
            'date': file_date.strftime('%Y.%m.%d'),
            'time': file_time.strftime('%H:%M.%S'),
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

    # return exchange rates items list
    return exchange_rates_items


def insert_into_sqlite(exchange_rates_items, sqlite_file):

    try:
        conn = sqlite3.connect(sqlite_file)
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
                        banknote_buying, banknote_selling, crossrate_usd, crossrate_other, date, time)
                        )
        cur.close()

        conn.commit()

    except Exception as error:
        print(error)

    finally:
        conn.close()


def parse_datetime_from_filename(xml_filename) -> datetime:

    str_list = xml_filename.rsplit('_')

    if len(str_list) == 2:
        part_a = str_list[0]
        str_list = part_a.rsplit(' ')

    date = str_list[0].replace('.', '')
    time = str_list[1]

    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    hour = int(time[0:2])
    min = int(time[2:4])
    sec = int(time[4:6])

    return datetime(year, month, day, hour, min, sec)



def update_crossrates_in_sqlite(sqlite_file, items):

    for item in items:

        if item['crossrate_usd'] or item['crossrate_other']:

            try:
                conn = sqlite3.connect(sqlite_file)
                cur = conn.cursor()

                date = item['date']
                currency = item['currency']
                crossrate_usd = item['crossrate_usd']
                crossrate_other = item['crossrate_other']

                # qmark style:
                sql = '''
                        UPDATE 
                            Currency 
                        SET 
                            crossrate_usd = ?,
                            crossrate_other = ?
                        WHERE
                            date = ? 
                            AND
                            currency = ?
                        '''

                cur.execute(sql, (crossrate_usd, crossrate_other, date, currency, ))
                cur.close()

                conn.commit()

            except Exception as error:
                print(error)

            finally:
                conn.close()



def main():

    xml_path = r'D:\My Documents\Databases\tcmbDailyRates\xml'
    sqlite_file = r'D:\My Documents\Databases\SQLite\ExchangeRates.db'

    for xml_filename in os.listdir(xml_path):
        
        xml_datetime = parse_datetime_from_filename(xml_filename)
        exchange_rates_items = parse_xml(os.path.join(xml_path, xml_filename), xml_datetime)
        update_crossrates_in_sqlite(sqlite_file, exchange_rates_items)

        #insert_into_sqlite(exchange_rates_items)

    return 0

if __name__ == "__main__":
    main()
