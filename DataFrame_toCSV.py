import numpy as np
import pandas as pd
import os
from sklearn.datasets import make_classification #Для создания синтетического датафрейма


# Генерация синтетического датасета
def getSynthoDataset(n_samples, n_features, random_seed):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, random_state=random_seed)
    data = pd.DataFrame(X, columns=[i for i in range(1, n_features+1)])
    data['Target'] = y
    
    return data



# Экспорт датафрейма data в CSV-файл по пути 
def exportToCsv(data, export_filename=None, separator=",", nan_input='', idxs=None):
    
    # data.to_csv вернет None, если export_file не пуст и произошел экспорт (если export_filename корректен)
    # Если data.to_csv вернет строковое значение, значит путь (название файла экспорта) не был указан как параметр
    export_result = data.to_csv(export_filename, sep=separator, na_rep=nan_input, index=idxs)
    
    if(export_result == None):
        print(f"Датафрейм был экспортирован в {export_filename}? {os.path.exists(export_filename)}")
    else:
        print("Вы не указали путь к экспорт-файлу")
    

# Основная функция 
def main():
    
    filename = input("Введите путь к экспорт-файлу в string-формате: ")
    n_samples, n_features, rand_seed = list(map(int, 
                                                input("Введите кол-во строк, признаков датафрейма, а также случайное число: ").split()))
    sep = input("Введите разделитель: ")
    nans_input = input("Введите символ, чем заполнять пропуски: ")
    
    new_dataset = getSynthoDataset(n_samples=n_samples, n_features=n_features, random_seed=rand_seed)
    exportToCsv(new_dataset, filename, separator=sep, nan_input=nans_input, idxs=None)
    
    
main()