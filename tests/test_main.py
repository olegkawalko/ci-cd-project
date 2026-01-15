from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from src.main import init_last_price
import requests
from bs4 import BeautifulSoup
import time
import json
import os
import random

def test_init_last_price():
    init_last_price()    
