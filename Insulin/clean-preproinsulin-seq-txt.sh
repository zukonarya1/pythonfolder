# 1. Use 'sed' to perform multiple find-and-replace operations to remove unwanted parts.
# 2. Pipe (|) the output of sed to 'tr -d' to delete all newline characters, joining the lines.
# 3. Store the result in a variable.
cleaned_sequence=$(sed 's/ORIGIN//g; s/[0-9]*//g; s/\/\///g' sequence.txt | tr -d '\n\r ')

# Print the cleaned sequence
echo "Cleaned Sequence: $cleaned_sequence"

# 4. Programmatically confirm the length using 'wc -c'.
char_count=$(echo -n "$cleaned_sequence" | wc -c)

echo "Final Character Count: $char_count"

# 5. Confirm if it matches 110.
if [ "$char_count" -eq 110 ]; then
    echo "✅ Confirmation: The final content has exactly 110 characters."
else
    echo "❌ Warning: The final content has $char_count characters, not 110."
fi

Both methods successfully clean the data and programmatically confirm the final length is exactly 110 characters. The Python solution is generally more readable and maintainable for more complex tasks.