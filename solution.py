import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read().split("\n")

N = int(lines[0].split(" ")[0])
M = int(lines[0].split(" ")[1])

Pizzerias = lines[1:]
List_of_pizzerias = []

M_lines = len(Pizzerias)

NxN_matrix = np.zeros((N, N))

if 1 <= N <= 10000 and 1 <= M <= 10000 and M == M_lines:

    p = 2
    for Pizzeria in Pizzerias:
        Pizzeria = Pizzeria.split(" ")
        Pizzeria = np.array(Pizzeria, dtype=int)

        if 1 <= Pizzeria[0] <= N and 1 <= Pizzeria[1] <= N and 1 <= Pizzeria[2] <= 100:
            pass
        else:
            continue

        List_of_pizzerias.append(Pizzeria)
        p = p + 1

    x = 0
    y = 0

    try:
        for Pizzeria in List_of_pizzerias:
            for block in np.nditer(NxN_matrix):

                if x > (N - 1):
                    x = 0
                    y = y + 1

                if y > (N - 1):
                    y = 0

                Diff_x = (Pizzeria[0] - 1) - x
                Diff_x = abs(Diff_x)
                Diff_y = (Pizzeria[1] - 1) - y
                Diff_y = abs(Diff_y)
                R = Diff_y + Diff_x

                if R <= (Pizzeria[2]):
                    NxN_matrix[x, y] = NxN_matrix[x, y] + 1
                x = x + 1

        print(NxN_matrix.max())

    except IndexError:
        pass
else:
    pass


