#!/usr/bin/env python3
# License: MIT License
# Copyright (C) 2023  Daniel Haden
from pathlib import Path
from setuptools import setup

AUTHOR_NAME = "Daniel Haden"

ROOT = Path(__file__).resolve().parent


def get_version():
    v = {}
    