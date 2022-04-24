#!/usr/bin/python
import os,xml.etree.ElementTree as ET

# Set up paths (global variables)
proj_dir = '../projects/'

# Function to insert cwd into paths in template init_data.xml
def mod_init_data_xml(template,modified):
        tree = ET.parse(template)
        root = tree.getroot()
        dir1 = root.find('project_dir')
        dir1.text=os.path.normpath(os.path.join(os.getcwd(),proj_dir))
        dir2 = root.find('boinc_dir')
        dir2.text = os.path.normpath(os.path.join(os.getcwd(),'../'))
        tree.write(modified)

# create init_data.xml with correct paths
mod_init_data_xml('init_data_template.xml','init_data.xml')
