import yaml

with open('items.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.SafeLoader)
    print(data)
