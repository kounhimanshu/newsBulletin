import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import time
import random


def screen(root):
    l1 = Label(root,
        justify= 'center',
        text="News Bulletin",
        padx=0,
        pady=0,
        bg= "DarkSlateBlue",
        font=('Helvetica', 22),
        fg="white"
    ).place(x=85, y= 150)

    l1 = Label(root,
        justify= 'center' ,
        text="Developed with passion by Himanshu",
        padx=0,
        pady=0,
        bg= "DarkSlateBlue",
        font=('Helvetica', 10),
        fg="white"
    ).place(x=60, y= 200)

    l1 = Label(root,
        justify= 'center' ,
        text="click and wait for a moment to load",
        padx=0,
        pady=0,
        bg= "DarkSlateBlue",
        font=('Helvetica', 8),
        fg="white"
    ).place(x=90, y= 580)
    
    i = Button(root,
            text= "Go to News",
            width= 20, 
            bg= "DarkSlateBlue",
            activebackground= "DeepPink",
            command=lambda: change(root))
    i.config(fg='white')
    i.place(x=100, y = 450)

def change(root):
    root.destroy()
    # print("destroyed")

def load_gui():
    root = Tk()
    root.geometry('350x600')
    root.resizable(0,0)
    # root.iconbitmap('newspaper.ico')
    root.title('NewsBulletin')
    root.configure(background='DarkSlateBlue')
    screen(root)
    root.mainloop()

load_gui()



class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        r = random.randint(0, 20)
        self.load_news_item(r)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        # self.root.iconbitmap('newspaper.ico')
        self.root.title('NewsBulletin')
        self.root.configure(background='DarkSlateBlue')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        # print('hi')

        if index == -1:
            index = 19
        if index == 20:
            index = 0

        # clear the screen for the new news item
        self.clear()

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo,bg= "DarkSlateBlue")
        label.pack()

		#Heading
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg= "DarkSlateBlue",fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))


		#Details
        details = Label(self.root, text=self.data['articles'][index]['description'], bg= "DarkSlateBlue", fg='white', wraplength=350,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg= "DarkSlateBlue")
        frame.pack(expand=True,fill=BOTH)

        # print(index)

        

        prev = Button(frame,text='Prev',width=16,height=3,activebackground= "DeepPink",command=lambda :self.load_news_item(index-1))
        prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3,activebackground= "DeepPink",command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)


        next = Button(frame, text='Next', width=16, height=3,activebackground= "DeepPink",command=lambda :[self.load_news_item(index+1)])
        next.pack(side=LEFT)





        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()