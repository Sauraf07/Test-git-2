def search(items, keyword):    
    return [        item for item in items        if keyword.lower() in item.lower()    ]
