import gmplot
import webbrowser
import os
from tkinter import *
def f():
    lat = [19.093706, 13.198382]
    lon = [72.865046,77.714200]
    gmap = gmplot.GoogleMapPlotter(19.093706,72.865046,12)
    gmap.scatter( lat, lon,size = 40, marker = False )
    gmap.plot(lat, lon, 'cornflowerblue', edge_width = 2.5)
    gmap.draw('/Users/fardeenmac/Documents/Gmap/gmap1.html')
    webbrowser.open('file://' + os.path.realpath('/Users/fardeenmac/Documents/Gmap/gmap1.html'))

root = Tk()
root.geometry('300x300')
btn = Button(root, text="Click Me", command=f, width=50, height=10)
btn.pack()

root.mainloop()


# webbrowser.open('https://www.google.com')
