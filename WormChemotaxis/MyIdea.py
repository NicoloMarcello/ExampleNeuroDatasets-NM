# Some ideas...

import h5py
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Open file
filepath1 = "Chemotaxis-Data-and-Analysis/Mock_worms/chemotaxis_mock_24_2_23_08_20240123_144841/metadata_featuresN_oneworm.hdf5"
filepath2 = "Chemotaxis-Data-and-Analysis/sexually_conditioned_worms/chemotaxis_sexc_24_1_26_09_20240126_143858/metadata_featuresN_oneworm.hdf5"


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

print(f"Loading dataset from: {filepath1} and {filepath2}...")

# load timeseries data (if present) from both

with h5py.File(filepath1, "r") as f:
    
    print("Loaded dataset from:", filepath1)
    print("Keys for datasets:", list(f.keys()))
    
    traj_data1 = pd.DataFrame(f["trajectories_data"][:])
    print(
            f"Trajectory data loaded with shape: {traj_data1.shape} and columns: {traj_data1.columns.tolist()}"
        )
    
    if "timeseries_data" in f:
        timeseries1 = pd.DataFrame(f["timeseries_data"][:])
        print(
        f"Timeseries data loaded with shape: {timeseries1.shape} and columns: {timeseries1.columns.tolist()}"
        )
        
with h5py.File(filepath2, "r") as f:
    
    print("Loaded dataset from:", filepath2)
    print("Keys for datasets:", list(f.keys()))
    
    traj_data2 = pd.DataFrame(f["trajectories_data"][:])
    print(
            f"Trajectory data loaded with shape: {traj_data2.shape} and columns: {traj_data2.columns.tolist()}"
        )
    
    if "timeseries_data" in f:
        timeseries2 = pd.DataFrame(f["timeseries_data"][:])
        print(
        f"Timeseries data loaded with shape: {timeseries2.shape} and columns: {timeseries2.columns.tolist()}"
        )

# plot graph of speeds of worms throughout tracking (x axis: time course (s), y axis: speed (micrometres/s))

plt.figure()
plt.plot(traj_data1['timestamp_time'],timeseries1['speed'],'r:d',linewidth=2,label='mock')
plt.show()