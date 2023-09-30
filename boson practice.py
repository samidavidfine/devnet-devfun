print('Hello World!')
configuration = [
    {
        "hostname": "Switch1",
        "version": "15.2",
        "interfaces": ["Fa0/0", "Fa0/1", "Fa0/2"]
    },{
        "hostname": "Switch2",
        "version": "15.2",
        "interfaces": ["Fa0/0", "Fa0/1", "Gi0/0"]
    },{
        "hostname": "Switch3",
        "version": "15.2",
        "interfaces": ["Gi0/0", "Fa0/1", "Fa0/2"]
    }
]
for switch in configuration:
    print(switch['hostname'])
    i = 0
    while i < len(switch['interfaces']):
        print(switch["interfaces"][i])
        i = i + 1
    