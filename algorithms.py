import max_horses_in_board as hb
import numpy as np

# Expands the current board of the given path
def expand(path):
    result = []
    successors = hb.get_successors(path[0])

    for successor in successors:
        result.append([successor] + path)

    return result

# Eliminates paths that take to the same state but with a higher cost
def prune(path_list):
    result = []

    if len(path_list) == 0:
        return result

    current_states = [np.zeros(np.shape(path_list[0][0]))]

    for path in path_list:
        if not path_in_list(path[0], current_states):
            current_states.append(path[0])
            result.append(path)

    return result


# Returns True if board is in states
def path_in_list(board, states):
    for state in states:
        if hb.equal_boards(board, state):
            return True

    return False


# Algorithm for A*
def order_astar(old_paths, new_paths, g, h, *args, **kwargs):
    cp = [[old_paths]]
    j = 0
    while cp:
        if not cp:
            return []

        if hb.is_solution(cp[0][0]):
            return list(reversed(cp[0]))

        print(f'-- Paso {j} -- Caminos pendientes')
        for i, c in enumerate(cp):
            print(f'CP[{i}]: ')
            print_camino(c, g(c) + h(c[0]) )

        expansion = new_paths(cp[0])
        print(f'-- Paso {j} -- Expandidos')
        for i, c in enumerate(expansion):
            print(f'E[{i}]: ')
            print_camino(c, g(c) + h(c[0]) )

        unsrt = cp[1:] + expansion
        unsrt.sort(key=lambda x: g(x) + h(x[0]) )
        cp = prune(unsrt)
        j+=1
    print("No se ha encontrado camino")
    return []

def print_camino(c, coste=None, final=False):
  for j, s in enumerate(c):
    if j==0 and not coste is None:
      print(f'S{(j if final else len(c)-j-1)}: [g={coste}] \n{s}')
    else:
      print(f'S{(j if final else len(c)-j-1)}: \n{s}')
  print()


def run():
    board = hb.initial_state(5, 5)
    print(board)
    final_path = order_astar(board, expand, hb.cost_function, hb.heuristic_function)
    print("------------FINAL------------")
    print_camino(final_path, hb.cost_function(final_path), final=True)