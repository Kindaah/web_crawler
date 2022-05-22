from cProfile import label
from fileinput import close
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests 
from requests import request
import jsonschema

page_count = 1
next_url = ""
is_over_ten = False
while not is_over_ten: 
    url = "https://fuckinghomepage.com/"
    if len(next_url) == 0:
        response = urlopen(url)
    else:
        # print(next_url)
        response = urlopen(next_url)
        page_count = page_count + 1
    the_page = response.read()
    # print(the_page)
    soup = BeautifulSoup(the_page, 'html.parser')


    print(soup.findAll('a')[0])
    print(soup.findAll('a')[0] .getText())
    print(soup.findAll('p')[0].getText())
    print(soup.findAll('p')[2].getText())
    # print(len(soup.findAll('small')))
    # print(soup.findAll('small'))
    #to find the Titles texts of links: 
    # We can either use ID attribute or CSS selector 
    # print(soup.findAll(id = 'text').getText())

    #print(soup.select("p"))

    print(soup.findAll('a')[1])
    print(soup.findAll('a')[1] .getText())
    print(soup.findAll('p')[1].getText())
    print(soup.findAll('p')[4].getText())
    # print(len(soup.findAll('small')))

    # print(soup.findAll('small'))      
    print(soup.findAll('a')[2])
    print(soup.findAll('a')[2] .getText())
    print(soup.findAll('p')[2].getText())
    print(soup.findAll('p')[6].getText())

    print(soup.findAll('a')[3])
    print(soup.findAll('a')[3] .getText())
    print(soup.findAll('p')[3].getText())
    print(soup.findAll('p')[8].getText())

    print(soup.findAll('a')[4])
    print(soup.findAll('a')[4] .getText())
    print(soup.findAll('p')[4].getText())
    print(soup.findAll('p')[10].getText())

    print(soup.findAll('a')[5])
    print(soup.findAll('a')[5] .getText())
    print(soup.findAll('p')[5].getText())
    print(soup.findAll('p')[12].getText())


    # section one contain word of the day text and link


    #"Quote of the Day: QOD"
    label1 = "QOD"
    title1 = soup.findAll('small')[0].getText()
    content_section1 = soup.findAll('p')[2].getText()
    link_section1 = "None"

    print("section: " + label1, "\nTitle: " + title1, "\nContent: " + content_section1, "\nLink: " + link_section1, "\n")
    # print(label1 + title1 + content_section1 + link_section1)

    section1 ={ "section" : label1, "title" : title1, "content" : content_section1, "link" : link_section1 }

    section2 = ["article of the day: AOD"]
    label2 = "AOD"
    title2 = soup.findAll('small')[1].getText()
    content_section2 = soup.findAll('p')[4].getText()
    link_section2 = soup.findAll('a')[1]['href']
    print("section: " + label2, "\nTitle: " + title2, "\nContent: " + content_section2, "\nLink: " + link_section2, "\n")

    section2 ={ "section" : label2, "title" : title2, "content" : content_section2, "link" : link_section2 }

    # section3 = ["Book of the day: BOK"]
    label3 = "BOK"
    title3 = soup.findAll('small')[2].getText()
    content_section3 = soup.findAll('p')[6].getText()
    link_section3 = soup.findAll('a')[2]['href']

    section3 ={ "section" : label3, "title" : title3, "content" : content_section3, "link" : link_section3 }

    # section4 = ["Product of the Day: POD"]
    label4 = "POD"
    title4 = soup.findAll('small')[3].getText()
    content_section4 = soup.findAll('p')[8].getText()
    link_section4 = soup.findAll('a')[3]['href']

    section4 ={ "section" : label4, "title" : title4, "content" : content_section4, "link" : link_section4 }

    # section5 = ["Website of the Day: WOD"]
    label5 = "WOD"
    title5 = soup.findAll('small')[4].getText()
    content_section5 = soup.findAll('p')[10].getText()
    link_section5 = soup.findAll('a')[4]['href']

    section5 ={ "section" : label5, "title" : title5, "content" : content_section5, "link" : link_section5 }

    # section6 = ["video of the day: VOD"]
    label6 = "VOD"
    title6 = soup.findAll('small')[5].getText()
    content_section6 = soup.findAll('p')[12].getText()
    link_section6 = soup.findAll('a')[5]['href']

    section6 ={ "section" : label6, "title" : title6, "content" : content_section6, "link" : link_section6 }

    button_location = 0 if len(next_url) == 0 else 1 
    print(button_location)
    print(soup.find('div', {'id': 'Footer'}).findAll('a'))
    page_url = soup.find('div', {'id': 'Footer'}).findAll('a')[button_location]['href']
    print(page_url)
    next_url = url[0:-1] + page_url
    is_over_ten = True if int(page_url[6:]) > 10 else False 
    print(next_url)

    with open('posts_list.txt', 'w') as posts_list: 
        posts_list.writelines("section: " + label1 + "\nTitle: " + title1 + "\nContent: " + content_section1 + "\nLink: " + link_section1 + "\n\n")
        posts_list.writelines("section: " + label2 + "\nTitle: " + title2 + "\nContent: " + content_section2 + "\nLink: " + link_section2 + "\n\n")
        posts_list.writelines("section: " + label3 + "\nTitle: " + title3 + "\nContent: " + content_section3 + "\nLink: " + link_section3 + "\n\n")
        posts_list.writelines("section: " + label4 + "\nTitle: " + title4 + "\nContent: " + content_section4 + "\nLink: " + link_section4 + "\n\n")
        posts_list.writelines("section: " + label5 + "\nTitle: " + title5 + "\nContent: " + content_section5 + "\nLink: " + link_section5 + "\n\n")
        posts_list.writelines("section: " + label6 + "\nTitle: " + title6 + "\nContent: " + content_section6 + "\nLink: " + link_section6 + "\n\n")
    close
        
    with open('data.json', 'a') as data: 
        section1_vr = json.dumps(section1)
        if page_count == 1: 
            data.writelines("[")
        data.writelines(section1_vr)
        data.writelines(",")
        section2_vr = json.dumps(section2)
        data.writelines(section2_vr)
        data.writelines(",")
        section3_vr = json.dumps(section3)
        data.writelines(section3_vr)
        data.writelines(",")
        section4_vr = json.dumps(section4)
        data.writelines(section4_vr)
        data.writelines(",")
        section5_vr = json.dumps(section5)
        data.writelines(section5_vr)
        data.writelines(",")
        section6_vr = json.dumps(section6)
        data.writelines(section6_vr)
        print(is_over_ten)
        if is_over_ten:
            data.writelines("]")
        else:
            data.writelines(",")
    close

   


#div class = PostBody
#convert the sections to dictionary or a class 

# PostBody = soup.find_all('div', {'class': 'PostBody'})



# quote = []
# title = []
# links = []
# for item in soup.findAll('small'):
#     # if small doens't have a string of a tag or if it has more, return small
#     if ("more" not in item.getText()):
#         quote.append([item.getText()])
#         print(item)
# for item in soup.findAll('small'):
#     print("Links")
#     print(item)
#     print(len(item.findAll("a")))
#     links.append([len(item.findAll("a"))])


# posts_list = zip(quote, title, links)


