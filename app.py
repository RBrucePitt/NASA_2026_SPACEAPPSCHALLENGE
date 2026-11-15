from flask import Flask
from flask import render_template

import sqlite3

app = Flask(__name__)

DATABASE = "database/catalog.db"


def get_items():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM items
        WHERE active=1
        ORDER BY display_order
    """)

    items = cur.fetchall()

    conn.close()

    return items


@app.route("/")
def home():

    items = get_items()

    return render_template(
        "index.html",
        items=items
    )

@app.route("/item/<slug>")
def item_detail(slug):

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    # Current item

    item = conn.execute(
        """
        SELECT *
        FROM items
        WHERE slug = ?
        """,
        (slug,)
    ).fetchone()

    # All moon objects for plotting
    moon_objects = conn.execute(
        """
        SELECT
            id,
            title,
            slug,
            lunar_latitude,
            lunar_longitude,
            marker_color,
            mission_name,
            moon_region
        FROM items
        WHERE active = 1
        AND lunar_latitude IS NOT NULL
        AND lunar_longitude IS NOT NULL
        ORDER BY title
        """
    ).fetchall()

    conn.close()

    return render_template(
        "item.html",
        item=item,
        moon_objects=[
            dict(row)
            for row in moon_objects
        ]
    )

@app.route("/moon_features")
def moon_features():

    return jsonify([
        {
            "name": item.title,
            "lat": item.lunar_latitude,
            "lon": item.lunar_longitude,
            "type": "equipment"
        }
        for item in lunar_items
    ])


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
