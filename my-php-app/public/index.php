<?php
require __DIR__ . '/../vendor/autoload.php';

use App\Calculator;

$calc = new Calculator();

echo "<h1>PHP Default App</h1>";
echo "<p>2 + 3 = " . $calc->add(2, 3) . "</p>";
echo "<p>4 × 5 = " . $calc->multiply(4, 5) . "</p>";
