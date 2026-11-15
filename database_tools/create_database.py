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


def create_database():
    """Create database and tables."""

    Path(DB_FOLDER).mkdir(parents=True,exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            short_description TEXT,
            long_description TEXT,
            lunar_latitude REAL,
            lunar_longitude REAL,
            marker_color TEXT,
            thumbnail_image TEXT,
            hero_image TEXT,
            target_url TEXT,
            wikipedia_url TEXT,
            nasa_images_url TEXT,
            moon_region TEXT,
            mission_name TEXT,
            display_order INTEGER DEFAULT 0,
            active INTEGER DEFAULT 1,
            created_date TEXT,
            modified_date TEXT
        )
        """
    )

    conn.commit()

    print(f"Database Created : {DB_FILE}")

    return conn

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

        conn = create_database()

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