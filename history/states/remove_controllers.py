import os

def process_txt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        # Remove lines containing "add_claim_by" or "add_core_of"
        if "add_claim_by" not in line and "add_core_of" not in line:
            # Replace lines containing "owner =" with "		owner = ZZZ"
            if "owner =" in line:
                line = "		owner = ZZZ\n"
            new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def main():
    current_directory = os.getcwd()
    txt_files = [file for file in os.listdir(current_directory) if file.endswith(".txt")]

    for txt_file in txt_files:
        file_path = os.path.join(current_directory, txt_file)
        process_txt_file(file_path)
        print(f"Processed {txt_file}")

if __name__ == "__main__":
    main()