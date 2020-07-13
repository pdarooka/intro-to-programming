#include "calculator.h"
#include "ui_calculator.h"

double calc_value = 0.0;
bool divTrigger = false;
bool multTrigger = false;
bool subrigger = false;
bool addTrigger = false;

calculator::calculator(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::calculator)
{
    ui->setupUi(this);

    ui->display->setText(QString::number(calc_value));
    QPushButton *numButtons[10];
    for(int i = 0; i < 10; i++){
        QString buttonName =  "Button" + QString::number(i);
        numButtons[i] = calculator::findChild<QPushButton *>(buttonName);
        connect(numButtons[i], SIGNAL(released()), this, SLOT(NumPressed()));
    }
}

calculator::~calculator()
{
    delete ui;
}

void calculator::NumPressed(){
    QPushButton *button = (QPushButton*)sender();
    QString button_value = button->text();
    QString display_value = ui->display->text();

    if(display_value.toDouble() == 0.0 || display_value.toDouble() == 0){
        ui->display->setText(button_value);
    }
    else{
        QString new_value = display_value + button_value;
        double dbl_new_value = new_value.toDouble();
        ui->display->setText(QString::number(dbl_new_value, 'g', 16));
    }
}
