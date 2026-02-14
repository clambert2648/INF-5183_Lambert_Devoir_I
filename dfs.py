"""
dfs.py - Implémentation de la recherche en profondeur (Depth-First Search)
DFS utilise une pile (LIFO) pour explorer le labyrinthe.
Il avance le plus loin possible avant de revenir en arrière.
"""

import time


def dfs(labyrinthe):
    """
    Recherche en profondeur dans le labyrinthe.
    
    Args:
        labyrinthe: Matrice 2D représentant le labyrinthe
    
    Returns:
        Un dictionnaire contenant :
        - 'chemin': liste des coordonnées du chemin trouvé
        - 'explores': ensemble des cases explorées
        - 'noeuds_explores': nombre total de noeuds explorés
        - 'longueur': longueur du chemin
        - 'temps': temps d'exécution en millisecondes
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

    # La pile contient des tuples (position_actuelle, chemin_parcouru)
    pile = [(depart, [depart])]

    # Ensemble des cases déjà visitées (pour ne pas tourner en rond)
    visites = set()
    visites.add(depart)

    # Ensemble de toutes les cases explorées (pour la visualisation)
    explores = set()

    # Les 4 directions : droite, bas, gauche, haut (ordre demandé par l'énoncé)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pile:
        # Dépiler le dernier élément (LIFO = Last In, First Out)
        position, chemin = pile.pop()
        explores.add(position)

        # Si on a trouvé l'arrivée, on a terminé !
        if position == arrivee:
            fin_temps = time.time()
            return {
                'chemin': chemin,
                'explores': explores,
                'noeuds_explores': len(explores),
                'longueur': len(chemin),
                'temps': (fin_temps - debut_temps) * 1000  # en ms
            }

        # Explorer les voisins dans l'ordre : droite, bas, gauche, haut
        for delta_ligne, delta_colonne in directions:
            voisin = (position[0] + delta_ligne, position[1] + delta_colonne)

            # Vérifier que le voisin est valide et pas encore visité
            if (0 <= voisin[0] < taille and
                    0 <= voisin[1] < taille and
                    labyrinthe[voisin[0]][voisin[1]] != '#' and
                    voisin not in visites):

                visites.add(voisin)
                # Empiler avec le chemin mis à jour
                pile.append((voisin, chemin + [voisin]))

    # Si la pile est vide et qu'on n'a pas trouvé G, pas de solution
    return None


def afficher_exploration(labyrinthe, explores):
    """Affiche le labyrinthe avec les cases explorées marquées 'p'."""
    copie = [ligne[:] for ligne in labyrinthe]  # Copie pour ne pas modifier l'original
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

    resultat = dfs(laby)

    if resultat:
        print(f"\n=== DFS - Exploration ({resultat['noeuds_explores']} noeuds) ===")
        afficher_exploration(laby, resultat['explores'])

        print(f"\n=== DFS - Solution (longueur {resultat['longueur']}) ===")
        afficher_solution(laby, resultat['chemin'])

        print(f"\n=== DFS - Chemin ===")
        afficher_chemin(resultat['chemin'])

        print(f"\nNoeuds explorés : {resultat['noeuds_explores']}")
        print(f"Longueur du chemin : {resultat['longueur']}")
        print(f"Temps : {resultat['temps']:.3f} ms")
    else:
        print("Aucun chemin trouvé !")