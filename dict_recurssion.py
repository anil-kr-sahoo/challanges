import json
input_str = {
    'user': {
        'name': {"op": 90, "mo": 88},
        'at': {"po": 80}
    },
    'contact': [1, {"some": "value", "most": "things"}]
}

# o/p -
# {
#   user.name.op:90,
#   user.name.mo:88,
#   user.at.po:80,
#   contact.0:1,
#   contact.1.some:'value',
#   contact.1.most:'things'
# }


final = dict()
k_name = ''


def doit(comp: dict):
    global final, k_name
    for k, v in comp.items():
        k_name += '.' + k if k_name else k
        if isinstance(v, dict):
            doit(v)
            k_name = k_name.split(k)[0][:-1]
        elif isinstance(v, list):
            for index, val in enumerate(v):
                k_name += '.' + str(index) if k_name else index
                if isinstance(val, dict):
                    doit(val)
                    k_name = k_name.split(str(index))[0][:-1]
                else:
                    final[k_name] = val
                    k_name = k_name.split(str(index))[0][:-1]
        else:
            final[k_name] = v
            k_name = k_name.split(k)[0][:-1]


doit(input_str)
print(json.dumps(final, indent=2))
