"""PDF Gluer - Batch merge related PDF files in a directory."""

from pdf_gluer.core import (
    merge_pdfs,
    merge_all_pdfs,
    batch_merge_pdfs_grouped,
    get_base_name,
    group_similar_pdfs,
    main,
)

__all__ = [
    "merge_pdfs",
    "merge_all_pdfs",
    "batch_merge_pdfs_grouped",
    "get_base_name",
    "group_similar_pdfs",
    "main",
]
