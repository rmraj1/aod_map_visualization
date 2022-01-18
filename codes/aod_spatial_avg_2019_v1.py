# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 00:45:01 2022

@author: rmraj
"""

import netCDF4
from netCDF4 import Dataset
import xarray as xr
import numpy as np
import cmocean # for perceptually uniform colormaps
import cartopy as cr # for geographic mapping
import cartopy.crs as ccrs # for map projections
import matplotlib.pyplot as plt # plotting tool
import cartopy.feature as cfeature # to add coastlines, land and ocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER



data1= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\aod_avg_pl_2003_20.nc','r')

ds_comb1 = xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_pl1_2019.nc',combine='by_coords')
ds_comb2 = xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld1_2019.nc',combine='by_coords')
ds_comb3= xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld2_2019.nc',combine='by_coords')
ds_comb4 = xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld3_2019.nc',combine='by_coords')
ds_comb5 = xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld4_2019.nc',combine='by_coords')
ds_comb6 = xr.open_mfdataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ul1_2019.nc',combine='by_coords')

lats=data1.variables['lat'][:]
lons=data1.variables['lon'][:]
y1=ds_comb1.ANOM_2019_PL
y2=ds_comb2.ANOM_2019_LD1
y3=ds_comb3.ANOM_2019_LD2
y4=ds_comb4.ANOM_2019_LD3
y5=ds_comb5.ANOM_2019_LD4
y6=ds_comb6.ANOM_2019_UL1

delhi_d_19_pl1=y1.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_pl1=np.nanmean(delhi_d_19_pl1)

delhi_d_19_ld1=y2.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_ld1=np.nanmean(delhi_d_19_ld1)

delhi_d_19_ld2=y3.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_ld2=np.nanmean(delhi_d_19_ld2)

delhi_d_19_ld3=y4.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_ld3=np.nanmean(delhi_d_19_ld3)

delhi_d_19_ld4=y5.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_ld4=np.nanmean(delhi_d_19_ld4)
delhi_d_19_ul1=y6.sel(LAT=slice(17,18), LON=slice(76,77))
delhi_ul1=np.nanmean(delhi_d_19_ul1)


ci_d_19_pl1=y1.sel(LAT=slice(16,22), LON=slice(73,84))
ci_pl1=np.nanmean(ci_d_19_pl1)

ci_d_19_ld1=y2.sel(LAT=slice(16,22), LON=slice(73,84))
ci_ld1=np.nanmean(ci_d_19_ld1)

ci_d_19_ld2=y3.sel(LAT=slice(16,22), LON=slice(73,84))
ci_ld2=np.nanmean(ci_d_19_ld2)

ci_d_19_ld3=y4.sel(LAT=slice(16,22), LON=slice(73,84))
ci_ld3=np.nanmean(ci_d_19_ld3)

ci_d_19_ld4=y5.sel(LAT=slice(16,22), LON=slice(73,84))
ci_ld4=np.nanmean(ci_d_19_ld4)

ci_d_19_ul1=y6.sel(LAT=slice(16,22), LON=slice(73,84))
ci_ul1=np.nanmean(ci_d_19_ul1)


ig_d_19_pl1=y1.sel(LAT=slice(21,25), LON=slice(76,88))
ig_pl1=np.nanmean(ig_d_19_pl1)

ig_d_19_ld1=y2.sel(LAT=slice(21,25), LON=slice(76,88))
ig_ld1=np.nanmean(ig_d_19_ld1)

ig_d_19_ld2=y3.sel(LAT=slice(21,25), LON=slice(76,88))
ig_ld2=np.nanmean(ig_d_19_ld2)

ig_d_19_ld3=y4.sel(LAT=slice(21,25), LON=slice(76,88))
ig_ld3=np.nanmean(ig_d_19_ld3)

ig_d_19_ld4=y5.sel(LAT=slice(21,25), LON=slice(76,88))
ig_ld4=np.nanmean(ig_d_19_ld4)

ig_d_19_ul1=y6.sel(LAT=slice(21,25), LON=slice(76,88))
ig_ul1=np.nanmean(ig_d_19_ul1)



ne_d_19_pl1=y1.sel(LAT=slice(22,30), LON=slice(89,97))
ne_pl1=np.nanmean(ne_d_19_pl1)

ne_d_19_ld1=y2.sel(LAT=slice(22,30), LON=slice(89,97))
ne_ld1=np.nanmean(ne_d_19_ld1)

ne_d_19_ld2=y3.sel(LAT=slice(22,30), LON=slice(89,97))
ne_ld2=np.nanmean(ne_d_19_ld2)

ne_d_19_ld3=y4.sel(LAT=slice(22,30), LON=slice(89,97))
ne_ld3=np.nanmean(ne_d_19_ld3)

ne_d_19_ld4=y5.sel(LAT=slice(22,30), LON=slice(89,97))
ne_ld4=np.nanmean(ne_d_19_ld4)

ne_d_19_ul1=y6.sel(LAT=slice(22,30), LON=slice(89,97))
ne_ul1=np.nanmean(ne_d_19_ul1)


sp_d_19_pl1=y1.sel(LAT=slice(7,14), LON=slice(74,83))
sp_pl1=np.nanmean(sp_d_19_pl1)

sp_d_19_ld1=y2.sel(LAT=slice(7,14), LON=slice(74,83))
sp_ld1=np.nanmean(sp_d_19_ld1)

sp_d_19_ld2=y3.sel(LAT=slice(7,14), LON=slice(74,83))
sp_ld2=np.nanmean(sp_d_19_ld2)

sp_d_19_ld3=y4.sel(LAT=slice(7,14), LON=slice(74,83))
sp_ld3=np.nanmean(sp_d_19_ld3)

sp_d_19_ld4=y5.sel(LAT=slice(7,14), LON=slice(74,83))
sp_ld4=np.nanmean(sp_d_19_ld4)

sp_d_19_ul1=y6.sel(LAT=slice(7,14), LON=slice(74,83))
sp_ul1=np.nanmean(sp_d_19_ul1)

pl_sp="spone" + str(sp_pl1)
print(pl_sp)
ld1_sp="two" + str(sp_ld1)
print(ld1_sp)
ld2_sp="three" + str(sp_ld2)
print(ld2_sp)
ld3_sp="four" + str(sp_ld3)
print(ld3_sp)

ld4_sp="five" + str(sp_ld4)
print(ld4_sp)


ul1_sp="six" + str(sp_ul1)
print(ul1_sp)




pl_ig="igone" + str(ig_pl1)
print(pl_ig)
ld1_ig="two" + str(ig_ld1)
print(ld1_ig)
ld2_ig="three" + str(ig_ld2)
print(ld2_ig)
ld3_ig="four" + str(ig_ld3)
print(ld3_ig)

ld4_ig="five" + str(ig_ld4)
print(ld4_ig)


ul1_ig="six" + str(ig_ul1)
print(ul1_ig)

pl_ne="neone" + str(ne_pl1)
print(pl_ne)
ld1_ne="two" + str(ne_ld1)
print(ld1_ne)
ld2_ne="three" + str(ne_ld2)
print(ld2_ne)
ld3_ne="four" + str(ne_ld3)
print(ld3_ne)

ld4_ne="five" + str(ne_ld4)
print(ld4_ne)


ul1_ne="six" + str(ne_ul1)
print(ul1_ne)



pl_ci="cione" + str(ci_pl1)
print(pl_ci)
ld1_ci="two" + str(ci_ld1)
print(ld1_ci)
ld2_ci="three" + str(ci_ld2)
print(ld2_ci)
ld3_ci="four" + str(ci_ld3)
print(ld3_ci)

ld4_ci="five" + str(ci_ld4)
print(ld4_ci)


ul1_ci="six" + str(ci_ul1)
print(ul1_ci)



pl_delhi="odelhi" + str(delhi_pl1)
print(pl_delhi)
ld1_delhi="two" + str(delhi_ld1)
print(ld1_delhi)
ld2_delhi="three" + str(delhi_ld2)
print(ld2_delhi)
ld3_delhi="four" + str(delhi_ld3)
print(ld3_delhi)

ld4_delhi="five" + str(delhi_ld4)
print(ld4_delhi)


ul1_delhi="six" + str(delhi_ul1)
print(ul1_delhi)




