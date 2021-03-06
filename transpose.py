class Note():
    def __init__(self, note, sharp=False, octave=0):
        if not note or note not in "CDEFGAB":
            raise ValueError(f"{note} is invalid note letter.")
        
        if note in "EB" and sharp:
            raise ValueError(f"Note {note} does not have sharp.")

        if octave not in range(10):
            raise ValueError(f"Octave {octave} is out of range.")

        self.note = note
        if sharp:
            self.note += "#"
        self.octave = octave
        self.update_pitch()


    def update_pitch(self):
        self.pitch = 12+12*self.octave + Note.NOTES.index(self.note)

    def update_note(self):
        self.octave = self.pitch // 12 - 1
        self.note = Note.NOTES[self.pitch % 12]
        
    def transpose(self, value):
        self.pitch += value
        self.update_note()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.note}{self.octave}"
      
    NOTES = ["C",
             "C#",
             "D",
             "D#",
             "E",
             "F",
             "F#",
             "G",
             "G#",
             "A",
             "A#",
             "B"]

def parse_notes(text):
    text = text.upper()
    phrase = []
    
    note = ""
    sharp = False
    octave = 0
    
    for char in text:
        if char.isalpha():
            note = char
        if char == "#":
            sharp = True
        if char.isdigit():
            octave = int(char)

            phrase.append(Note(note,sharp,octave))
            note = ""
            sharp = False
            octave = 0

    return phrase

if __name__ == '__main__':
    import argparse
    
    argparser = argparse.ArgumentParser(description = "Transpose a music phrase")

    argparser.add_argument(
        'phrase',
        metavar='phrase',
        type = str,
        help = "A music phrase, e.g. 'A2 C2 G#4'"
        )

    argparser.add_argument(
        'transpose_by',
        metavar='transpose_by',
        type = int,
        help = "The value to transpose by, e.g. 1: 'A2 C2 G#4' => 'A#2 C#2 A4'"
        )

    args = argparser.parse_args()

    notes = parse_notes(args.phrase)
    for note in notes:
        note.transpose(args.transpose_by)
        print (note, end=" ")
    print()