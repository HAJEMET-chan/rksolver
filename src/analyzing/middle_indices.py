from pprint import pprint
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt


from ..rubics_cube.main import RС
from ..rubics_cube.move import Moves
from ..rubics_cube.utils import permutation_to_index, orientation_to_index

def create_data(n = 100, move_count = 50):
    
    cube = RС()
    avg_indices_data = []
    data = []

    for _ in range(n):
        moves_data = []
        moves = Moves.get_random_moves(move_count)
        for m in moves:
            cube.apply_move(m)
            moves_data.append({
                "move": m.notation,
                "index_cp": permutation_to_index(cube._cp),
                "index_co": orientation_to_index(cube._co, 3),
                "index_ep": permutation_to_index(cube._ep),
                "index_eo": orientation_to_index(cube._eo, 2),
            })
        
        avg_indices = {
            "avg_index_cp": sum(d["index_cp"] for d in moves_data) / len(moves_data),
            "avg_index_co": sum(d["index_co"] for d in moves_data) / len(moves_data),
            "avg_index_ep": sum(d["index_ep"] for d in moves_data) / len(moves_data),
            "avg_index_eo": sum(d["index_eo"] for d in moves_data) / len(moves_data),
        }

        avg_indices_data.append(avg_indices)
        cube.reset()
    
    return{
        "n": n,
        "move_count": move_count,
        "avg_index_cp": sum(d["avg_index_cp"] for d in avg_indices_data) / len(avg_indices_data),
        "avg_index_co": sum(d["avg_index_co"] for d in avg_indices_data) / len(avg_indices_data),
        "avg_index_ep": sum(d["avg_index_ep"] for d in avg_indices_data) / len(avg_indices_data),
        "avg_index_eo": sum(d["avg_index_eo"] for d in avg_indices_data) / len(avg_indices_data),
    }

def create_middle_indices_data(cnt = 99):
    n = 1
    move_count = 1
    data = []

    for _ in range(cnt):
        data.append(create_data(n, move_count))
        move_count += 1
        data.append(create_data(n, move_count))
        n += 1
    
    
    df = pd.DataFrame(data)
    df.to_csv("data/middle_indices_data.csv")

def analyze_middle_indices_data():
    csv_path = Path("data/middle_indices_data.csv")
    if not csv_path.exists():
        create_middle_indices_data()
    df = pd.read_csv(csv_path)

    cols_to_plot = ['avg_index_cp', 'avg_index_co', 'avg_index_ep', 'avg_index_eo']

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Зависимость среднего индекса от количества ходов')

    for ax, col in zip(axes.flatten(), cols_to_plot):
        sns.lineplot(data=df, x='move_count', y=col, ax=ax)
        ax.set_title(col)
    
    plt.tight_layout(pad=3.0)
    plt.show()

if __name__ == "__main__":
    analyze_middle_indices_data()