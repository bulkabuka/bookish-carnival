import numpy as np


def seidel(matrix, vector, approximation, max_steps, tolerance):
    print("\nМетод Зейделя\n-----------")
    n = len(matrix)
    x = approximation
    step = 1

    for k in range(max_steps):
        x_old = x.copy()

        for i in range(n):
            sum1 = sum(matrix[i][j] * x[j] for j in range(i))
            sum2 = sum(matrix[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (vector[i] - sum1 - sum2) / matrix[i][i]

        print(f"Итерация {step}: {x}")
        step += 1

        if all(abs(x[i] - x_old[i]) < tolerance for i in range(n)):
            return x

    print("\nВ заданное количество шагов метод не сошелся, возвращаю последнюю итерацию.")
    return x


def jacobi(matrix, vector, approximation, max_steps, tolerance):
    print("\nМетод Итераций\n-----------")
    n = len(matrix)
    x = approximation
    step = 1

    for k in range(max_steps):
        x_old = x.copy()

        for i in range(n):
            sum1 = sum(matrix[i][j] * x_old[j] for j in range(i))
            sum2 = sum(matrix[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (vector[i] - sum1 - sum2) / matrix[i][i]

        print(f"Итерация {step}: {x}")
        step += 1

        if all(abs(x[i] - x_old[i]) < tolerance for i in range(n)):
            return x

    print("\nВ заданное количество шагов метод не сошелся, возвращаю последнюю итерацию.")
    return x
