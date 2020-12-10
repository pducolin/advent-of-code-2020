#!/bin/bash
TODAY=$(date +"%d");
XMAS=$(date -d '20201225' +"%d");
if [[ "$TODAY" > "$XMAS" ]]; then
    echo "Xmas is over, so is AoC"
    exit 1
else
    echo "🎄 It's AoC day $TODAY, get ready to code 👩‍💻"
fi
# create code folder and placeholder files
mkdir -p src/day_"$TODAY";
touch src/day_"$TODAY"/input.txt;
touch src/day_"$TODAY"/main.py;
touch src/day_"$TODAY"/part_1.py;
touch src/day_"$TODAY"/part_2.py;
touch src/day_"$TODAY"/README.md;
# create test folder and placeholder files
mkdir -p src/tests/day_"$TODAY";
touch src/tests/day_"$TODAY"/__init__.py;
touch src/tests/day_"$TODAY"/test_part_1.py;
touch src/tests/day_"$TODAY"/test_part_2.py;