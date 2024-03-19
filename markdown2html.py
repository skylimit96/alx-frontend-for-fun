#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''

import sys
import os
import markdown

def convert_markdown_to_html(md_file, output_file):
    try:
        # Check if Markdown file exists
        if not os.path.exists(md_file):
            print(f"Missing {md_file}", file=sys.stderr)
            sys.exit(1)

        # Convert Markdown to HTML
        with open(md_file, 'r') as f:
            markdown_content = f.read()
            html_content = markdown.markdown(markdown_content)

        # Write HTML content to output file
        with open(output_file, 'w') as f:
            f.write(html_content)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <MarkdownFile> <OutputFile>", file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(md_file, output_file)
    sys.exit(0)
