#!/bin/bash

factorial() {
  if [ "$1" -eq 0 ]; then
    echo 1
  else
    local prev=$(factorial $(($1 - 1)))
    echo $(($1 * prev))
  fi
}

fibonacci() {
  if [ "$1" -eq 0 ]; then
    echo 0
  elif [ "$1" -eq 1 ]; then
    echo 1
  else
    local prev1=$(fibonacci $(($1 - 1)))
    local prev2=$(fibonacci $(($1 - 2)))
    echo $(($prev1 + $prev2))
  fi
}

echo "factorial(5) = $(factorial 5)"
echo "fibonacci(10) = $(fibonacci 10)"
