# 📰 La república scraper

This repository downloads the daily news from the Colombian newspaper **La República** https://www.larepublica.co/

The steps performed are:

- 🔗 The links to each news are obtained
- 📰 Access to each news
- 🧾 The title, summary, and body of the news are extracted
- 📂 Each news is stored in a `news_title`.txt file,



## Requirements
- python
  - requests
  - lxml

You can install them with: 
```
pip3 install requests
pip3 install lxml
```

## Execution
```
python3 scraper.py
```
Each time we run the `scraper.py` file, it will download the current day's news by creating a folder  where the program will store the information. **Each folder is named with the date it was executed**. All folders were stored in the main folder called 📂 `data` if this folder doesn't exist, the program will create it. 


> Please consider that this repository may stop working since La República is constantly changing its HTML structure. If this happens, feel free to leave an issue.