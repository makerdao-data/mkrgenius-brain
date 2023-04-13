import pandas as pd

from llama_index import GPTSimpleVectorIndex, GPTListIndex
from llama_index.indices.composability import ComposableGraph
from llama_index.indices.struct_store import GPTPandasIndex


index1 = GPTSimpleVectorIndex.load_from_disk('index.json')

df = pd.read_csv("./training-datasets/collaterals.csv")
index2 = GPTPandasIndex(df=df)

graph = ComposableGraph.from_indices(GPTListIndex, [index1, index2], index_summaries=["summary1", "summary2"])
response = graph.query("<query_str>", mode="recursive", query_configs=...)


print(response)







'''
from pathlib import Path
from llama_index import download_loader

MarkdownReader = download_loader("MarkdownReader")

loader = MarkdownReader()
documents = loader.load_data(file=Path('./README.md'))

from llama_index import download_loader, GPTSimpleVectorIndex, ServiceContext
from pathlib import Path

years = [2022, 2021, 2020, 2019]

UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True)


loader = UnstructuredReader()
doc_set = {}
all_docs = []
for year in years:
    year_docs = loader.load_data(file=Path(f'./data/UBER/UBER_{year}.html'), split_documents=False)
    # insert year metadata into each year
    for d in year_docs:
        d.extra_info = {"year": year}
    doc_set[year] = year_docs
    all_docs.extend(year_docs)

# initialize simple vector indices + global vector index
# NOTE: don't run this cell if the indices are already loaded! 
index_set = {}
service_context = ServiceContext.from_defaults(chunk_size_limit=512)
for year in years:
    cur_index = GPTSimpleVectorIndex.from_documents(doc_set[year], service_context=service_context)
    index_set[year] = cur_index
    cur_index.save_to_disk(f'index_{year}.json')

'''