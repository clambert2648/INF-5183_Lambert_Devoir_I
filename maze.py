"""
maze.py - Génération et gestion du labyrinthe
Ce module crée un labyrinthe 16x16 et garantit qu'un chemin existe entre S et G.
"""

import random


def generer_labyrinthe(taille=16, seed=None):
    """
    Génère un labyrinthe de taille donnée.
    
    Stratégie :
    1. On remplit toute la grille de murs (#)
    2. On "creuse" des passages avec un DFS aléatoire
    3. Cela garantit qu'un chemin existe entre S et G
    
    Args:
        taille: Dimension du labyrinthe (16 par défaut)
        seed: Graine aléatoire pour la reproductibilité
    
    Returns:
        Une matrice 2D (liste de listes) représentant le labyrinthe
    """
    # Initialiser le générateur aléatoire avec la seed
    if seed is not None:
        random.seed(seed)

    # Étape 1 : Créer une grille remplie de murs
    labyrinthe = [['#' for _ in range(taille)] for _ in range(taille)]

    # Étape 2 : Creuser des passages avec un DFS aléatoire
    # On commence au point de départ (1, 1)
    _creuser(labyrinthe, 1, 1, taille)

    # Étape 3 : Garantir l'accès à la position d'arrivée
    # L'algorithme de creusement visite les positions impaires (1,3,5...)
    # mais G est à (14,14) qui est pair, donc on ouvre un passage vers G
    arrivee_ligne = taille - 2
    arrivee_colonne = taille - 2
    labyrinthe[arrivee_ligne][arrivee_colonne] = '.'
    # Ouvrir le voisin au-dessus et à gauche pour connecter au réseau de passages
    labyrinthe[arrivee_ligne - 1][arrivee_colonne] = '.'
    labyrinthe[arrivee_ligne][arrivee_colonne - 1] = '.'

    # Étape 4 : Placer le départ (S) et l'arrivée (G)
    labyrinthe[1][1] = 'S'
    labyrinthe[arrivee_ligne][arrivee_colonne] = 'G'

    return labyrinthe


def _creuser(labyrinthe, ligne, colonne, taille):
    """
    Creuse des passages dans le labyrinthe avec un DFS aléatoire.
    
    L'idée : depuis une case, on regarde les 4 directions dans un ordre
    aléatoire. Si la case à 2 pas de distance est encore un mur, on
    "creuse" en transformant les 2 cases en passages.
    
    Pourquoi 2 pas ? Pour garder des murs entre les couloirs et créer
    un vrai labyrinthe avec des impasses.
    """
    # Marquer la case actuelle comme passage
    labyrinthe[ligne][colonne] = '.'

    # Les 4 directions possibles : (delta_ligne, delta_colonne)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # droite, bas, gauche, haut
    random.shuffle(directions)  # Mélanger pour que le labyrinthe soit aléatoire

    for delta_ligne, delta_colonne in directions:
        # Calculer la position à 2 pas
        nouvelle_ligne = ligne + delta_ligne
        nouvelle_colonne = colonne + delta_colonne

        # Vérifier que la nouvelle position est dans les limites
        # (entre 1 et taille-2 pour rester à l'intérieur des bords)
        if (1 <= nouvelle_ligne < taille - 1 and
                1 <= nouvelle_colonne < taille - 1 and
                labyrinthe[nouvelle_ligne][nouvelle_colonne] == '#'):
            
            # Creuser le mur entre la case actuelle et la nouvelle case
            labyrinthe[ligne + delta_ligne // 2][colonne + delta_colonne // 2] = '.'
            
            # Continuer à creuser depuis la nouvelle case (récursion)
            _creuser(labyrinthe, nouvelle_ligne, nouvelle_colonne, taille)


def afficher_labyrinthe(labyrinthe):
    """Affiche le labyrinthe dans le terminal."""
    for ligne in labyrinthe:
        print(' '.join(ligne))


# --- Test rapide ---
if __name__ == '__main__':
    laby = generer_labyrinthe(taille=16, seed=42)
    afficher_labyrinthe(laby)