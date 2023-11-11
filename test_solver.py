import solver

input_grid = [[5, 0, 0, 0, 8, 0, 0, 4, 9],
              [0, 0, 0, 5, 0, 0, 0, 3, 0],
              [0, 6, 7, 3, 0, 0, 0, 0, 1],
              [1, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 2, 0, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 8],
              [7, 0, 0, 0, 0, 4, 1, 5, 0],
              [0, 3, 0, 0, 0, 2, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    sg = solver.solve_gen(input_grid)
    for i in sg:
        print(i)
