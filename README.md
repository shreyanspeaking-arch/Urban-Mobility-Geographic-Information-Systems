<div align="center">

# 📐 Ward Area Map

**A branch of [Urban Mobility Geographic Information Systems](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The area of a ward is a basic measure of urban form: comparing ward sizes across a city shows where administrative units are packed tightly, usually in the dense core, and where they spread out towards the edges.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Ward Area Map**](#ward-area-map) | Area of each ward in km², saved to Excel and shown on a map |

## ⚙️ Getting started

```bash
git clone -b Ward-Area-Map --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas pandas matplotlib openpyxl
python ward_area.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows a map. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch.

---

## Ward Area Map

📄 **File:** [`ward_area.py`](./ward_area.py)

Computes the area of every ward in a city from a ward-boundary file, saves the list of wards and their areas to Excel, and draws a choropleth map of the wards shaded by area.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. If the file has no `WARD` column, the program lists its columns and asks which one holds the ward name or number; it does the same for the geometry column.
2. The ward shapes are projected to UTM zone 45N (`EPSG:32645`) so that they can be measured in metres, and the area of each ward is computed and converted to km².
3. The user enters a name for the output file (without `.xlsx`). The program saves the columns `WARD` and `Area (in km2)` to that Excel file, then projects the wards back to latitude and longitude and draws a map of the wards shaded by area.

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`ahmedabad_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/ahmedabad_wards.gpkg) | [`ahmedabad.xlsx`](./ahmedabad.xlsx)<br>[`ahmedabad.png`](./ahmedabad.png) |
| [`bengaluru_wards_2022.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/bengaluru_wards_2022.gpkg) | [`bengaluru.xlsx`](./bengaluru.xlsx)<br>[`bengaluru.png`](./bengaluru.png) |
| [`chennai_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/chennai_wards.gpkg) | [`chennai.xlsx`](./chennai.xlsx)<br>[`chennai.png`](./chennai.png) |
| [`delhi_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/delhi_wards.gpkg) | [`delhi.xlsx`](./delhi.xlsx)<br>[`delhi.png`](./delhi.png) |
| [`hyderabad_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/hyderabad_wards.gpkg) | [`hyderabad.xlsx`](./hyderabad.xlsx)<br>[`hyderabad.png`](./hyderabad.png) |
| [`jaipur_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/jaipur_wards.gpkg) | [`jaipur.xlsx`](./jaipur.xlsx)<br>[`jaipur.png`](./jaipur.png) |
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`kolkata.xlsx`](./kolkata.xlsx)<br>[`kolkata.png`](./kolkata.png) |
| [`mumbai_electoral_wards_2017.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg) | [`mumbai.xlsx`](./mumbai.xlsx)<br>[`mumbai.png`](./mumbai.png) |

**🗺️ Sample maps**

| | |
|:-:|:-:|
| **Ahmedabad**<br><img src="./ahmedabad.png" alt="Ahmedabad wards shaded by area" width="400"> | **Bengaluru**<br><img src="./bengaluru.png" alt="Bengaluru wards shaded by area" width="400"> |
| **Chennai**<br><img src="./chennai.png" alt="Chennai wards shaded by area" width="400"> | **Delhi**<br><img src="./delhi.png" alt="Delhi wards shaded by area" width="400"> |
| **Hyderabad**<br><img src="./hyderabad.png" alt="Hyderabad wards shaded by area" width="400"> | **Jaipur**<br><img src="./jaipur.png" alt="Jaipur wards shaded by area" width="400"> |
| **Kolkata**<br><img src="./kolkata.png" alt="Kolkata wards shaded by area" width="400"> | **Mumbai**<br><img src="./mumbai.png" alt="Mumbai wards shaded by area" width="400"> |

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
