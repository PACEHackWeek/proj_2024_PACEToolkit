from netCDF4 import Dataset
import numpy as np

filename = 'PACE_OCI.20240413.L3b.DAY.CHL.V2_0.NRT.nc'
dataset = Dataset(filename, 'r')

print(dataset.groups["level-3_binned_data"]["chlor_a"])

#np_chlor_a = np.array(dataset.groups["level-3_binned_data"]["chlor_a"])
np_chlor_a = dataset.groups["level-3_binned_data"]["chlor_a"][:]
print(type(np_chlor_a))
print(np_chlor_a.shape)
print(np_chlor_a.dtype)

chla_10lat = np.reshape(chla, (180, 10, 3600))

chla_latregrid = np.mean(chla_10lat, axis=1)

chla_latregrid_10lon = np.reshape(chla_latregrid, (180, 360, 10))


chla_latregrid_lonregrid = np.mean(chla_latregrid_10lon, axis=2)

    pics.append(1e3 * \
        missing2number(np.array(files[i]["pic"]))\
        .reshape(latitude.shape[0], 10, longitude.shape[0], 10)\
        .mean(axis=1).mean(axis=-1))