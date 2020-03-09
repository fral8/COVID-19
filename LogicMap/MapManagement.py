# -*- coding: utf-8 -*-

import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import geoplot



def loadData():
    filepath="dati-province/dpc-covid19-ita-province-20200308.csv"
    data = pd.read_csv(filepath,encoding = "ISO-8859-1") 
    return data
dat=loadData()
dat = dat[dat["lat"] > 0 ]
dat=dat[dat["casi_totali"]>0]
    
    

gdf = geopandas.GeoDataFrame(
    dat, geometry=geopandas.points_from_xy(dat.long, dat.lat))
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
#Non deve essere il geopanda points from xy

# We restrict to South America.
ax = world[world.continent == 'Italy'].plot(
    color='white', edgecolor='black')

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color='red')

plt.show()


ax = geoplot.voronoi(
    collisions.head(1000), projection=geoplot.crs.AlbersEqualArea(),
    clip=boroughs.simplify(0.001),
    hue='NUMBER OF PERSONS INJURED', cmap='Reds',
    legend=True,
    edgecolor='white'
)
geoplot.polyplot(boroughs, edgecolor='black', zorder=1, ax=ax)



class MapManagement():
    