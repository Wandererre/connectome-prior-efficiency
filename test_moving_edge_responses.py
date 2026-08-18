import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import torch
import numpy as np
from pathlib import Path

from flyvis import results_dir, NetworkView
from flyvis.datasets.moving_bar import MovingEdge

print("=== Cleaning up Moving Edge Response Plots ===")

# 1. Initialize MovingEdge dataset
dataset = MovingEdge(
    dynamic_range=[0, 1],
    t_stim=1.0,
    t_pre=0.5,
    dt=1 / 200,
)

# 2. Load top pretrained ensemble model
network_view = NetworkView(results_dir / "flow/0000/000")

# 3. Get responses
stims_and_resps = network_view.moving_edge_responses(dataset=dataset)
responses = stims_and_resps['responses']

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# Function to generate clean plot without giant text overlay legend
def save_clean_plot(cell_type, title, filename):
    plt.figure(figsize=(9, 5), dpi=300)
    
    # Generate traces
    sub_resp = responses.custom.where(cell_type=cell_type)
    sub_resp.custom.plot_traces(x='time')
    
    ax = plt.gca()
    # Remove cluttering raw xarray legend containing full parameter strings
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    
    plt.title(title, fontsize=12, fontweight='bold', pad=10)
    plt.xlabel("Time (s)", fontsize=10)
    plt.ylabel("Membrane Voltage Response", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.4)
    
    # Add clean informative annotation instead of 144 raw parameter lines
    plt.annotate(
        "Spike = Preferred Direction Motion\nFlat = Null / Non-Preferred Direction",
        xy=(0.7, 0.85),
        xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="gray", lw=1, alpha=0.9),
        fontsize=9
    )
    
    plt.tight_layout()
    plt.savefig(output_dir / filename, bbox_inches='tight')
    plt.close()
    print(f"Clean plot saved: {output_dir / filename}")

save_clean_plot("T4a", "T4a Cell Moving Edge Responses (ON Directional Motion)", "t4a_moving_edge_responses.png")
save_clean_plot("T5a", "T5a Cell Moving Edge Responses (OFF Directional Motion)", "t5a_moving_edge_responses.png")
