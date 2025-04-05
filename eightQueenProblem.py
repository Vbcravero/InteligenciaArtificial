from simpleai.search import SearchProblem, iterative_limited_depth_first

# Todas las reinas en la fila (0,0,0,0,0,0,0,0): cada índice representa una columna del tablero, y el valor en ese índice representa la fila
initial_state = (0,) * 8

class EightQueenProblem(SearchProblem):
    def cost(self, state, action, state2):
        return 1
    
    def actions(self, state):
        available_actions = [ ]
        for queen, row in enumerate(state):
            for new_row in range(8):
                if new_row != row:  
                    available_actions.append((queen, new_row))  
        return available_actions
    
    def result(self, state, action):
        queen, new_row = action
        new_state = list(state)
        new_state[queen] = new_row
        return tuple(new_state)
    
    def is_goal(self, state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (
                    state[i] == state[j] or  # Misma fila
                    abs(state[i] - state[j]) == abs(i - j)  # Misma diagonal
                ):
                    return False  # Hay conflicto
        return True  # No hay conflictos, es un estado meta
    

problem = EightQueenProblem(initial_state)
depth_limit = 20
result = iterative_limited_depth_first(problem,depth_limit)

if result:
    print("Camino a la solución:")
    for step, (action, state) in enumerate(result.path()):
        print(f"Paso {step}: Acción {action} -> Estado {state}")

    print("\nCosto total:", result.cost)
    print("Estado final alcanzado:", result.state)
    print("¿Es un estado meta?", problem.is_goal(result.state))
else:
    print("No se encontró solución dentro del límite de profundidad.")