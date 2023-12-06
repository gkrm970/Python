# Demonstrate the usage of orderedDict.

def main():
    # TODO : list of sport teams with wins and losses
    sport_teams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                   ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                   ("Kings", (15, 15)), ("Chargers", (20, 10)),
                   ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # TODO : sort the teams by number of wins
    sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)
    # print(sorted_teams)

    # # TODO : create an ordered dictionary of the teams instead of sorted
    from collections import OrderedDict
    teams = OrderedDict(sorted_teams)  # sorted_teams is a list of tuples
    print(teams)
    #
    # TODO : Use popitem to remove the top item
    tm, wl = teams.popitem(False)  # False means the first item in the list will be removed
    print("Top team: ", tm, wl)
    #
    # TODO : What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break
    #
    # TODO : test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    b = {"a": 1, "c": 3, "b": 2}
    print("Equality test: ", a == b)
    #


if __name__ == "__main__":
    main()

# Application of Ordered Dict.
# 1. It is used to create an ordered dictionary.
# 2. It is used to create a dictionary that remembers the order of the keys that were inserted first.
# 3. It is used to create a dictionary that remembers the order of the keys that were inserted last.
# 4. It is used to create a dictionary that remembers the order of the keys that were inserted in the order of their values.