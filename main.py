# Это программа на Python
# Импортируем модуль sqlite3
import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect("solutions1.db")

# Создаем курсор для работы с базой данных
cur = conn.cursor()

# Создаем таблицу для хранения решений
cur.execute("CREATE TABLE IF NOT EXISTS solutions (a INTEGER, b INTEGER, c INTEGER, a_cubed INTEGER, b_cubed INTEGER, c_cubed INTEGER, Begin INTEGER, End INTEGER)")

# Задаем диапазон значений для a, b и c
Begin = 2
End = 20001

# Вставляем данные в таблицу
for a in range(Begin,End):
    for b in range(Begin,End):
        for c in range(Begin,End):
            if(a**3 + b**3 == c**3+1):
                # Выводим решение
                print (a,'³','+',b,'³','=',c,'³','+1', '|', a ** 3,'+',b ** 3,'=',c ** 3,'+1', '|', Begin, End)

                # Если да, то вставляем решение и пределы в таблицу solutions
                cur.execute("INSERT INTO solutions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (a, b, c, a**3, b**3, c**3, Begin, End))

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()