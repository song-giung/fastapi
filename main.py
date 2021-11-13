from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: Optional[str] = Query(None,
                                              title="Query string",
                                              description='Query string for the items',
                                              min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})
    return results
