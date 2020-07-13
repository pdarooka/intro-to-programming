#include <iostream>
#include <fstream>
#include <map>

using namespace std;

void CertGen(const map<string, string> &m)
{
    string out_fname;
    for (auto elem : m)
    {
        out_fname = elem.first + ".tex";
        ofstream out(out_fname);
        out << "\\documentclass[10pt]{article}"
            << "\\usepackage[a4paper, left=2cm, right=2cm, landscape]{geometry}\n"
            << "\\usepackage{xcolor}\n"
            << "\\definecolor{grey}{rgb}{0.9,0.9,0.9}\n"
            << "\\usepackage[utf8]{inputenc}\n"
            << "\\usepackage[T1]{fontenc}\n"
            << "\\usepackage[sfdefault]{ClearSans}\n"
            << "\\begin{document}\n"
            << "\\begin{titlepage}\n"
            << "\\colorbox{grey}{\n"
            << "\\parbox[t]{0.93\\textwidth}{\n"
            << "\\parbox[t]{0.91\\textwidth}{\n"
            << "\\raggedleft\n"
            << "\\fontsize{50pt}{80pt}\\selectfont\n"
            << "\\vspace{0.7cm}\n"

            << "Name : " << elem.second << "\\\\\n"
            << "For : " << elem.first << "\\\\\n"
            << "\\vspace{0.7cm}\n}\n}\n}\n"
            << "\\vfill\n"
            << "Congratulations!\\\\\n"
            << "\\end{titlepage}\n"
            << "\\end{document}\n";

        system("echo hello\n");
        system("cd /Users/prathamdarooka/Desktop/SCU/CS60");
        string command = "pdflatex " + out_fname;
        system(command.c_str());
        // cout << command.c_str() << endl;
    }
}

int main()
{
    string csv_fname;
    cout << "Please upload the CSV file with all the details.\n"
         << "Format: \"filename.csv\" (Without the quotation marks.)\n"; //FILE UPLOAD : HOW? or TYPE IN FILE NAME?
    cin >> csv_fname;

    ifstream in;
    in.open(csv_fname);
    if (in.fail())
        exit(0);

    string name, award;
    map<string, string> awardee;
    //Map<string, pair<string, string> temp> : Can use this for extra information? Like institution
    while (!in.eof())
    {
        getline(in, name, ',');
        getline(in, award);
        awardee[award] = name;
    }

    in.close();
    CertGen(awardee);
    return 0;
}

/*
Output - .TEX file insteaad of PDF
Try bash scripting for auto compiling the TEX files.
*/

/*
beamer package TEX
*/

/*
Further applications:

Upload Template of the certificate, Can USE OCR
*/