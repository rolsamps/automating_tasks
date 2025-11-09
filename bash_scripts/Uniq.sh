#Given a text file, display only those lines which are not followed or preceded by identical replications.

#!/bin/bash

input=$(cat)

# Display only unique lines
output=$(echo "$input" | uniq -u)

# Print the result
echo "$output"