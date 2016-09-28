import feedparser
import tkinter
from tkinter import *
import random
import time
import webbrowser
from _thread import start_new_thread
import urllib.request


ran=100
display_pane=Tk(className='mReel')
display_pane.iconbitmap(r'mReel.ico')
var=StringVar()
text=Label(display_pane,textvariable=var,bg='black',fg='green',font='fixedsys')
def callback(one):
    webbrowser.open(run.link_rotate['link'])
def title(choice):
    choice=urllib.request.urlopen(run.link_rotate).read()
    title=str(choice).split('<title>')[1].split('</title>')[0]
    return title
def run():
    run.link_rotate=random.choice(feed_now['entries'])
    var.set(run.link_rotate['title'])
    text.bind("<Button-1>",callback)
    text.update_idletasks()
    text.pack()
    time.sleep(11)
def app_launch():
    while ran!=0:
       run()
feedlist=[]
f=open('playlist.feed','r')
while True:
   for lines in f:
       feedlist.append(lines)
   for feeds in feedlist:
      feed_now=feedparser.parse(feeds)
   start_new_thread(app_launch,())
   display_pane.mainloop()

      

