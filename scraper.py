import requests
from bs4 import BeautifulSoup
import pandas as pd
import tabula

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')
#
#
# artist_name_list = soup.find(class_='BodyText')
#
# artist_name_list_items = artist_name_list.find_all('a')



# file = "Data Order for Math Climate.pdf"
# df = tabula.read_pdf(file, pages = '76', multiple_tables = True)
# print(df)

mydict = {}

import glob
import errno
path = 'allsites/*.txt'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:
            f=open(name.replace("\\","/"),"r")
            lines=f.readlines()
            dateresult=[]
            tempresult=[]
            dictresult = {}
            for x in lines:
                try:
                    dateresult.append(x.split('         ')[2])
                except:
                    None
                try:
                    tempresult.append(x.split('         ')[3])
                except:
                    None
            f.close()


            for i in range(len(dateresult)):
                dateresult[i] = dateresult[i].strip()

            # print(dateresult)

            for i in range(len(tempresult)):
                tempresult[i] = tempresult[i].strip()

            # print(tempresult)

            print(str(((name.split("\\")[1])[-(len(name)-2):])[:-4]) + " (" + str((name.split("\\")[1])[:2]) + ")")
            # print()


            dictresult = dict(zip(dateresult, tempresult))
            # print(dictresult)
            sumvalues = 0.0
            avgtemps = 0.0
            for x in dictresult.values():
                try:
                    sumvalues += float(x)
                except:
                    None
            # print(sumvalues)
            for x,y in dictresult.items():
                print(x + "   :   " + y)
            avgtemps = sumvalues/len(dictresult.values())
            print("\nTotal Average Temp: " + str(avgtemps))

            print("\n\n")
            # mydict[name] = F.read()
            # print(F.read())
            pass # do what you want
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise



# for vals in mydict.values():
#   myarray = ([x.strip() for x in vals.split('         ')])
  # myarray = ([myarray.strip() for x in vals.split('\n')])

  # print(myarray[0])
  # # print(myarray[])
  #
  # i = 0
  # for i in range(len(myarray)):
  #     print(myarray[i])




# for x in mydict.keys():
#   print(x)
