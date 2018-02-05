######################################## list view
# y = [200, 300, 4000]
# x = ['demo','demo']
# x.append(y)

######################################## condition
# if x[0] == 120:
#     print(str(x[0])+" is equal to 120")
# elif x[0] == 'demo':
#     print(str(x[0])+" is equal to demo")
# else:
#     print("Wrong input")

# print(len(x))
# #for loop
# for index in x:
#     print(index)

####################################### range
# for index in range(5,20, 2):
#     print(index)

############################################## while loop
# lst = []
# x = 200
# while x > 0:
#     lst.append(x)
#     x -= 10

# print(lst)

######################################## continue break statement
# x = 200
# lst = []
# while x > 0:
#     x -= 5
#     if x == 100:
#         continue
#     elif x == 50:
#         break
#     lst.append(x)
# print(lst)

######################################### function 
# def bitcoin_to_usd(btc):
#     usd = 9810.73*btc
#     return usd

# usd = bitcoin_to_usd(5)
# print('$'+str(usd))

######################################### set
# mySet = {'apple', 'banana', 'cake', 'banana'}
# print(mySet)

##################################### dictionary
# rahim = {'age': 26, 'varsity': 'uiu'}
# karim = {'age': 27, 'varsity': 'diu'}
# gopal = {'age': 28, 'varsity': 'ulab'}
# users = {'rahim': rahim, 'karim': karim, 'gopal': gopal}

# for k, v in users.items():
#     print(str(k)+": " +str(v))

################################## Download image
# import random
# import urllib.request

# def download_web_image(url):
#     name = random.randrange(20000,70000)
#     image_name = str(name)+".jpg"
#     urllib.request.urlretrieve(url, image_name)
#     return image_name

# download_web_image('https://artfiles.alphacoders.com/910/91054.jpg')

################################ file read write
# fw = open('sample.txt', 'w')
# fw.write("Hello there,\nThis is a file full with dummy data.\nThis file is created only for demo purpose.")
# fw.close()

# fr = open('sample.txt', 'r')
# text_data = fr.read()
# print(text_data)

############################### web crawler
# import requests
# from bs4 import BeautifulSoup

# def trade_spider(url, className):
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for link in soup.find_all('li', {'class': className}):
#         print(link.string)

# site_url = "https://www.amazon.com/s/ref=sr_qz_back?sf=qz%2Crba&rh=i%3Amobile%2Ck%3Amobile&keywords=mobile&unfiltered=1&ie=UTF8&qid=1517822790"
# trade_spider(site_url, "s-result-item")