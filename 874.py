def robotSim(commands, obstacles):
    """
    :type commands: List[int]
    :type obstacles: List[List[int]]
    :rtype: int
    """
    res = 0

    x,y=0,0
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    d = 0
    obstacles = {tuple(o) for o in obstacles}

    for c in commands:
        if c == -1:
            d=(d+1)%4
        elif c == -2:
            d=(d-1)%4
        else:
            dx,dy = dir[d]
            for _ in range(c):
                if (x+dx,y+dy) in obstacles:
                    break
                x,y=x+dx,y+dy
        res = max(res,x**2+y**2)


    return res

r = robotSim(commands = [4,-1,3], obstacles = [])
print(r)