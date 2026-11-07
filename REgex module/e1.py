"""
 python REgex module/e1.py
Reagex or Regular expressions are pattern searching method to analyze a given
 pattern and python have a built in re module for this 
 """
import re

text = "Contact me at rahul.sharma@gmail.com today."

# We use parentheses () to split the email into two specific groups:
# Group 1: The username (rahul.sharma)
# Group 2: The domain (gmail.com)
pattern = r"([a-zA-Z.]+)\@([a-zA-Z.]+)"

match = re.search(pattern, text)

if match:
    # group() or group(0) returns the ENTIRE matched string
    print("Full match:", match.group())       
    # Output: rahul.sharma@gmail.com

    # group(1) returns only what was caught in the FIRST set of parentheses
    print("Username only:", match.group(1))   
    # Output: rahul.sharma

    # group(2) returns only what was caught in the SECOND set of parentheses
    print("Domain only:", match.group(2))     
    # Output: gmail.com