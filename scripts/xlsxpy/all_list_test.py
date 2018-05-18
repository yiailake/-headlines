from xml.etree.ElementTree import parse

def get_all_list():
    all_list = []
    for i in range(0, 12):
        rulist = []
        rupath = 'C:/Users/Administrator/Desktop/xlsxpy/xml/' + str(i) +'.xml'
        #print(rupath)
        document = parse(rupath)
        tree = document.getroot()
        for string in tree.findall('string'):
            name = string.get('name')
            rulist.append(name)
        all_list = all_list + rulist
    return list(set(all_list))

all_list = get_all_list()
all_list = sorted(all_list)
print(len(all_list))

small_list = ['set_advice_app', 'set_advice_handle', 'set_advice_info', 'set_advice_info_hint', 'set_advice_info_txt']

new_list = []
for i in all_list:
    new_list.append(None)
    for j in small_list:
        if i == j:
            new_list[all_list.index(i)]=j
print(new_list)
