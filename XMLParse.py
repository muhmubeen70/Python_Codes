import re
import xml.etree.ElementTree as ET


def preprocess_xml(xml_content):
    # Replace special characters with white spaces
    xml_content = re.sub(r'&;', '', xml_content)
    return xml_content


def split_into_chunks(file_path, chunk_size):
    chunks = []
    current_chunk = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            current_chunk += line
            if line.strip() == "</article>":  # Replace with your root element
                chunks.append(current_chunk)
                current_chunk = ""
    return chunks


def process_chunk(chunk):
    root = ET.fromstring(chunk)
    for element in root:
        print(f"{element.tag}: {element.text}")


def main():
    xml_file_path = 'dblp.xml'
    chunk_size = 10000  # Adjust this based on your system's memory capacity

    with open(xml_file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    preprocessed_xml = preprocess_xml(xml_content)
    chunks = split_into_chunks(xml_file_path, chunk_size)

    for chunk in chunks:
        process_chunk(chunk)


if __name__ == "__main__":
    main()
