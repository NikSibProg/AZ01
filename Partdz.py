import pandas as pd

# Путь к файлу
file_path = 'dz.csv'

# Чтение данных из CSV-файла
data = pd.read_csv(file_path)

# Удаление строк с отсутствующими значениями в столбцах 'City' или 'Salary'
cleaned_data = data.dropna(subset=['City', 'Salary'])

# Группировка по городам и расчет средней зарплаты
average_salary_by_city = cleaned_data.groupby('City')['Salary'].mean()

# Вывод результата
print("Средняя зарплата по городам:")
for city, avg_salary in average_salary_by_city.items():
    print(f"{city}: {avg_salary:.2f}")
