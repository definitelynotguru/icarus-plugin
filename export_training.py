"""Wrapper entry point for export-training.py console script."""
import runpy
from pathlib import Path


def main():
    runpy.run_path(
        str(Path(__file__).with_name("export-training.py")),
        run_name="__main__",
    )
