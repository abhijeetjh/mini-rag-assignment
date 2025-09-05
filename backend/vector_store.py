import faiss
import numpy as np

class SimpleVectorDB:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []  # To map indices to texts

    def add(self, vectors, texts):
        self.index.add(np.array(vectors).astype('float32'))
        self.data.extend(texts)

    def search(self, vector, k=5):
        D, I = self.index.search(np.array([vector]).astype('float32'), k)
        return [self.data[i] for i in I]
