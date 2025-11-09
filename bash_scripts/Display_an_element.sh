#Given a list of countries, each on a new line, your task is to read them into an array and then display the element indexed at 3. Note that indexing starts from 0.

#!/bin/bash

countries=(`cat`)

# Print the result

echo ${countries[2]}