import pathlib
import re

print("=" * 60)
print("CinderX LOAD_LOCAL Research")
print("=" * 60)

root = pathlib.Path(".")

targets = []

for path in root.rglob("*.py"):
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        continue

    if "LOAD_LOCAL" in text:
        targets.append(path)

print(f"\n[+] Found {len(targets)} files referencing LOAD_LOCAL\n")

for p in sorted(targets):
    print(p)

print("\n[+] Searching test cases")

for p in targets:
    if "test_" in p.name:
        print(f"\n==== {p} ====")

        try:
            lines = p.read_text(errors="ignore").splitlines()
        except Exception:
            continue

        for idx, line in enumerate(lines):
            if "LOAD_LOCAL" in line:
                start = max(0, idx - 5)
                end = min(len(lines), idx + 10)

                for l in lines[start:end]:
                    print(l)

                print("-" * 50)

print("\n[+] Complete")
