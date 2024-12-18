import pandas as pd

# Укажите путь к вашему файлу CSV
file_path = "C:/LessonPython/3Praktik/AZ01/AZ01/index.csv"

# Шаг 1: Загрузка данных в DataFrame
df = pd.read_csv(file_path)

# Шаг 2: Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Шаг 3: Информация о данных
print("\nИнформация о данных:")
print(df.info())

# Шаг 4: Статистическое описание данных
print("\nСтатистическое описание данных:")
print(df.describe())