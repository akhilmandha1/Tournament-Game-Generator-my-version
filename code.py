# Tournament Game Generator

def get_team_name(team_number):
    while True:
        name = input(f"Enter the name for team #{team_number}: ")
        if len(name.split()) > 2:
            print("Team names may have at most 2 words, try again.")
        elif len(name) < 2:
            print("Team names must have at least 2 characters, try again.")
        else:
            return name


def get_positive_integer(prompt, min_value):
    while True:
        value = int(input(prompt))
        if value < min_value:
            print(
                f"Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            return value


def get_wins_for_team(team, max_wins):
    while True:
        wins = int(input(f"Enter the number of wins Team {team} had: "))
        if 0 <= wins <= max_wins:
            return wins
        else:
            print(f"The maximum number of wins is {max_wins}, try again.")


def main():
    # Get the number of teams
    num_teams = get_positive_integer("Enter the number of teams in the tournament: ", 2)

    # Get team names
    teams = []
    for i in range(1, num_teams + 1):
        teams.append(get_team_name(i))

    # Get number of games played by each team
    num_games = get_positive_integer("Enter the number of games played by each team: ", num_teams - 1)

    # Get number of wins for each team
    wins = []
    for team in teams:
        wins.append(get_wins_for_team(team, num_games))

    # Sort teams by wins in descending order
    sorted_teams = sorted(zip(teams, wins), key=lambda x: x[1], reverse=True)

    # Generate and display first-round games
    print("Generating the games to be played in the first round of the tournament...")
    num_matches = num_teams // 2
    for i in range(num_matches):
        home_team = sorted_teams[num_teams - i - 1][0]
        away_team = sorted_teams[i][0]
        print(f"Home: {home_team} VS Away: {away_team}")


if __name__ == "__main__":
    main()
