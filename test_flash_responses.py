import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import torch
import numpy as np
from pathlib import Path

from flyvis import results_dir, NetworkView
from flyvis.datasets.flashes import Flashes

print("=== Cleaning up Flash Response Plots ===")

# 1. Initialize Flashes dataset
dataset = Flashes(
    dynamic_range=[0, 1],
    t_stim=1.0,
    t_pre=1.0,
    dt=1 / 200,
    radius=[-1, 6],
    alternations=(0, 1, 0),
)

# 2. Load top pretrained ensemble model
network_view = NetworkView(results_dir / "flow/0000/000")
stims_and_resps = network_view.flash_responses(dataset=dataset)
responses = stims_and_resps['responses']

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

def save_clean_flash_plot(cell_type, title, filename):
    plt.figure(figsize=(9, 5), dpi=300)
    sub_resp = responses.custom.where(cell_type=cell_type, radius=6)
    sub_resp.custom.plot_traces(x='time')
    
    ax = plt.gca()
    # Replace raw parameter strings with clean human-readable legend
    plt.legend(["OFF Flash (Intensity = 0.0)", "ON Flash (Intensity = 1.0)"], loc="upper left", frameon=True, fontsize=9)
    
    plt.title(title, fontsize=12, fontweight='bold', pad=10)
    plt.xlabel("Time (s)", fontsize=10)
    plt.ylabel("Membrane Voltage Response", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.4)
    
    plt.tight_layout()
    plt.savefig(output_dir / filename, bbox_inches='tight')
    plt.close()
    print(f"Clean flash plot saved: {output_dir / filename}")

save_clean_flash_plot("L1", "L1 Cell Flash Responses (Biphasic ON vs OFF)", "l1_flash_responses.png")
save_clean_flash_plot("Mi1", "Mi1 Cell Flash Responses (ON Pathway Transient Spike)", "mi1_flash_responses.png")
