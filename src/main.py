import requests
from bs4 import BeautifulSoup
import time
import json
import os
import random

"https://www.rebel.pl/pokemon/pokemon-tcg-scarlet-violet-surging-sparks-booster-display-36-2024721.html"
URL = "https://twojekarty.pl/pokmon-tcg-phantasmal-flames-elite-trainer-box-p-1857.html"
PRICE_SELECTOR = "[itemprop='price']"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1443642856664469526/E4akg33wgLqr5RAynAwf5JLkdSliXt4IO60Lh3CB2NMpmYakKGApfMcsHWkuqr4jvb4v"
MIN_INTERVAL = 15
MAX_INTERVAL = 150
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "last_price.json")
INITIAL_PRICE = "00.0"

def init_last_price():
    print("Init last price...")
    data = {"price": INITIAL_PRICE}
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def get_current_price():
    headers = {
        "User-Agent": "projekt juugcatm2003@gmail.com"
    }

    resp = requests.get(URL, headers=headers, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    el = soup.select_one(PRICE_SELECTOR)
    if not el:
        raise RuntimeError(
            f"Nie znaleziono elementu z ceną (selector: {PRICE_SELECTOR})"
        )
    text = el.get_text(strip=True)
    digits = "".join(ch for ch in text if ch.isdigit() or ch in ",.")
    digits = digits.replace(",", ".")
    return float(digits)

def save_last_price(price):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({"price": price}, f, ensure_ascii=False)
   
def load_last_price():
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)          
    return float(data.get("price"))
        

def send_discord_message(message: str):
    data = {"content": message}
    r = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    r.raise_for_status()


def main():
    current = get_current_price()
    print(f"Aktualna cena na stronie: {current}")
    last_price = load_last_price()
    if current != last_price:
        msg = (
            f"UWAGA: cena się zmieniła!\n"
            f"Było: {last_price}\n"
            f"Jest: {current}\n"
            f"Produkt: {URL}"
        )
        print(msg)
        send_discord_message(msg)
        save_last_price(current)
    else:
        print(f"Cena bez zmian: {current}")

def main_loop():
    while True:
        try:
            main()
        except Exception as e:
            print(f"Błąd: {e}")
        sleep_time = random.randint(MIN_INTERVAL, MAX_INTERVAL)
        print(f"Śpię {sleep_time} sekund")
        time.sleep(sleep_time)


if __name__ == "__main__":
    init_last_price()
    main_loop()
