"""Wrapper entry point for fabric-retrieve.py console script."""
import runpy
from pathlib import Path


def main():
    runpy.run_path(
        str(Path(__file__).with_name("fabric-retrieve.py")),
        run_name="__main__",
    )
