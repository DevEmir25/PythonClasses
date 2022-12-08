"""
Kullanici arayuzu olacak
Arayuzde parite ve tarih araliklari olacak

"""

# Tkinter kütüphanesini içe aktarın
# Kütüphaneleri içe aktaralım
import tkinter as tk
from tkinter import StringVar, ttk
from tkcalendar import DateEntry
from cryptocmd import CmcScraper
import matplotlib.pyplot as plt
import numpy as np

# Pencere oluşturalım
window = tk.Tk()
window.title("CrytoCurrency Graph Project")
window.geometry('310x200')

tarih_bas = StringVar()
tarih_bit = StringVar()

# Başlangıç ve bitiş tarihi etiketlerini ve giriş alanlarını oluşturalım
start_date_label = tk.Label(window, text="Başlangiç Tarihi:")
start_date_label.grid(column=0, row=0)
cal=DateEntry(window, selectmode='day' ,  textvariable=tarih_bas , date_pattern ='dd-mm-yyyy')
cal.grid(column=1, row=0)

end_date_label = tk.Label(window, text="Bitiş Tarihi:")
end_date_label.grid(column=0, row=1)
cal2=DateEntry(window, selectmode='day' ,textvariable=tarih_bit , date_pattern ='dd-mm-yyyy')
cal2.grid(column=1, row=1)

variable = StringVar(window)
variable.set("BTC") # default value

# Parite seçme seçeneğini oluşturalım
parity_label = tk.Label(window, text="Parite:")
parity_label.grid(column=0, row=2)
values = ["BTC", "ETH", "ADA"]
parity_combo = ttk.OptionMenu(window, variable, *values)
parity_combo.grid(column=1, row=2)

def clickEvent():
    parity = variable.get()
    tarih_baslangic = tarih_bas.get()
    tarih_bitis = tarih_bit.get()
    scraper = CmcScraper(parity, tarih_baslangic, tarih_bitis)
    headers, data = scraper.get_data()
    date_data = []
    close_value = []
    running_average = []
    for i, veri in enumerate(data):
        date_data.append(veri[0])
        close_value.append(veri[4])
        if i > 4:
            average = close_value[i] + close_value[i-1]
            average += close_value[i-2] + close_value[i-3]
            average += close_value[i - 4]
            running_average.append(average/5)
    running_average.append(0)
    running_average.append(0)
    running_average.append(0)
    running_average.append(0)
    date_data.reverse()
    close_value.reverse()
    running_average.reverse()
    plt.plot(date_data, close_value)
    plt.plot(running_average)
    plt.show()
    
# Grafik çizme düğmesini oluşturalım
plot_button = tk.Button(window, text="Grafik Çiz" , bg="orange" , fg="blue" ,command=clickEvent)
plot_button.grid(column=1, row=3,pady= 20)

# Girdiler arasına boşluk ekleyelim
window.columnconfigure(1, pad=60)
window.rowconfigure(1, pad=60)

# Arayüzü gösterelim
window.mainloop()