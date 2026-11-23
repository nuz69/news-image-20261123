import hashlib
import os
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    src = script_dir / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry.png not found at {src}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        dest_dir = Path(out_dir)
    else:
        dest_dir = Path("/output")

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    
    src_bytes = src.read_bytes()
    dest.write_bytes(src_bytes)

    src_hash = hashlib.sha256(src_bytes).hexdigest()
    dest_hash = hashlib.sha256(dest.read_bytes()).hexdigest()

    if src_hash != dest_hash:
        raise RuntimeError(f"Copy verification failed: source SHA-256 ({src_hash}) does not match destination SHA-256 ({dest_hash})")

if __name__ == "__main__":
    main()
