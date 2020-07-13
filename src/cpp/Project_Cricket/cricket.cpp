#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

struct Player
{
    string name;
    int balls_faced;
    int runs_chased;
};

//Map of rank and player? find rank, increase rank of all other players behind (++)
//Display current leaderboard before and after the match.

void UpdateLeaderboard(Player &p, const string &fname, map<string, int> m)
{
}

int main()
{
    ifstream in;
    int prev_nplayers = 0;
    string dummy;
    map<string, int> ranks;
    in.open("leaderboard.txt");
    while (!in.eof())
    {
        Player temp;
        string tmp;
        getline(in, dummy);
        prev_nplayers++;
        vector<string> tokens;
        istringstream str(dummy);
        while (str >> tmp)
            tokens.push_back(tmp);
        temp.name = tokens[1];
        temp.runs_chased = stoi(tokens[2]);
        temp.balls_faced = stoi(tokens[3]);
        ranks[temp.name] = stoi(tokens[0]);
    }
    cout << "You are competing against " << prev_nplayers << " other player(s). Be Serious.\nPress Enter to continue.\n";
    cin.ignore();
    Player p;

    cout << "Welcome to the game of Cricket.\n"
         << "The objective is simple, chase the target, with the minimum balls faced, without getting out.\n"
         << "Rules:\nEnter the number of runs you want to score.\n"
         << "If this equals to the number of runs the CPU scores, you're OUT.\n"
         << "Enter your name to continue:\n";
    cin >> p.name;

again:
    int target, runs_user, runs_cpu, total_user = 0, balls = 0, to_win;
    bool bad = false, out = false;
    srand(time(NULL));
    target = (rand() % 50) + 0;
    to_win = target + 1;
    cout << "The opponent scored: " << target << endl;
    cout << "Your target is: " << to_win << endl;

    while (total_user <= target)
    {
        cout << "To win: " << to_win << endl;
        cout << "Enter the number of runs:\n";
        cin >> runs_user;
        runs_cpu = (rand() % 6) + 1;
        if (runs_user > 6 || runs_user < 0)
        {
            bad = true;
            break;
        }
        else if (runs_cpu == runs_user)
        {
            cout << "HOWZAT!\nYou lose!\n";
            out = true;
            break;
        }

        total_user += runs_user;
        to_win -= runs_user;
        balls++;
        cout << "Your score: " << total_user << endl;
    }

    if (!bad && !out)
    {
        cout << "You Win!\n";
        cout << "Balls faced: " << balls << endl;
        p.balls_faced = balls;
        p.runs_chased = runs_cpu;
        UpdateLeaderboard(p, "leaderboard.txt", ranks);
    }
    else if (out)
    {
        cout << "Better luck next time, " << p.name << "!\n";
        return 0;
    }
    else
    {
        cout << p.name << ", you cheat!\n";
        return 0;
    }

    char ch1;
    cout << "Do you want to play again? (Press Y or N)\n";
    cin >> ch1;
    if (ch1 == 'y')
    {
        goto again;
    }
    else
    {
        cout << "Bye!\n";
    }

    return 0;
}