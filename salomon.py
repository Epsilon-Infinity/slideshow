import os

class Slide():
    def __init__(self, id, orient, tags):
        self.tags = set(tags)
        self.orient = orient
        self.id = id
    



def read_file(file_path):
    file = open(file_path)
    lines = file.readlines()
    collection = list(map(int, lines[0].strip().split()))
    all_file = []
    first = True
    save_i = None
    for i in range(1,collection[0]+1):
        line = lines[i].strip().split()
        or_ = line[0]
        tag = line[2:]

        if or_ == 'H':
            all_file.append(Slide(list([i]), or_, tag))
        else :
            if first:
                all_file.append(Slide(list([i]), or_, tag))
                save_i = i-1
                first = False
            else: 
                all_file[save_i].tags.update(tag)
                all_file[save_i].id.append(i)

    return all_file
                



print(read_file('/home/aims/Documents/Epsilon-Infinity/slideshow/data/a_example.txt'))
