"""
main.py - Point d'entrée principal
Exécute les trois algorithmes (DFS, BFS, A*) sur le même labyrinthe
et affiche un tableau comparatif des résultats.
"""

from maze import generer_labyrinthe, afficher_labyrinthe
from dfs import dfs, afficher_exploration as dfs_exploration, afficher_solution as dfs_solution, afficher_chemin as dfs_chemin
from bfs import bfs, afficher_exploration as bfs_exploration, afficher_solution as bfs_solution, afficher_chemin as bfs_chemin
from astar import astar, afficher_exploration as astar_exploration, afficher_solution as astar_solution, afficher_chemin as astar_chemin


def main():
    # Générer le labyrinthe avec une seed fixe pour la reproductibilité
    seed = 42
    print(f"Génération du labyrinthe 16x16 (seed={seed})")
    print("=" * 50)
    laby = generer_labyrinthe(taille=16, seed=seed)
    afficher_labyrinthe(laby)

    # Stocker les résultats pour le tableau comparatif
    resultats = {}

    # ========== DFS ==========
    print("\n" + "=" * 50)
    print("DFS (Depth-First Search)")
    print("=" * 50)
    res_dfs = dfs(laby)
    if res_dfs:
        resultats['DFS'] = res_dfs
        print(f"\nExploration ({res_dfs['noeuds_explores']} noeuds) :")
        dfs_exploration(laby, res_dfs['explores'])
        print(f"\nSolution (longueur {res_dfs['longueur']}) :")
        dfs_solution(laby, res_dfs['chemin'])
        print()
        dfs_chemin(res_dfs['chemin'])

    # ========== BFS ==========
    print("\n" + "=" * 50)
    print("BFS (Breadth-First Search)")
    print("=" * 50)
    res_bfs = bfs(laby)
    if res_bfs:
        resultats['BFS'] = res_bfs
        print(f"\nExploration ({res_bfs['noeuds_explores']} noeuds) :")
        bfs_exploration(laby, res_bfs['explores'])
        print(f"\nSolution (longueur {res_bfs['longueur']}) :")
        bfs_solution(laby, res_bfs['chemin'])
        print()
        bfs_chemin(res_bfs['chemin'])

    # ========== A* ==========
    print("\n" + "=" * 50)
    print("A* (A-Star avec heuristique Manhattan)")
    print("=" * 50)
    res_astar = astar(laby)
    if res_astar:
        resultats['A* (manhattan)'] = res_astar
        print(f"\nExploration ({res_astar['noeuds_explores']} noeuds) :")
        astar_exploration(laby, res_astar['explores'])
        print(f"\nSolution (longueur {res_astar['longueur']}) :")
        astar_solution(laby, res_astar['chemin'])
        print()
        astar_chemin(res_astar['chemin'])

    # ========== Tableau Comparatif ==========
    print("\n" + "=" * 50)
    print("TABLEAU COMPARATIF")
    print("=" * 50)
    print(f"{'Algorithme':<20} {'Noeuds':<10} {'Longueur':<12} {'Temps (ms)':<10}")
    print("-" * 52)
    for nom, res in resultats.items():
        print(f"{nom:<20} {res['noeuds_explores']:<10} {res['longueur']:<12} {res['temps']:.3f}")


if __name__ == '__main__':
    main()