from pathlib import Path
import re
import os
import urllib.request as u

"""
Validates links from Markdown file
:return: If file exists or link is available returns True, else - False
:rtype: boolean
"""
    
INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
root_path = r"D:\Courses\BILab_2"

def find_md_links(md: str):
    """ Return dict of links in markdown """
    links = dict(INLINE_LINK_RE.findall(md))
    return links

def internet_on(url: str):
    """ Check that internet resource is available"""
    try:
        u.urlopen(url, timeout=1)
        return True
    except u.URLError as err: 
        return False

with open(r"D:\Courses\BILab_2\README.md", "r", encoding="UTF-8") as f:
    lines = "".join(f.readlines())
    md_links_dict = find_md_links(lines)
    for link in md_links_dict.values():
        # Validate that local file exists
        if not str(link).startswith("http"):
            link = str.replace(link, "%20", " ")
            link_path = Path(os.path.join(root_path, link))
            if not link_path.is_file():
                print(f"IS NOT FOUND: {link_path}")
        else:
            if not internet_on(link):
                print(f"IS NOT FOUND: {link}")
