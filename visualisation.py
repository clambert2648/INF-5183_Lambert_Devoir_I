import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def dessiner(ax, laby, chemin=None, explores=None, titre=""):
    taille = len(laby)
    img = np.ones((taille, taille, 3))

    # Couleurs
    COULEUR_MUR = [0, 0, 0]          # noir
    COULEUR_PASSAGE = [1, 1, 1]      # blanc
    COULEUR_EXPLORE = [0.72, 0.84, 0.96]  # bleu clair
    COULEUR_CHEMIN = [1, 0, 0]       # rouge
    COULEUR_START = [0, 1, 0]        # vert
    COULEUR_GOAL = [0.65, 0, 1]      # violet

    for i in range(taille):
        for j in range(taille):
            if laby[i][j] == '#':
                img[i, j] = COULEUR_MUR
            elif laby[i][j] == '.':
                img[i, j] = COULEUR_PASSAGE
            elif laby[i][j] == 'S':
                img[i, j] = COULEUR_START
            elif laby[i][j] == 'G':
                img[i, j] = COULEUR_GOAL

    # Cases explorées
    if explores:
        for (i, j) in explores:
            if laby[i][j] == '.':
                img[i, j] = COULEUR_EXPLORE

    # Chemin final
    if chemin:
        for (i, j) in chemin:
            if laby[i][j] not in ('S', 'G'):
                img[i, j] = COULEUR_CHEMIN

    ax.imshow(img, interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(titre, fontsize=16, fontweight="bold")


def afficher_comparaison(laby, dfs_res, bfs_res, astar_res, sauvegarder=True):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5.5))

    dessiner(
        axes[0],
        laby,
        chemin=dfs_res["chemin"],
        explores=dfs_res["explores"],
        titre=f"DFS ({dfs_res['noeuds_explores']} nœuds)"
    )

    dessiner(
        axes[1],
        laby,
        chemin=bfs_res["chemin"],
        explores=bfs_res["explores"],
        titre=f"BFS ({bfs_res['noeuds_explores']} nœuds)"
    )

    dessiner(
        axes[2],
        laby,
        chemin=astar_res["chemin"],
        explores=astar_res["explores"],
        titre=f"A* ({astar_res['noeuds_explores']} nœuds)"
    )

    # Légende globale
    legende = [
        Patch(facecolor=(0, 0, 0), edgecolor='black', label='Mur'),
        Patch(facecolor=(1, 1, 1), edgecolor='black', label='Passage'),
        Patch(facecolor=(0.72, 0.84, 0.96), edgecolor='black', label='Exploré'),
        Patch(facecolor=(1, 0, 0), edgecolor='black', label='Chemin'),
        Patch(facecolor=(0, 1, 0), edgecolor='black', label='Départ (S)'),
        Patch(facecolor=(0.65, 0, 1), edgecolor='black', label='Arrivée (G)')
    ]

    fig.legend(
        handles=legende,
        loc="lower center",
        ncol=6,
        fontsize=10,
        frameon=False,
        bbox_to_anchor=(0.5, -0.02)
    )

    plt.tight_layout(rect=[0, 0.06, 1, 1])

    if sauvegarder:
        plt.savefig(
            "comparaison_algorithmes.png",
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()