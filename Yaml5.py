import yaml

with open('items.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.SafeLoader)
    print(data)

    sorted = yaml.dump(data, sort_keys=True)
    print(sorted)
