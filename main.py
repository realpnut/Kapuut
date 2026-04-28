from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

filename = "uses.txt"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("1")
with open(filename, "r") as f:
    value = f.read().strip()
if value == "1":
    print(f"{RED} THIS TOOL IS MADE FOR LEGAL AND ETHICAL PURPOSES ONLY. PROCEED AT YOUR OWN RISK.{RESET}")
    input("Press enter to continue.")
    new_value = str(int(value) + 1)
    with open(filename, "w") as f:
        f.write(new_value)

print("""
██ ▄█▀  ▄▄▄  ▄▄▄▄  ▄▄ ▄▄ ▄▄ ▄▄ ▄▄▄▄▄▄ 
████   ██▀██ ██▄█▀ ██ ██ ██ ██   ██   
██ ▀█▄ ██▀██ ██    ▀███▀ ▀███▀   ██   
                     The best Kahoot nuker ever!
                     
Press CTRL+C to close.
""")

def join_kahoot(code, base_name, number):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    nickname = f"{base_name}_{number}" 

    try:
        driver.get("https://kahoot.it/")
        wait.until(EC.visibility_of_element_located((By.NAME, "gameId"))).send_keys(code)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button__Button-sc-vzgdbz-0"))).click()
        wait.until(EC.visibility_of_element_located((By.NAME, "nickname"))).send_keys(nickname) 
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button__Button-sc-vzgdbz-0"))).click()

        print(f"{GREEN}[+] Joined: {nickname}{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error for {nickname}: {e}{RESET}")
    finally:
        time.sleep(2)
        driver.quit()

code = input("Join code: ")
name = input("Name: ")
multi = input("Multithreading (Y/N)?: ").strip().upper()

if multi == "Y":
    threads = int(input("How many threads?: "))
    total = int(input("How many bots?: "))

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for i in range(1, total + 1):
            executor.submit(join_kahoot, code, name, i)
else:
    n = 1
    while True:
        join_kahoot(code, name, n)
        n += 1
