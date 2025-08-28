import csv
import json
import os
import sys
from typing import Any, Dict, List, Optional


def parse_float(value: str) -> Optional[float]:
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def csv_to_geojson(input_csv: str, output_geojson: str) -> None:
    with open(input_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows: List[Dict[str, Any]] = list(reader)

    features: List[Dict[str, Any]] = []
    for row in rows:
        # Preserve all attributes as-is in properties
        properties: Dict[str, Any] = dict(row)

        lat = parse_float(row.get("Lat"))
        lon = parse_float(row.get("Lon"))

        geometry: Optional[Dict[str, Any]]
        if lat is not None and lon is not None:
            geometry = {
                "type": "Point",
                "coordinates": [lon, lat],
            }
        else:
            geometry = None

        features.append({
            "type": "Feature",
            "properties": properties,
            "geometry": geometry,
        })

    collection = {
        "type": "FeatureCollection",
        "features": features,
    }

    with open(output_geojson, "w", encoding="utf-8") as f_out:
        json.dump(collection, f_out, ensure_ascii=False, indent=2)

    print(f"Wrote GeoJSON with {len(features)} features to: {output_geojson}")


def main(argv: List[str]) -> int:
    root = os.path.abspath(os.path.dirname(__file__))
    input_csv = os.path.join(root, "all-aid-mapped.csv")
    output_geojson = os.path.join(root, "all-aid-mapped.geojson")

    # Optional CLI override: csv_to_geojson.py <input> <output>
    if len(argv) >= 2:
        input_csv = argv[1]
    if len(argv) >= 3:
        output_geojson = argv[2]

    if not os.path.exists(input_csv):
        print(f"Input CSV not found: {input_csv}")
        return 1

    csv_to_geojson(input_csv, output_geojson)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))


