#Given an input file, in each line, highlight all the occurrences of 'thy' by wrapping them up in brace brackets. The search should be case-insensitive.

#!/bin/bash

input=$(cat)

# Remove repititions from the input
output=$(echo "$input" | sed -e 's/thy/{&}/Ig')

# Print the result
echo "$output"