
def slides_to_dict(slides):

    dicts = {}
    for slide in slides:

        for tag in slide.tags:
            if tag in dicts:
                dicts[tag].append(slide)
            else:
                dicts[tag] = [slide]
    return dicts

def metric(s1, s2):
    s1s2 = len(s1.tags.intersection(s2.tags))
    s1l =  max(0,len(s1.tags) - s1s2)
    s2l = max(0, len(s2.tags) - s1s2)

    return min(s1l, s2l, s1s2)


if __name__ == '__main__':

    class Slide():

        def __init__(self, photo_ids, tags):
            self.photos = photo_ids
            self.tags = tags
        
        def __str__(self):
            return self.photos
    
    s1 = Slide([1,2], {'a','d'})
    s2 = Slide([3], {'c', 'd'})
    print(slides_to_dict([s1, s2]))
    print(metric(s1,s2))