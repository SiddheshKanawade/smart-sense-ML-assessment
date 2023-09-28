import os
from dotenv import load_dotenv

load_dotenv()

DATASET_PATH = os.getenv("DATASET_PATH")
TEST_DATA_PATH=os.getenv("TEST_DATA_PATH")
