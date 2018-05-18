from xml.etree.ElementTree import parse
import xlsxwriter

workbook = xlsxwriter.Workbook('C:/Users/Administrator/Desktop/xlsxpy/output.xlsx')
worksheet = workbook.add_worksheet()

begin = '<resources>\n'
end = '</resources>'

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

def parse_doc(doc):
    root = doc.getroot()
    element = {}
    for string in root.findall('string'):
        name = string.get('name')
        element[name] = string.text
    return element

li = [7, 2, 3, 9, 10, 4, 8, 5, 1, 0, 11, 6]

language = {0:'UK', 1:'Turkish', 2:'Russian', 3:'意大利', 4:'荷兰语', 5:'匈牙利语', 6:'法语', 7:'芬兰语', 8:'西班牙语', 9:'希腊语', 10:'捷克语', 11:'德语'}

for i in li:
    new_list = []
    #print(language[i])
    #new_list.append(language[i])
    #new_list.append(begin)
    xmlpath = 'C:/Users/Administrator/Desktop/xlsxpy/xml/' + str(i) + '.xml'
    doc = parse(xmlpath)
    element = parse_doc(doc)
    sorted_element = sorted(element.items())

    for a in all_list:
        new_list.append(None)
        for k, v in sorted_element:
            if a == k:
                if v == None:
                    dystr = '<string name="' + k + '"></string>\n'
                else:
                    dystr = '<string name="' + k + '">' + v + '</string>\n'
                new_list[all_list.index(a)] = dystr

    #new_list.append(end)
    j = li.index(i)
    #print(li.index(i))
    worksheet.write_column(0, j, new_list)
    #print(lists)
    #path = "C:/Users/Administrator/Desktop/test_new/" + str(i) + ".txt"
    #f = open(path, "w", encoding='UTF-8')
    #f.writelines(lists)
    #f.close()

#nums = {}
#print(str(i) + ' ' + str(len(lists)))
#sorted_nums = sorted(nums.items(),key = lambda x:x[1],reverse = True)
#keys = []
#for num in sorted_nums:
#    keys.append(num[0])
#print(keys)
workbook.close()
    




