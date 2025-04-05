from simpleai.search import SearchProblem
from simpleai.search import breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, greedy, astar

inicial = (
    (7,2,4),
    (5,0,6),
    (8,3,1,)
)
goal = (
    (1,2,3),
    (4,5,6),
    (7,8,0,)
)

def find_piece(state,piece):
    for idx_row, row in enumerate(state):
        for idx_col, current_piece in enumerate(row):
            if current_piece == piece:
                return idx_row, idx_col

class EightPuzzleProblem(SearchProblem):

    # Función de Costo
    def cost(self,state,action,state2):
        return 1

    #Función Meta
    def is_goal(self,state):
        return state == goal

    #Función Actions
    def actions(self,state):
        zero_row, zero_col = find_piece(state,0)
        available_actions = [ ]
        moves = [
            (zero_row-1,zero_col),
            (zero_row+1,zero_col),
            (zero_row,zero_col-1),
            (zero_row,zero_col+1)
        ]
        
        for new_row, new_col in moves:
            if 0 <= new_row <= 2 and 0 <= new_col <= 2:
                piece = state[new_row][new_col]
                available_actions.append(piece)
        return available_actions

    #Función Result
    def result(self,state,action):
        zero_row, zero_col = find_piece(state,0)
        piece_row, piece_col = find_piece(state,action)
        #Convierto la tupla a lista
        state = list(list(row) for row in state)

        state[zero_row][zero_col] = action
        state[piece_row][piece_col] = 0

        state = tuple(tuple(row) for row in state)

        return state

    #Función heurística sólo para algoritmos informados
    def heuristic(self,state):
        total_distance = 0
        for piece in range(1,9):
            row,col = find_piece(state,piece)
            goal_row,goal_col = find_piece(goal,piece)
            distance = abs(goal_row - row) + abs(goal_col - col)
            total_distance += distance
        
        return total_distance


problem = EightPuzzleProblem(inicial)
result = astar(problem,graph_search=True)

print("Costo total:", result.cost)
print("Número de pasos:", len(result.path()))
print("Solución:")

for i, (action, state) in enumerate(result.path()):
    print(f"\nPaso {i}:")
    if action is not None:
        print("Acción:", action)
    for row in state:
        print(row)