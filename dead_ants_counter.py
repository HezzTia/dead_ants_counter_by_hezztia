#emily cabrera - 1106145
# this program counts dead ants in a line of text

def count_dead_ants():
# this function asks the user for a line of text and counts the dead ants in it
    line = input("Enter a line of text: ")

    dead_ants = _count_dead_ants(line)
    return dead_ants

# internal function to avoid duplication of code
def _count_dead_ants(line):
    dead_ants = 0
    ant_count = line.count("ant")

# counts the number of dead ants
    if ant_count > 0:
        bodies_count = line.count("nt") + line.count("tn")
        dead_ants = min(ant_count, bodies_count // 2)

    return dead_ants

# prints the number of dead ants
dead_ants = count_dead_ants()
print(f"Number of dead ants: {dead_ants}")