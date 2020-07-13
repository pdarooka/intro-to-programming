#ifndef LEARNER_H
#define LEARNER_H

#include <iostream>
#include <fstream>
#include "voice.h"

using namespace std;

class Learner
{
public:
    void respond(string phrase)
    {
        ifstream mem("mem.txt");

        while (!mem.eof())
        {
            string id;
            getline(mem, id);

            if (id == phrase)
            {
                string response;
                getline(mem, response);
                voice.say(response);

                return;
            }
        }

        mem.close();

        ofstream memory("mem.txt", ios::app);
        memory << phrase << endl;

        voice.say(phrase);
        string userResp;
        cout << "You: ";
        getline(cin, userResp);
        memory << userResp << endl;
        memory.close();
    }

    void say(string phrase) { this->voice.say(phrase); }

    Voice voice;
};

#endif