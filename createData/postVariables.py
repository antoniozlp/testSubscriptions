postVaribles = [
    # {'varialeCode':'Quality_OEE', 'rangeValues':{'min':0, 'max':100}, 'frequency':5},
    # {'varialeCode':'Performance_OEE', 'rangeValues':{'min':0, 'max':100}, 'frequency':5},
    # {'varialeCode':'Availability_OEE', 'rangeValues':{'min':0, 'max':100}, 'frequency':5},
    # {'varialeCode':'OEE', 'rangeValues':{'min':0, 'max':100}, 'frequency':10},
    # {'varialeCode':'Throughput_LittleLaw', 'rangeValues':{'min':0, 'max':100}, 'frequency':5},

    # {'varialeCode':'C.T._LittleLaw', 'rangeValues':{'min':0, 'max':100}, 'frequency':5, 'increment': 3},
    # {'varialeCode':'WIP_LittleLaw', 'rangeValues':{'min':0, 'max':100}, 'frequency':5, 'increment': 13},
    # {'varialeCode':'Good_Count_OEE', 'rangeValues':{'min':200, 'max':500}, 'frequency':3, 'increment': 5},
    # {'varialeCode':'Total_Count_OEE', 'rangeValues':{'min':1800, 'max':2300}, 'frequency':7, 'increment': 23},
    # {'varialeCode':'Stop_Time_OEE', 'rangeValues':{'min':0, 'max':120}, 'frequency':5, 'increment': 5},
    # {'varialeCode':'Planned_Production_Time_OEE', 'rangeValues':{'min':500, 'max':700}, 'frequency':5, 'increment': 5},
    # {'varialeCode':'Run_Time_OEE', 'rangeValues':{'min':0, 'max':400}, 'frequency':5, 'increment': 20}
    {'varialeCode':'RTF_random_int', 'rangeValues':{'min':0, 'max':100}, 'frequency':30, 'increment': 'randint'},
    {'varialeCode':'RTF_random_gauss', 'rangeValues':{'min':40, 'max':60, 'mean':50, 'std':25}, 'frequency':30, 'increment': 'randgauss'},
    {'varialeCode':'Test_RTF', 'rangeValues':{'min':1, 'max':100}, 'frequency':3, 'increment': 1}
]