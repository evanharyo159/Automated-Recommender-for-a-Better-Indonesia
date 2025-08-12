"""
Prepare Indonesia Socioeconomic & Infrastructure Database
=========================================================

This script initializes a SQLite database (`BetterIndonesia.db`) with
socioeconomic and infrastructure data for Indonesia's provinces and
cities/regencies.

Source data: `All_Indo_rasterNsocio.xlsx` (Excel format)
Output: SQLite database with table `indonesia_data_socio_infra`

Author: Evan H
"""

import sqlite3
import pandas as pd
from pathlib import Path

# --- Configuration ---
DB_NAME = "BetterIndonesia.db"
TABLE_NAME = "indonesia_data_socio_infra"
EXCEL_FILE = "All_Indo_rasterNsocio.xlsx"

# --- Create database connection ---
db_path = Path(DB_NAME)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# --- Create table schema ---
cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        province TEXT,
        city_regency TEXT,
        gdp_billion REAL,
        poverty_line REAL,
        avg_years_schooling REAL,
        avg_monthly_expenses REAL,
        min_monthly_wage REAL,
        perc_roads_passable REAL,
        population INTEGER,
        population_density REAL,
        ratio_motorbike_ownership REAL,
        pop_0_14 REAL,
        pop_15_24 REAL,
        pop_25_44 REAL,
        pop_45_64 REAL,
        pop_65_plus REAL,
        pop_with_computer REAL,
        pop_with_internet REAL,
        pop_with_mobile REAL,
        area_km2 REAL,
        elevation_mean REAL,
        elevation_variance REAL,
        light_mean REAL,
        co_mean REAL,
        no2_mean REAL,
        so2_mean REAL,
        population_density_dup REAL,
        transport_points_per_area REAL,
        poi_points_per_area REAL,
        places_points_per_area REAL,
        natural_points_per_area REAL,
        railway_length_km_per_area REAL,
        water_length_km_per_area REAL,
        road_length_km_per_area REAL
    );
""")

# --- Load Excel data ---
if not Path(EXCEL_FILE).exists():
    raise FileNotFoundError(f"Data file '{EXCEL_FILE}' not found.")

data = pd.read_excel(EXCEL_FILE)

# --- Insert data into database ---
data.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

# --- Commit and close ---
conn.commit()
conn.close()

print(f"✅ Database '{DB_NAME}' initialized successfully with table '{TABLE_NAME}'.")
