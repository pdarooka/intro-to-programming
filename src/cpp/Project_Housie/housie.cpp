#include <vector>
#include <iostream>

using namespace std;

int main()
{
    vector<int> numbers, done;
    int count = 0;

    for (int i = 1; i <= 90; i++)
        numbers.push_back(i);

    while (numbers.size() != done.size())
    {
        srand(time(NULL));
        int num = (rand() % 90) + 0;
        std::vector<int>::iterator it = find(done.begin(), done.end(), numbers[num]);
        if (it == done.end())
        {
            count++;
            cout << "Next Number is:\n";
            cout << numbers[num] << endl;
            done.push_back(numbers[num]);
        }
        else
            continue;

        int ch, temp;
        ch = cin.get();

        if (ch != '\n')
        {
            cout << "Enter the number you want to check.\n";
            cin >> temp;
            std::vector<int>::iterator it2 = find(done.begin(), done.end(), temp);
            if (it2 != done.end())
            {
                cout << "Done.\n\n";
            }
            else
            {
                cout << "Boogie.\n\n";
            }
        }

        if (count % 15 == 0)
        {
            cout << "\nNumbers currently done:\n";
            for (auto e : done)
                cout << e << " ";
            cout << endl
                 << endl;
        }
    }
    cout << "The end. Thank you for playing.\n";
}