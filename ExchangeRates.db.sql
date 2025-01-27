BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "countries" (
	"country_short_name"	TEXT,
	"country_long_name"	TEXT
);
CREATE TABLE IF NOT EXISTS "Currency" (
	"currency"	TEXT,
	"currency_name"	TEXT,
	"forex_buying"	TEXT,
	"forex_selling"	TEXT,
	"banknote_buying"	TEXT,
	"banknote_selling"	TEXT,
	"crossrate_usd"	TEXT,
	"crossrate_other"	TEXT,
	"date"	TEXT,
	"time"	TEXT
);
CREATE VIEW view_australian_dollar
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'AUD';
CREATE VIEW view_azerbaijani_new_manat
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'AZN';
CREATE VIEW view_bulgarian_lev
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'BGN';
CREATE VIEW view_canadian_dollar
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'CAD';
CREATE VIEW view_chinese_renminbi
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'CNY';
CREATE VIEW view_danish_krone
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'DKK';
CREATE VIEW view_euro
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'EUR';
CREATE VIEW view_iranian_rial
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'IRR';
CREATE VIEW view_japanese_yen
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'JPY';
CREATE VIEW view_kuwaiti_dinar
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'KWD';
CREATE VIEW view_new_leu
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'RON';
CREATE VIEW view_norwegian_krone
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'NOK';
CREATE VIEW view_pakistani_rupee
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'PKR';
CREATE VIEW view_pound_sterling
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'GBP';
CREATE VIEW view_qatari_rial
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'QAR';
CREATE VIEW view_russian_rouble
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'RUB';
CREATE VIEW view_saudi_riyal
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'SAR';
CREATE VIEW view_south_korean_won
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'KRW';
CREATE VIEW view_swedish_krona
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'SEK';
CREATE VIEW view_swiss_frank
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'CHF';
CREATE VIEW view_united_arab_emirates_dirham
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'AED';
CREATE VIEW view_us_dollar 
AS 
SELECT
	c.date,
	c.time,
	c.forex_buying, 
	c.forex_selling, 
	c.banknote_buying, 
	c.banknote_selling,
	c.crossrate_usd,
	c.crossrate_other
FROM 
	Currency as c
WHERE 
	currency = 'USD';
COMMIT;
