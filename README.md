# Transpose
A simple command line tool to transpose music phrases. 

## Installation and usage
Just clone the repository and run `python transpose.py [notes] [transpose_by]`

For example, if you want to play [this great song](https://www.youtube.com/watch?v=wVRbi-RowTA) with higher pitch (+5), you can run:
```
python transpose.py "A2 E3 A3 C4 A3 E3" 5
D3 A3 D4 F4 D4 A3
python transpose.py "F#2 D3 A3 C4 A3 D3" 5
B2 G3 D4 F4 D4 G3
python transpose.py "G2 D3 G3 B3 G3 D3 B3 G3 D3 B3 G3 D3" 5
C3 G3 C4 E4 C4 G3 E4 C4 G3 E4 C4 G3 
```

## History behind this micro project
I wanted to play a few melodies written for guitar on my ukulele, and I needed them transposed. I’m not good enough to transpose them on the fly, pen-and-paper approach is tedious, but I’m a programmer, am I not? So I sat down and came up with a simple and straightforward solution and I really enjoy the result. 
