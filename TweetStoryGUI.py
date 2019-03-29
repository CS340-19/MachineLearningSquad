import tkinter as tk
import requests
import json

class Window(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=150, height=50)
        self.boxes = list()
        self.submit = tk.Button(self, text = "Get Stories", command=self.GetStoriesFromUrl)
        self.submit.pack()
        self.url = tk.Entry(self, width = 75)
        self.url.pack()
    def GetStoriesFromUrl(self):
        for x in self.boxes:
            x.pack_forget();
        s = self.url.get()
        s = s[s.rfind("/")+1:]
        url = "http://107.161.31.193:5000/?tweetid="+s
        print(url)
        r = requests.get(url)
        if r.status_code != 200:
            print("bad url");
            quit()
        stories = r.json();
        for x in stories:
            print(x)
            v = tk.Label(self, text = x["title"], font=("Helvetica", 20))
            self.boxes.append(v)
            v.pack();

            d = tk.Label(self, text = x["description"], font=("Helvetica", 12))
            self.boxes.append(d)
            d.pack()

            l = tk.Label(self, text = x["link"], font=("Courier", 10))
            self.boxes.append(l)
            l.pack()


root = tk.Tk()
W = Window(root)
W.pack()
root.mainloop()
