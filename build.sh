#!/bin/bash
python -m pip install . --target build
find build -path '*/__pycache__*' -delete
mv build/terestun/__main__.py build/
python -m zipapp -c -p '/usr/bin/env python3' build -o terestun.pyz
