#include "notepad.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication program(argc, argv);
    notepad w;
    w.show();
    return program.exec();
}
