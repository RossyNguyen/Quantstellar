def Tictoc():
    start_stack = []
    start_named = {}

    def tic(name=None):
        if name is None:
            start_stack.append(time())
        else:
            start_named[name] = time()

    def toc(name=None):
        if name is None:
            start = start_stack.pop()
        else:
            start = start_named.pop(name)
        elapsed = time() - start
        return elapsed
    return tic, toc