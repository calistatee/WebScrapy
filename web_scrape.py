from bs4 import BeautifulSoup
import requests
import csv

# request web source to get source code
source = requests.get('insert your url here').text

# assign a var for parsed information w standard BS syntax
soup = BeautifulSoup(source, 'lxml')

csv_file = open('name your csv file', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headlines', 'Summary', 'YouTube link'])

# to print out web source code w proper indentations
# print (soup.prettify())

# grab first headline + snippet for first post on the web
# find to find_all to grab every posts shown
for article in soup.find_all('article'):

    # headline
    # doesn't necessarily need to include every single parent tags
    headline = article.h2.a.text
    print(headline)

    # return the summary (just the first paragraph) of article
    # use class_ because class also a term used in python
    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)

    # in case some posts don't include a video
    # to prevent software crash if vid link is not detected

    try:
        # return the video source code within article ('iframe')
        #['src'] -- access source attribute like a dictionary
        # it's to clearly show the youtube link within the vid source code
        vid_src = article.find('iframe', class_ = 'youtube-player')['src']
        
        # splitting vid link into a few chunks when code sees a '/'
        # since our youtube id is rested on the 4th index
        # we want to print out our 4th index 
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    # if youtube link is not available, you want to label it as None
    # 'None' will show up as a blank space in the .csv file
    except Exception as e:
        yt_link = None

    print (yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

# check your CSV file for results! 
