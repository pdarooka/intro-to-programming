#include <iostream>
#include <map>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <sstream>
#include <map>
#include <ctype.h>

using namespace std;

int main()
{
    map<char, int> counter;
    ifstream indata;
    ofstream outdata;
    indata.open("text.txt");
    outdata.open("text_analysis.txt");
    if (outdata.fail() || indata.fail())
        exit(1);
    vector<string> tokens;
    while (!indata.eof())
    {
        string text, tmp, tmp2;
        getline(indata, text);
        istringstream str(text);
        while (str >> tmp)
            tokens.push_back(tmp);

        for (auto e : tokens)
        {
            for_each(e.begin(), e.end(), [](char &c) {
                c = toupper(c);
            });
            for (auto c : e)
            {
                if (isalpha(c))
                {
                    counter[c]++;
                }
            }
        }
    }
    char tmp = 'A';
    for (int i = 0; i < 26; i++)
    {
        string s(1, tmp);
        outdata << s << ": " << counter[tmp++] << endl;
    }

    tmp = 'A';
    char sub;
    while (!isdigit(sub) || sub == '0')
    {
        if (!isdigit(sub) || sub == '0')
        {
            if (counter[tmp] != 0)
            {
                cout << "Swap " << tmp << " with? (Enter a digit to exit. 0 to skip a letter)\n";
                cin >> sub;

                for (auto p : tokens)
                {
                    for_each(p.begin(), p.end(), [](char &c) {
                        c = toupper(c);
                    });

                    for (auto chr : p)
                    {
                        if (chr == tmp)
                        {
                            chr = toupper(sub);
                        }
                        else if (chr == sub)
                        {
                            chr = toupper(tmp);
                        }
                    }

                    outdata << p << " ";
                }
                outdata << endl;
            }
            tmp++;
        }
    }
    return 0;
}
