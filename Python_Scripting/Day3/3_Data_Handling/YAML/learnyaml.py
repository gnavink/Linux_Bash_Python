import yaml

with open('interface.yaml') as fh:
    data = fh.read()

data_dict = yaml.load(data, Loader = yaml.FullLoader)
print(data_dict)

data_dict['interface']['ipv4']['address'][0]['ip'] = '192.168.0.2'
print(data_dict)

with open('interface.yaml','w') as fh:
    fh.write(yaml.dump(data_dict, default_flow_style = False))