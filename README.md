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
python Data_on_Healthcare_Facilities_by_Ward_Division.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows its maps. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. This program also needs an internet connection, because it downloads the healthcare facilities from OpenStreetMap.

---

## Data on Healthcare Facilities by Ward Division

📄 **File:** [`Data_on_Healthcare_Facilities_by_Ward_Division.py`](./Data_on_Healthcare_Facilities_by_Ward_Division.py)

Counts the healthcare facilities in every ward of a city, using OpenStreetMap data, works out how many there are per km² of each ward, saves the results to Excel, and draws two choropleth maps: one of the number of healthcare facilities in each ward and one of their density.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. The program lists the file's columns and asks which one holds the ward name or number. If the file has no `geometry` column, it also asks which column holds the ward shapes.
2. All healthcare facilities inside the wards are downloaded from OpenStreetMap with `osmnx`: places tagged as a clinic, dentist, doctor's practice, hospital, nursing home or baby hatch under the `amenity` key, every place carrying any `healthcare` tag, such as pharmacies, laboratories and blood donation centres, and every feature carrying any `emergency` tag, which covers ambulance stations and emergency wards but also items such as fire hydrants and defibrillators.
3. Each facility is reduced to a single point that is guaranteed to lie inside its shape, so a hospital mapped as a building outline that crosses a ward boundary is still counted. Each point is matched to the ward it falls in; a point lying exactly on the boundary between two wards is counted in only one of them. The healthcare facilities in each ward are then counted.
4. The wards are projected to the local UTM zone, chosen automatically for the city, and the area of each ward is computed in km². The density is the number of healthcare facilities divided by the area.
5. The user enters a name for the output file (without `.xlsx`). The program saves each ward's `Count`, `Area (in km2)` and `Density` (per km²) to that Excel file.
6. It then draws two maps, one after the other, with the ward boundaries outlined: the wards coloured by the number of healthcare facilities, and the wards shaded by their density per km².

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`ahmedabad_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/ahmedabad_wards.gpkg) | [`Ahmedabad_Healthcare_Facilities_by_Ward.xlsx`](./Ahmedabad_Healthcare_Facilities_by_Ward.xlsx)<br>[`Ahmedabad Healthcare Facilities by Number in each Ward.png`](./Ahmedabad%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Ahmedabad Healthcare Facilities by Ward Area.png`](./Ahmedabad%20Healthcare%20Facilities%20by%20Ward%20Area.png) |
| [`bengaluru_wards_2022.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/bengaluru_wards_2022.gpkg) | [`Bengaluru_Healthcare_Facilities_by_Ward.xlsx`](./Bengaluru_Healthcare_Facilities_by_Ward.xlsx)<br>[`Bengaluru Healthcare Facilities by Number in each Ward.png`](./Bengaluru%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Bengaluru Healthcare Facilities by Ward Area.png`](./Bengaluru%20Healthcare%20Facilities%20by%20Ward%20Area.png) |
| [`chennai_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/chennai_wards.gpkg) | [`Chennai_Healthcare_Facilities_by_Ward.xlsx`](./Chennai_Healthcare_Facilities_by_Ward.xlsx)<br>[`Chennai Healthcare Facilities by Number in each Ward.png`](./Chennai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Chennai Healthcare Facilities by Ward Area.png`](./Chennai%20Healthcare%20Facilities%20by%20Ward%20Area.png) |
| [`delhi_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/delhi_wards.gpkg) | [`Delhi_Healthcare_Facilities_by_Ward.xlsx`](./Delhi_Healthcare_Facilities_by_Ward.xlsx)<br>[`Delhi Healthcare Facilities by Number in each Ward.png`](./Delhi%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Delhi Healthcare Facilities by Ward Area.png`](./Delhi%20Healthcare%20Facilities%20by%20Ward%20Area.png) |
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`Kolkata_Healthcare_Facilities_by_Ward.xlsx`](./Kolkata_Healthcare_Facilities_by_Ward.xlsx)<br>[`Kolkata Healthcare Facilities by Number in each Ward.png`](./Kolkata%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Kolkata Healthcare Facilities by Ward Area.png`](./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png) |
| [`mumbai_electoral_wards_2017.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg) | [`Mumbai_Healthcare_Facilities_by_Ward.xlsx`](./Mumbai_Healthcare_Facilities_by_Ward.xlsx)<br>[`Mumbai Healthcare Facilities by Number in each Ward.png`](./Mumbai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png)<br>[`Mumbai Healthcare Facilities by Ward Area.png`](./Mumbai%20Healthcare%20Facilities%20by%20Ward%20Area.png) |

<!-- preview:start -->
**📋 First five rows**

<details>
<summary><code>Ahmedabad_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 48 RAMOL HATHIJAN | 5 | 30786045.509 | 30.786 | 0.162 |
| 47 VATVA | 24 | 11306182.516 | 11.306 | 2.123 |
| 46 LAMBHA | 16 | 48163155.266 | 48.163 | 0.332 |
| 45 ISANPUR | 47 | 4092708.236 | 4.093 | 11.484 |
| 44 KHOKHRA | 17 | 3588188.239 | 3.588 | 4.738 |

<sub>48 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Bengaluru_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 1 | 41 | 11373055.257 | 11.373 | 3.605 |
| 2 | 5 | 6960329.536 | 6.96 | 0.718 |
| 3 | 42 | 3867141.054 | 3.867 | 10.861 |
| 4 | 16 | 5146416.14 | 5.146 | 3.109 |
| 5 | 33 | 4048418.451 | 4.048 | 8.151 |

