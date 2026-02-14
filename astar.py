"""
astar.py - Implémentation de la recherche A* (A-Star)
A* utilise une file de priorité et une heuristique (distance de Manhattan)
pour trouver le chemin le plus court de manière efficace.
"""

import time
import heapq


def heuristique_manhattan(position, arrivee):
    """
    Calcule la distance de Manhattan entre deux positions.
    C'est la somme des distances horizontale et verticale.
    
    Exemple : de (1,1) à (14,14) → |1-14| + |1-14| = 13 + 13 = 26
    
    Cette heuristique est admissible : elle ne surestime jamais
    la vraie distance, ce qui garantit que A* trouve le chemin optimal.
    """
    return abs(position[0] - arrivee[0]) + abs(position[1] - arrivee[1])


def astar(labyrinthe):
    """
    Recherche A* dans le labyrinthe.
    
    A* est comme BFS, mais au lieu de traiter les cases dans l'ordre
    d'arrivée (FIFO), il traite en priorité les cases les plus
    prometteuses selon f(n) = g(n) + h(n) :
    - g(n) : coût réel depuis le départ (nombre de pas)
    - h(n) : estimation du coût restant (distance de Manhattan)
    - f(n) : coût total estimé
    
    Args:
        labyrinthe: Matrice 2D représentant le labyrinthe
    
    Returns:
        Un dictionnaire contenant les résultats (comme dfs.py et bfs.py)
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

    # File de priorité : (f_score, compteur, position, chemin)
    # Le compteur sert à départager les cas où f_score est identique
    compteur = 0
    file_priorite = [(heuristique_manhattan(depart, arrivee), compteur, depart, [depart])]

    # Ensemble des cases déjà visitées
    visites = set()

    # Ensemble de toutes les cases explorées (pour la visualisation)
    explores = set()

    # Les 4 directions : droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while file_priorite:
        # Extraire la case avec le plus petit f(n)
        f_score, _, position, chemin = heapq.heappop(file_priorite)
        
        # Si déjà visité, on passe (on a peut-être trouvé un meilleur chemin entre-temps)
        if position in visites:
            continue
            
        visites.add(position)
        explores.add(position)

        # g(n) = longueur du chemin actuel depuis le départ
        g_score = len(chemin) - 1

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

                # g(voisin) = g(position) + 1 (coût d'un pas)
                nouveau_g = g_score + 1
                # h(voisin) = distance de Manhattan jusqu'à l'arrivée
                h = heuristique_manhattan(voisin, arrivee)
                # f(voisin) = g + h
                nouveau_f = nouveau_g + h

                compteur += 1
                heapq.heappush(file_priorite, (nouveau_f, compteur, voisin, chemin + [voisin]))

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

    resultat = astar(laby)

    if resultat:
        print(f"\n=== A* - Exploration ({resultat['noeuds_explores']} noeuds) ===")
        afficher_exploration(laby, resultat['explores'])

        print(f"\n=== A* - Solution (longueur {resultat['longueur']}) ===")
        afficher_solution(laby, resultat['chemin'])

        print(f"\n=== A* - Chemin ===")
        afficher_chemin(resultat['chemin'])

        print(f"\nNoeuds explorés : {resultat['noeuds_explores']}")
        print(f"Longueur du chemin : {resultat['longueur']}")
        print(f"Temps : {resultat['temps']:.3f} ms")
    else:
        print("Aucun chemin trouvé !")