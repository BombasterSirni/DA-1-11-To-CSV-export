import numpy as np
import pandas as pd
import os
from sklearn.datasets import make_classification #Для создания синтетического датафрейма

#Генерация синтетического датафрейма
X, y = make_classification(n_samples=400, n_features=5, random_state=52)
data = pd.DataFrame(X, columns=['A', 'B', 'C', 'D', 'E'])
data['Target'] = y

#Просмотр верхушки таблицы
print(data.head(5))

#Экспортируем в CSV
data.to_csv("CSV-SYNTHODATA.csv", index=None)

#Проверка экспорта
print(f"Файл в папке? {os.path.exists('CSV-SYNTHODATA.csv')}")