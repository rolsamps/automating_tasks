#In this challenge, we practice reading and transforming arrays. 
#You are given a list of countries, each on a new line. Your task is to read them into an array and then transform them in the following way:
#The first capital letter (if present) in each element of the array should be replaced with a dot ('.'). Then, display the entire array with a space between each country's names.

# Explanation:
#1. `[[ ${my_array[i]} =~ ^[A-Z] ]]`: Checks if the element starts with a capital letter.
#2. `${my_array[i]:1}`: Extracts the substring starting from the second character (index #1).
#3. `"."${my_array[i]:1}`: Prepends a `.` to the rest of the string.
#4. `for i in "${!my_array[@]}"`: Loops through the indices of the array to modify #elements in place.

#!/bin/bash

countries=(`cat`)

# Loop through the array and modify elements starting with a capital letter
for i in "${!countries[@]}"; do
  if [[ ${countries[i]} =~ ^[A-Z] ]]; then
    countries[i]=".${countries[i]:1}"
  fi
done

# Print the modified array
echo "${countries[@]}"