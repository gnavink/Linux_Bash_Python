import json

#'description': 'Router link' initially in interface.json
with open('interface.json') as fh:
    data = fh.read()
    data_dict = json.loads(data)
    print(data_dict)


with open('interface.json','w') as fh:
    data_dict['interface']['description'] = 'Backup link'
    json.dump(data_dict, fh, indent = 4)


