import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QComboBox, QScrollArea, QGridLayout, 
                             QPushButton, QLabel, QLineEdit, QSlider)
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import pyperclip

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
    "Round and square noteheads (U+E110–U+E11F)": (0xE110, 0xE11F),
    "Note clusters (U+E120–U+E14F)": (0xE120, 0xE14F),
    "Note name noteheads (U+E150–U+E1AF)": (0xE150, 0xE1AF),
    "Shape note noteheads (U+E1B0–U+E1CF)": (0xE1B0, 0xE1CF),
    "Individual notes (U+E1D0–U+E1EF)": (0xE1D0, 0xE1EF),
    "Beamed groups of notes (U+E1F0–U+E20F)": (0xE1F0, 0xE20F),
    "Stems (U+E210–U+E21F)": (0xE210, 0xE21F),
    "Tremolos (U+E220–U+E23F)": (0xE220, 0xE23F),
    "Flags (U+E240–U+E25F)": (0xE240, 0xE25F),
    "Standard accidentals (12-EDO) (U+E260–U+E26F)": (0xE260, 0xE26F),
    "Gould arrow quartertone (24-EDO) (U+E270–U+E27F)": (0xE270, 0xE27F),
    "Stein-Zimmermann (24-EDO) (U+E280–U+E28F)": (0xE280, 0xE28F),
    "Extended Stein-Zimmermann (U+E290–U+E29F)": (0xE290, 0xE29F),
    "Sims accidentals (72-EDO) (U+E2A0–U+E2AF)": (0xE2A0, 0xE2AF),
    "Johnston accidentals (just intonation) (U+E2B0–U+E2BF)": (0xE2B0, 0xE2BF),
    "Extended Helmholtz-Ellis (U+E2C0–U+E2FF)": (0xE2C0, 0xE2FF),
    "Spartan Sagittal single-shaft (U+E300–U+E30F)": (0xE300, 0xE30F),
    "Spartan Sagittal multi-shaft (U+E310–U+E33F)": (0xE310, 0xE33F),
    "Athenian Sagittal extension (U+E340–U+E36F)": (0xE340, 0xE36F),
    "Trojan Sagittal extension (U+E370–U+E38F)": (0xE370, 0xE38F),
    "Promethean Sagittal extension (single) (U+E390–U+E3AF)": (0xE390, 0xE3AF),
    "Promethean Sagittal extension (multi) (U+E3B0–U+E3DF)": (0xE3B0, 0xE3DF),
    "Herculean Sagittal extension (U+E3F0–U+E3F3)": (0xE3F0, 0xE3F3),
    "Olympian Sagittal extension (U+E3F4–U+E3F7)": (0xE3F4, 0xE3F7),
    "Magrathean Sagittal extension (U+E3F8–U+E41F)": (0xE3F8, 0xE41F),
    "Wyschnegradsky accidentals (72-EDO) (U+E420–U+E43F)": (0xE420, 0xE43F),
    "Arel-Ezgi-Uzdilek (AEU) (U+E440–U+E44F)": (0xE440, 0xE44F),
    "Turkish folk music accidentals (U+E450–U+E45F)": (0xE450, 0xE45F),
    "Persian accidentals (U+E460–U+E46F)": (0xE460, 0xE46F),
    "Other accidentals (U+E470–U+E49F)": (0xE470, 0xE49F),
    "Articulation (U+E4A0–U+E4BF)": (0xE4A0, 0xE4BF),
    "Holds and pauses (U+E4C0–U+E4DF)": (0xE4C0, 0xE4DF),
    "Rests (U+E4E0–U+E4FF)": (0xE4E0, 0xE4FF),
    "Bar repeats (U+E500–U+E50F)": (0xE500, 0xE50F),
    "Octaves (U+E510–U+E51F)": (0xE510, 0xE51F),
    "Dynamics (U+E520–U+E54F)": (0xE520, 0xE54F),
    "Lyrics (U+E550–U+E55F)": (0xE550, 0xE55F),
    "Common ornaments (U+E560–U+E56F)": (0xE560, 0xE56F),
    "Other baroque ornaments (U+E570–U+E58F)": (0xE570, 0xE58F),
    "Combining strokes for trills (U+E590–U+E5AF)": (0xE590, 0xE5AF),
    "Precomposed trills/mordents (U+E5B0–U+E5CF)": (0xE5B0, 0xE5CF),
    "Brass techniques (U+E5D0–U+E5EF)": (0xE5D0, 0xE5EF),
    "Wind techniques (U+E5F0–U+E60F)": (0xE5F0, 0xE60F),
    "String techniques (U+E610–U+E62F)": (0xE610, 0xE62F),
    "Plucked techniques (U+E630–U+E63F)": (0xE630, 0xE63F),
    "Vocal techniques (U+E640–U+E64F)": (0xE640, 0xE64F),
    "Keyboard techniques (U+E650–U+E67F)": (0xE650, 0xE67F),
    "Harp techniques (U+E680–U+E69F)": (0xE680, 0xE69F),
    "Tuned mallet percussion (U+E6A0–U+E6BF)": (0xE6A0, 0xE6BF),
    "Chimes pictograms (U+E6C0–U+E6CF)": (0xE6C0, 0xE6CF),
    "Drums pictograms (U+E6D0–U+E6EF)": (0xE6D0, 0xE6EF),
    "Wooden struck percussion (U+E6F0–U+E6FF)": (0xE6F0, 0xE6FF),
    "Metallic struck percussion (U+E700–U+E70F)": (0xE700, 0xE70F),
    "Bells pictograms (U+E710–U+E71F)": (0xE710, 0xE71F),
    "Cymbals pictograms (U+E720–U+E72F)": (0xE720, 0xE72F),
    "Gongs pictograms (U+E730–U+E73F)": (0xE730, 0xE73F),
    "Shakers or rattles pictograms (U+E740–U+E74F)": (0xE740, 0xE74F),
    "Whistles and aerophones (U+E750–U+E75F)": (0xE750, 0xE75F),
    "Miscellaneous percussion (U+E760–U+E76F)": (0xE760, 0xE76F),
    "Beaters pictograms (U+E770–U+E7EF)": (0xE770, 0xE7EF),
    "Percussion playing techniques (U+E7F0–U+E80F)": (0xE7F0, 0xE80F),
    "Handbells (U+E810–U+E82F)": (0xE810, 0xE82F),
    "Guitar (U+E830–U+E84F)": (0xE830, 0xE84F),
    "Chord diagrams (U+E850–U+E85F)": (0xE850, 0xE85F),
    "Analytics (U+E860–U+E86F)": (0xE860, 0xE86F),
    "Chord symbols (U+E870–U+E87F)": (0xE870, 0xE87F),
    "Tuplets (U+E880–U+E88F)": (0xE880, 0xE88F),
    "Conductor symbols (U+E890–U+E89F)": (0xE890, 0xE89F),
    "Accordion (U+E8A0–U+E8DF)": (0xE8A0, 0xE8DF),
    "Beams and slurs (U+E8E0–U+E8EF)": (0xE8E0, 0xE8EF),
    "Medieval and Renaissance staves (U+E8F0–U+E8FF)": (0xE8F0, 0xE8FF),
    "Medieval and Renaissance clefs (U+E900–U+E90F)": (0xE900, 0xE90F),
    "Medieval and Renaissance prolations (U+E910–U+E92F)": (0xE910, 0xE92F),
    "Medieval/Renaissance notes/stems (U+E930–U+E94F)": (0xE930, 0xE94F),
    "Medieval/Renaissance individual notes (U+E950–U+E96F)": (0xE950, 0xE96F),
    "Medieval and Renaissance oblique forms (U+E970–U+E98F)": (0xE970, 0xE98F),
    "Plainchant single-note forms (U+E990–U+E9AF)": (0xE990, 0xE9AF),
    "Plainchant multiple-note forms (U+E9B0–U+E9CF)": (0xE9B0, 0xE9CF),
    "Plainchant articulations (U+E9D0–U+E9DF)": (0xE9D0, 0xE9DF),
    "Medieval and Renaissance accidentals (U+E9E0–U+E9EF)": (0xE9E0, 0xE9EF),
    "Medieval and Renaissance rests (U+E9F0–U+E9FF)": (0xE9F0, 0xE9FF),
    "Medieval and Renaissance miscellany (U+EA00–U+EA1F)": (0xEA00, 0xEA1F),
    "Medieval/Renaissance symbols in CMN (U+EA20–U+EA2F)": (0xEA20, 0xEA2F),
    "Daseian notation (U+EA30–U+EA4F)": (0xEA30, 0xEA4F),
    "Figured bass (U+EA50–U+EA6F)": (0xEA50, 0xEA6F),
    "Function theory symbols (U+EA70–U+EA9F)": (0xEA70, 0xEA9F),
    "Multi-segment lines (U+EAA0–U+EB0F)": (0xEAA0, 0xEB0F),
    "Electronic music pictograms (U+EB10–U+EB5F)": (0xEB10, 0xEB5F),
    "Arrows and arrowheads (U+EB60–U+EB8F)": (0xEB60, 0xEB8F),
    "Combining staff positions (U+EB90–U+EB9F)": (0xEB90, 0xEB9F),
    "Renaissance lute tablature (U+EBA0–U+EBBF)": (0xEBA0, 0xEBBF),
    "French/English Renaissance lute (U+EBC0–U+EBDF)": (0xEBC0, 0xEBDF),
    "Italian/Spanish Renaissance lute (U+EBE0–U+EBFF)": (0xEBE0, 0xEBFF),
    "German Renaissance lute tablature (U+EC00–U+EC2F)": (0xEC00, 0xEC2F),
    "Kievan square notation (U+EC30–U+EC3F)": (0xEC30, 0xEC3F),
    "Kodály hand signs (U+EC40–U+EC4F)": (0xEC40, 0xEC4F),
    "Simplified Music Notation (U+EC50–U+EC5F)": (0xEC50, 0xEC5F),
    "Miscellaneous symbols (U+EC60–U+EC7F)": (0xEC60, 0xEC7F),
    "Time signatures supplement (U+EC80–U+EC8F)": (0xEC80, 0xEC8F),
    "Octaves supplement (U+EC90–U+EC9F)": (0xEC90, 0xEC9F),
    "Metronome marks (U+ECA0–U+ECBF)": (0xECA0, 0xECBF),
    "Figured bass supplement (U+ECC0–U+ECCF)": (0xECC0, 0xECCF),
    "Shape note noteheads supplement (U+ECD0–U+ECDF)": (0xECD0, 0xECDF),
    "Turned time signatures (U+ECE0–U+ECEF)": (0xECE0, 0xECEF),
    "Reversed time signatures (U+ECF0–U+ECFF)": (0xECF0, 0xECFF),
    "Function theory symbols supplement (U+ED00–U+ED0F)": (0xED00, 0xED0F),
    "Fingering (U+ED10–U+ED2F)": (0xED10, 0xED2F),
    "Arabic accidentals (U+ED30–U+ED3F)": (0xED30, 0xED3F),
    "Articulation supplement (U+ED40–U+ED4F)": (0xED40, 0xED4F),
    "Stockhausen accidentals (24-EDO) (U+ED50–U+ED5F)": (0xED50, 0xED5F),
    "Standard accidentals chord symbols (U+ED60–U+ED6F)": (0xED60, 0xED6F),
    "Clefs supplement (U+ED70–U+ED7F)": (0xED70, 0xED7F),
    "Fingering supplement (U+ED80–U+ED9F)": (0xED80, 0xED9F),
    "Kahnotation (U+EDA0–U+EDFF)": (0xEDA0, 0xEDFF),
    "German organ tablature (U+EE00–U+EE4F)": (0xEE00, 0xEE4F),
    "Extended Helmholtz-Ellis supplement (U+EE50–U+EE5F)": (0xEE50, 0xEE5F),
    "Other accidentals supplement (U+EE60–U+EE6F)": (0xEE60, 0xEE6F),
    "Techniques noteheads (U+EE70–U+EE7F)": (0xEE70, 0xEE7F),
    "Chop (percussive bowing) notation (U+EE80–U+EE8F)": (0xEE80, 0xEE8F),
    "Medieval/Renaissance prolations supp (U+EE90–U+EE9F)": (0xEE90, 0xEE9F),
    "Noteheads supplement (U+EEA0–U+EEDF)": (0xEEA0, 0xEEDF),
    "Note name noteheads supplement (U+EEE0–U+EEFF)": (0xEEE0, 0xEEFF),
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