#!/usr/bin/env python3

"""
Database Initialization Script

Creates:
    database/catalog.db

Creates Table:
    items

Verifies:
    SQLite installation
    Database connectivity
    Read/Write capability
"""

from pathlib import Path
import sqlite3
import sys
from datetime import datetime

DB_FOLDER = "..\\database"
DB_FILE = DB_FOLDER + "\\catalog.db"

now = datetime.utcnow().isoformat()

moon_items = [

    # -----------------------------
    # APOLLO ROVERS
    # -----------------------------

    (
        "Apollo 15 Rover",
        "apollo-15-rover",
        "First lunar rover used by astronauts.",
        "The Apollo 15 Lunar Roving Vehicle was used by David Scott and Jim Irwin during three EVAs in July-August 1971. After completion of the mission it was left parked near the Apollo 15 landing site in the Hadley-Apennine region.",
        26.132,
        3.633,
        "#00a2ff",
        "",
        "",
        "/item/apollo-15-rover",
        "https://en.wikipedia.org/wiki/Lunar_Roving_Vehicle",
        "https://images.nasa.gov/search?q=apollo%2015%20Rover&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Hadley-Apennine",
        "Apollo 15",
        1,
        1,
        now,
        now
    ),

    (
        "Apollo 16 Rover",
        "apollo-16-rover",
        "Second lunar rover used by astronauts.",
        "The Apollo 16 rover remains in the Descartes Highlands near the Apollo 16 landing site.",
        -8.973,
        15.501,
        "#00a2ff",
        "",
        "",
        "/item/apollo-16-rover",
        "https://en.wikipedia.org/wiki/Lunar_Roving_Vehicle",
        "https://images.nasa.gov/search?q=apollo%2016%20Rover&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Descartes Highlands",
        "Apollo 16",
        2,
        1,
        now,
        now
    ),

    (
        "Apollo 17 Rover",
        "apollo-17-rover",
        "Final Apollo lunar rover.",
        "The Apollo 17 rover was used by Eugene Cernan and Harrison Schmitt and remains in Taurus-Littrow Valley.",
        20.191,
        30.772,
        "#00a2ff",
        "",
        "",
        "/item/apollo-17-rover",
        "https://en.wikipedia.org/wiki/Lunar_Roving_Vehicle",
        "https://images.nasa.gov/search?q=apollo%2017%20Rover&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Taurus-Littrow",
        "Apollo 17",
        3,
        1,
        now,
        now
    ),

    # -----------------------------
    # ALSEP STATIONS
    # -----------------------------

    (
        "Apollo 12 ALSEP",
        "apollo-12-alsep",
        "Apollo scientific station.",
        "ALSEP package deployed in Oceanus Procellarum by Apollo 12 astronauts.",
        -3.0098,
        -23.4249,
        "#00ffff",
        "",
        "",
        "/item/apollo-12-alsep",
        "https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package",
        "https://images.nasa.gov/search?q=apollo%2012%20ALSEP&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Oceanus Procellarum",
        "Apollo 12",
        20,
        1,
        now,
        now
    ),

    (
        "Apollo 14 ALSEP",
        "apollo-14-alsep",
        "Apollo scientific station.",
        "Apollo 14 ALSEP located at the Fra Mauro landing site.",
        -3.64419,
        -17.47768,
        "#00ffff",
        "",
        "",
        "/item/apollo-14-alsep",
        "https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package",
        "https://images.nasa.gov/search?q=apollo%2014%20ALSEP&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
         "Fra Mauro",
        "Apollo 14",
        21,
        1,
        now,
        now
    ),

    (
        "Apollo 15 ALSEP",
        "apollo-15-alsep",
        "Apollo scientific station.",
        "Apollo 15 ALSEP in the Hadley-Apennine region.",
        26.13406,
        3.62991,
        "#00ffff",
        "",
        "",
        "/item/apollo-15-alsep",
        "https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package",
        "https://images.nasa.gov/search?q=apollo%2015%20ALSEP&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
         "Hadley-Apennine",
        "Apollo 15",
        22,
        1,
        now,
        now
    ),

    (
        "Apollo 16 ALSEP",
        "apollo-16-alsep",
        "Apollo scientific station.",
        "ALSEP deployment site in the Descartes Highlands.",
        -8.9759,
        15.4986,
        "#00ffff",
        "",
        "",
        "/item/apollo-16-alsep",
        "https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package",
        "https://images.nasa.gov/search?q=apollo%2016%20ALSEP&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
         "Descartes Highlands",
        "Apollo 16",
        23,
        1,
        now,
        now
    ),

    (
        "Apollo 17 ALSEP",
        "apollo-17-alsep",
        "Apollo scientific station.",
        "Final ALSEP deployment in Taurus-Littrow Valley.",
        20.1923,
        30.7655,
        "#00ffff",
        "",
        "",
        "/item/apollo-17-alsep",
        "https://en.wikipedia.org/wiki/Apollo_Lunar_Surface_Experiments_Package",
        "https://images.nasa.gov/search?q=apollo%2017%20ALSEP&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
         "Taurus-Littrow",
        "Apollo 17",
        24,
        1,
        now,
        now
    ),

# =========================================================
# RANGER MISSIONS
# =========================================================

    (
        "Ranger 4",
        "ranger-4",
        "First U.S. spacecraft to reach the Moon.",
        "Ranger 4 became the first American spacecraft to impact the Moon. Contact was lost before useful scientific data could be transmitted, but the spacecraft successfully reached the lunar surface on April 26, 1962.",
        -15.5,
        -130.7,
        "#ff0000",
        "",
        "",
        "/item/ranger-4",
        "https://en.wikipedia.org/wiki/Ranger_4",
        "https://images.nasa.gov/search?q=Ranger%204&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
         "Far Side",
        "Ranger 4",
        100,
        1,
        now,
        now
    ),

    (
        "Ranger 6",
        "ranger-6",
        "Successful impact mission with camera failure.",
        "Ranger 6 reached the Moon on February 2, 1964. The spacecraft impacted successfully but a failure in the television system prevented the return of lunar images.",
        9.4,
        21.5,
        "#ff0000",
        "",
        "",
        "/item/ranger-6",
        "https://en.wikipedia.org/wiki/Ranger_6",
        "https://images.nasa.gov/search?q=Ranger%206&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Mare Tranquillitatis",
        "Ranger 6",
        101,
        1,
        now,
        now
    ),

    (
        "Ranger 7",
        "ranger-7",
        "First fully successful Ranger mission.",
        "Ranger 7 returned more than 4,000 close-up lunar photographs before impacting Mare Cognitum on July 31, 1964. The mission demonstrated the viability of high-resolution lunar reconnaissance and paved the way for Apollo landing-site selection.",
        -10.70,
        -20.67,
        "#ff0000",
        "",
        "",
        "/item/ranger-7",
        "https://en.wikipedia.org/wiki/Ranger_7",
        "https://images.nasa.gov/search?q=Ranger%207&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Mare Cognitum",
        "Ranger 7",
        102,
        1,
        now,
        now
    ),

    (
        "Ranger 8",
        "ranger-8",
        "Photographed the future Apollo region.",
        "Ranger 8 transmitted thousands of images while descending toward Mare Tranquillitatis. The photographs provided critical information used during planning for future Apollo missions.",
        2.71,
        24.81,
        "#ff0000",
        "",
        "",
        "/item/ranger-8",
        "https://en.wikipedia.org/wiki/Ranger_8",
        "https://images.nasa.gov/search?q=Ranger%208&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Mare Tranquillitatis",
        "Ranger 8",
        103,
        1,
        now,
        now
    ),

    (
        "Ranger 9",
        "ranger-9",
        "Final Ranger mission.",
        "Ranger 9 targeted Alphonsus Crater and transmitted 5,814 images during its final descent in March 1965. Millions of television viewers watched the live broadcast of the final approach.",
        -12.83,
        -2.37,
        "#ff0000",
        "",
        "",
        "/item/ranger-9",
        "https://en.wikipedia.org/wiki/Ranger_9",
        "https://images.nasa.gov/search?q=Ranger%209&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
        "Alphonsus Crater",
        "Ranger 9",
        104,
        1,
        now,
        now
    ),

 # =========================================================
# LUNAR LASER RETROREFLECTORS (MIRROR ARRAYS)
# =========================================================

(
    "Apollo 11 Mirror Array",
    "apollo-11-lrrr",
    "First lunar laser reflector.",
    "Apollo 11 deployed the first Lunar Laser Ranging Retroreflector on July 21, 1969. The mirror array remains operational and is still used by observatories around the world to precisely measure the Earth-Moon distance.",
    0.67345,
    23.47307,
    "#00ff88",
    "",
    "",
    "/item/apollo-11-lrrr",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Mare Tranquillitatis",
    "Apollo 11",
    200,
    1,
    now,
    now
),

(
    "Apollo 14 Mirror Array",
    "apollo-14-lrrr",
    "Lunar laser ranging reflector.",
    "Apollo 14 deployed a lunar laser retroreflector at the Fra Mauro landing site. The instrument continues to support lunar ranging experiments more than fifty years after installation.",
    -3.64417,
    -17.47865,
    "#00ff88",
    "",
    "",
    "/item/apollo-14-lrrr",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Fra Mauro",
    "Apollo 14",
    201,
    1,
    now,
    now
),

(
    "Apollo 15 Mirror Array",
    "apollo-15-lrrr",
    "Largest Apollo reflector array.",
    "Apollo 15 deployed the largest lunar laser retroreflector array left by the Apollo program. Located in the Hadley-Apennine region, it contains three times as many corner-cube reflectors as the Apollo 11 and Apollo 14 arrays.",
    26.13341,
    3.62850,
    "#00ff88",
    "",
    "",
    "/item/apollo-15-lrrr",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Hadley-Apennine",
    "Apollo 15",
    202,
    1,
    now,
    now
),

(
    "Lunokhod 1 Mirror Array",
    "lunokhod-1-lrrr",
    "Soviet rover reflector.",
    "A French-built laser reflector carried by the Soviet Lunokhod 1 rover. After being rediscovered in Lunar Reconnaissance Orbiter imagery, it was returned to active lunar laser ranging service.",
    38.3152,
    -35.0080,
    "#ffaa00",
    "",
    "",
    "/item/lunokhod-1-lrrr",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Mare Imbrium",
    "Luna 17",
    203,
    1,
    now,
    now
),

(
    "Lunokhod 2 Mirror Array",
    "lunokhod-2-lrrr",
    "Soviet rover reflector.",
    "The Lunokhod 2 rover carried a French-built retroreflector array to Le Monnier crater. It remains one of the most important targets for lunar laser ranging experiments.",
    25.8323,
    30.9221,
    "#ffaa00",
    "",
    "",
    "/item/lunokhod-2-lrrr",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Le Monnier Crater",
    "Luna 21",
    204,
    1,
    now,
    now
),

(
    "Vikram Laser Reflector",
    "vikram-lra",
    "Indian lunar reflector.",
    "The Chandrayaan-3 Vikram lander carries a small laser retroreflector supplied for future lunar ranging experiments. It is located near the lunar south pole at Shiv Shakti Point.",
    -69.367621,
    32.348126,
    "#00ff88",
    "",
    "",
    "/item/vikram-lra",
    "https://en.wikipedia.org/wiki/List_of_retroreflectors_on_the_Moon",
    "https://images.nasa.gov/search?q=Apollo%2011%20lrr&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Shiv Shakti Point",
    "Chandrayaan-3",
    205,
    1,
    now,
    now
),

# =========================================================
# AMERICAN FLAGS ON THE MOON
# =========================================================

(
    "Apollo 11 Flag",
    "apollo-11-flag",
    "First American flag placed on the Moon.",
    "Apollo 11 astronauts Neil Armstrong and Buzz Aldrin erected the first American flag on the lunar surface at Tranquility Base on July 20, 1969. Buzz Aldrin later reported seeing the flag knocked over during liftoff of the Lunar Module ascent stage.",
    0.67416,
    23.47314,
    "#0000ff",
    "",
    "",
    "/item/apollo-11-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2011%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Mare Tranquillitatis",
    "Apollo 11",
    400,
    1,
    now,
    now
),

(
    "Apollo 12 Flag",
    "apollo-12-flag",
    "American flag at Oceanus Procellarum.",
    "Apollo 12 astronauts Charles Conrad and Alan Bean deployed an American flag near the Intrepid Lunar Module during their November 1969 mission.",
    -3.0128,
    -23.4219,
    "#0000ff",
    "",
    "",
    "/item/apollo-12-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2012%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Oceanus Procellarum",
    "Apollo 12",
    401,
    1,
    now,
    now
),

(
    "Apollo 14 Flag",
    "apollo-14-flag",
    "American flag at Fra Mauro.",
    "Apollo 14 astronauts Alan Shepard and Edgar Mitchell erected an American flag near the Antares Lunar Module in February 1971.",
    -3.64589,
    -17.47194,
    "#0000ff",
    "",
    "",
    "/item/apollo-14-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2014%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Fra Mauro",
    "Apollo 14",
    402,
    1,
    now,
    now
),

(
    "Apollo 15 Flag",
    "apollo-15-flag",
    "American flag at Hadley-Apennine.",
    "Apollo 15 astronauts David Scott and James Irwin erected an American flag beside the Falcon Lunar Module in July 1971.",
    26.13239,
    3.63330,
    "#0000ff",
    "",
    "",
    "/item/apollo-15-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2015%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Hadley-Apennine",
    "Apollo 15",
    403,
    1,
    now,
    now
),

(
    "Apollo 16 Flag",
    "apollo-16-flag",
    "American flag at the Descartes Highlands.",
    "Apollo 16 astronauts John Young and Charles Duke planted an American flag near the Orion Lunar Module in April 1972.",
    -8.9734,
    15.5011,
    "#0000ff",
    "",
    "",
    "/item/apollo-16-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2016%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Descartes Highlands",
    "Apollo 16",
    404,
    1,
    now,
    now
),

(
    "Apollo 17 Flag",
    "apollo-17-flag",
    "Last American flag placed on the Moon.",
    "Apollo 17 astronauts Eugene Cernan and Harrison Schmitt planted the final Apollo flag in Taurus-Littrow Valley in December 1972.",
    20.1911,
    30.7723,
    "#0000ff",
    "",
    "",
    "/item/apollo-17-flag",
    "https://en.wikipedia.org/wiki/Lunar_Flag_Assembly",
    "https://images.nasa.gov/search?q=Apollo%2017%20flag&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
    "Taurus-Littrow",
    "Apollo 17",
    405,
    1,
    now,
    now
),

(
    "Eugene Shoemaker Memorial",
    "eugene-shoemaker-ashes",
    "First human remains placed on the Moon.",
    "A small portion of planetary scientist Eugene Shoemaker's cremated remains was carried aboard NASA's Lunar Prospector spacecraft. On July 31, 1999, after completing its science mission, Lunar Prospector was intentionally crashed into Shoemaker Crater near the lunar south pole. Shoemaker became the first and, for many years, only person whose ashes were placed on the Moon. The memorial capsule carried a quotation from Romeo and Juliet and an image of Comet Hale-Bopp.",
    -87.7,
    42.0,
    "#ffffff",
    "",
    "",
    "/item/eugene-shoemaker-ashes",
    "https://en.wikipedia.org/wiki/Eugene_Merle_Shoemaker",
    "https://images.nasa.gov/search?q=Eugene%2017%20Shoemaker&page=1&media=image,video,audio&yearStart=1920&yearEnd=2026",
     "Shoemaker Crater",
    "Lunar Prospector",
    300,
    1,
    now,
    now
)

   ]

