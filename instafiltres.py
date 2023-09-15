from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox,
                               QHBoxLayout, QLineEdit, QButtonGroup, QRadioButton)
from PySide6.QtGui import QImage, QPixmap
from abc import ABC, abstractmethod

# Membres de l'équipe (Nom complet + nom d'usager Github)
#
#
#
class InstaFiltres(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_image = QLabel()
        self.pixmap = QPixmap('barbenheimer')
        self.etiquette_image.setPixmap(self.pixmap)
        self.dict_filtres = {}

    def appliquer_filtres(self):
        # Fait une copy pour s'assurer de ne pas modifier l'original
        pixmap_copy = self.pixmap.copy()
        # On itère à travers tous les filtres contenus dans le dictionnaire
        # La filtre[0] est l'instance du filtre, filtre[1] contient les paramètres passés au filtre
        for filtre in self.dict_filtres.values():
            pixmap_copy = filtre[0].appliquer_filtre(pixmap_copy, filtre[1])
        self.etiquette_image.setPixmap(pixmap_copy)


class AbstractFiltre(ABC):

    @abstractmethod
    def appliquer_filtre(self, qpixmap: QPixmap, params: {}) -> QPixmap:
        pass


class NuancesGrisFiltre(AbstractFiltre):

    def appliquer_filtre(self, qpixmap: QPixmap, params: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class RGBSwapFiltre(AbstractFiltre):

    def appliquer_filtre(self, qpixmap: QPixmap,  params: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class InterpolationFiltre(AbstractFiltre):

    def appliquer_filtre(self, qpixmap: QPixmap,  params: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


class SepiaFiltre(AbstractFiltre):

    def appliquer_filtre(self, qpixmap: QPixmap, params: {}) -> QPixmap:
        qimage = qpixmap.toImage()
        # Votre code du filtre ici

        return QPixmap.fromImage(qimage)


app = QApplication()
insta_filtres = InstaFiltres()
insta_filtres.show()
app.exec()



