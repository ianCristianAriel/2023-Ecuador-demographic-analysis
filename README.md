## Project status
- **In Progress**

## File structure

    2023, Ecuador: demographic analyst
    │
    ├── data
    │   ├── processed_csv # processed .csv files
    │   └── raw_csv # raw .csv files
    │   │
    │   ├── ml_best_models # best ml models
    |   |   └── best_model.pkl
    │   │
    │   ├── images # images used on different stage and files
    |   |   └── approximate_location_of_population_age_60_plus.png
    |   |   └── census_by_age_2010__2022.png
    |   |   └── census_percentage_by_age_2010__2022.png
    |   |
    │   |__ genered_maps # interactive maps
    |       └── heatmap_grouped_marker_density_clusters_map.html
    |
    ├── notebooks
    |   |
    │   ├── packages # commons function from multiple notebooks
    |   |   └── common_functions.py
    |   |
    │   |-- 1_etl.ipynb
    |   |__ 2_eda_enrichment_pre_prosesing.ipynb
    |   |__ 3_data_viz.ipynb
    |   |__ 4_auto_sklearn.ipynb
    |
    ├── .gitattributes
    |
    ├── .gitignore
    │
    ├── REQUIREMENTS.txt
    |
    │-- LICENSE.md
    |
    └── README.md


## Functions

- Interest Insights on Ecuador, Segmented by Pichincha, Quito, and Sub-segmented by Current Population (2023) Age 50 Plus

    - Population by Educational Level
    - Population Distribution by Age and Educational Level
    - Population by Area
    - Population by Natural Region
    - Population by Education Level and Sex
    - Education Trends Between 2013 and 2014
    - Population Age 60 Plus by approximately geographic Location

## Packages used
- Python
  - numpy
  - pandas
  - seaborn
  - matplotlib
  - scikit-learn
  - joblib
  - scipy
  - missingno
  - folium

### Package installation
```bash
pip3 install -r requirements.txt
```
## Team
- [Yane, Ian Cristian](https://github.com/ianCristianAriel): Data Scientist
- [Mantilla, Jhon](https://www.linkedin.com/in/jhon-m-mantilla/): Project Manager

## Target Company
- [CORPORACIÓN GESTIÓN SOSTENIBLE](https://www.linkedin.com/company/corporacion-gestion-sostenible/)
