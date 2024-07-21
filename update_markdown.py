import os
import glob
import re

def replace_always_with_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the replacement pattern with the target="_blank" attribute
    replacement_pattern = r'[\1](https://media.gifdb.com/severus-snape-always-7uaebm4cohnfo0a6.gif){:target="_blank"}'

    # Replace 'always' with the hyperlink and target attribute, ignoring case
    updated_content = re.sub(
        r'\b(always)\b',
        replacement_pattern,
        content,
        flags=re.IGNORECASE
    )

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
