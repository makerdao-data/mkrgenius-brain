from llama_index.indices.struct_store import GPTPandasIndex
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
df = pd.read_csv("./datasets/collaterals.csv")

index = GPTPandasIndex(df=df)
response = index.query(
    "How much Dai has been minted from ETH collateral?",
    verbose=False
)

print(response)
print()