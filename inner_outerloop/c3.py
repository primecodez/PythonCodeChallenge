##python inner_outerloop/c3.py
"""This is a more improved and effiecient version for c2.py file as:
    Optimized C implementation: Python's string repetition operator (*) is 
    executed in highly optimized C code under the hood.
      It instantly allocates the exact memory needed and builds the entire string in one step.
     In contrast, a Python for loop evaluates line-by-line with higher runtime overhead.
     Function call overhead: The nested loop method calls the print() function multiple times per row.
     Function calls in Python are relatively expensive and slow down execution. 
     The string multiplication method calls print() exactly once per row.
     Fewer loop iterations: The nested loop method requires $O(N^2)$ Python-level iterations to complete 
     the pattern. The multiplication method handles the inner repetition natively, 
     requiring only $O(N)$ Python-level loop iterations.
"""

rows = int(input("Enter number of rows:"))

for i in range(1, rows + 1):
    # Left right-angled triangle (straight vertical on the far left)
    left_part = "hi " * i
    
    # Middle gap (shrinks as the triangles get wider)
    gap = "   " * (rows - i)
    
    # Right right-angled triangle (straight vertical on the far right)
    right_leading_spaces = "   " * (rows - i)
    right_part = right_leading_spaces + "hi " * i
    
    print(left_part + gap + right_part)