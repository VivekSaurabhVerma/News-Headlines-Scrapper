#! python3
# technew.py - Prints Tech related headlines from the newsite of users choice

import requests, sys, webbrowser, bs4, time

def choice():
    # Providng user the list of websites
    '''
    Returns a tuple with following elements:
        1) website name
        2) address of site
        3) string of CSS selector for element to be searched
    '''
    print('Hi Tech Enthusiast')
    print('Where do you want to get news from?')
    print('1. Gadgets 360')
    print('2. hindustantimes')
    print('3. The IndianEXPRESS')
    choice = int(input('Enter serial number your choice: '))
    site = [('Gadgets 360','https://gadgets.ndtv.com/news', '.caption_box span'), \
     ('hindustantimes', 'https://www.hindustantimes.com/tech/', '.media-body a'), \
     ('The IndianEXPRESS', 'https://indianexpress.com/section/technology/tech-news-technology/', 'h2 a')]
    return site[choice-1]

site_data = choice()
print('Getting news for you. . .') # display text while downloading the news page
res = requests.get(site_data[1])

# checking proper download of webpage
try:
    res.raise_for_status()
except:
    print('Please get an active internet connection and restart the program')

print("Here are today's Tech Headlines from", site_data[0], " :")


soup = bs4.BeautifulSoup(res.text, features="lxml")  # creating a BeautifulSoap object
elems = soup.select(site_data[2])  #obtaining list of required tag objects
count = 1
for i in elems:
    print(count,')', i.getText(), '\n')     #printing each elements text
    count+=1
    time.sleep(2)   #providing a 2s time gap between two headlines

