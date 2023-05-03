import PySimpleGUI as sg

import numerical


def create_layout(n):
    left_matrix_layout = [[sg.Input(size=(5, 1), key=("left", i, j)) for j in range(n)] for i in range(n)]
    right_matrix_layout = [[sg.Input(size=(5, 1), key=("right", i))] for i in range(n)]

    layout = [
        [sg.Text("Введите матрицу коэффициентов:")],
        *left_matrix_layout,
        [sg.Text("Введите результирующий вектор:")],
        *right_matrix_layout,
        [sg.Text("Кол-во итерации"), sg.Input(key="iterations",size=(5, 1)),
         sg.Text("Точность"), sg.Input(key="tolerance", size=(7, 1))],
        [sg.Button("Увеличить Размер"), sg.Button("Уменьшить Размер"), sg.Button("Решить"), sg.Button("Выход")],
        [sg.Text("Решение:"), sg.Text("", key="solution")],
    ]
    return layout


def main():
    n = 2
    sg.theme("DarkPurple1")
    window = sg.Window("Решение Систем Уравнений", create_layout(n))

    while True:
        event, values = window.read()
        print(values)

        if event in (sg.WIN_CLOSED, "Выход"):
            break
        elif event == "Увеличить Размер":
            n += 1
            window.close()
            window = sg.Window("Решение Систем Уравнений", create_layout(n))
        elif event == "Уменьшить Размер":
            n = max(2, n - 1)
            window.close()
            window = sg.Window("Решение Систем Уравнений", create_layout(n))
        elif event == "Решить":
            try:
                matrix = [[float(values[("left", i, j)]) for j in range(n)] for i in range(n)]
                right_vector = [float(values[("right", i)]) for i in range(n)]
                tolerance = float(values["tolerance"])
                iterations = int(values["iterations"])
                solution = "Метод Зейделя\n"
                solution += '\n'.join(numerical.seidel(matrix, right_vector, [0] * n, iterations, tolerance))
                solution += "\n\nМетод Итераций\n"
                solution += '\n'.join(numerical.jacobi(matrix, right_vector, [0] * n, iterations, tolerance))
                window["solution"].update(solution)
                # window += numerical.jacobi(matrix, right_vector, [0] * n, 20, 0.0001)
            except Exception as e:
                sg.popup_error(f"Ошибка: {e}")

    window.close()


if __name__ == "__main__":
    main()