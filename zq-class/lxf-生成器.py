def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    print('ALL DONE')
    yield (5)

o = odd()
next(o)
next(o)
next(o)