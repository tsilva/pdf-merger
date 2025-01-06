import os
import argparse
import logging
import re
from collections import defaultdict
import pikepdf
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_base_name(filename):
    # Remove common suffix patterns like "- 1", "- 2", " (1)", etc.
    return re.sub(r'[-_ ]+\d+$', '', os.path.splitext(filename)[0])

def group_similar_pdfs(directory):
    groups = defaultdict(list)
    for file in os.listdir(directory):
        if file.lower().endswith('.pdf'):
            base_name = get_base_name(file)
            groups[base_name].append(file)
    
    # Only return groups with multiple files
    return {k: sorted(v) for k, v in groups.items() if len(v) > 1}

def merge_pdfs(input_files, output_path):
    try:
        pdf = pikepdf.new()
        for input_file in input_files:
            src = pikepdf.open(input_file)
            pdf.pages.extend(src.pages)
        
        pdf.save(output_path)
        return True
    except Exception as e:
        logger.error(f"Failed to merge PDFs: {e}")
        return False

def process_pdf_group(directory, base_name, files):
    output_path = os.path.join(directory, f"{base_name}.merged.pdf")
    
    if os.path.exists(output_path):
        logger.info(f"Skipping '{base_name}': merged version already exists")
        return False

    logger.info(f"\nFound potentially related PDFs for '{base_name}':")
    for idx, file in enumerate(files, 1):
        logger.info(f"  {idx}. {file}")
    
    if input("\nWould you like to merge these files? [Y/n]: ").lower() in ['n', 'no']:
        logger.info("Skipping merge at user request")
        return False

    input_files = [os.path.join(directory, f) for f in files]
    
    logger.info(f"Merging files into: {os.path.basename(output_path)}")
    if merge_pdfs(input_files, output_path):
        logger.info("Merge completed successfully")
        return True
    return False

def batch_merge_pdfs(input_dir):
    pdf_groups = group_similar_pdfs(input_dir)
    
    if not pdf_groups:
        logger.info("No PDF files found that need merging")
        return

    with tqdm(pdf_groups.items(), desc="Processing PDF groups", unit="group") as pbar:
        for base_name, files in pbar:
            pbar.set_postfix_str(base_name)
            process_pdf_group(input_dir, base_name, files)

def main():
    parser = argparse.ArgumentParser(description='Batch merge related PDF files')
    parser.add_argument('input_dir', help='Directory containing PDF files to merge')
    batch_merge_pdfs(parser.parse_args().input_dir)

if __name__ == "__main__":
    main()
