import re

text = "The cab number is KA 01 EG 9999, arriving now."

# \w{2} = 2 letters
# \s = 1 space
# \d{2} = 2 digits
pattern = r"\w{2}\s\d{2}\s\w{2}\s\d{4}"

match = re.search(pattern, text)
if match:
    print("Found vehicle:", match.group())
    # Output: Found vehicle: KA 01 EG 9999