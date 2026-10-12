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
r1=ox.features_from_polygon(g.geometry.union_all(),tags={'railway':'station'})
r1['geometry']=r1.representative_point()
r4=r1[pd.isna(r1['operator'])]
r1=r1[pd.isna(r1['operator'])==False]
l=r1['operator'].unique()
print('The list of operators are:')
for i in l:
    print(i)
r1['Kind of Railway']=[np.nan for i in range(len(r1))]
l1=[]
l2=[]
for i in l:
    co=int(input(f'''Press 1 if {i} is a suburban or local system
Press 2 if {i} is a subway system'''))
    if co==1:
        l1+=[i]
    elif co==2:
        l2+=[i]
    else:
        print('Invalid Input')
        sys.exit()
for i in list(r1.index):
    if r1.loc[i,'operator'] in l1:
        r1.loc[i,'Kind of Railway']='Suburban/Local Rail'
    else:
        r1.loc[i,'Kind of Railway']='Subway'
n=len(r4['name'])
co=input(f'''There are {n} stations of unknown type. If you want to enter there types 
individually one by one enter <YES> else press anything/enter''')
if co.upper()=='YES':
    for i in list(r4.index):
        co=int(input(f'''Enter 1 if {r4.loc[i,'name']} is a part of Suburban/Local Rail System
Enter 2 if {r4.loc[i,'name']} is a part of Subway System
Enter 3 if the system of {r4.loc[i,'name']} is unknown'''))
        if co==1:
            r1.loc[i,'geometry']=r4.loc[i,'geometry']
            r1.loc[i,'Kind of Railway']='Suburban/Local Rail'
            r4=r4.drop(index=i)
        elif co==2:
            r1.loc[i,'geometry']=r4.loc[i,'geometry']
            r1.loc[i,'Kind of Railway']='Subway'
            r4=r4.drop(index=i)
        elif co!=3:
            print('Invalid Input')
            sys.exit()
r5=r4.copy()
r2=r1[r1['Kind of Railway']=='Subway']
r2=r2[~r2.index.duplicated(keep='first')]
r3=r1[r1['Kind of Railway']=='Suburban/Local Rail']
r3=r3[~r3.index.duplicated(keep='first')]
r5['Kind of Railway']=['Unknown/Other System' for i in range(len(r4))]
r1=pd.concat([r1,r5],axis=0)
f=input('Enter Output Filename. Exclude .xlsx.')
r1.to_excel(f+'.xlsx',index=False)
fig,ax=plt.subplots(figsize=(6,6))
g.plot(ax=ax,color='lightgrey')
g.boundary.plot(ax=ax,color='black',linewidth=1,label='Ward boundary')
r2.plot(ax=ax,color='red',markersize=20,label='Subway')
r3.plot(ax=ax,color='blue',markersize=20,label='Suburban/Local Rail')
r4.plot(ax=ax,color='forestgreen',markersize=20,label='Unknown/Other System')
ax.set_title('Map Displaying the Presence of Railway Stations in wards')
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
ax.legend()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.tight_layout()
plt.show()

