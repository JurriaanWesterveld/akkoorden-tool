
mineur_toonladders = {
    "G#": ["G#m", "A#°", "B", "C#m", "D#m", "E", "F#"],
    "C#": ["C#m", "D#°", "E", "F#m", "G#m", "A", "B"],
    "F#": ["F#m", "G#°", "A", "Bm", "C#m", "D", "E"],
    "B": ["Bm", "C#°", "D", "Em", "F#m", "G", "A"],
    "E": ["Em", "F#°", "G", "Am", "Bm", "C", "D"],
    "A": ["Am", "B°", "C", "Dm", "Em", "F", "G"],
    "D": ["Dm", "E°", "F", "Gm", "Am", "Bb", "C"],
    "G": ["Gm", "A°", "Bb", "Cm", "Dm", "Eb", "F"],
    "C": ["Cm", "D°", "Eb", "Fm", "Gm", "Ab", "Bb"],
    "F": ["Fm", "G°", "Ab", "Bbm", "Cm", "Db", "Eb"],
    "Bb": ["Bbm", "Cm", "Db", "Ebm", "Fm", "Gb", "Ab"],
    "Eb": ["Ebm", "Fm", "Gb", "Abm", "Bbm", "Cb", "Db"],
}

majeur_toonladders = {
    "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "C°"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "G°"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Db°"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Am°"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "E°"],
    "C": ["C", "Dm", "Em", "F", "G", "Am", "B°"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#°"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#°"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#°"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#°"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#°"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#°"],
}

sharp_to_flat = {
    "Cb": "B",
    "Fb": "E",
    "Gb": "F#",
    "B#": "C",
    "E#": "F",
    "C#": "Db",
    "D#": "Eb",
    "G#": "Ab",
    "A#": "Bb"
    }


flat_to_sharp = {
    "A#": "Bb",
    "B#": "Cb",
    "D#": "Eb",
    "E#": "F",
    "Gb": "F#",
    "Db": "C#",
    "Ab": "G#",
    "Cb": "B",
    "Fb": "E"
    }