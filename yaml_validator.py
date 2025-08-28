import yaml, sys
from pathlib import Path

req_keys = {"id","title","source","status","date_start"}
case = Path("cases/kc7-c01-scandal-in-valdoria/CaseMetadata.yaml")
data = yaml.safe_load(case.read_text(encoding="utf-8"))
missing = req_keys - data.keys()
print("Missing:", missing) if missing else print("CaseMetadata looks good.")
