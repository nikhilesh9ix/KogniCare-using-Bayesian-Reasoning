#!/bin/bash
set -e

echo "Installing build dependencies..."
pip install --upgrade pip setuptools wheel

echo "Installing application dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"