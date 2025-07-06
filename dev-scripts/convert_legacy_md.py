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

def create_week_folders(weeks_dict):
    base_path = 'content/weeks'

    for date, content in weeks_dict.items():
        week_path = os.path.join(base_path, date)
        index_path = os.path.join(week_path, 'index.md')

        # Only create if folder doesn't exist
        if not os.path.exists(week_path):
            os.makedirs(week_path)

            # Create index.md with front matter and content
            with open(index_path, 'w') as f:
                f.write(f'---\ndate: {date}\n---\n\n{content}')
            print(f'Created folder and index.md for {date}')
        else:
            print(f'Folder {date} already exists, skipping')

weeks = parse_legacy_md('legacy.md')
create_week_folders(weeks)
