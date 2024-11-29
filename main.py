from opencage.geocoder import OpenCageGeocode
from tkinter import*
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates" : f"Широта: {lat}, Долгота: {lon} \n Страна: {country} \n Регион: {region} \n Валюта {results[0]['annotations']['currency']['name']}",
                    "map_url" : osm_url
                }
            else:
                return {
                    "coordinates" : f"Широта: {lat}, Долгота: {lon} \n Страна: {country} \n Валюта {results[0]['annotations']['currency']['name']}",
                    "map_url" : osm_url
                }
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


def show_coordinates(event = None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text = f"Координаты города {city}: \n {result['coordinates']}")
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


def clear_results():
    entry.delete(0, END)
    label.config(text="Введите город и нажмите на кнопку")
    global map_url
    map_url = ""


key = '1f8e91418aca4e65b8d5fa8f0fd2ee7d'
map_url = ""

window = Tk()
window.title("Координаты городов")
window.geometry("500x300")


entry = Entry()
entry.pack(padx = 10, pady = 10)
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack(padx = 10, pady = 10)

button = Button(text="Показать карту", command=show_map)
button.pack(padx = 10, pady = 10)

label = Label(text = "Введите город и нажмите на кнопку")
label.pack(padx=10, pady=10)

button_clear = Button(window, text="Очистить", command=clear_results)
button_clear.pack(padx=10, pady=10)

window.mainloop()