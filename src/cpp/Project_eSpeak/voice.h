#ifndef VOICE_H
#define VOICE_H

#include <iostream>

using namespace std;

class Voice
{
public:
    void say(string phrase)
    {
        string command = "say " + phrase;
        const char *charComm = command.c_str();

        cout << phrase << endl;
        system(charComm);
    }
};

#endif