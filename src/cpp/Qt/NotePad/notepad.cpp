#include "notepad.h"
#include "ui_notepad.h"

notepad::notepad(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::notepad)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->textEdit);
}

notepad::~notepad()
{
    delete ui;
}


void notepad::on_actionNew_triggered()
{
    currFile.clear();
    ui->textEdit->setPlainText(QString());
}

void notepad::on_actionOpen_triggered()
{
    QString fileName = QFileDialog::getOpenFileName(this, "Open the file");
    QFile file(fileName);
    currFile = fileName;
    if(!file.open(QIODevice::ReadOnly | QFile::Text)){
         QMessageBox::warning(this, "Warning", "Cannot open file: " + file.errorString());
         return;
    }
    setWindowTitle(fileName);
    QTextStream indata(&file);
    QString txt = indata.readAll();
    ui->textEdit->setPlainText(txt);
    file.close();
}

void notepad::on_actionSave_triggered()
{
    QString fileName = QFileDialog::getSaveFileName(this, "Save as");
    QFile file(fileName);
    currFile = fileName;
    if(!file.open(QFile::WriteOnly | QFile::Text)){
         QMessageBox::warning(this, "Warning", "Cannot save file: " + file.errorString());
         return;
    }
    currFile = fileName;
    setWindowTitle(fileName);
    QTextStream outdata(&file);
    QString txt = ui->textEdit->toPlainText();
    outdata << txt;
    file.close();
}

void notepad::on_actionPrint_triggered()
{
    QPrinter printer;
    printer.setPrinterName("Printer Name");
    QPrintDialog pDialog(&printer, this);
    if(pDialog.exec() == QDialog::Rejected){
        QMessageBox::warning(this, "Warning", "Cannot access printer");
        return;
    }
     ui->textEdit->print(&printer);
}

void notepad::on_actionExit_triggered()
{
    QApplication::quit();
}

void notepad::on_actionCopy_triggered()
{
    ui->textEdit->copy();
}

void notepad::on_actionCut_triggered()
{
    ui->textEdit->cut();
}

void notepad::on_actionPaste_triggered()
{
    ui->textEdit->paste();

}

void notepad::on_actionUndo_triggered()
{
    ui->textEdit->undo();
}

void notepad::on_actionRedo_triggered()
{
    ui->textEdit->redo();
}
