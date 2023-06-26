# RamachandranChecker
RamachandranChecker is a pymol script that uses machine learning to analyze the Ramachandran plot of any structure loaded into pymol



To use, one must first download RamachandranPymol.py, labels.txt, and Model.h5. Then, go in RamachandranPymol.py to lines 85 and 88.

`model = load_model("<REPLACE WITH PATH TO Model.h5>", compile=False)`

In 85, one should replace the text with the path to Model.h5.

`class_names = open("<REPLACE WITH PATH TO labels.txt>", "r").readlines()`

Likewise for 88. Then, you type in `run` followed by the pathname to RamachandranPymol.py in the pymol command line with your molecule of interest loaded like so:

`run <REPLACE WITH PATH TO RamachandranPymol.py>`

Then you will get your results.

NOTE: This model was made with Teachable Machine.
