from typing import Dict

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from ..rubics_cube.main import RС
from ..rubics_cube.move import Moves
from ..rubics_cube.utils import permutation_to_index, orientation_to_index
from .base import collect_move_data


def create_data():
    rows = []
    cube = RС()
    for move in Moves.get_all_moves():
        new_cube = cube.apply_move(move, copy=True)
        rows.append(collect_move_data(new_cube, cube, move))

    data = pd.DataFrame(rows)

    data.to_csv("data/one_move_data.csv")

def analyze_data():
    
    csv_path = Path("data/one_move_data.csv")
    if not csv_path.exists():
        create_data()
    df = pd.read_csv(csv_path)

    cols_to_plot = ['delta_index_cp', 'delta_index_co', 'delta_index_ep', 'delta_index_eo']

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Delta Indices Analysis by Move')

    for ax, col in zip(axes.flatten(), cols_to_plot):
        sns.barplot(data=df, x='move', y=col, ax=ax)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout(pad=3.0)
    plt.show()

if __name__ == "__main__":
    analyze_data()