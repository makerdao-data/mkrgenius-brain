
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import SimpleDirectoryReader
from llama_index.indices.struct_store import GPTPandasIndex
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


df = pd.read_csv("./training-datasets/collaterals.csv")
index = GPTPandasIndex(df=df)
response = index.query(
    "How much Dai has been minted from ETH?",
    verbose=True
)
print(response.extra_info["pandas_instruction_str"])
