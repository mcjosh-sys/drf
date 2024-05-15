def collect_data(data: dict, method='create') -> int:
    id = None
    if method == 'update':
        id = input('ProductId: ')
        try:
            id = int(id)
        except:
            print('Id must be an integer!')
            collect_data(data, method)
    try:
        print(data)
        title = input("Title: ")
        if method == 'create':
            if not title:
                raise Exception("Title is required")
        if title:
            data['title'] = title
            print(data)
        content = input("Content: ")
        if content:
            data['content'] = content
            print(data)
        price = input("Price: ")
        if price:
            data['price'] = float(price)
            print(data)
        
        
    except Exception as e:
        print(e)
        collect_data(data)
        
    return id