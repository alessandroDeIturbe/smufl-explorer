import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QComboBox, QScrollArea, QGridLayout, 
                             QPushButton, QLabel, QLineEdit, QSlider)
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import pyperclip

# DIZIONARIO COMPLETO ESTRATTO DAI TUOI SCREENSHOT
SM_RANGES = {
    "All ranges (U+E000–U+F3FF)": (0xE000, 0xF3FF),
    "Staff brackets and dividers (U+E000–U+E00F)": (0xE000, 0xE00F),
    "Staves (U+E010–U+E02F)": (0xE010, 0xE02F),
    "Barlines (U+E030–U+E03F)": (0xE030, 0xE03F),
    "Repeats (U+E040–U+E04F)": (0xE040, 0xE04F),
    "Clefs (U+E050–U+E07F)": (0xE050, 0xE07F),
    "Time signatures (U+E080–U+E09F)": (0xE080, 0xE09F),
    "Noteheads (U+E0A0–U+E0FF)": (0xE0A0, 0xE0FF),
    "Slash noteheads (U+E100–U+E10F)": (0xE100, 0xE10F),
    "Round/Square noteheads (U+E110–U+E11F)": (0xE110, 0xE11F),
    "Note clusters (U+E120–U+E14F)": (0xE120, 0xE14F),
    "Note name noteheads (U+E150–U+E1AF)": (0xE150, 0xE1AF),
    "Shape note noteheads (U+E1B0–U+E1CF)": (0xE1B0, 0xE1CF),
    "Individual notes (U+E1D0–U+E1EF)": (0xE1D0, 0xE1EF),
    "Beamed groups of notes (U+E1F0–U+E20F)": (0xE1F0, 0xE20F),
    "Stems (U+E210–U+E21F)": (0xE210, 0xE21F),
    "Tremolos (U+E220–U+E23F)": (0xE220, 0xE23F),
    "Flags (U+E240–U+E25F)": (0xE240, 0xE25F),
    "Standard accidentals (12-EDO) (U+E260–U+E26F)": (0xE260, 0xE26F),
    "Gould arrow (24-EDO) (U+E270–U+E27F)": (0xE270, 0xE27F),
    "Stein-Zimmermann (24-EDO) (U+E280–U+E28F)": (0xE280, 0xE28F),
    "Extended Stein-Zimmermann (U+E290–U+E29F)": (0xE290, 0xE29F),
    "Sims accidentals (72-EDO) (U+E2A0–U+E2AF)": (0xE2A0, 0xE2AF),
    "Johnston accidentals (just intonation) (U+E2B0–U+E2BF)": (0xE2B0, 0xE2BF),
    "Extended Helmholtz-Ellis (U+E2C0–U+E2FF)": (0xE2C0, 0xE2FF),
    "Sagittal accidentals (U+E300–U+E41F)": (0xE300, 0xE41F),
    "Wyschnegradsky accidentals (U+E420–U+E43F)": (0xE420, 0xE43F),
    "Turkish/Persian accidentals (U+E440–U+E46F)": (0xE440, 0xE46F),
    "Articulation (U+E4A0–U+E4BF)": (0xE4A0, 0xE4BF),
    "Holds and pauses (U+E4C0–U+E4DF)": (0xE4C0, 0xE4DF),
    "Rests (U+E4E0–U+E4FF)": (0xE4E0, 0xE4FF),
    "Bar repeats (U+E500–U+E50F)": (0xE500, 0xE50F),
    "Octaves (U+E510–U+E51F)": (0xE510, 0xE51F),
    "Dynamics (U+E520–U+E54F)": (0xE520, 0xE54F),
    "Lyrics (U+E550–U+E55F)": (0xE550, 0xE55F),
    "Common ornaments (U+E560–U+E56F)": (0xE560, 0xE56F),
    "Other baroque ornaments (U+E570–U+E58F)": (0xE570, 0xE58F),
    "Brass techniques (U+E5D0–U+E5EF)": (0xE5D0, 0xE5EF),
    "Wind techniques (U+E5F0–U+E60F)": (0xE5F0, 0xE60F),
    "String techniques (U+E610–U+E62F)": (0xE610, 0xE62F),
    "Plucked techniques (U+E630–U+E63F)": (0xE630, 0xE63F),
    "Vocal techniques (U+E640–U+E64F)": (0xE640, 0xE64F),
    "Keyboard techniques (U+E650–U+E67F)": (0xE650, 0xE67F),
    "Harp techniques (U+E680–U+E69F)": (0xE680, 0xE69F),
    "Percussion pictograms (U+E6A0–U+E82F)": (0xE6A0, 0xE82F),
    "Guitar (U+E830–U+E84F)": (0xE830, 0xE84F),
    "Chord diagrams/symbols (U+E850–U+E87F)": (0xE850, 0xE87F),
    "Tuplets/Conductor symbols (U+E880–U+E89F)": (0xE880, 0xE89F),
    "Medieval/Renaissance (U+E8F0–U+EA2F)": (0xE8F0, 0xEA2F),
    "Figured bass (U+EA50–U+EA6F)": (0xEA50, 0xEA6F),
    "Electronic music (U+EB10–U+EB5F)": (0xEB10, 0xEB5F),
    "Lute tablatures (U+EBA0–U+EC2F)": (0xEBA0, 0xEC2F),
    "Kodály hand signs (U+EC40–U+EC4F)": (0xEC40, 0xEC4F),
    "Metronome marks (U+ECA0–U+ECBF)": (0xECA0, 0xECBF),
    "Fingering (U+ED10–U+ED2F)": (0xED10, 0xED2F),
    "Stockhausen accidentals (U+ED50–U+ED5F)": (0xED50, 0xED5F),
    "German organ tablature (U+EE00–U+EE4F)": (0xEE00, 0xEE4F),
    "Scale degrees (U+EF00–U+EF0F)": (0xEF00, 0xEF0F),
}

class SmuflExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.current_zoom = 35
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SMuFL Explorer Pro - Database Completo')
        self.resize(1200, 900)
        main_layout = QVBoxLayout(self)

        # Riga 1: Ricerca e Font
        top_bar = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cerca categoria...")
        self.search_bar.textChanged.connect(self.filter_categories)
        top_bar.addWidget(self.search_bar, 2)

        self.font_combo = QComboBox()
        self.font_combo.addItems(QFontDatabase.families())
        if "Finale Maestro" in QFontDatabase.families():
            self.font_combo.setCurrentText("Finale Maestro")
        self.font_combo.currentTextChanged.connect(self.update_grid)
        top_bar.addWidget(self.font_combo, 1)
        main_layout.addLayout(top_bar)

        # Riga 2: Slider Zoom
        zoom_layout = QHBoxLayout()
        zoom_layout.addWidget(QLabel("Dimensione Simboli:"))
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_slider.setRange(20, 120)
        self.zoom_slider.setValue(self.current_zoom)
        self.zoom_slider.valueChanged.connect(self.change_zoom)
        zoom_layout.addWidget(self.zoom_slider)
        main_layout.addLayout(zoom_layout)

        # Riga 3: Menu Categorie
        self.combo = QComboBox()
        self.all_keys = list(SM_RANGES.keys())
        self.combo.addItems(self.all_keys)
        self.combo.currentIndexChanged.connect(self.update_grid)
        main_layout.addWidget(self.combo)

        # Area Griglia
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.container = QWidget()
        self.grid = QGridLayout(self.container)
        self.scroll_area.setWidget(self.container)
        main_layout.addWidget(self.scroll_area)

        self.status = QLabel("Pronto")
        self.status.setStyleSheet("padding: 8px; background: #2b2b2b; color: #aaa; border-top: 1px solid #444;")
        main_layout.addWidget(self.status)

        self.update_grid()

    def change_zoom(self, val):
        self.current_zoom = val
        self.update_grid()

    def filter_categories(self, text):
        filtered = [k for k in self.all_keys if text.lower() in k.lower()]
        self.combo.blockSignals(True)
        self.combo.clear()
        self.combo.addItems(filtered)
        self.combo.blockSignals(False)
        if filtered: self.update_grid()

    def update_grid(self):
        # Pulizia sicura per evitare errori Pylance/Runtime
        while self.grid.count() > 0:
            item = self.grid.takeAt(0)
            if item:
                w = item.widget()
                if w: w.deleteLater()

        key = self.combo.currentText()
        font_name = self.font_combo.currentText()
        if not key or key not in SM_RANGES: return
        
        start, end = SM_RANGES[key]
        cols = 10 if self.current_zoom > 60 else 14
        
        # Protezione per "All Ranges"
        limit = 1200 if "All" in key else (end - start + 1)

        for i in range(limit):
            code = start + i
            if code > end: break
            char = chr(code)
            btn = QPushButton(char)
            btn.setFont(QFont(font_name, self.current_zoom))
            btn.setFixedSize(self.current_zoom + 40, self.current_zoom + 40)
            btn.setToolTip(f"U+{code:04X}")
            btn.clicked.connect(lambda _, c=char: self.copy_to(c))
            self.grid.addWidget(btn, i // cols, i % cols)

        # Fix Pylance per reportOptionalMemberAccess
        vbar = self.scroll_area.verticalScrollBar()
        if vbar is not None:
            vbar.setValue(0)

    def copy_to(self, char):
        pyperclip.copy(char)
        self.status.setText(f"Copiato: {char} (U+{ord(char):04X}) con font {self.font_combo.currentText()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget { background-color: #1e1e1e; color: white; }
        QPushButton { background-color: #333; border: 1px solid #444; border-radius: 4px; }
        QPushButton:hover { background-color: #444; border-color: #555; }
        QComboBox, QLineEdit { background-color: #2b2b2b; border: 1px solid #444; padding: 4px; }
    """)
    ex = SmuflExplorer()
    ex.show()
    sys.exit(app.exec())