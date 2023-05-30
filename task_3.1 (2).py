class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for _ in range(columns)] for _ in range(rows)]

    def set_value(self, row, column, value):
        if 1 <= row <= self.rows and 1 <= column <= self.columns:
            self.matrix[row-1][column-1] = value
        else:
            print("Неправильный номер столбца или строки.")

    def get_value(self, row, column):
        if 1 <= row <= self.rows and 1 <= column <= self.columns:
            return self.matrix[row-1][column-1]
        else:
            print("Неправильный номер столбца или строки.")
            return None

    def get_num_rows(self):
        return self.rows

    def get_num_columns(self):
        return self.columns


# Пример использования класса Matrix:

# Создание матрицы 10 на 10 и заполнение ее единицами
matrix = Matrix(10, 10)
for row in range(1, matrix.get_num_rows() + 1):
    for column in range(1, matrix.get_num_columns() + 1):
        matrix.set_value(row, column, 1)

# Вывод значения в ячейке (3, 5)
print(matrix.get_value(3, 5))  # Вывод: 1

# Замена значения в ячейке (3, 5) на 5
matrix.set_value(3, 5, 5)

# Вывод обновленного значения в ячейке (3, 5)
print(matrix.get_value(3, 5))  # Вывод: 5

# Вывод количества строк и столбцов
print(matrix.get_num_rows())  # Вывод: 10
print(matrix.get_num_columns())  # Вывод: 10
