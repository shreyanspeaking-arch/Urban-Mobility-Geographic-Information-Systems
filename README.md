<div align="center">

# 🏥 Density of Healthcare Facilities per Ward

**A branch of [Urban Mobility Geographic Information Systems](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The density of healthcare facilities is the number of hospitals, clinics and similar facilities in an area divided by the size of that area, in facilities per km². It shows how evenly healthcare is spread across a city, and which wards have few facilities within easy reach of their residents.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Density of Healthcare Facilities per Electoral Ward**](#density-of-healthcare-facilities-per-electoral-ward) | Healthcare facilities per km² of each ward, using OpenStreetMap data, saved to Excel and shown on a map |

## ⚙️ Getting started

```bash
git clone -b Density-of-Healthcare-Facilities-per-Ward --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas osmnx pandas numpy matplotlib openpyxl
python Density_of_Healthcare_Facilities_per_Electoral_Ward.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows a map. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. This program also needs an internet connection, because it downloads the healthcare facilities from OpenStreetMap.

---

## Density of Healthcare Facilities per Electoral Ward

📄 **File:** [`Density_of_Healthcare_Facilities_per_Electoral_Ward.py`](./Density_of_Healthcare_Facilities_per_Electoral_Ward.py)

Counts the healthcare facilities in every ward of a city, using OpenStreetMap data, divides the count by the ward's area, saves the results to Excel, and draws a choropleth map of the wards shaded by the number of facilities per km².

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. The program lists the file's columns and asks which one holds the ward name or number. If the file has no `geometry` column, it also asks which column holds the ward shapes.
2. All healthcare facilities inside the wards are downloaded from OpenStreetMap with `osmnx`: places tagged as a clinic, dentist, doctor's practice, hospital or nursing home under either the `amenity` or the `healthcare` key, so a facility is found whichever way it was mapped.
3. Each facility is reduced to a single point that is guaranteed to lie inside its shape, so a hospital mapped as a building outline that crosses a ward boundary is still counted. Each point is matched to the ward it falls in; a point lying exactly on the boundary between two wards is counted in only one of them. The facilities in each ward are then counted.
4. The wards are projected to the local UTM zone, chosen automatically for the city, and the area of each ward is computed in km². The density is the number of facilities divided by the area.
5. The user enters a name for the output file (without `.xlsx`). The program saves each ward's area and density to that Excel file, where the `CMF` column holds the number of healthcare facilities per km². It then draws a map of the wards shaded by density, with the ward boundaries outlined.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`Kolkata Healthcare Facilities by Ward Area.xlsx`](./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.xlsx)<br>[`Kolkata Healthcare Facilities by Ward Area.png`](./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png) |

**🗺️ Sample map**

<p align="center">
  <img src="./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Kolkata wards shaded by healthcare facilities per km²" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
