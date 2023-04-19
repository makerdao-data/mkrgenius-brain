import pandas as pd
from dotenv import load_dotenv

from llama_index import GPTSimpleVectorIndex, GPTListIndex
from llama_index.indices.composability import ComposableGraph
from llama_index.indices.struct_store import GPTPandasIndex

load_dotenv()

index1 = GPTSimpleVectorIndex.load_from_disk('index.json')
df = pd.read_csv("./datasets/collaterals.csv")
index2 = GPTPandasIndex(df=df)

graph = ComposableGraph.from_indices(GPTListIndex, [index1, index2], index_summaries=["MakerDAO documentation", "DAI collaterals summary"])
response = graph.query("how much ETH is locked")

print(response)
