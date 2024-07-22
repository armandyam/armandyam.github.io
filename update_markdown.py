import os
import glob
import re

def replace_always_with_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the regex pattern to find 'always' and its replacement with the target attribute
    pattern = r'\b(always)\b'
    replacement_pattern = r'[\1](https://tenor.com/view/always-severus-snape-harry-potter-alan-rickman-gif-17624951){:target="_blank"}'

    # Check if 'always' is already a hyperlink
    if re.search(r'\[always\]\(https://tenor.com/view/always-severus-snape-harry-potter-alan-rickman-gif-17624951\)\{:target="_blank"\}', content, re.IGNORECASE):
        return

    # Replace 'always' with the hyperlink and target attribute, ignoring case
    updated_content = re.sub(pattern, replacement_pattern, content, flags=re.IGNORECASE)

    # Check if the content has changed
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        print(f'Updated {file_path}')

def main():
    folders = ["_posts/*.md", "_portfolio/*.md"]  # Add more paths as needed

    for folder in folders:
        for file_path in glob.glob(folder):
            replace_always_with_link(file_path)

if __name__ == "__main__":
    main()
