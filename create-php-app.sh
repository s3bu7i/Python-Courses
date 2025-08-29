
#!/bin/bash

# Layihə adı
APP_NAME="my-php-app"

# Layihə qovluğunu yarat
mkdir -p $APP_NAME/{public,src,tests}

# composer.json faylı
cat > $APP_NAME/composer.json <<'EOL'
{
  "name": "my/php-app",
  "autoload": {
    "psr-4": {
      "App\\\": "src/"
    }
  }
}
EOL

# Calculator.php (src)
cat > $APP_NAME/src/Calculator.php <<'EOL'
<?php
namespace App;

class Calculator {
    public function add($a, $b) {
        return $a + $b;
    }

    public function multiply($a, $b) {
        return $a * $b;
    }
}
EOL

# index.php (public)
cat > $APP_NAME/public/index.php <<'EOL'
<?php
require __DIR__ . '/../vendor/autoload.php';

use App\Calculator;

$calc = new Calculator();

echo "<h1>PHP Default App</h1>";
echo "<p>2 + 3 = " . $calc->add(2, 3) . "</p>";
echo "<p>4 × 5 = " . $calc->multiply(4, 5) . "</p>";
EOL

# test_calculator.php (tests)
cat > $APP_NAME/tests/test_calculator.php <<'EOL'
<?php
require __DIR__ . '/../vendor/autoload.php';

use App\Calculator;

$calc = new Calculator();

echo "Testing Calculator...\n";
echo "2 + 3 = " . $calc->add(2, 3) . "\n";
echo "4 × 5 = " . $calc->multiply(4, 5) . "\n";
EOL

echo "✅ PHP app strukturu yaradıldı: $APP_NAME"
echo "👉 İndi bu əmrləri işlət:"
echo "   cd $APP_NAME"
echo "   composer install"
echo "   composer dump-autoload"
echo "   php -S localhost:8000 -t public"
