from tkinter import *
import key
import requests


class Weather():
    def __init__(self, root):
        self.root = root
        self.root.title("Weather-O-fy")
        self.root.geometry("450x300+500+300")
        self.search = StringVar()
        title = Label(self.root, text="Weather-o-fy",
                      font=(30), fg="black").place(x=0, y=0, relwidth=1, height=70)
        label_city = Label(self.root, text="Location",
                           font=(15), bg="black", fg="white", anchor="w", padx=5).place(x=0, y=70, relwidth=1, height=40)
        text_city = Entry(self.root, textvariable=self.search, font=(
            15), bg="white", fg="black").place(x=100, y=77, width=230, height=25)
        btn_city = Button(self.root, text="Get Weather", bg="red", fg="black", cursor="hand2").place(
            x=350, y=77, width=80, height=25)
        label_bar = Label(self.root, text="Created by Ani",
                          font=(10), bg="black", fg="white", padx=5).pack(side=BOTTOM, fill=X)

        self.label_cities = Label(self.root, text="City Name",
                                  font=(15), bg="white", fg="black")
        self.place(x=0, y=120, relwidth=1, height=20)

        self.label_temp = Label(self.root, text="Temp",
                                font=(15), bg="white", fg="black")
        self.place(x=0, y=150, relwidth=1, height=20)

        self.label_wind = Label(self.root, text="Wind",
                                font=(15), bg="white", fg="black")
        self.place(x=0, y=180, relwidth=1, height=20)
        self.error = Label(self.root, text="Error",
                           font=(15), bg="white", fg="black")
        self.place(x=0, y=210, relwidth=1, height=20)

    def get_weather(self):
        api_key = w.api_key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.search.get()}&appid={api_key}"
        results = requests.get(url)
        if results:
            json = results.json()
            city = json["name"]
            country = json["sys"]["country"]
            tempc = json["main"]["temp"]-273.15
            tempf = (json["main"]["temp"]-273.15)*9/5+32
            wind = json["weather"][0]["main"]
            print(city, country, tempc, tempf, wind)
            self.label_cities.config(text=city+" "+country)
            degrees = u"\N{DEGREE SIGN}"
            self.label_temp.config(text=round(
                tempc, 2)+degrees+"C |"+round(tempf, 2)+degrees+" f")
            self.label_wind.config(text=wind)
            self.error.config(text=" ")
        else:
            self.label_cities.config(text=" ")
            degrees = u"\N{DEGREE SIGN}"
            self.label_temp.config(text=" ")
            self.label_wind.config(text=" ")
            self.error.config(text="enter valid city ")


root = Tk()
w = Weather(root)
root.mainloop()
