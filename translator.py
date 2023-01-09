import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget

# Define codon table
codon_table = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "*", "TAG": "*",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W",
}

# Create reverse codon table
reverse_codon_table = {v: k for k, v in codon_table.items()}

class DNA_Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle("DNA Translator")
        self.setGeometry(100, 100, 400, 300)
        # Create widgets
        self.input_field = QTextEdit()
        self.translate_button = QPushButton("Translate DNA")
        self.reverse_translate_button = QPushButton("Reverse Translate")
        self.output_field = QTextEdit()
        # Style widgets
        self.input_field.setStyleSheet("font-size: 18px;")
        self.translate_button.setStyleSheet("font-size: 18px;")
        self.reverse_translate_button.setStyleSheet("font-size: 18px;")
        self.output_field.setStyleSheet("font-size: 18px;")
        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.translate_button)
        self.layout.addWidget(self.reverse_translate_button)
        self.layout.addWidget(self.output_field)
        # Create central widget and set layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        # Set central widget
        self.setCentralWidget(self.central_widget)
        # Connect buttons to translation methods
        self.translate_button.clicked.connect(self.translate)
        self.reverse_translate_button.clicked.connect(self.reverse_translate)
        
    def translate(self):
        # Get DNA sequence from input field
        sequence = self.input_field.toPlainText()
        # Pad sequence with "N" until it is a multiple of 3
        while len(sequence) % 3 != 0:
            sequence += "N"
        # Initialize empty protein string
        protein = ""
        # Iterate over codons in sequence
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            # Translate codon using codon table
            if codon in codon_table:
                amino_acid = codon_table[codon]
            else:
                amino_acid = "X"
            # Add amino acid to protein string
            protein += amino_acid
        # Display protein string in output field
        self.output_field.setPlainText(protein)
        
    def reverse_translate(self):
        # Get protein sequence from input field
        sequence = self.input_field.toPlainText()
        # Pad sequence with "X" until it is a multiple of 3
        while len(sequence) % 3 != 0:
            sequence += "X"
        # Initialize empty DNA string
        dna = ""
        # Iterate over amino acids in sequence
        for amino_acid in sequence:
            # Translate amino acid using reverse codon table
            if amino_acid in reverse_codon_table:
                codon = reverse_codon_table[amino_acid]
            else:
                codon = "XXX"
            # Add codon to DNA string
            dna += codon
        # Display DNA string in output field
        self.output_field.setPlainText(dna)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = DNA_Translator()
    translator.show()
    sys.exit(app.exec())

