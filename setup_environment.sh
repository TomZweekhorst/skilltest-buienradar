#!/usr/bin/env bash
set -e

# Step 1 — ensure Python 3.10 is installed  
if ! command -v python3.10 &>/dev/null; then
  sudo apt update
  sudo apt install -y software-properties-common
  sudo add-apt-repository -y ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install -y python3.10 python3.10-venv python3.10-dev
fi

# Step 2: Create virtual environment
python3.10 -m venv venv

# Activate venv
source venv/bin/activate

# Step 3: install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete! Activate your venv with:"
echo "source venv/bin/activate"
echo "Then run: python src/etl.py --mode simulate"
