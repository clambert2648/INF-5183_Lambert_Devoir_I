"""
bfs.py - Implémentation de la recherche en largeur (Breadth-First Search)
BFS utilise une file (FIFO) pour explorer le labyrinthe.
Il explore niveau par niveau, ce qui garantit le chemin le plus court.
"""

import time
from collections import deque


def bfs(labyrinthe):
    """
    Recherche en largeur dans le labyrinthe.
    
    La différence avec DFS :
    - DFS utilise une pile (LIFO) → explore en profondeur
    - BFS utilise une file (FIFO) → explore en largeur, niveau par niveau
    
    Comme BFS explore tous les chemins de longueur N avant ceux de longueur N+1,
    le premier chemin trouvé est garanti d'être le plus court.
    
    Args:
        labyrinthe: Matrice 2D représentant le labyrinthe
    
    Returns:
        Un dictionnaire contenant les résultats (comme dfs.py)
    """
    taille = len(labyrinthe)

    # Trouver les positions de S (départ) et G (arrivée)
    depart = None
    arrivee = None
    for i in range(taille):
        for j in range(taille):
            if labyrinthe[i][j] == 'S':
                depart = (i, j)
            elif labyrinthe[i][j] == 'G':
                arrivee = (i, j)

    debut_temps = time.time()

    # File FIFO : on utilise deque pour des opérations efficaces
    # (popleft est O(1) avec deque, contre O(n) avec une liste)
    file = deque([(depart, [depart])])

    # Ensemble des cases déjà visitées
    visites = set()
    visites.add(depart)

    # Ensemble de toutes les cases explorées (pour la visualisation)
    explores = set()

    # Les 4 directions : droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while file:
        # Défiler le premier élément (FIFO = First In, First Out)
        # C'est LA seule différence avec DFS qui fait pop() (le dernier)
        position, chemin = file.popleft()
        explores.add(position)

        # Si on a trouvé l'arrivée
        if position == arrivee:
            fin_temps = time.time()
            return {
                'chemin': chemin,
                'explores': explores,
                'noeuds_explores': len(explores),
                'longueur': len(chemin),
                'temps': (fin_temps - debut_temps) * 1000
            }

        # Explorer les voisins
        for delta_ligne, delta_colonne in directions:
            voisin = (position[0] + delta_ligne, position[1] + delta_colonne)

            if (0 <= voisin[0] < taille and
                    0 <= voisin[1] < taille and
                    labyrinthe[voisin[0]][voisin[1]] != '#' and
                    voisin not in visites):

                visites.add(voisin)
                file.append((voisin, chemin + [voisin]))

    return None


def afficher_exploration(labyrinthe, explores):
    """Affiche le labyrinthe avec les cases explorées marquées 'p'."""
    copie = [ligne[:] for ligne in labyrinthe]
    for (ligne, colonne) in explores:
        if copie[ligne][colonne] == '.':
            copie[ligne][colonne] = 'p'
    for ligne in copie:
        print(' '.join(ligne))


def afficher_solution(labyrinthe, chemin):
    """Affiche le labyrinthe avec le chemin solution marqué '*'."""
    copie = [ligne[:] for ligne in labyrinthe]
    for (ligne, colonne) in chemin:
        if copie[ligne][colonne] == '.':
            copie[ligne][colonne] = '*'
    for ligne in copie:
        print(' '.join(ligne))


def afficher_chemin(chemin):
    """Affiche le chemin sous forme de coordonnées."""
    parties = []
    for i, (ligne, colonne) in enumerate(chemin):
        if i == 0:
            parties.append(f"S ({ligne},{colonne})")
        elif i == len(chemin) - 1:
            parties.append(f"G ({ligne},{colonne})")
        else:
            parties.append(f"({ligne},{colonne})")
    print("Chemin : " + " -> ".join(parties))


# --- Test rapide ---
if __name__ == '__main__':
    from maze import generer_labyrinthe, afficher_labyrinthe

    laby = generer_labyrinthe(taille=16, seed=42)
    print("=== Labyrinthe ===")
    afficher_labyrinthe(laby)

    resultat = bfs(laby)

    if resultat:
        print(f"\n=== BFS - Exploration ({resultat['noeuds_explores']} noeuds) ===")
        afficher_exploration(laby, resultat['explores'])

        print(f"\n=== BFS - Solution (longueur {resultat['longueur']}) ===")
        afficher_solution(laby, resultat['chemin'])

        print(f"\n=== BFS - Chemin ===")
        afficher_chemin(resultat['chemin'])

        print(f"\nNoeuds explorés : {resultat['noeuds_explores']}")
        print(f"Longueur du chemin : {resultat['longueur']}")
        print(f"Temps : {resultat['temps']:.3f} ms")
    else:
        print("Aucun chemin trouvé !")