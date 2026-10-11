<div align="center">

# 🏥 Ward Healthcare Facilities

**A branch of [Urban Mobility Geographic Information Systems](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The number and density of healthcare facilities show how evenly healthcare is spread across a city. The count says how many hospitals, clinics and similar facilities each ward has; the density divides that by the ward's area, in facilities per km², so that large and small wards can be compared fairly and wards with few facilities within easy reach of their residents stand out.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Data on Healthcare Facilities by Ward Division**](#data-on-healthcare-facilities-by-ward-division) | Number of healthcare facilities in each ward and their density per km², using OpenStreetMap data, saved to Excel and shown on two maps |

## ⚙️ Getting started

```bash
git clone -b Ward-Healthcare-Facilities --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas osmnx pandas numpy matplotlib openpyxl
python Data_on_Healthcare_Facilities_by_Ward_Division
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows its maps. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. This program also needs an internet connection, because it downloads the healthcare facilities from OpenStreetMap.

---

## Data on Healthcare Facilities by Ward Division

📄 **File:** [`Data_on_Healthcare_Facilities_by_Ward_Division`](./Data_on_Healthcare_Facilities_by_Ward_Division)

Counts the healthcare facilities in every ward of a city, using OpenStreetMap data, works out how many there are per km² of each ward, saves the results to Excel, and draws two choropleth maps: one of the number of healthcare facilities in each ward and one of their density.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. The program lists the file's columns and asks which one holds the ward name or number. If the file has no `geometry` column, it also asks which column holds the ward shapes.
2. All healthcare facilities inside the wards are downloaded from OpenStreetMap with `osmnx`: places tagged as a clinic, dentist, doctor's practice, hospital or nursing home under either the `amenity` or the `healthcare` key, so a facility is found whichever way it was mapped.
3. Each facility is reduced to a single point that is guaranteed to lie inside its shape, so a hospital mapped as a building outline that crosses a ward boundary is still counted. Each point is matched to the ward it falls in; a point lying exactly on the boundary between two wards is counted in only one of them. The healthcare facilities in each ward are then counted.
4. The wards are projected to the local UTM zone, chosen automatically for the city, and the area of each ward is computed in km². The density is the number of healthcare facilities divided by the area.
5. The user enters a name for the output file (without `.xlsx`). The program saves each ward's `Count`, `Area (in km2)` and `Density` (per km²) to that Excel file.
6. It then draws two maps, one after the other, with the ward boundaries outlined: the wards coloured by the number of healthcare facilities, and the wards shaded by their density per km².

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`Kolkata_Healthcare_Facilities_by_Ward.xlsx`](./Kolkata_Healthcare_Facilities_by_Ward.xlsx)<br>[`Kolkata Healthcare Facilities by Number in each Ward.png`](./Kolkata%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Kolkata Healthcare Facilities by Ward Area.png`](./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png) |

**🗺️ Sample maps**

<p align="center">
  <img src="./Kolkata%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Kolkata wards coloured by the number of healthcare facilities" width="720">
</p>

<p align="center">
  <img src="./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Kolkata wards shaded by healthcare facilities per km²" width="720">
</p>

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
