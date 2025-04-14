from simpleai.search import SearchProblem
from simpleai.search import breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, greedy, astar

initial = ((3,3),(0,0),0) #Orilla izquierda (canibal, misionero), Orilla derecha, bote (0: izq, 1: der) 
goal = ((0,0),(3,3)) 


def side_ok(state): #devuelve si ese estado es True: que haya menor o iguales canibales o False
    izq = state[0]
    der = state[1]

    canibal_izq = izq[0]
    misionero_izq = izq[1]
    canibal_der =  der[0]
    misionero_der = der[1]

    # Validar que no se vaya del rando de (0,3)
    if not all(0 <= val <= 3 for val in [canibal_izq, misionero_izq, canibal_der, misionero_der]):
        return False

    # Valida que no haya mas canibales ni misioneros siempre que la cantidad de misioneros sea mayor a 0
    if (misionero_izq > 0 and canibal_izq > misionero_izq) or (misionero_der > 0 and canibal_der > misionero_der):
        return False
    
    return True

class CanibalMonjeProblem(SearchProblem):
    
    def cost(self, state, action, state2):
        return 1 

    def is_goal(self,state):
        return state[0] == (0,0) and state[1] == (3,3)
    
    def actions(self, state): 
        available_actions = []
        moves = [
            (1, 1), # 1 canibal y 1 misionero
            (1, 0), # 1 canibal
            (0, 1), # 1 misionero
            (2, 0), # 2 canibales
            (0, 2)  # 2 misioneros
        ]

        for move in moves:
            if side_ok(self.result(state,move)):
                available_actions.append(move)

        return available_actions
                                        

    def result(self, state, action):
        orilla_izq, orilla_der, bote = state
        canibal, misionero = action

        orilla_izq = list(orilla_izq)
        orilla_der = list(orilla_der)
        
        #si mi estado es ((3,3),(0,0),0), y mi acción es (1,1)
        # estado resultante es (2,1),(2,1),1)

        if bote == 0:
            orilla_izq[0] -= canibal
            orilla_izq[1] -= misionero
            orilla_der[0] += canibal
            orilla_der[1] += misionero
            bote = 1        
       
        else:
            orilla_izq[0] += canibal
            orilla_izq[1] += misionero
            orilla_der[0] -= canibal
            orilla_der[1] -= misionero
            bote = 0
        
        new_state = (tuple(orilla_izq), tuple(orilla_der), bote)
        return new_state
    
problem = CanibalMonjeProblem(initial)
result = breadth_first(problem)

print("Solución encontrada:\n")

for action, state in result.path():
    if action is None:
        print(f"Estado inicial: {state}")
    else:
        print(f"Acción: {action} -> Estado: {state}")
