# Demonstrate how to use dictionary comprehension

def main():
    # define a list of temperature values
    c_temps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    temp_dict = {t: (t * 9 / 5) + 32 for t in c_temps if t < 100}
    print(temp_dict)
    print(temp_dict[12])

    # Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)

    # Filter a dictionary using a comprehension
    # dict comprehension
    new_team2 = {k: v for k, v in new_team.items() if v > 18}
    print(new_team2)


if __name__ == "__main__":
    main()
