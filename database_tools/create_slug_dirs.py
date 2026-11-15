
#!/usr/bin/env python3

from pathlib import Path
import sqlite3

DB_FILE = "..\\database\\catalog.db"

IMAGE_ROOT = Path(
    "..\\static\\images"
)

def main():

    print()
    print("=" * 60)
    print("Create Image Directories")
    print("=" * 60)

    IMAGE_ROOT.mkdir(
        parents=True,
        exist_ok=True
    )

    conn = sqlite3.connect(
        DB_FILE
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT slug
        FROM items
        WHERE active = 1
        ORDER BY slug
        """
    )

    rows = cursor.fetchall()

    created = 0
    existing = 0

    for row in rows:

        slug = row[0]

        folder = (
            IMAGE_ROOT /
            slug
        )

        if folder.exists():

            existing += 1

            print(
                f"EXISTS   : {folder}"
            )

        else:

            folder.mkdir(
                parents=True,
                exist_ok=True
            )

            created += 1

            print(
                f"CREATED  : {folder}"
            )

    conn.close()

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(
        f"Created : {created}"
    )

    print(
        f"Existing: {existing}"
    )

    print(
        f"Total   : {created + existing}"
    )

    print()

if __name__ == "__main__":
    main()