from .PCBWay import PCBWay

manufacturers = {
    PCBWay.NAME.lower(): PCBWay,
}

manufacturers_list = list(manufacturers.keys())

if len(set([x for x in manufacturers_list if manufacturers_list.count(x) > 1])) > 0:
    raise Exception("Invalid manufacturer name detected, check that all names are unique")