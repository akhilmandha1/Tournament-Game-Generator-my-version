# Tournament Game Generator my version
 my personal project


For this project, I’ll be creating a program that schedules the games teams will play in the first round of an end-of-year tournament.
The program will start by asking the user to input the total number of teams, assuming there will always be an even number, so no validation for this is needed. It will then prompt for the names of all teams and store them appropriately.

Next, the program will determine the number of games each team played in the regular season, with the assumption that each team has played the same number of games. It will also gather the number of wins each team achieved during the season.

The program will validate user input to ensure it meets specific criteria and will prompt the user to try again if they enter invalid information. I can assume the data type will be correct (e.g., integers for numbers), but the program will check for these constraints:

- A minimum of 2 teams in the tournament.
- Each team must have played every other team at least once.
- Team names should contain at least 2 characters and at most 2 words.
- Wins should range from 0 to the total number of games played.

For the first round of the tournament, teams with the highest number of wins will play against teams with the lowest. For instance, if Team A has 5 wins, Team B has 4, Team C has 3, and Team D has 2, then Team A would play Team D, and Team B would play Team C. If there is a tie in wins, the program can choose any appropriate team.

The program will output each game in a specific format, with the team with fewer wins acting as the "home" team. If wins are tied, the program can choose any suitable team as the home team.

Here’s are a couple of examples of the program’s execution:


Sample Program Execution #1

Enter the number of teams in the tournament: 1
The minimum number of teams is 2, try again.

Enter the number of teams in the tournament: 4
Enter the name for team #1: Python
Enter the name for team #2: Ruby
Enter the name for team #3: JavaScript
Enter the name for team #4: C
Team names must have at least 2 characters, try again.
Enter the name for team #4: C Is Great

Team names may have at most 2 words, try again.
Enter the name for Team #4: C#

Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.
Enter the number of games played by each team: 3

Enter the number of wins Team Python had: 2 
Enter the number of wins Team Ruby had: 1 
Enter the number of wins Team JavaScript had: 0 
Enter the number of wins Team C# had: -2

The minimum number of wins is 0, try again.
Enter the number of wins Team C# had: 3

Generating the games to be played in the first round of the tournament...
Home: JavaScript VS Away: C#
Home: Ruby VS Away: Python

-------------------------------------------------------------------------

Sample Program Execution #2

Enter the number of teams in the tournament: 6

Enter the name for team #1: AA
Enter the name for team #2: BB
Enter the name for team #3: CC
Enter the name for team #4: DD
Enter the name for team #5: EE
Enter the name for team #6: FF

Enter the number of games played by each team: 2
Invalid number of games. Each team plays each other at least once in the regular season, try again.

Enter the number of games played by each team: 6

Enter the number of wins Team AA had: 1 
Enter the number of wins Team BB had: 4 
Enter the number of wins Team CC had: 3 
Enter the number of wins Team DD had: 4 
Enter the number of wins Team EE had: 2 
Enter the number of wins Team FF had: 7 
The maximum number of wins is 6, try again.

Enter the number of wins Team FF had: 5 
Generating the games to be played in the first round of the tournament...

Home: AA VS Away: FF
Home: EE VS Away: BB
Home: CC VS Away: DD


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
