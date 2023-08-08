#!/bin/bash
# Bash test case

add() {
    echo $(($1 + $2))
}

result=$(add 2 3)
echo "$result"  # Expected output: 5
