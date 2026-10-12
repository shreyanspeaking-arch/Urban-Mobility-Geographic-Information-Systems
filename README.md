<div align="center">

# 🚆 Ward Railway Network

**A branch of [Urban Mobility Geographic Information Systems](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

Railway stations are the entry points to a city's rail network. Plotting them over the ward map shows which wards are served by suburban or local trains, which by the metro, and which have no station at all.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Railway Station Mapping with Electoral Ward Grid**](#railway-station-mapping-with-electoral-ward-grid) | Every railway station in a city from OpenStreetMap, sorted into suburban or local rail and subway, saved to Excel and shown on the ward map |

## ⚙️ Getting started

```bash
git clone -b Ward-Railway-Network --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas osmnx pandas numpy matplotlib openpyxl
python Railway_Station_Mapping_with_Electoral_Ward_Grid.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows its maps. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. This program also needs an internet connection, because it downloads the railway stations from OpenStreetMap.

---

## Railway Station Mapping with Electoral Ward Grid

📄 **File:** [`Railway_Station_Mapping_with_Electoral_Ward_Grid.py`](./Railway_Station_Mapping_with_Electoral_Ward_Grid.py)

Finds every railway station inside a city's wards using OpenStreetMap data, lets the user sort the stations into suburban or local rail and subway systems by their operator, plots them over the ward map, and saves the list of stations to Excel.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. The program lists the file's columns and asks which one holds the ward name or number. If the file has no `geometry` column, it also asks which column holds the ward shapes.
2. All railway stations inside the wards (`railway=station`) are downloaded from OpenStreetMap with `osmnx`, and each station is reduced to a single point that is guaranteed to lie inside its shape.
3. The stations are grouped by their operator, and the program prints the list of operators. For each operator, the user enters whether it runs a suburban or local rail system or a subway system, and every station of that operator is labelled accordingly.
4. Stations with no operator recorded in OpenStreetMap are counted. The user can either label each of them one by one as suburban or local rail, subway, or unknown, or leave them all as an unknown or other system.
5. The program draws the wards in grey with their boundaries outlined, and marks the stations in three colours: one for suburban or local rail, one for subway and one for unknown or other systems.
6. The user enters a name for the output file (without `.xlsx`), and the program saves every station, with its OpenStreetMap details and a `Kind of Railway` column, to that Excel file.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`Railway_Stations_in_Kolkata.xlsx`](./Railway_Stations_in_Kolkata.xlsx)<br>[`Railway_Stations_in_Kolkata.png`](./Railway_Stations_in_Kolkata.png) |
| [`mumbai_electoral_wards_2017.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg) | [`Railway_Stations_in_Mumbai.xlsx`](./Railway_Stations_in_Mumbai.xlsx)<br>[`Railway_Stations_in_Mumbai.png`](./Railway_Stations_in_Mumbai.png) |

**🗺️ Sample maps**

<p align="center">
  <img src="./Railway_Stations_in_Kolkata.png" alt="Railway stations in Kolkata on the ward map" width="720">
</p>

<p align="center">
  <img src="./Railway_Stations_in_Mumbai.png" alt="Railway stations in Mumbai on the ward map" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
