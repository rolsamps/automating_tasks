#There are N integers in an array A. All but one integer occur in pairs. Your task is to find the number that occurs only once.
Output S, the number that occurs only once.

#!/bin/bash
read n
read -a a

# Declare an associative array to count occurrences
declare -A count

# Iterate over the array and count occurrences
for number in "${a[@]}"; do
  ((count["$number"]++))
done

# Print elements with multiple occurrences
for key in "${!count[@]}"; do
  if [ "${count[$key]}" -eq 1 ]; then
  s=$key
    
  fi
done

echo $s