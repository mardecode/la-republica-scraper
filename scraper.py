from base64 import decode
from importlib.resources import contents
from urllib import response
import requests
import lxml.html as html
import os
import datetime


HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//a/@href'
XPATH_TITLE = '//h2[@class=""]/span/text()'
XPATH_SUMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not (@class)]/text()'

def get_title(link):
    #separamos por "/" y nos quedamos con el ultimo que elemento 
    url = link.split('/')[-1]
    #separamos por "-" y eliminamos el ultimo elemento
    title_list=url.split('-')[:-1]
    #Unimos lo anterior
    title = " ".join(title_list)

    return(title)


def parse_notice(link, today):
  try:
    response = requests.get(link)
    if response.status_code==200:
      notice = response.content.decode('utf-8')
      parsed = html.fromstring(notice)
      try:
        # title = parsed.xpath(XPATH_TITLE)[0]
        title = get_title(link)
        # title = title.replace('\"','')
        sumary = parsed.xpath(XPATH_SUMARY)[0]
        body = parsed.xpath(XPATH_BODY)
      except IndexError:
        return
      with open(f'data/{today}/{title}.txt','w',encoding='utf-8') as f:
        f.write(title)
        f.write('\n\n')
        f.write(sumary)
        f.write('\n\n')
        for p in body:
          f.write(p)
          f.write('\n')

    else:
      raise ValueError(f'Error: {response.status_code}')
  except ValueError as ve:
    print(ve)



def parse_home():
  try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
      home = response.content.decode('utf-8')
      # tomar el contenido de home
      parsed = html.fromstring(home)
      links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
      # print(links_to_notices)

      today = datetime.date.today().strftime('%d-%m-%Y')
      if not os.path.isdir("data/"+today):
        os.mkdir("data/"+today)
      for link in links_to_notices:
        parse_notice(link,today)
    else: 
      raise ValueError(f'Error: {response.status_code}')
  except ValueError as ve:
    print(ve)

def run():
  if not os.path.isdir("data"):
    os.mkdir("data")
  parse_home()


# entry point ?
if __name__ == '__main__':
  run()