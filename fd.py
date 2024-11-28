import requests
import json
import pprint
from tkinter import*
from tkinter import messagebox as mb


def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rates = data['rates'][code]
                #{exchange_rates:.2f}
                mb.showinfo("Курс обмена", f"Курс {exchange_rates} за 1 USD")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произшла ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты")


# result = recuests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)

# p = pprint.PrettyPrinter(indent=4)

# p.pprint(data)

window = Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к USD", command=exchange).pack(padx=10,pady=10)

window.mainloop()
