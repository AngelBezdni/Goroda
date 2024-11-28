import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_t_label(event):
    t_code = t_combobox.get()
    name = cur[t_code]
    t_label.config(text=name)


def update_b_label(event):
    b_code = b_combobox.get()
    name = cur[b_code]
    b_label.config(text=name)

def update_second_b_label(event):
    second_b_code = second_b_combobox.get()
    name = cur[second_b_code]
    second_b_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    second_base_currency = second_b_combobox.get()

    if t_code and b_code and second_base_currency:
        try:
            # Первый запрос для первой базовой валюты
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()

            if t_code in data['rates']:
                first_exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]

                # Второй запрос для второй базовой валюты
                second_response = requests.get(f'https://open.er-api.com/v6/latest/{second_base_currency}')
                second_response.raise_for_status()
                second_data = second_response.json()

                if t_code in second_data['rates']:
                    second_exchange_rate = second_data['rates'][t_code]
                    second_b_name = cur[second_base_currency]

                    # Форматируем сообщение с двумя курсами
                    message = (
                        f"Курс {first_exchange_rate:.2f} {t_name} за 1 {b_name}\n"
                        f"Курс {second_exchange_rate:.2f} {t_name} за 1 {second_b_name}"
                    )
                    mb.showinfo("Курсы обмена", message)
                else:
                    mb.showerror("Ошибка", f"Валюта {t_code} не найдена для второй базовой валюты")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите коды валют")


cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
}

window = Tk()
window.title("Курс обмена валют")
window.geometry("400x700")

Label(text="Первая базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта").pack(padx=10, pady=10)
second_b_combobox = ttk.Combobox(values=list(cur.keys()))
second_b_combobox.pack(padx=10, pady=10)
second_b_combobox.bind("<<ComboboxSelected>>", update_second_b_label)

second_b_label = ttk.Label()
second_b_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курсы обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()