import unittest

import transpose

class TestNote(unittest.TestCase):
    def test_str(self):
        n = transpose.Note("A", False, 0)
        self.assertEqual(str(n), "A0")
        n = transpose.Note("A", True, 0)
        self.assertEqual(str(n), "A#0")

    def test_pitch(self):
        # See table of note frequencies: https://en.wikipedia.org/wiki/Scientific_pitch_notation
        n = transpose.Note("C", False, 0)
        self.assertEqual(n.pitch, 12)
        n = transpose.Note("A", False, 0)
        self.assertEqual(n.pitch, 21)
        n = transpose.Note("G", True, 1)
        self.assertEqual(n.pitch, 32)
        n = transpose.Note("F", True, 4)
        self.assertEqual(n.pitch, 66)
        n = transpose.Note("D", False, 6)
        self.assertEqual(n.pitch, 86)
        n = transpose.Note("E", False, 8)
        self.assertEqual(n.pitch, 112)

    def test_note(self):
        # Previous function in reverse
        n = transpose.Note("C", False, 0)
        n.pitch = 12
        n.update_note()
        self.assertEqual(str(n), "C0")
        n.pitch = 21
        n.update_note()
        self.assertEqual(str(n), "A0")
        n.pitch = 32
        n.update_note()
        self.assertEqual(str(n), "G#1")
        n.pitch = 66
        n.update_note()
        self.assertEqual(str(n), "F#4")
        n.pitch = 86
        n.update_note()
        self.assertEqual(str(n), "D6")
        n.pitch = 112
        n.update_note()
        self.assertEqual(str(n), "E8")

    def test_transpose(self):
        n = transpose.Note("C", False, 0)
        n.transpose(9)
        self.assertEqual(str(n), "A0")
        n.transpose(11)
        self.assertEqual(str(n), "G#1")
        n.transpose(80)
        self.assertEqual(str(n), "E8")
        n.transpose(-26)
        self.assertEqual(str(n), "D6")
        n.transpose(-20)
        self.assertEqual(str(n), "F#4")
        n.transpose(0)
        self.assertEqual(str(n), "F#4")

    def test_invalid_octave(self):
        with self.assertRaises(ValueError):
            transpose.Note("A", True, 11)
        with self.assertRaises(ValueError):
            transpose.Note("A", True, -1)

    def test_invalid_sharp(self):
        with self.assertRaises(ValueError):
            transpose.Note("E", True, 2)
        with self.assertRaises(ValueError):
            transpose.Note("B", True, 2)

    def test_invalid_text(self):
        with self.assertRaises(ValueError):
            transpose.Note("J", True, 2)
        with self.assertRaises(ValueError):
            transpose.Note("", True, 2)
        with self.assertRaises(ValueError):
            transpose.Note("Better late than never", True, 2)

if __name__ == '__main__':
    unittest.main()