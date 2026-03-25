# Some ideas...

import h5py
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Open file
filepath1 = "Chemotaxis-Data-and-Analysis/Mock_worms/chemotaxis_mock_210825_3_20250722_161220/metadata_featuresN_oneworm.hdf5"
filepath2 = "Chemotaxis-Data-and-Analysis/sexually_conditioned_worms/chemotaxis_sexc_24_1_26_09_20240126_143858/metadata_featuresN_oneworm.hdf5"
filepath3 = "Chemotaxis-Data-and-Analysis/Aversive_worms/chemotaxis_avsv_24_1_23_01_20240124_140022/metadata_featuresN_oneworm.hdf5"


# check if file exists
if not os.path.exists(filepath1):
    print(
        f"\nFile not found: {filepath1}!\nPlease clone the repository into this folder using:\n"
    )
    print(
        "    git clone https://github.com/Barrios-Lab/Chemotaxis-Data-and-Analysis.git\n"
    )
    quit()
elif not os.path.exists(filepath2):
    print(
        f"\nFile not found: {filepath2}!\nPlease clone the repository into this folder using:\n"
    )
    print(
        "    git clone https://github.com/Barrios-Lab/Chemotaxis-Data-and-Analysis.git\n"
    )
    quit()
elif not os.path.exists(filepath3):
    print(
        f"\nFile not found: {filepath3}!\nPlease clone the repository into this folder using:\n"
    )
    print(
        "    git clone https://github.com/Barrios-Lab/Chemotaxis-Data-and-Analysis.git\n"
    )
    quit()
    
print(f"Loading dataset from: {filepath1} and {filepath2} and {filepath3}...")



# load timeseries data (if present) from both

with h5py.File(filepath1, "r") as f:
    
    print("Loaded dataset from:", filepath1)
    print("Keys for datasets:", list(f.keys()))
    
    traj_data1 = pd.DataFrame(f["trajectories_data"][:])
    print(
            f"Trajectory data loaded with shape: {traj_data1.shape} and columns: {traj_data1.columns.tolist()}"
        )
    
with h5py.File(filepath2, "r") as f:
    
    print("Loaded dataset from:", filepath2)
    print("Keys for datasets:", list(f.keys()))
    
    traj_data2 = pd.DataFrame(f["trajectories_data"][:])
    print(
            f"Trajectory data loaded with shape: {traj_data2.shape} and columns: {traj_data2.columns.tolist()}"
        )

# plot graph of speeds of worms throughout tracking (x axis: time course (s), y axis: speed (micrometres/s))

plt.figure()

strange_scale = 13 

plt.scatter(
        [i * strange_scale for i in traj_data1["coord_x"]],
        [i * strange_scale for i in traj_data1["coord_y"]],
        s=1,
        c="red",
        label=f"Worm centroid trajectory (x{strange_scale})",
    )

plt.scatter(
        [i * strange_scale for i in traj_data2["coord_x"]],
        [i * strange_scale for i in traj_data2["coord_y"]],
        s=1,
        c="blue",
        label=f"Worm centroid trajectory (x{strange_scale})",
    )

plt.show()