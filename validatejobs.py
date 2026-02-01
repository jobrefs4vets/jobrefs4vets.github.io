import os
import sys
import yaml
from datetime import datetime

REQUIRED_FIELDS = [
    "title",
    "description",
    "datePosted",
    "validThrough",
    "employmentType",
    "hiringOrganization",
    "jobLocation"
]

def fail(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)

jobs_dir = "_jobs"

for filename in os.listdir(jobs_dir):
    if not filename.endswith(".md"):
        continue

    path = os.path.join(jobs_dir, filename)
    print(f"Checking {path}...")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        fail(f"{filename}: Missing YAML front matter")

    try:
        front_matter = content.split("---")[1]
        data = yaml.safe_load(front_matter)
    except Exception as e:
        fail(f"{filename}: Invalid YAML front matter: {e}")

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            fail(f"{filename}: Missing required field '{field}'")

    # Check validThrough date
    try:
        valid_through = datetime.strptime(data["validThrough"], "%Y-%m-%d")
    except ValueError:
        fail(f"{filename}: validThrough must be YYYY-MM-DD")

    if valid_through < datetime.now():
        fail(f"{filename}: Job posting is expired (validThrough < today)")

print("All job postings validated successfully.")