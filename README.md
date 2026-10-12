<div align="center">

# 🏙️ Urban Mobility Geographic Information Systems

**Python programs that map and measure the wards of Indian cities: ward area, ward perimeter, road density, the number and density of healthcare and education facilities, and the railway stations serving each ward, drawn as choropleth maps from ward-boundary GeoPackages.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-6-2ea44f) ![Topics](https://img.shields.io/badge/topic%20branches-6-blue) ![Cities](https://img.shields.io/badge/sample%20cities-8-purple) ![Updated](https://img.shields.io/badge/updated-12%20Oct%202026-orange)

</div>

## 👋 About

Each program lives on its **own branch**, with its sample outputs, and a README explaining how it works. The ward-boundary files that every program reads are kept together on a separate data branch. Pick a topic below to jump to its branch.

This repository has 7 sub-branches (excluding main) as of 12th October 2026.

## 🧭 Browse by topic

| | Topic | What's inside | Programs |
|:-:|---|---|:-:|
| 📐 | [**Ward Area Map**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Area-Map) | Area of every ward in km², with a choropleth map | 1 |
| 📏 | [**Ward Perimeter Map**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Perimeter-Map) | Perimeter of every ward in km, with a choropleth map | 1 |
| 🛣️ | [**Ward Road Density**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Road-Density) | Road length per km² of every ward, using OpenStreetMap roads | 1 |
| 🏥 | [**Ward Healthcare Facilities**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Healthcare-Facilities) | Number of hospitals, clinics and other healthcare facilities in every ward and their density per km², using OpenStreetMap | 1 |
| 🎓 | [**Ward Educational Institutions**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Educational-Institutions) | Number of schools, colleges, universities and other educational institutes in every ward and their density per km², using OpenStreetMap | 1 |
| 🚆 | [**Ward Railway Network**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Railway-Network) | Railway stations of every ward, sorted into suburban or local rail and subway, using OpenStreetMap | 1 |
| 🗂️ | [**Input gpkg files**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) | Ward-boundary GeoPackages for 8 cities, the input for every program | – |

## 📚 All programs

### 📐 [Ward Area Map](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Area-Map)

[**Ward Area Map**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Area-Map/ward_area.py): Area of each ward in km², saved to Excel and shown on a map

### 📏 [Ward Perimeter Map](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Perimeter-Map)

[**Ward Perimeter Map**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Perimeter-Map/ward_perimeter.py): Perimeter of each ward in km, saved to Excel and shown on a map

### 🛣️ [Ward Road Density](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Road-Density)

[**Road Density per Electoral Ward**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Road-Density/Road_Density_per_Electoral_Ward.py): Total length of drivable roads in each ward divided by its area (km/km²), with a map

### 🏥 [Ward Healthcare Facilities](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Healthcare-Facilities)

[**Data on Healthcare Facilities by Ward Division**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Healthcare-Facilities/Data_on_Healthcare_Facilities_by_Ward_Division.py): Number of healthcare facilities in each ward and their density per km², saved to Excel and shown on two maps

### 🎓 [Ward Educational Institutions](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Educational-Institutions)

[**Data on Educational Institutes by Ward Division**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Educational-Institutions/Data_on_Educational_Institutes_by_Ward_Division.py): Number of educational institutes in each ward and their density per km², saved to Excel and shown on two maps

### 🚆 [Ward Railway Network](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Ward-Railway-Network)

[**Railway Station Mapping with Electoral Ward Grid**](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Ward-Railway-Network/Railway_Station_Mapping_with_Electoral_Ward_Grid.py): Every railway station in a city, sorted into suburban or local rail and subway, saved to Excel and shown on the ward map

## ⚙️ Getting started

Clone just the topic you need (swap in any branch name from the table above), download a ward-boundary file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch, install the packages listed in that branch's README, and run the program:

```bash
git clone -b Ward-Area-Map --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas pandas matplotlib openpyxl
python ward_area.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows its maps.

## 📝 About the sample data

- The input files are **GeoPackages** (`.gpkg`) of ward boundaries for 8 cities: Ahmedabad, Bengaluru, Chennai, Delhi, Hyderabad, Jaipur, Kolkata and Mumbai. Each holds the ward name or number and the ward's shape.
- Only the Kolkata and Mumbai files have a column named `WARD`; for the others the programs ask which column holds the ward name or number. The [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) README lists the column to use for each city.
- Sample outputs are `.xlsx` tables and `.png` maps whose names start with the city. The commit message of each output file says which program and input created it.
