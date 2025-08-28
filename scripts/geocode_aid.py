import csv
import os
import sys
import time
import urllib.parse
from typing import Optional, Tuple

import requests
from dotenv import load_dotenv


MAPBOX_GEOCODE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"


def geocode_address(address: str, access_token: str, session: requests.Session, max_attempts: int = 5) -> Optional[Tuple[float, float]]:
    """Return (lat, lon) for the first result of the given address via Mapbox, or None if not found.

    Retries with exponential backoff for transient errors (429/5xx).
    """
    if not address:
        return None

    # Encode the address into the path component per Mapbox API
    encoded_address = urllib.parse.quote(address)
    url = f"{MAPBOX_GEOCODE_URL}/{encoded_address}.json"
    params = {
        "access_token": access_token,
        "limit": 1,
        "autocomplete": "false",
        "country": "US",
    }

    backoff_seconds = 1.0
    attempt = 0

    while attempt < max_attempts:
        attempt += 1
        try:
            resp = session.get(url, params=params, timeout=15)
        except requests.RequestException as exc:
            if attempt >= max_attempts:
                print(f"Request error on address '{address}': {exc}")
                return None
            time.sleep(backoff_seconds)
            backoff_seconds *= 2
            continue

        # Retry on 429 or 5xx
        if resp.status_code == 429 or 500 <= resp.status_code < 600:
            if attempt >= max_attempts:
                print(f"HTTP {resp.status_code} for address '{address}' after {attempt} attempts")
                return None
            time.sleep(backoff_seconds)
            backoff_seconds *= 2
            continue

        if resp.status_code != 200:
            try:
                data = resp.json()
                message = data.get("message", "")
            except Exception:
                message = ""
            print(f"Geocode failed for '{address}' - HTTP {resp.status_code}: {message}")
            return None

        try:
            data = resp.json()
        except ValueError:
            if attempt >= max_attempts:
                print(f"Invalid JSON response for address '{address}'")
                return None
            time.sleep(backoff_seconds)
            backoff_seconds *= 2
            continue

        # Mapbox returns features[]
        features = data.get("features", [])
        if not features:
            return None
        feature0 = features[0]
        center = feature0.get("center") or []
        if not isinstance(center, list) or len(center) != 2:
            return None
        lon, lat = center[0], center[1]
        try:
            return float(lat), float(lon)
        except (TypeError, ValueError):
            return None


def main() -> int:
    # Load .env if present
    load_dotenv()
    access_token = os.environ.get("MAPBOX_ACCESS_TOKEN")
    if not access_token:
        print("Missing MAPBOX_ACCESS_TOKEN environment variable. Create a .env file with MAPBOX_ACCESS_TOKEN=... or export it in your shell.")
        return 1

    root = os.path.abspath(os.path.dirname(__file__))
    in_path = os.path.join(root, "aid.csv")
    out_path = os.path.join(root, "aid_geocoded.csv")

    if not os.path.exists(in_path):
        print(f"Input CSV not found: {in_path}")
        return 1

    with open(in_path, newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        fieldnames = reader.fieldnames or []
        if not fieldnames:
            print("CSV has no header row.")
            return 1

        # Ensure required columns exist
        required = {"Approx. Address", "Lat", "Lon"}
        missing = [c for c in required if c not in fieldnames]
        if missing:
            print(f"CSV is missing required columns: {', '.join(missing)}")
            return 1

        rows = list(reader)

    session = requests.Session()

    total = len(rows)
    attempted = 0
    updated = 0

    for idx, row in enumerate(rows, start=1):
        lat_val = (row.get("Lat") or "").strip()
        lon_val = (row.get("Lon") or "").strip()
        address = (row.get("Approx. Address") or "").strip()

        # Skip if already has coordinates
        if lat_val and lon_val:
            continue

        if not address:
            continue

        attempted += 1
        coords = geocode_address(address, access_token, session)
        if coords is not None:
            lat, lon = coords
            row["Lat"] = f"{lat:.7f}"
            row["Lon"] = f"{lon:.7f}"
            updated += 1
        # Be kind to the API
        time.sleep(0.1)

    with open(out_path, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(
        f"Processed {total} rows. Attempted geocoding {attempted}, updated {updated}.\n"
        f"Wrote: {out_path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())


