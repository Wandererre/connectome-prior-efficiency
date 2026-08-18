import sys
import torch
import flyvis
from flyvis import connectome_file, ConnectomeFromAvgFilters, ConnectomeView

print("=== Flyvis Environment Verification ===")
print(f"Python version: {sys.version.split()[0]}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")

print("\n=== Day 1 Tutorial: Loading the 64-cell-type Optic Lobe Connectome ===")
config = dict(file=connectome_file.name, extent=15, n_syn_fill=1)
connectome = ConnectomeFromAvgFilters(config)

nodes_df = connectome.nodes.to_df()
edges_df = connectome.edges.to_df()

print(f"\n[CONNECTOME SUMMARY]")
print(f"Total modeled neurons (nodes): {len(nodes_df):,}")
print(f"Total modeled synapses (edges): {len(edges_df):,}")

print(f"\n[NODE COLUMNS]")
print(list(nodes_df.columns))

print(f"\n[CELL TYPES SAMPLE (First 15 nodes)]")
print(nodes_df.head(15).to_string())

print(f"\n[SYNAPTIC EDGES SAMPLE (First 10 edges)]")
print(edges_df.head(10).to_string())

print("\n=== Pretrained Models CLI Test ===")
from flyvis import network
print("Flyvis core framework & Day 1 Connectome loading verified successfully!")
