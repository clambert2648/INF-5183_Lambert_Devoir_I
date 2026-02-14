# Devoir I - Algorithmes de Recherche dans un Labyrinthe

**Cours** : INF-5183 – Fondements de l'Intelligence Artificielle  
**Session** : Hiver 2026  
**Université** : Université du Québec en Outaouais

## Description

Ce projet implémente trois algorithmes de recherche pour résoudre un labyrinthe 16x16 :

- **DFS** (Depth-First Search) : Recherche en profondeur utilisant une pile (LIFO)
- **BFS** (Breadth-First Search) : Recherche en largeur utilisant une file (FIFO)
- **A*** (A-Star) : Recherche informée utilisant la distance de Manhattan comme heuristique

## Prérequis

- Python 3.11

Aucune dépendance externe requise.

## Exécution

```bash
python main.py
```

## Structure du projet

```
Devoir_I/
  maze.py          # Génération et gestion du labyrinthe
  dfs.py           # Implémentation de DFS
  bfs.py           # Implémentation de BFS
  astar.py         # Implémentation de A*
  main.py          # Point d'entrée principal
  requirements.txt # Dépendances
  README.md        # Documentation
```

## Fonctionnement

Le programme génère un labyrinthe aléatoire avec une seed pour la reproductibilité, puis exécute les trois algorithmes et affiche pour chacun :

- La visualisation de l'exploration (cases parcourues marquées `p`)
- La visualisation de la solution (chemin marqué `*`)
- La liste des coordonnées du chemin
- Les statistiques (noeuds explorés, longueur du chemin, temps d'exécution)
- Un tableau comparatif des trois algorithmes