def open_database():
    """Open database and tables."""

    Path(DB_FOLDER).mkdir(parents=True,exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    print(f"Database Opened : {DB_FILE}")

    return conn

def check_sqlite():
    """Verify SQLite support is available."""

    try:
        version = sqlite3.sqlite_version

        print("=" * 60)
        print("SQLite Check")
        print("=" * 60)
        print(f"SQLite Version : {version}")
        print("SQLite Status  : AVAILABLE")
        print()

        return True

    except Exception as ex:
        print("ERROR: SQLite not available")
        print(ex)
        return False

def seed_data(conn):
    """Insert sample records if table empty."""

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM items
        """
    )

    count = cursor.fetchone()[0]

    if count > 0:
        print(f"Existing Records : {count}")
        return

    now = datetime.utcnow().isoformat()

    for i, item in enumerate(moon_items):

        if len(item) != 18:
            print()
            print("BAD RECORD")
            print(f"Index: {i}")
            print(f"Length: {len(item)}")
            print(item)
            print()

    cursor.executemany(
    """
    INSERT INTO items
    (
        title,
        slug,
        short_description,
        long_description,
        lunar_latitude,
        lunar_longitude,
        marker_color,
        thumbnail_image,
        hero_image,
        target_url,
        wikipedia_url,
        nasa_images_url,
        moon_region,
        mission_name,
        display_order,
        active,
        created_date,
        modified_date
    )
    VALUES
    (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
    """,
    moon_items
    )

    conn.commit()

    print(f"Sample Records Added : {len(moon_items)}")


def verify_database(conn):
    """Verify database can be queried."""

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            title,
            slug
        FROM items
        ORDER BY display_order
        """
    )

    rows = cursor.fetchall()

    print()
    print("=" * 60)
    print("Database Verification")
    print("=" * 60)

    print(f"Records Found : {len(rows)}")
    print()

    for row in rows:
        print(
            f"ID={row[0]:<3} "
            f"Title={row[1]} "
            f"Slug={row[2]}"
        )

    print()
    print("Database verification successful.")

def main():

    print()
    print("Website Database Setup")
    print()

    if not check_sqlite():
        sys.exit(1)

    conn = None

    try:

        conn = open_database()

        seed_data(conn)

        verify_database(conn)

        print()
        print("=" * 60)
        print("SUCCESS")
        print("=" * 60)
        print(f"Database Location : {Path(DB_FILE).resolve()}")
        print()

    except Exception as ex:

        print()
        print("DATABASE ERROR")
        print(ex)
        sys.exit(1)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()