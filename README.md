# RamachandranChecker
RamachandranIndependent.py is a python script designed to take the phi and psi angles from pymol as an input.



To use, one must first download RamachandranIndependent.py, labels.txt, and Model.h5. Then, go in RamachandranPymol.py to lines 70 and 73.

`model = load_model("<REPLACE WITH PATH TO Model.h5>", compile=False)`

In 70, one should replace the text with the path to Model.h5.

`class_names = open("<REPLACE WITH PATH TO labels.txt>", "r").readlines()`

Likewise for 73. Then, you type in `phi_psi <REPLACE WITH NAME OF OBJECT OF INTEREST>`. This gives a list of numbers and three letter identifiers. Copy and paste this into the text at line 3, like so:
`Input = """<COPY AND PASTE PYMOL OUTPUT HERE>"""`
Then run the script to get results.

NOTE: This model was made with teachable machine.
