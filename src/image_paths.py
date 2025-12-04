import os
import re
import sys

BASE_PATH = os.getcwd()

def fix_image_path(image_ref: str) -> str:
    sections = image_ref.split('/')
    if sections[0] == '..':
        return os.path.join(BASE_PATH, *sections[1:])
    else:
        return image_ref

def fix_images(file: str) -> None:
    folder = 'markdowns'
    pattern2 = r'!\[[^\]]*\]\(\.\./[^\)]+\)'
    patternx = r'!\[.*\]\((.*)\)'
    pattern = r'!\[.*?\]\((.*?)\)'
    
    with open(file, 'r') as f:
        content = f.read()
    image_refs = re.findall( pattern, content)
    for image_ref in image_refs:
        fixed_path = fix_image_path(image_ref)
        content = content.replace(image_ref, fixed_path)
    with open(file, 'w') as f:
        f.write(content)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python image_paths.py markdown_file')
        sys.exit(1)

    markdown_file = sys.argv[1]
    fix_images(markdown_file)
            
