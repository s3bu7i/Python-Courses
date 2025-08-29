<?php
require __DIR__ . '/../vendor/autoload.php';

use App\Calculator;

$calc = new Calculator();

echo "Testing Calculator...\n";
echo "2 + 3 = " . $calc->add(2, 3) . "\n";
echo "4 × 5 = " . $calc->multiply(4, 5) . "\n";
