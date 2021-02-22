"""
    Some people have been killed!
    You have managed to narrow the suspects down to 
        just a few. Luckily, you know every person who 
        those suspects have seen on the day of the murders.

    Task.
    Given a dictionary with all the names of the suspects
        and everyone that they have seen on that day 
        which may look like this:

    {'James': ['Jacob', 'Bill', 'Lucas'],
    'Johnny': ['David', 'Kyle', 'Lucas'],
    'Peter': ['Lucy', 'Kyle']}
    and also a list of the names of the dead people:

    ['Lucas', 'Bill']
    return the name of the one killer, in our case 
        'James' because he is the only person that saw 
        both 'Lucas' and 'Bill'
"""

# inital quick answer
# BAD for efficiency becuase you want to avoid double for loops
def killer_INITIAL(suspect_info, dead):
    met_dead = True
    for key, value in suspect_info.items():
        met_dead = True
        for i in dead:
            if i not in value:
                met_dead = False
        if met_dead:
            return key

# Smart solution, utilize sets so you can easily compare
# the lists contents without using 2nd for loop
def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name