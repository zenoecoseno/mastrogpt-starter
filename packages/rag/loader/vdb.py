import os, requests as req
from pymilvus import MilvusClient, DataType

MODEL="mxbai-embed-large:latest"
DIMENSION_EMBEDDING=1024
DIMENSION_TEXT=4096

LIMIT=30

class VectorDB:

  def __init__(self, args, collection):
      uri = f"http://{args.get("MILVUS_HOST", os.getenv("MILVUS_HOST"))}"
      token = args.get("MILVUS_TOKEN", os.getenv("MILVUS_TOKEN"))    
      db_name = args.get("MILVUS_DB_NAME", os.getenv("MILVUS_DB_NAME"))
      self.client =  MilvusClient(uri=uri, token=token, db_name=db_name)

      host = args.get("OLLAMA_HOST", os.getenv("OLLAMA_HOST"))
      auth = args.get("OLLAMA_TOKEN", os.getenv("AUTH"))
      self.url = f"https://{auth}@{host}/api/embeddings"

      self.setup(collection)

  def destroy(self, collection):
    self.client.drop_collection(collection)
    return f"Dropped {collection}\n"+self.setup("default")

  def setup(self, collection):
    self.collection = collection    
    ls = self.client.list_collections()
    print('vdb.py list'+str(ls))
    if not collection in ls:
      schema = self.client.create_schema()
      schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True, auto_id=True)
      schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=DIMENSION_TEXT)
      schema.add_field(field_name="embeddings", datatype=DataType.FLOAT_VECTOR, dim=DIMENSION_EMBEDDING)
      schema.add_field(field_name="img_description" ,datatype=DataType.VARCHAR, max_length=DIMENSION_TEXT)
      
      index_params = self.client.prepare_index_params()
      index_params.add_index("embeddings", index_type="AUTOINDEX", metric_type="IP")
      print("collection_name=", self.collection)
      self.client.create_collection(collection_name=collection, schema=schema, index_params=index_params)
      ls.append(collection)

    self.client.load_collection(collection_name=self.collection)

    count = self.count()
    return f"Collections: {" ".join(ls)}\n Current: {self.collection} [{count}]"
  
  def embed(self, text):
    msg = { "model": MODEL, "prompt": text, "stream": False }
    res = req.post(self.url, json=msg).json()
    return res.get('embedding', [])

  def insert(self, text, img_description=None):
    vec = self.embed(text)
    
    # Prepare the data to insert
    data_to_insert = {"text": text, "embeddings": vec}
    
    # Include the img field only if it's provided
    if img_description is not None:
        data_to_insert['img_description'] = img_description
    
    response = self.client.insert(self.collection, data_to_insert)
    print("Insert Response:", response)  # Log the response for debugging
    return response
  
  def count(self):
    MAX="1000"
    res = self.client.query(collection_name=self.collection, output_fields=["id"], limit=int(MAX))
    count = str(len(res))
    if count == MAX:
      count += " or more..."
    return count

  def vector_search(self, inp, limit=LIMIT):
    vec = self.embed(inp)
    cur = self.client.search(
      collection_name=self.collection,
      search_params={"metric_type": "IP"},
      anns_field="embeddings", data=[vec],
      output_fields=["text"],
      limit=limit
    )
    res = []
    if len(cur[0]) > 0:
      for item in cur[0]:
        dist = item.get('distance', 0)
        text = item.get("entity", {}).get("text", "")
        res.append((dist, text))
    return res

  def remove_by_substring(self, inp):
    cur = self.client.query_iterator(collection_name=self.collection, 
              batchSize=2, output_fields=["text"])
    res = cur.next()
    ids = []
    while len(res) > 0:
      for ent in res:
        if ent.get('text', "").find(inp) != -1:
          ids.append(ent.get('id'))
      res = cur.next()
    if len(ids) >0:
      res = self.client.delete(collection_name=self.collection, ids=ids)
      return res['delete_count']
    return 0
