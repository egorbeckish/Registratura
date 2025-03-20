def matrix_rank(matrix_1d, rows, cols):
    # Функция для вычисления определителя подматрицы
    def determinant(submatrix, n):
        if n == 1:
            return submatrix[0]
        if n == 2:
            return submatrix[0] * submatrix[3] - submatrix[1] * submatrix[2]
        det = 0
        for col in range(n):
            # Создаем подматрицу для минора
            minor = []
            for i in range(1, n):
                for j in range(n):
                    if j != col:
                        minor.append(submatrix[i * n + j])
            # Рекурсивно вычисляем определитель минора
            det += ((-1) ** col) * submatrix[col] * determinant(minor, n - 1)
        return det

    # Функция для получения подматрицы (минора) из одномерного массива
    def get_submatrix(matrix_1d, rows, cols, selected_rows, selected_cols):
        submatrix = []
        for i in selected_rows:
            for j in selected_cols:
                submatrix.append(matrix_1d[i * cols + j])
        return submatrix

    # Функция для генерации всех комбинаций
    def generate_combinations(n, k):
        combinations = []
        def backtrack(start, path):
            if len(path) == k:
                combinations.append(path)
                return
            for i in range(start, n):
                backtrack(i + 1, path + [i])
        backtrack(0, [])
        return combinations

    # Основная логика
    rank = min(rows, cols)
    for k in range(rank, 0, -1):
        # Генерация всех комбинаций строк и столбцов
        row_combinations = generate_combinations(rows, k)
        col_combinations = generate_combinations(cols, k)
        # Проверка всех миноров порядка k
        for rows_comb in row_combinations:
            for cols_comb in col_combinations:
                submatrix = get_submatrix(matrix_1d, rows, cols, rows_comb, cols_comb)
                det = determinant(submatrix, k)
                if det != 0:
                    return k
    return 0

# Пример использования
matrix_1d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Представление матрицы 3x4 в виде одномерного массива
rows = 3
cols = 4

rank = matrix_rank(matrix_1d, rows, cols)
print(f"Ранг матрицы: {rank}")
