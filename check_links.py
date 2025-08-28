import re, os
from pathlib import Path

root = Path(".")
md_files = list(root.rglob("*.md"))

link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
broken = []

for f in md_files:
    text = f.read_text(encoding="utf-8", errors="ignore")
    for m in link_re.finditer(text):
        target = m.group(2)
        # ignore anchors and http(s)
        if target.startswith("#") or "://" in target:
            continue
        target_path = (f.parent / target).resolve()
        if not target_path.exists():
            broken.append((str(f), target))
print("OK" if not broken else "Broken links:\n" + "\n".join(f"{a} -> {b}" for a,b in broken))
