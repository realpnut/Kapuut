set -e

echo "[+] Creating virtual environment..."
python3 -m venv venv

echo "[+] Activating virtual environment..."
source venv/bin/activate

echo "[+] Upgrading pip..."
pip install --upgrade pip

echo "[+] Installing dependencies..."
pip install -e .

echo "[+] Installation complete!"
echo "--------------------------------------------------"
echo "[+] To run the tool using Python, execute:"
echo "    source venv/bin/activate && python3 src/kapuut/main.py"
echo "--------------------------------------------------"
