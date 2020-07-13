#include <iostream>
#include "learner.h"

using namespace std;

int main()
{
    Learner AI;

    while (true)
    {
        cout << "\nYou: ";
        string phrase;
        getline(cin, phrase);

        cout << "\nAI: ";
        AI.respond(phrase);
    }
}

//SOURCE: https://www.instructables.com/id/A-Learning-Chatterbot-in-C/