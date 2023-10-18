E-SpotFinder
===
E-SpotFinder is a machine-learning algorithm for identifying tissue or cell-specific eQTL hotspots based on sequence and epigenomic features. It was constructed using pan-tissue eQTL hotspots derived through a non-homogeneous Poisson Process.

Input file
===
Feature matrix
Feature matrix contains 396 k-mer, GC contant and 9 epigenetic marks. An example of Feature matrix format is Example_input.txt.gz.

Running E-SpotFinder
===
The syntax looks like: 

    python E-SpotFinder.py <input_feature_matrix> 

Examples
===
To run a standard E-SpotFinder experiment on a simple example, run these commands:

    git clone git@github.com:Lhhuan/E-SpotFinder.git
    
    cd E-SpotFinder
    
    python E-SpotFinder.py Example_input.txt.gz
    
Required modules
===

Python: 3.9.12

    pandas: 1.2.5

    numpy: 1.20.3

    pickle: 4.0
    
    xgboost: 1.5.0

