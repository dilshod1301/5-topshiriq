# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u0AvtHeL2Qoj9uW_tRnpKj8HTKDDrEha
"""

import pandas as pd
baza={
    "FIISH":["Ikromaliyev Dilshodbek ","Abduhahharov Diyorbek " ,"Muminova Muharram","Alloberdiyeva Odina", "Musohonova Madina","Baxriddinoov Inomjan","Usmonjonov Ravshan" ],
    "Yoshi":['7','10','17','16','11','12','9'  ],
    "Maktabi":["53-maktab" ,"32-maktab","39-maktab","33-maktab","32-maktab","3-maktab","2-maktab" ],
    "Jinsi":[  "erkak","erkak","ayol","ayol","ayol","erkak","erka"],
    "Manzili":[ "Namangan shahar","Namangan shahar","Namangan shahar","Toshkent shahar","Namangan shahar","Andijon shahar","Fargona shahar" ]
}
db=pd.DataFrame(baza)
print(db)

Filtr=db[(db['Yoshi']=='7') &(db['Jinsi']=='erkak')]
print(Filtr)

data = {
    "Temirxanova Sug'diyona": {"tug'ilgan sana": "2006-03-18", "maktab": "20-maktab"},
    "Aliyev Anvar": {"tug'ilgan sana": "2005-06-15", "maktab": "15-maktab"},
    "Karimova Madina": {"tug'ilgan sana": "2007-08-21", "maktab": "10-maktab"}
}

# Qidirilayotgan ism-familiyalar ro'yxati
search_names = ["Temirxanova Sug'diyona", "Karimova Madina", "Akbarov Diyor"]

# Qidiruv funksiyasi
def search_data(names, database):
    results = {}
    for name in names:
        if name in database:
            results[name] = database[name]
        else:
            results[name] = "Ma'lumot topilmadi"