def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active == True:
        return power_pellet_active
    if power_pellet_active == False:
        return power_pellet_active

power_pellet_active = False and True
touching_ghost = True and True
print(eat_ghost(power_pellet_active, touching_ghost))
"""Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """ 