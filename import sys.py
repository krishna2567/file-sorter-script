import sys
from pathlib import Path
import shutil

def sort_files(root: Path) -> None:
    """Move each file in root (non-recursively) into a sub-folder
    named after its lowercase extension ('.pdf' -> 'pdf')."""
    moved = 0
    for item in root.iterdir():
        if item.is_file():
            ext = item.suffix.lower().lstrip(".") or "no_ext"
            dest_dir = root / ext
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), dest_dir / item.name)
            moved += 1
    print(f"Sorted {moved} files inside “{root}”. ✅")

if __name__ == "_main_":
    target_dir = Path(sys.argv[1] if len(sys.argv) > 1 else ".").expanduser().resolve()
    if not target_dir.is_dir():
        sys.exit(f"❌  Directory not found: {target_dir}")
    sort_files(target_dir)