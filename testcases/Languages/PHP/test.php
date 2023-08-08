<?php
// PHP test case

function factorial($n) {
    if ($n == 0) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

function sumOfSquares($n) {
    $sum = 0;
    for ($i = 1; $i <= $n; $i++) {
        $sum += $i * $i;
    }
    return $sum;
}

// Calculate factorial and sum of squares values
$number = 5;
$factorialResult = factorial($number);
$sumOfSquaresResult = sumOfSquares($number);

// Output results
echo "Factorial($number) = $factorialResult\n";
echo "Sum of Squares($number) = $sumOfSquaresResult\n";
?>
