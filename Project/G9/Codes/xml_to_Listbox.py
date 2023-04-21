import tkinter as tk
import xml.etree.cElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Create a new Tkinter window
window = tk.Tk()

# Create a Listbox widget
listbox = tk.Listbox(window)

# Add the data from the XML file to the ListBox
for item in root.findall('item'):
    name = item.find('name').text
    listbox.insert(tk.END, name)

# Pack the Listbox into the window
listbox.pack()

# Run the main event loop
window.mainloop()


# if __name__ == '__main__':
#     xmlFile = input("Enter file name: ")
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-n', '--file', default=xmlFile+'.xml')
#     args = parser.parse_args()
#
#     parseTree = parsed
