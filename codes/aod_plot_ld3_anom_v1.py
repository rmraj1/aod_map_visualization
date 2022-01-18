# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:29:27 2022

@author: rmraj
"""

import os
os.environ['PROJ_LIB'] = r'C:\Users\rmraj\anaconda3\envs\out1\Lib\site-packages\osgeo\data\proj'
os.environ['GDAL_DATA'] = r'C:\Users\rmraj\anaconda3\envs\out1\Lib\site-packages\osgeo'

import netCDF4
import xarray as xr
import numpy as np
import cmocean # for perceptually uniform colormaps
import cartopy as cr # for geographic mapping
import cartopy.crs as ccrs # for map projections
import matplotlib.pyplot as plt # plotting tool
import cartopy.feature as cfeature # to add coastlines, land and ocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

from netCDF4 import Dataset
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.basemap
from mpl_toolkits.basemap import Basemap
import pylab as pl
import sys
import os
import matplotlib.colors as colors
from osgeo import gdal,osr,ogr

import geopandas as gpd
import fiona





# read the netcdf data file
data1= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\aodavg_ld3_2018.nc','r')
data2= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\aodavg_ld3_2019.nc','r')
data3= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\aodavg_ld3_2020.nc','r')
data4= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld3_2018.nc','r')
data5= netCDF4.Dataset(r'D:\extra\assgnmnet\data3\dout1\anom_aod_ld3_2019.nc','r')
## get the precipitation
in1= data1.variables['MYD08_D3_6_1_Deep_Blue_Aerosol_Optical_Depth_550_Land_Mean'][::-1]
in2= data2.variables['MYD08_D3_6_1_Deep_Blue_Aerosol_Optical_Depth_550_Land_Mean'][::-1]
in3= data3.variables['MYD08_D3_6_1_Deep_Blue_Aerosol_Optical_Depth_550_Land_Mean'][::-1]
in4= data4.variables['ANOM_2018_LD3'][::-1]
in5= data5.variables['ANOM_2019_LD3'][::-1]

# function to create the mask of your shapefile

def makeMask(lon,lat,res):
    source_ds = ogr.Open(shapefile)
    source_layer = source_ds.GetLayer()
 
    # Create high res raster in memory
    mem_ds = gdal.GetDriverByName('MEM').Create('', lon.size, lat.size, gdal.GDT_Byte)
    mem_ds.SetGeoTransform((lon.min(), res, 0, lat.max(), 0, -res))
    band = mem_ds.GetRasterBand(1)
 
    # Rasterize shapefile to grid
    gdal.RasterizeLayer(mem_ds, [1], source_layer, burn_values=[1])
 
    # Get rasterized shapefile as numpy array
    array = band.ReadAsArray()
 
    # Flush memory file
    mem_ds = None
    band = None
    return array
 
lats=data1.variables['lat'][:]
lons=data1.variables['lon'][:]   
# calculate the cellsize
cellsize = lons[:][1] - lons[:][0] 
shapefile = r"D:\extra\assgnmnet\data3\shp\merge2_india.shp"


mask = makeMask(lons,lats,cellsize)
  
 # show the mask
plt.imshow(mask)
plt.show()
  
 # mask the data

var1_1 = np.ma.masked_where(mask==0,in1)
var1=var1_1[::-1]
var2_1 = np.ma.masked_where(mask==0,in2)
var2=var2_1[::-1]
var3_1 = np.ma.masked_where(mask==0,in3)
var3=var3_1[::-1]
var4_1 = np.ma.masked_where(mask==0,in4)
var4=var4_1[::-1]
var5_1 = np.ma.masked_where(mask==0,in5)
var5=var5_1[::-1]
  
mp=Basemap(projection ="merc",
           llcrnrlon=60,
           llcrnrlat=5,
           urcrnrlon=100,
           urcrnrlat=40,
           resolution = 'i')


plt.figure(figsize=(12,8))

plt.subplot(2,3,1)


lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)
c=mp.pcolormesh(x,y,var1,vmin=0, vmax=1,cmap='jet')


parallels = np.arange(0.,45.,5.)
mp.drawparallels(parallels,labels=[1,0,0,1],linewidth=0.0)
meridians = np.arange(60.,100.,10.)
mp.drawmeridians(meridians,labels=[1,0,0,1],linewidth=0.0)
mp.readshapefile(r"D:\extra\assgnmnet\data1\modisdata\out\India_State_Boundary_Updated", name="India_State_Boundary_Updated")
plt.title("2018 LD3")


plt.subplot(2,3,2)
lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)

c=mp.pcolormesh(x,y,var2,vmin=0, vmax=1,cmap='jet')


parallels = np.arange(0.,45.,5.)
mp.drawparallels(parallels,labels=[1,0,0,1],linewidth=0.0)
meridians = np.arange(60.,100.,10.)
mp.drawmeridians(meridians,labels=[1,0,0,1],linewidth=0.0)

mp.readshapefile(r"D:\extra\assgnmnet\data1\modisdata\out\India_State_Boundary_Updated", name="India_State_Boundary_Updated")
plt.title("2019 LD3")

plt.subplot(2,3,3)
lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)

c=mp.pcolormesh(x,y,var3,vmin=0, vmax=1,cmap='jet')


#cbar=mp.colorbar(c,location ='right',pad='10%')



parallels = np.arange(0.,45.,5.)
mp.drawparallels(parallels,labels=[1,0,0,1],linewidth=0.0)
meridians = np.arange(60.,100.,10.)
mp.drawmeridians(meridians,labels=[1,0,0,1],linewidth=0.0)
mp.readshapefile(r"D:\extra\assgnmnet\data1\modisdata\out\India_State_Boundary_Updated", name="India_State_Boundary_Updated")
plt.title("2020 LD3")


plt.subplot(2,3,4)


lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)
c=mp.pcolormesh(x,y,var4,vmin=-0.7, vmax=0.7,cmap='seismic')


parallels = np.arange(0.,45.,5.)
mp.drawparallels(parallels,labels=[1,0,0,1],linewidth=0.0)
meridians = np.arange(60.,100.,10.)
mp.drawmeridians(meridians,labels=[1,0,0,1],linewidth=0.0)
mp.readshapefile(r"D:\extra\assgnmnet\data1\modisdata\out\India_State_Boundary_Updated", name="India_State_Boundary_Updated")
plt.title("AOD Anomaly 2018-2020 LD3")

plt.subplot(2,3,5)
lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)


c=mp.pcolormesh(x,y,var5,vmin=-0.7, vmax=0.7,cmap='seismic')

parallels = np.arange(0.,45.,5.)
mp.drawparallels(parallels,labels=[1,0,0,1],linewidth=0.0)
meridians = np.arange(60.,100.,10.)
mp.drawmeridians(meridians,labels=[1,0,0,1],linewidth=0.0)

mp.readshapefile(r"D:\extra\assgnmnet\data1\modisdata\out\India_State_Boundary_Updated", name="India_State_Boundary_Updated")
plt.title("AOD Anomaly 2019-2020 LD3")


#cbar=mp.colorbar(c,location ='right',pad='10%')




plt.savefig(r"D:\extra\assgnmnet\presentatiom\final_figures\anom_ld3_aod.png",
            bbox_inches ="tight",
            pad_inches = 1,
            transparent = True,
            facecolor ="w",
            edgecolor ='w',
            orientation ='landscape')


plt.show()



 
