<div align="center">

# 🎓 Ward Educational Institutions

**A branch of [Urban Mobility Geographic Information Systems](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems), a collection of Python programs that map and measure the wards of Indian cities.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Programs](https://img.shields.io/badge/programs-1-2ea44f) ![Interactive](https://img.shields.io/badge/run%20in-terminal-lightgrey)

</div>

The number and density of educational institutes show how evenly education is spread across a city. The count says how many schools, colleges, universities and similar institutes each ward has; the density divides that by the ward's area, in institutes per km², so that large and small wards can be compared fairly and wards with few institutes within easy reach of their residents stand out.

## 📂 Programs in this branch

| Program | What it does |
|---|---|
| [**Data on Educational Institutes by Ward Division**](#data-on-educational-institutes-by-ward-division) | Number of educational institutes in each ward and their density per km², using OpenStreetMap data, saved to Excel and shown on two maps |

## ⚙️ Getting started

```bash
git clone -b Ward-Educational-Institutions --single-branch https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems.git
cd Urban-Mobility-Geographic-Information-Systems
curl -LO https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/raw/Input-gpkg-files/kolkata_wards_141.gpkg
pip install geopandas osmnx pandas numpy matplotlib openpyxl
python Data_on_Educational_Institutes_by_Ward_Division.py
```

Every program is interactive: it asks for its inputs one at a time in the terminal, then saves the results to an `.xlsx` file and shows its maps. Input files for 8 cities are on the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. This program also needs an internet connection, because it downloads the educational institutes from OpenStreetMap.

---

## Data on Educational Institutes by Ward Division

📄 **File:** [`Data_on_Educational_Institutes_by_Ward_Division.py`](./Data_on_Educational_Institutes_by_Ward_Division.py)

Counts the educational institutes in every ward of a city, using OpenStreetMap data, works out how many there are per km² of each ward, saves the results to Excel, and draws two choropleth maps: one of the number of educational institutes in each ward and one of their density.

**How it works**

1. The user enters the name of a ward-boundary file, such as a `.gpkg` file from the [Input gpkg files](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/tree/Input-gpkg-files) branch. The program lists the file's columns and asks which one holds the ward name or number. If the file has no `geometry` column, it also asks which column holds the ward shapes.
2. All educational institutes inside the wards are downloaded from OpenStreetMap with `osmnx`: places tagged as a kindergarten, school, college, university, research institute or training centre, together with land marked for educational use (`landuse=education`), such as school and college campuses.
3. Each facility is reduced to a single point that is guaranteed to lie inside its shape, so a campus mapped as an outline that crosses a ward boundary is still counted. Each point is matched to the ward it falls in; a point lying exactly on the boundary between two wards is counted in only one of them. The educational institutes in each ward are then counted.
4. The wards are projected to the local UTM zone, chosen automatically for the city, and the area of each ward is computed in km². The density is the number of educational institutes divided by the area.
5. The user enters a name for the output file (without `.xlsx`). The program saves each ward's `Count`, `Area (in km2)` and `Density` (per km²) to that Excel file.
6. It then draws two maps, one after the other, with the ward boundaries outlined: the wards coloured by the number of educational institutes, and the wards shaded by their density per km².

**🧪 Sample input and output**

| Input | Output |
|---|---|
| [`ahmedabad_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/ahmedabad_wards.gpkg) | [`Ahmedabad_Educational_Institutions_by_Ward.xlsx`](./Ahmedabad_Educational_Institutions_by_Ward.xlsx)<br>[`Ahmedabad Educational Institutions by Number in each Ward.png`](./Ahmedabad%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Ahmedabad No of Educations Institutions per unit Ward Area.png`](./Ahmedabad%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`bengaluru_wards_2022.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/bengaluru_wards_2022.gpkg) | [`Bengaluru_Educational_Institutions_by_Ward.xlsx`](./Bengaluru_Educational_Institutions_by_Ward.xlsx)<br>[`Bengalurui No of Educations Institutions per unit Ward Area.png`](./Bengalurui%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png)<br>[`Bengaluru No of Educations Institutions per unit Ward Area.png`](./Bengaluru%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`chennai_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/chennai_wards.gpkg) | [`Chennai_Educational_Institutions_by_Ward.xlsx`](./Chennai_Educational_Institutions_by_Ward.xlsx)<br>[`Chennai Educational Institutions by Number in each Ward.png`](./Chennai%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Chennai No of Educations Institutions per unit Ward Area.png`](./Chennai%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`delhi_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/delhi_wards.gpkg) | [`Delhi_Educational_Institutions_by_Ward.xlsx`](./Delhi_Educational_Institutions_by_Ward.xlsx)<br>[`Delhi Educational Institutions by Number in each Ward.png`](./Delhi%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Delhi No of Educations Institutions per unit Ward Area.png`](./Delhi%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`hyderabad_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/hyderabad_wards.gpkg) | [`Hyderabad_Educational_Institutions_by_Ward.xlsx`](./Hyderabad_Educational_Institutions_by_Ward.xlsx)<br>[`Hyderabad Educational Institutions by Number in each Ward.png`](./Hyderabad%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Hyderabad No of Educations Institutions per unit Ward Area.png`](./Hyderabad%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`jaipur_wards.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/jaipur_wards.gpkg) | [`Jaipur_Educational_Institutions_by_Ward.xlsx`](./Jaipur_Educational_Institutions_by_Ward.xlsx)<br>[`Jaipur Educational Institutions by Number in each Ward.png`](./Jaipur%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Jaipur No of Educations Institutions per unit Ward Area.png`](./Jaipur%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`kolkata_wards_141.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/kolkata_wards_141.gpkg) | [`Kolkata_Educational_Institutions_by_Ward.xlsx`](./Kolkata_Educational_Institutions_by_Ward.xlsx)<br>[`Kolkata Educational Institutions by Number in each Ward.png`](./Kolkata%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Kolkata No of Educations Institutions per unit Ward Area.png`](./Kolkata%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |
| [`mumbai_electoral_wards_2017.gpkg`](https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems/blob/Input-gpkg-files/mumbai_electoral_wards_2017.gpkg) | [`Mumbai_Educational_Institutions_by_Ward.xlsx`](./Mumbai_Educational_Institutions_by_Ward.xlsx)<br>[`Mumbai Educational Institutions by Number in each Ward.png`](./Mumbai%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png)<br>[`Mumbai No of Educations Institutions per unit Ward Area.png`](./Mumbai%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png) |

<!-- preview:start -->
**📋 First five rows**

<details>
<summary><code>Ahmedabad_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 48 RAMOL HATHIJAN | 0 | 30786045.509 | 30.786 | 0 |
| 47 VATVA | 0 | 11306182.516 | 11.306 | 0 |
| 46 LAMBHA | 0 | 48163155.266 | 48.163 | 0 |
| 45 ISANPUR | 0 | 4092708.236 | 4.093 | 0 |
| 44 KHOKHRA | 0 | 3588188.239 | 3.588 | 0 |

<sub>48 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Bengaluru_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 1 | 34 | 11373055.257 | 11.373 | 2.99 |
| 2 | 3 | 6960329.536 | 6.96 | 0.431 |
| 3 | 13 | 3867141.054 | 3.867 | 3.362 |
| 4 | 11 | 5146416.14 | 5.146 | 2.137 |
| 5 | 27 | 4048418.451 | 4.048 | 6.669 |

<sub>243 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Chennai_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 119 | 8 | 1381005.254 | 1.381 | 5.793 |
| 7 | 0 | 7735900.17 | 7.736 | 0 |
| 26 | 0 | 4809087.648 | 4.809 | 0 |
| 174 | 10 | 8340795.421 | 8.341 | 1.199 |
| 132 | 8 | 1403502.758 | 1.404 | 5.7 |

<sub>201 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Delhi_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| CANT_1 | 0 | 1274680.409 | 1.275 | 0 |
| CANT_2 | 5 | 8760167.474 | 8.76 | 0.571 |
| CANT_4 | 4 | 8382204.276 | 8.382 | 0.477 |
| CANT_5 | 3 | 3493525.693 | 3.494 | 0.859 |
| CANT_6 | 6 | 15247664.011 | 15.248 | 0.394 |

<sub>290 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Hyderabad_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| Ward 91 Khairatabad | 23 | 8614755.376 | 8.615 | 2.67 |
| Ward 105 Gachibowli | 54 | 49103996.012 | 49.104 | 1.1 |
| Ward 60 Rajendra Nagar | 15 | 21251826.188 | 21.252 | 0.706 |
| Ward 95 Jubilee Hills | 26 | 8668646.165 | 8.669 | 2.999 |
| Ward 6 Nacharam | 9 | 5116544.605 | 5.117 | 1.759 |

<sub>145 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Jaipur_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 76 | 1 | 11056093.311 | 11.056 | 0.09 |
| 34 | 3 | 39624172.69 | 39.624 | 0.076 |
| 11 | 7 | 9802919.284 | 9.803 | 0.714 |
| 12 | 4 | 20441244.988 | 20.441 | 0.196 |
| 13 | 5 | 6933213.746 | 6.933 | 0.721 |

<sub>77 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Kolkata_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 93 | 10 | 1867950.649 | 1.868 | 5.353 |
| 61 | 3 | 642597.239 | 0.643 | 4.669 |
| 86 | 5 | 887935.917 | 0.888 | 5.631 |
| 90 | 2 | 1145646.051 | 1.146 | 1.746 |
| 26 | 1 | 352579.077 | 0.353 | 2.836 |

<sub>141 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>

<details>
<summary><code>Mumbai_Educational_Institutions_by_Ward.xlsx</code></summary>

| ward | Count | Area (in m2) | Area (in km2) | Density |
|---|---|---|---|---|
| 227 | 12 | 3245346.262 | 3.245 | 3.698 |
| 225 | 26 | 4778852.65 | 4.779 | 5.441 |
| 224 | 1 | 1073583.608 | 1.074 | 0.931 |
| 226 | 12 | 3175394.776 | 3.175 | 3.779 |
| 208 | 0 | 1653071.115 | 1.653 | 0 |

<sub>227 rows in total; the `geometry` column (ward shapes) is left out.</sub>

</details>
<!-- preview:end -->

**🗺️ Sample maps**

| City | Number of institutes in each ward | Institutes per km² |
|:-:|:-:|:-:|
| **Ahmedabad** | <img src="./Ahmedabad%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Ahmedabad wards coloured by the number of educational institutes" width="400"> | <img src="./Ahmedabad%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Ahmedabad wards shaded by educational institutes per km²" width="400"> |
| **Bengaluru** | <img src="./Bengalurui%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Bengaluru wards coloured by the number of educational institutes" width="400"> | <img src="./Bengaluru%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Bengaluru wards shaded by educational institutes per km²" width="400"> |
| **Chennai** | <img src="./Chennai%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Chennai wards coloured by the number of educational institutes" width="400"> | <img src="./Chennai%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Chennai wards shaded by educational institutes per km²" width="400"> |
| **Delhi** | <img src="./Delhi%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Delhi wards coloured by the number of educational institutes" width="400"> | <img src="./Delhi%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Delhi wards shaded by educational institutes per km²" width="400"> |
| **Hyderabad** | <img src="./Hyderabad%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Hyderabad wards coloured by the number of educational institutes" width="400"> | <img src="./Hyderabad%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Hyderabad wards shaded by educational institutes per km²" width="400"> |
| **Jaipur** | <img src="./Jaipur%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Jaipur wards coloured by the number of educational institutes" width="400"> | <img src="./Jaipur%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Jaipur wards shaded by educational institutes per km²" width="400"> |
| **Kolkata** | <img src="./Kolkata%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Kolkata wards coloured by the number of educational institutes" width="400"> | <img src="./Kolkata%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Kolkata wards shaded by educational institutes per km²" width="400"> |
| **Mumbai** | <img src="./Mumbai%20Educational%20Institutions%20by%20Number%20in%20each%20Ward.png" alt="Mumbai wards coloured by the number of educational institutes" width="400"> | <img src="./Mumbai%20No%20of%20Educations%20Institutions%20per%20unit%20Ward%20Area.png" alt="Mumbai wards shaded by educational institutes per km²" width="400"> |

---

<div align="center"><sub>📚 <a href="https://github.com/shreyanspeaking-arch/Urban-Mobility-Geographic-Information-Systems">Back to all topics</a></sub></div>
