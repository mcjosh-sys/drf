from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(name='cfe_Product'):
    client = get_client()
    index = client.init_index(name)
    return index

def perform_search(query, **kwargs):
    print(kwargs)
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags):
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if (v or v==False)]
    if len(index_filters):
        params['facetFilters'] = index_filters
    print(params)
    results = index.search(query, params)
    return results