# EC552_MARSBuilder_Project

Running LFR: https://github.com/CIDARLAB/pyLFR/tree/dev <br>
Running 3DuF: https://github.com/CIDARLAB/3DuF

## Pipelining Algorithm 
Requirements: Python3.8, networkx dependency, and dot dependency <br>

Each MARS device test cases includes pa.draw([name]) in the end. This is the function that generates a dot file. If only the first argument (name of the file) is passed, it will generate an unpipelined graph. If True is passed in as the second argument (i.e. `pa.draw(“ligation”, True)`), it will generate a pipelined graph using the algorithm. `python3 [file_name]` to run the program. 


## Guide Tool
Just click the index.html, then you can see the webpage, you will see the similar layout after you upload the design files from 3duf
