from seth import *


class Image:
    def __init__(self, tags: set, id: int):
        self.tags = tags
        self.id = id


def get_vertical(images):
    pairs = []
    while len(images) > 1:
        i = 0
        possible_pairs = []
        while i < len(images):
            j = i+1
            while j < len(images):
                possible_pairs.append((images[i], images[j], len(images[i].tags.union(images[j].tags))))
                j+=1
            max_pair = None
            max_value = -1
            for pair in possible_pairs:
                if pair[2] > max_value:
                    max_pair = (pair[0], pair[1])
                    max_value = pair[2]
            pairs.append(max_pair)
            images.remove(max_pair[0])
            images.remove(max_pair[1])
            i+=1
    return pairs


def get_optimal_transitions(slides : list):
    s1 = slides[0]
    slides.remove(slides[0])
    value = 0
    transitions = [s1]
    while len(slides)>0:
        max_trans = None
        max_metric = 0
        for slide in slides:
            value = metric(s1,slide)
            if value>max_trans:
                max_trans=slide
                max_metric=value
        transitions.append(slide)
        slides.remove(slide)
    return transitions



# image1 = Image(tags={"sun", "sky", "beach", "grass"}, id=0)
# image2 = Image(tags={"sun", "grass", "ball"}, id=1)
# image3 = Image(tags={"ball", "sand", "sky"}, id=2)
# res = get_vertical([image1,image2, image3])
# print(len(res))
# print(res)
# print([(pair[0].id, pair[1].id) for pair in res])