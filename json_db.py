from pydantic import BaseModel
import json

from product import Product

class JsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data
    
    def insert(self, product: Product):
        data = self.read()
        if 'products' not in data:
            data['products'] = []
        data['products'].append(product.model_dump())  # Append the product model to the list
        with open(self.path, 'w') as f:
            f.write(json.dumps(data))
