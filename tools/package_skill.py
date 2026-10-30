#!/usr/bin/env python3
"""Build a reproducible standalone .skill ZIP containing only runtime resources."""
from __future__ import annotations

import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
RUNTIME_DIRS = {"agents", "references", "scripts", "assets"}
SUFFIXES = {".md", ".py", ".json", ".yaml"}


def runtime_files(root: Path = ROOT) -> list[Path]:
    paths = [root / "SKILL.md"]
    for directory in sorted(RUNTIME_DIRS):
        base = root / directory
        if base.is_symlink():
            raise ValueError(f"Refusing symlink: {base}")
        for path in sorted(base.rglob("*")):
            relative = path.relative_to(root)
            if any(part.startswith(".") or part == "__pycache__" for part in relative.parts):
                continue
            if path.is_symlink():
                raise ValueError(f"Refusing symlink: {path}")
            if path.is_file() and path.suffix in SUFFIXES:
                paths.append(path)
    for path in paths:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing or unsafe runtime file: {path}")
    return sorted(paths)


def build(output: Path, root: Path = ROOT) -> Path:
    files = runtime_files(root)
    if output.is_symlink():
        raise ValueError(f"Refusing symlink output: {output}")
    resolved = output.resolve()
    if resolved in {path.resolve() for path in files}:
        raise ValueError("Output cannot overwrite a runtime file")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            name = "unslop/" + path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist" / "unslop.skill")
    args = parser.parse_args()
    try:
        output = build(args.output)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Built {output}: {len(runtime_files())} runtime files, {output.stat().st_size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
