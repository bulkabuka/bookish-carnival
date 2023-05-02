import numpy as np
from prettytable import PrettyTable
import sys

import numerical


def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Введите строку {i + 1}: ").split()))
        if len(row) != cols:
            print("Неправильный набор значений. Выход.")
            sys.exit(1)
        matrix.append(row)
    return matrix


def input_vector(length):
    vector = list(map(float, input("Введите вектор (разделяйте значения пробелом): ").split()))
    if len(vector) != length:
        print("Неправильный набор значений. Выход.")
        sys.exit(1)
    return vector


def main():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    approximation = [0, 0, 0]
    max_steps = 20
    tolerance = 1e-6

    print("\nМатрица\n------")
    matrix = input_matrix(rows, cols)

    print("\nВектор\n------")
    vector = input_vector(rows)

    table = PrettyTable()
    for i in range(rows):
        table.add_row(matrix[i])

    print("\nВведенная матрица:")
    print(table)

    table = PrettyTable(["Вектор"])
    for value in vector:
        table.add_row([value])

    print("\nВведенный вектор:")
    print(table)

    result = numerical.seidel(matrix, vector, approximation, max_steps, tolerance)
    result2 = numerical.jacobi(matrix, vector, approximation, max_steps, tolerance)
    print("\nРешение методом Зейделя:", result)
    print("\nРешение методом Итераций:", result2)


if __name__ == "__main__":
    main()
