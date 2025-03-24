import numpy as np

def encontrar_ciclos(adj_matrix):
    n = len(adj_matrix)
    ciclos = []
    inicio = np.argmax(np.sum(adj_matrix, axis=1))  # Nodo 1

    def dfs(nodo_actual, camino_actual, visitados):
        # Si el nodo actual ya está en el camino, se forma un ciclo
        if nodo_actual in camino_actual:
            idx = camino_actual.index(nodo_actual)
            ciclo = camino_actual[idx:] + [nodo_actual]
            # Normalizar el ciclo para evitar duplicados
            ciclo_str = '-'.join(map(str, ciclo))
            reversed_str = '-'.join(map(str, reversed(ciclo)))
            if ciclo_str not in ciclos and reversed_str not in ciclos:
                ciclos.append(ciclo_str)
            return

        # Evitar nodos ya visitados en este camino
        if nodo_actual in visitados:
            return

        # Marcar el nodo como visitado en este camino
        new_visitados = visitados.copy()
        new_visitados.add(nodo_actual)

        # Explorar vecinos
        for vecino, conectado in enumerate(adj_matrix[nodo_actual]):
            if conectado:
                dfs(vecino, camino_actual + [nodo_actual], new_visitados)

    # Iniciar DFS desde el nodo inicial (1)
    dfs(inicio, [], set())

    return ciclos

# Matriz de adyacencia
adj_matrix = np.array([
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0]
])

# Encontrar ciclos
ciclos = encontrar_ciclos(adj_matrix)

# Mostrar resultados
for i, ciclo in enumerate(ciclos):
    nodos = ciclo.split('-')
    print(f"Ciclo {i+1}: {' <- '.join(nodos)}")