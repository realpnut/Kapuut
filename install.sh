set -e
echo "[+] Creating virtual environment..."
python3 -m venv venv
echo "[+] Activating virtual environment..."
source venv/bin/activate
echo "[+] Upgrading pip..."
pip install --upgrade pip
echo "[+] Installing dependencies..."
pip install -r requirements.txt
echo "[+] Installation complete!"
echo "[+] Activate the environment with: source venv/bin/activate"
