import geopandas as gpd
import osmnx as ox
import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
g=gpd.read_file(input('Enter Filename'))
print(list(g.columns))
m=input('Enter the column which contains the ward name/number')
g=g.rename(columns={m:'ward'})
if 'geometry' not in list(g.columns):
    print(list(g.columns))
    m=input('Enter the column which contains the spatial geometry of ward shapes')
    g=g.rename(columns={m:'geometry'})
    g=gpd.GeoDataFrame(g)
g=g.to_crs('EPSG:4326')
g=g[['ward','geometry']]
h=ox.features_from_polygon(g.geometry.union_all(),tags={'amenity':['college','kindergarten','research_institute','school','training','university'],'office':'educational institution','landuse':'education'})
h=h.to_crs('EPSG:4326')
h['geometry']=h.representative_point()
r=h.sjoin(g, how='inner', predicate='intersects')
r=r[~r.index.duplicated(keep='first')]
g['Count']=[0 for i in range(len(g))]
g=g.set_index('ward')
for j in r['ward'].tolist():
    if j in list(g.index):
        g.loc[j,'Count']+=1
g=g.reset_index()
g=g.to_crs(g.estimate_utm_crs())
g['Area (in m2)']=list(g.area)
g['Area (in km2)']=g['Area (in m2)']*(10**(-6))
g['Density']=g['Count']/g['Area (in km2)']
g=g.to_crs('EPSG:4326')
f=input('Enter output spreadsheet filename')
g.to_excel(f+'.xlsx',index=False)

fig,ax=plt.subplots(figsize=(6,6))
g.plot(ax=ax,column='Count',cmap='YlGn',legend=True)
g.boundary.plot(ax=ax,color='black',linewidth=1,label='Ward boundary')
ax.set_title('Map Displaying the no. of educational facilities in each ward')
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
ax.legend()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()
plt.show()

fig,ax=plt.subplots(figsize=(6,6))
g.plot(ax=ax,column='Density',cmap='YlGnBu',legend=True)
g.boundary.plot(ax=ax,color='black',linewidth=1,label='Ward boundary')
ax.set_title('Map Displaying the no. of educational facilities per km2 in each ward')
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
ax.legend()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()
plt.show()
