options: dict = {
    "cloudFiles.format": "json",
    "wholetext": "true",
    "cloudFiles.schemaLocation": "schema_location"
}

for (k, v) in options.items():
    print(f"k -> {k}, v-> {v}")