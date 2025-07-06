import os
import re

def parse_legacy_md(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Split content by date headers
    weeks = re.split(r'\*\*(\d{4}-\d{2}-\d{2})\*\*', content)[1:]

    # Group dates with their content
    weeks_dict = {weeks[i]: weeks[i+1].strip() for i in range(0, len(weeks), 2)}

    return weeks_dict

def fix_heading_levels(content):
    """Fix heading levels to start at h2 and remove extra date headers"""
    # Remove h1 date headers and preceding separator lines
    content = re.sub(r'\n---\n\n# \d{4}-\d{2}-\d{2}\n\n', '\n\n', content)
    content = re.sub(r'^---\n\n# \d{4}-\d{2}-\d{2}\n\n', '', content)
    content = re.sub(r'\n# \d{4}-\d{2}-\d{2}\n\n', '\n\n', content)

    # Convert h4 to h3, h3 to h2 (in reverse order to avoid conflicts)
    content = re.sub(r'^#### ', '### ', content, flags=re.MULTILINE)
    content = re.sub(r'^### ', '## ', content, flags=re.MULTILINE)

    return content.strip()

def split_multiple_dates(content):
    """Split content that contains multiple dates into separate entries"""
    # Look for h1 date headers within the content
    date_splits = re.split(r'\n---\n\n# (\d{4}-\d{2}-\d{2})\n\n', content)

    if len(date_splits) == 1:
        # No additional dates found
        return {None: content}

    # First part is the main content, then alternating dates and content
    result = {None: date_splits[0].strip()}

    for i in range(1, len(date_splits), 2):
        if i + 1 < len(date_splits):
            date = date_splits[i]
            date_content = date_splits[i + 1].strip()
            result[date] = date_content

    return result

def create_week_folders(weeks_dict):
    base_path = 'content/weeks'

    for date, content in weeks_dict.items():
        # Split content if it contains multiple dates
        date_splits = split_multiple_dates(content)

        for split_date, split_content in date_splits.items():
            # Use the original date if no split date, otherwise use the split date
            actual_date = split_date if split_date else date
            week_path = os.path.join(base_path, actual_date)
            index_path = os.path.join(week_path, 'index.md')

            # Fix heading levels in content
            fixed_content = fix_heading_levels(split_content)

            # Always create/overwrite to fix heading levels
            if not os.path.exists(week_path):
                os.makedirs(week_path)

            # Create index.md with front matter and fixed content
            with open(index_path, 'w') as f:
                f.write(f'---\ndate: {actual_date}\n---\n\n{fixed_content}')
            print(f'Created/updated folder and index.md for {actual_date}')

weeks = parse_legacy_md('legacy.md')
create_week_folders(weeks)
