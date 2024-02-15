def count_dead_ants():

    line = input("Enter a line of text: ")

    dead_ants = _count_dead_ants(line)
    return dead_ants

def _count_dead_ants(line):
    dead_ants = 0
    ant_count = line.count("ant")

    if ant_count > 0:
        bodies_count = line.count("nt") + line.count("tn")
        dead_ants = min(ant_count, bodies_count // 2)

    return dead_ants

dead_ants = count_dead_ants()
print("Number of dead ants: {dead_ants}")