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

################################### Class
# class Anime:
#     name = ''
#     def __init__(self, name = ''): # it's a constructor
#         self.name = name
#         if name == '':
#             print("I love anime")
#         else:
#             print(str(name) + " loves anime")
#     def one_piece(self):
#         print("Chapter 893 is the best chapter so far in Whole Cake Island")
#     def naruto(self):
#         print("Shadow clone jutsu is the best jutsu Naruto has ever used")
#     def get_name(self):
#         return self.name

# anime1 = Anime() 
# anime2 = Anime("Shaion")
# print(anime1.get_name())
# print(anime2.get_name())

# class Enemy:
#     lifespan = 3
#     def attack(self):
#         print('You are being attacked')
#         self.lifespan -= 1
#     def check_life(self):
#         if self.lifespan <= 0:
#             print("You are dead")
#         else:
#             print("You have " + str(self.lifespan) +" lifes left")

# enemy = Enemy()
# enemy.attack()
# enemy.check_life()
# enemy.attack()
# enemy.check_life()
# enemy.attack()
# enemy.check_life()

################################# Inheritance
# class Anime():
#     def carton(self):
#         print('Anime is not carton')

# class Carton(Anime):
#     def carton_and_anime(self, carton = ''):
#         print(carton + ' is a carton as well as anime')

# carton = Carton()
# carton.carton()
# carton.carton_and_anime("One Piece")

# class Anime():
#     def __init__(self):
#         print("Hello Anime Lover")
#     def anime_lover(self):
#         print("I love anime")
    
# class Manga():
#     def __init__(self):
#         print("Hello Manga Lover")
#     def manga_lover(self):
#         print("I love manga")

# class User(Anime, Manga):
#     # def __init__(self):
#     #     Manga()
#     pass
    

# user = User()
# user.anime_lover()
# user.manga_lover()

################################## Threading
# import threading
# class Messanger(threading.Thread):
#     # def __init__(self, name, message):
#     #     threading.__init__()
#     #     print(str(name)+" "+str(message))
#     def run(self):
#         for _ in range(20):
#             print(threading.currentThread().getName())

# messanger1 = Messanger(name="Messanger 1 is running")
# messanger2 = Messanger(name="Messagner 2 is running")

# messanger1.start()
# messanger2.start()

##################################### zip 
# first_name = ["Mahmudul", "Tanvir", "Shaion"]
# last_name = ['Hasan', 'Hasan', 'Ahamed']
#
# name = zip(first_name, last_name)
# for fname, lname in name:
#     print(fname, lname)

########################################### image processing
################### Croping Image
# from PIL import Image
# luffy = Image.open("../luffy.png")
# #
# luffy_width = int(luffy.size[0]/2)
# luffy_height = int(luffy.size[1]/2)
# # #
# area = (int(luffy.size[0]/4),0, luffy_width+int(luffy.size[0]/4), luffy_height)
#
# luffy.crop(area).show()

########################### merge and effect image
# from PIL import Image
# luffy = Image.open("../luffy.png")
# zoro = Image.open("../zoro.jpg")
# #
# luffy_width = int(luffy.size[0]/2)
# luffy_height = int(luffy.size[1]/2)
# #
# # print(str(luffy_width)+" "+str(luffy_height))
# luffy = luffy.resize((luffy_width, luffy_height), Image.ANTIALIAS)
# # #
# area = (0,0, luffy_width, luffy_height)
# zoro.paste(luffy, area)
# luffy = luffy.resize((zoro.size[0], zoro.size[1]), Image.ANTIALIAS)
# #
# r1, g1, b1 = zoro.split()
# r2, g2, b2, a1 = luffy.split()
# new_img = Image.merge("RGB", (r1, g2, b1))
# new_img.show()

########### image filter
# from PIL import Image
# from PIL import ImageFilter
#
# zoro = Image.open("../zoro.jpg")
# blur = zoro.filter(ImageFilter.BLUR)
# detail = zoro.filter(ImageFilter.DETAIL)
# edges = zoro.filter(ImageFilter.FIND_EDGES)
# edges_enhance = zoro.filter(ImageFilter.EDGE_ENHANCE)
#
# blur.show();
# detail.show();
# edges.show();
# edges_enhance.show();



