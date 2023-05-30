# Penny stocks - Data processing, to become rich

## Description:
This project is based on a WebSite for Penny Stock trading, which the program Web scrapes, for data regarding the different firms, names and the price of their stock.

Using this data and python tools, the data is proccesed to show the user stuff like the firm that performs best, over a duration of time (in percentages), and plots data like this, to show the user, which firm would be best to invest in, not based on their current price, but how they're doing in general.

## List of used technologies:
...

## Installation guide:
- The Python CSV library / If installation needed, write this in console: pip install python-csv
- The Platform library / If installation needed, write this in console: pip install lib-platform
- The Pandas library / If installation needed, write this in console: pip install pandas
- The MatPlot library / If installation needed, write this in console: pip install matplotlib
- The Selenium library / If installation needed, write this in console: pip install selenium
- The bs4 library / If installation needed, write this in console: pip install beautifulsoup4

## User guide:
The program is split in 2, though normally the user would only have to interact with 1 of the parts.

The first part of the program is the Web Scraping part, which the user, if it were a deployed program, wouldn't have to interact with, only a admin or similar. But this part is run by:
1) Go into the "7.WebScraping.ipynb" file
2) Run the program, by clicking the "Execute Cell" button
by doing this, the program will scrape the https://www.marketbeat.com/types-of-stock/penny-stocks/ Website, and update the firms.csv file, with today's prices, for each firm. Meaning it will append today's price to an already existing firm, but if the firm doesn't exist in the firms.csv file, a completely new firm will be added, with the related price.

The second part of the program, minded towards the user, is a program, that runs through a Console, that let's the user use the functionallity that we have created, to get stuff like the cheapest firm, whether the latest price, is lower or higher than the general price, in percentage, etc. How to run the program:
1) Open a console in the FirmClass folder
2) Write 'python Commandline.py' into the console
3) Doing this, you're met with a few different options, such as selecting a specific firm, and look into their data, or get the cheapest firm, or get the most expensive firm, etc.
4) Chosing the least- or most expensive firm, will return these values, and go back to step 3, but chosing a specific firm, will give you a new menu / options regarding this firm, such as getting the firms current price, compared to the average, all their prices, the company name and making a png file of the prices, plotted into a table, to show the development of the price.
5) When done using the program, the program is closed by writting the corresponding number (written in the console).

## Status:
Most of what we've planed, have been done. We've accomplished making a program, that takes firm names and their prices, and proces these, to give a user guide or an idea on which firm to invest in, based on empirical data, to reason for this choice.

1) But if we should continue develop this project / program, a more user friendly interface / visual interface could be developed, using something like JavaScript.
2) Besides this, more data processing functions could be developed, all the ones we could think of, we've already implemented, but given more time, we could probably find more usable functionallity that could be added.
3) And lastly, currently to Web Scrape the Web Site, a admin or likely, has to open the project, and run the .ipynb file, if this process could be automated, so that it just runs once daily, it would become easier for the admin.

## Challenges:
- Web Scraping?
- Pandas?
- Commandline program?
