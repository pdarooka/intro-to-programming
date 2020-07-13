#include <iostream>
#include <string>

using namespace std;

void bleep(const string &word, string &text)
{
  for (int i = 0; i < text.size() - word.size() + 1; i++)
  {
    int count = 0;
    for (int j = 0; j < word.size(); j++)
    {
      if (text[i + j] == word[j])
      {
        count++;
      }
    }
    if (count == word.size())
    {
      for (int k = 0; k < word.size(); ++k)
      {
        text[i + k] = '*';
      }
    }
  }
}

int main()
{
  string word;
  string text;

  cout << "Enter the sentence you want to censor.\n";
  getline(cin, text);
  cout << "Enter the word you want to bleep out.\n";
  cin >> word;

  cout << "Before: ";
  cout << text << endl;
  bleep(word, text);
  cout << "After: ";
  cout << text << endl;

  return 0;
}