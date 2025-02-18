import csv
import os
import sys


def find_image_in_folder(folder_path):
    """
    Given a folder path, return the path of the first file that is not a JSON file.
    """
    if not os.path.isdir(folder_path):
        return None
    for fname in os.listdir(folder_path):
        # Skip json files; assume the first non-JSON (e.g., .png, .jpg) is the image
        if not fname.lower().endswith(".json"):
            return os.path.join(folder_path, fname)
    return None


def generate_markdown_report(csv_file, output_md):
    """
    Reads the experiment CSV and writes a Markdown report.
    Each experiment reports its category, query, and image.
    If there's an error, the error message is shown as well.
    """
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        report_lines = []
        experiment_number = 1

        for row in reader:
            category = row.get("category", "N/A")
            query = row.get("query", "N/A")
            folder_path = row.get("file_path", "").strip()
            error_log = row.get("error_log", "").strip()

            # Look for the image in the folder path.
            image_path = find_image_in_folder(folder_path)

            # Write a header for this experiment
            report_lines.append(f"## Experiment {experiment_number}")
            report_lines.append("")
            report_lines.append(f"**Category:** {category}")
            report_lines.append("")
            report_lines.append(f"**Query:** {query}")
            report_lines.append("")

            if image_path:
                # Embedding the image using Markdown syntax.
                report_lines.append(f"![Experiment {experiment_number}]({image_path})")
            else:
                report_lines.append("_No image found._")
            report_lines.append("")

            if error_log:
                report_lines.append("**Error Log:**")
                report_lines.append("```")
                report_lines.append(error_log)
                report_lines.append("```")
                report_lines.append("")

            # add a horizontal rule for clarity between experiments
            report_lines.append("---")
            report_lines.append("")

            experiment_number += 1

    # Write all the lines into the Markdown file.
    with open(output_md, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(report_lines))
    print(f"Report generated and saved to {output_md}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_report.py <input_csv> <output_md>")
        sys.exit(1)

    csv_file = sys.argv[1]
    output_md = sys.argv[2]
    generate_markdown_report(csv_file, output_md)
