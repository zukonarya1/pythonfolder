import re
import os # Import the os module to handle file paths

def clean_protein_sequence(raw_data):
    """
    Cleans a raw protein sequence string by removing metadata, numbers,
    and whitespace using regular expressions.

    Args:
        raw_data (str): The multiline string containing the sequence data.

    Returns:
        str: The cleaned protein sequence, containing only amino acid characters.
    """
    # This single regex pattern does all the cleaning steps at once:
    # - "ORIGIN"      -> Matches the word ORIGIN
    # - \d+           -> Matches one or more digits (the numbers)
    # - \s+           -> Matches one or more whitespace characters (spaces, newlines, etc.)
    # - \/\/          -> Matches the two forward slashes (slashes are special characters in regex, so they must be escaped)
    # The | character acts as an "OR", so it removes any of these patterns.
    pattern = r"ORIGIN|\d+|\s+|//"
    
    # Use re.sub() to find all matches for the pattern and replace them with an empty string.
    cleaned_sequence = re.sub(pattern, "", raw_data)
    
    return cleaned_sequence

# --- Main Execution ---
if __name__ == "__main__":
    # Get the file path from the user.
    input_filepath = input("Please enter the path to the sequence file you want to clean: ")

    try:
        # Open and read the entire content of the user-provided file.
        with open(input_filepath, 'r', encoding='utf-8') as file:
            input_data = file.read()

        # Get just the filename for cleaner output messages
        filename = os.path.basename(input_filepath)
        print(f"\n--- Starting Cleaning Process for '{filename}' ---")

        # Use the existing function to clean the data read from the file.
        final_sequence = clean_protein_sequence(input_data)

        if final_sequence:
            print(f"Cleaned Sequence: {final_sequence}")
            print("-" * 30)

            # Programmatically confirm the final character count.
            final_length = len(final_sequence)

            print(f"Final Character Count: {final_length}")
            print(f"✅ Success: File cleaned successfully.")
        else:
            print(f"-> Warning: The file '{filename}' did not contain any sequence data after cleaning.")

    except FileNotFoundError:
        print(f"❌ Error: The file at '{input_filepath}' was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

