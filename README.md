<h1> STOCKS ETL </h1>

<h3> Summary </h3>
This solution queries data from a postgres DB containing stock symbols an quntities and scrapes data from marketwatch, downloads the price, change and change % and uploads the data into the DB

<h4> Architecture </h4>
 - DB: postgres 14 Database hosted in a google cloud server
 - ETL Script: Python - Classh fro web Scraping Stock_prices.py , main script : download_prices.py
 - Dockerfile: Image . Python 3.9 , See crontab 