<sub>243 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Chennai_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 119 | 9 | 1381005.254 | 1.381 | 6.517 |
| 7 | 0 | 7735900.17 | 7.736 | 0 |
| 26 | 4 | 4809087.648 | 4.809 | 0.832 |
| 174 | 7 | 8340795.421 | 8.341 | 0.839 |
| 132 | 18 | 1403502.758 | 1.404 | 12.825 |

<sub>201 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Delhi_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| CANT_1 | 1 | 1274680.409 | 1.275 | 0.785 |
| CANT_2 | 3 | 8760167.474 | 8.76 | 0.342 |
| CANT_4 | 6 | 8382204.276 | 8.382 | 0.716 |
| CANT_5 | 0 | 3493525.693 | 3.494 | 0 |
| CANT_6 | 9 | 15247664.011 | 15.248 | 0.59 |

<sub>290 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Kolkata_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 93 | 6 | 1867950.649 | 1.868 | 3.212 |
| 61 | 4 | 642597.239 | 0.643 | 6.225 |
| 86 | 11 | 887935.917 | 0.888 | 12.388 |
| 90 | 6 | 1145646.051 | 1.146 | 5.237 |
| 26 | 0 | 352579.077 | 0.353 | 0 |

<sub>141 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Mumbai_Healthcare_Facilities_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 227 | 5 | 3245346.262 | 3.245 | 1.541 |
| 225 | 27 | 4778852.65 | 4.779 | 5.65 |
| 224 | 5 | 1073583.608 | 1.074 | 4.657 |
| 226 | 7 | 3175394.776 | 3.175 | 2.204 |
| 208 | 8 | 1653071.115 | 1.653 | 4.839 |

<sub>227 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>
<!-- preview:end -->

**🗺️ Sample maps**

| City | Number of facilities in each ward | Facilities per km² |
|:-:|:-:|:-:|
| **Ahmedabad** | <img src="./Ahmedabad%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Ahmedabad wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 1.</b> Ahmedabad wards coloured by the number of healthcare facilities<br><a href="./Ahmedabad%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Ahmedabad Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/ahmedabad_wards.gpkg">ahmedabad_wards.gpkg</a></sub> | <img src="./Ahmedabad%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Ahmedabad wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 2.</b> Ahmedabad wards shaded by healthcare facilities per km²<br><a href="./Ahmedabad%20Healthcare%20Facilities%20by%20Ward%20Area.png">Ahmedabad Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/ahmedabad_wards.gpkg">ahmedabad_wards.gpkg</a></sub> |
| **Bengaluru** | <img src="./Bengaluru%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Bengaluru wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 3.</b> Bengaluru wards coloured by the number of healthcare facilities<br><a href="./Bengaluru%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Bengaluru Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/bengaluru_wards_2022.gpkg">bengaluru_wards_2022.gpkg</a></sub> | <img src="./Bengaluru%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Bengaluru wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 4.</b> Bengaluru wards shaded by healthcare facilities per km²<br><a href="./Bengaluru%20Healthcare%20Facilities%20by%20Ward%20Area.png">Bengaluru Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/bengaluru_wards_2022.gpkg">bengaluru_wards_2022.gpkg</a></sub> |
| **Chennai** | <img src="./Chennai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Chennai wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 5.</b> Chennai wards coloured by the number of healthcare facilities<br><a href="./Chennai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Chennai Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/chennai_wards.gpkg">chennai_wards.gpkg</a></sub> | <img src="./Chennai%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Chennai wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 6.</b> Chennai wards shaded by healthcare facilities per km²<br><a href="./Chennai%20Healthcare%20Facilities%20by%20Ward%20Area.png">Chennai Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/chennai_wards.gpkg">chennai_wards.gpkg</a></sub> |
| **Delhi** | <img src="./Delhi%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Delhi wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 7.</b> Delhi wards coloured by the number of healthcare facilities<br><a href="./Delhi%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Delhi Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/delhi_wards.gpkg">delhi_wards.gpkg</a></sub> | <img src="./Delhi%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Delhi wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 8.</b> Delhi wards shaded by healthcare facilities per km²<br><a href="./Delhi%20Healthcare%20Facilities%20by%20Ward%20Area.png">Delhi Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/delhi_wards.gpkg">delhi_wards.gpkg</a></sub> |
| **Kolkata** | <img src="./Kolkata%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Kolkata wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 9.</b> Kolkata wards coloured by the number of healthcare facilities<br><a href="./Kolkata%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Kolkata Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg">kolkata_wards_141.gpkg</a></sub> | <img src="./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Kolkata wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 10.</b> Kolkata wards shaded by healthcare facilities per km²<br><a href="./Kolkata%20Healthcare%20Facilities%20by%20Ward%20Area.png">Kolkata Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg">kolkata_wards_141.gpkg</a></sub> |
| **Mumbai** | <img src="./Mumbai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png" alt="Mumbai wards coloured by the number of healthcare facilities" width="400"><br><sub><b>Figure 11.</b> Mumbai wards coloured by the number of healthcare facilities<br><a href="./Mumbai%20Healthcare%20Facilities%20by%20Number%20in%20each%20Ward.png">Mumbai Healthcare Facilities by Number in each Ward.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg">mumbai_electoral_wards_2017.gpkg</a></sub> | <img src="./Mumbai%20Healthcare%20Facilities%20by%20Ward%20Area.png" alt="Mumbai wards shaded by healthcare facilities per km²" width="400"><br><sub><b>Figure 12.</b> Mumbai wards shaded by healthcare facilities per km²<br><a href="./Mumbai%20Healthcare%20Facilities%20by%20Ward%20Area.png">Mumbai Healthcare Facilities by Ward Area.png</a> · from <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg">mumbai_electoral_wards_2017.gpkg</a></sub> |

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
