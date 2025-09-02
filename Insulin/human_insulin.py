import os

def extract_insulin_chains(preproinsulin_sequence):
    """
    Extracts the A and B chains of the mature insulin molecule from a
    full preproinsulin amino acid sequence.

    Args:
        preproinsulin_sequence (str): The clean 110-amino-acid sequence.

    Returns:
        tuple: A tuple containing the B chain, A chain, and the combined
               mature insulin sequence.
    """
    # In programming, indexing starts at 0. In biology, it starts at 1.
    # To get amino acids 25-54, we slice from index 24 up to (but not including) 54.
    lsinsulin = preproinsulin_sequence[0:23]
    binsulin = preproinsulin_sequence[24:53]
    
    # To get amino acids 90-110, we slice from index 89 up to (but not including) 110.
    cinsulin = preproinsulin_sequence[54:88]
    ainsulin = preproinsulin_sequence[89:110]
    
    # The final insulin molecule is the combination of these two chains.
    # In the body, they are linked by disulfide bonds, but for sequence
    # purposes, we can concatenate them.
    mature_insulin_sequence = lsinsulin + binsulin + cinsulin + ainsulin
    
    return lsinsulin, binsulin, cinsulin, ainsulin, mature_insulin_sequence

# --- Main Execution ---
if __name__ == "__main__":
    # Get the file path from the user.
    input_filepath = input("Please enter the path to the clean preproinsulin sequence file: ")

    try:
        with open(input_filepath, 'r') as file:
            # Read the sequence and remove any leading/trailing whitespace or newlines
            full_sequence = file.read().strip()

        # Proceed only if the file was not empty
        if full_sequence:
            filename = os.path.basename(input_filepath)
            print(f"\n--- Processing sequence from '{filename}' ---")
            
            # Optional: Validate the length of the sequence from the file
            if len(full_sequence) != 110:
                print(f"⚠️  Warning: The input sequence has {len(full_sequence)} characters, not the expected 110.")
                print("    Slicing will proceed, but results may be incorrect if this is not preproinsulin.")

            print(f"\nStarting with Preproinsulin (Length: {len(full_sequence)}aa)")
            print("-" * 50)

            b_chain, a_chain, final_insulin = extract_insulin_chains(full_sequence)

            print(f"B Chain (aa 25-54):  {b_chain} (Length: {len(b_chain)}aa)")
            print(f"A Chain (aa 90-110):  {a_chain} (Length: {len(a_chain)}aa)")
            
            print("-" * 50)
            print("Final Processed Insulin Molecule (B-Chain + A-Chain):")
            print(final_insulin)
            print(f"Total Length: {len(final_insulin)}aa")
        else:
            print(f"❌ Error: The file '{input_filepath}' is empty or contains only whitespace.")

    except FileNotFoundError:
        print(f"❌ Error: The file at '{input_filepath}' was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

