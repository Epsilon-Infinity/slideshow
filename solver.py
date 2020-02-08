import seth



def solver(word_photos):
    sol = []
    all_slides = set([])

    for word, slides in word_photos.items():
        if len(slides) > 1:
            all_slides.update(tuple(slides))

    all_slides = list(all_slides)
    sol.append(all_slides[0])
    others = all_slides.copy()
    others.remove(all_slides[0])
    for i in range(len(all_slides)):
        max_j = None
        for other in others:
            score = seth.metric(sol[i], other)
            if not max_j or max_j[1] < score:
                max_j = (other, score)
        if max_j:
            sol.append(max_j[0])
        others.remove(max_j[0])
    return sol