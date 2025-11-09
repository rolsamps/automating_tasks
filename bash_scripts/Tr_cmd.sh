#Replace all sequences of multiple spaces with just one space.

#!/bin/bash

input=$(cat)

# Delete all lowercase characters
output=$(echo "$input" | tr -s ' ')

# Print the result
echo "$output"

