import re
import sys
from pathlib import Path

def update_version(new_version):
    # 更新 __init__.py
    init_file = Path('spsspro/__init__.py')
    content = init_file.read_text(encoding='utf-8')
    content = re.sub(r"__version__ = '[^']+'", f"__version__ = '{new_version}'", content)
    init_file.write_text(content, encoding='utf-8')

    # 更新 setup.py
    setup_file = Path('setup.py')
    content = setup_file.read_text(encoding='utf-8')
    content = re.sub(r'version="[^"]+"', f'version="{new_version}"', content)
    setup_file.write_text(content, encoding='utf-8')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python bump_version.py NEW_VERSION')
        sys.exit(1)
    
    new_version = sys.argv[1]
    update_version(new_version)
    print(f'Version updated to {new_version}')