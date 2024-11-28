# pip install PySide6
import sys
import json
from Sanakysely import Sanakysely
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog

class Kyselyikkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,450,350)
        self.kysely = Sanakysely()
        self.alusta_UI()
        

    def alusta_UI(self):
        self.setWindowTitle("Sanakysely")

        self.e1 = QLabel("Oikeat: 0", self)
        self.e1.setGeometry(20,20,80,30)

        self.e2 = QLabel("Väärät: 0", self)
        self.e2.setGeometry(100,20,80,30)

        self.e3 = QLabel("Sana: 0", self)
        self.e3.setGeometry(270,20,80,30)

        self.t1 = QLineEdit(self.kysely.seuraavaSana(), self)
        self.t1.setGeometry(20,60,150,30)
        self.t1.setEnabled(False)

        self.t2 = QLineEdit(self)
        self.t2.setPlaceholderText("Kirjoita sana")
        self.t2.setGeometry(200,60,150,30)
        self.t2.returnPressed.connect(self.tarkista_sana)

        self.painike = QPushButton("Aloita alusta", self)
        self.painike.setGeometry(20,100,330,30)
        self.painike.clicked.connect(self.aloita_alusta)

        menupalkki = self.menuBar() # haetaan ikkunalta menu
        tiedostomenu = menupalkki.addMenu("&Tiedosto")
        avaa = tiedostomenu.addAction("&Avaa")
        avaa.triggered.connect(self.menu_avaa)

    def tarkista_sana(self):
        vastaus = self.t2.text()
        self.kysely.tarkista(vastaus)

        self.t1.setText(self.kysely.seuraavaSana())
        self.t2.clear()
        self.paivita_tiedot()

    def aloita_alusta(self):
        self.kysely.nollaa()
        self.t1.setText(self.kysely.seuraavaSana())
        self.paivita_tiedot()

    def paivita_tiedot(self):
        self.e1.setText(f"Oikeat: {self.kysely.oikeat}")
        self.e2.setText(f"Väärät: {self.kysely.vaarat}")
        self.e3.setText(f"Sana: {self.kysely.sananro}")

    def menu_avaa(self):
        tiedosto = QFileDialog.getOpenFileName(self, "Avaa sanasto")
        with open(tiedosto[0], "r") as t:
            tiedoston_sisalto = t.read()
            self.kysely.sanasto = json.loads(tiedoston_sisalto)
            self.aloita_alusta()
        


def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Kyselyikkuna() # olio luokasta Kyselyi, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()