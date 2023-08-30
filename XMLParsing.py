def clean_xml_file(input_file, output_file):
    with open(input_file, 'r') as file:
        xml_data = file.read()

    # Replace specific entities
    xml_data = xml_data.replace('&amp;', '')
    xml_data = xml_data.replace('&lt;', '')
    xml_data = xml_data.replace('&gt;', '')
    xml_data = xml_data.replace('&quot;', '')
    xml_data = xml_data.replace('&apos;', "")
    xml_data = xml_data.replace('&', "")
    xml_data = xml_data.replace(';', "")
# Write the cleaned data to the output file
    with open(output_file, 'w') as file:
        file.write(xml_data)

# Specify the paths to your input and output XML files


input_xml_file = 'dblp.xml'
output_xml_file = 'output_cleaned.xml'

# Clean the XML file
clean_xml_file(input_xml_file, output_xml_file)

print("XML file cleaned and saved to", output_xml_file)
