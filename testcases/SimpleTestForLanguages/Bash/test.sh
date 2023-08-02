#!/bin/bash

factorial() {
  if [ "$1" -eq 0 ]; then
    return 1
  else
    return $(($1 * factorial $1 - 1))
  fi
}

fibonacci() {
  if [ "$1" -eq 0 ]; then
    return 0
  elif [ "$1" -eq 1 ]; then
    return 1
  else
    return $(fibonacci $(($1 - 1)) + fibonacci $(($1 - 2)))
  fi
}

echo "factorial(5) = $(factorial 5)"
echo "fibonacci(10) = $(fibonacci 10)"
