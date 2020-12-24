import os
import json
from os import listdir, getcwd
from os.path import join

# 1: No entry
# 2: No parking / waiting
# 3: No turning
# 4: Max Speed
# 5: Other prohibition signs
# 6: Warning
# 7: Mandatory

classes = ["No entry","No parking/waiting","No turning","Max Speed","Other prohibition signs","Warning","Mandatory"]

#box form[x,y,w,h]
def convert(size,box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = box[0]*dw
    y = box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    return (x,y,w,h)

def convert_annotation():
    with open('annos.json','r',encoding='utf-8') as f:
        data = json.load(f)
    for item in data['images']:
        # print(item)
        image_id = item['id']
        #file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: (item1['image_id'] == image_id),data['annotations'])
        outfile = open('./lala/%s.txt'%(image_id), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = list(filter(lambda item3: (item3['id'] == category_id),data['categories']))
            #print(value1)
            name = value1[0]['name']
            #print(name)
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()
    
			
if __name__ == '__main__':
    convert_annotation()
    
