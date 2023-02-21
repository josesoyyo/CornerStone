import requests
import json


def download_text_from_json_links(text_json_file_dir, text_folder_dir):
    chunk_size = 2000
    with open(text_json_file_dir, 'r') as jb:
        documents_links = json.loads(jb.read())

    for n, document_link in enumerate(documents_links):
        print(f"[{n}]-[Starting KVT]-{document_link.split('/')[-1]}")
        document_pdf = requests.get(document_link, stream=True)
        with open(f"{text_folder_dir}/{document_link.split('/')[-1].split('.')[0]}.json", 'wb') as fd:
            for chunk in document_pdf.iter_content(chunk_size):
                fd.write(chunk)
                print(document_pdf)


def download_pdf_from_json_links(pdf_json_file_dir, pdf_folder_dir):
    chunk_size = 2000
    with open(pdf_json_file_dir, 'r') as jb:
        documents_links = json.loads(jb.read())

    for n, document_link in enumerate(documents_links):
        print(f"[{n}]-[Starting KVT]-{document_link.split('/')[-1]}")
        document_pdf = requests.get(document_link, stream=True)
        with open(f"{pdf_folder_dir}/{document_link.split('/')[-1].split('.')[0]}.pdf", 'wb') as fd:
            for chunk in document_pdf.iter_content(chunk_size):
                fd.write(chunk)
                print(document_pdf)

# Documentation
# download_text_from_json_links('<dir-of-json-file-containing-pdf-file-links>', ',folder-dir-where-you want-to save-text-data')
# download_pdf_from_json_links('<dir-of-json-file-containing-text-file-links>', ',folder-dir-where-you want-to save-pdf-data')

# Example
# download_text_from_json_links('data/text_data/MODETransportation_text_data_links.json', 'jsons/mode')
# download_pdf_from_json_links('data/raw_data/MODETransportation_documents_links.json', 'jsons/mode')
