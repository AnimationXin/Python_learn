import os
import sys

# os.path.dirname路径名
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from config import settings
from core import main

limit_money = 15000

main.login()