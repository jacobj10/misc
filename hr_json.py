y = ({
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
})

z = ({"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}})

def recursive_print(current_loc, indents=0, is_list=False, test_list=[]):
	for thing in current_loc:
		if is_list:
			current = thing
			thing = ''
		else:
			current = current_loc[thing]
			thing += ': '
		if isinstance(current, dict):
			test_list.append(' ' * indents + thing)
			recursive_print(current, indents + 3, test_list = test_list)
		elif isinstance(current, list):
			test_list.append(' ' * indents + thing)
			recursive_print(current, indents + 3, True, test_list = test_list)
		else:
			test_list.append(' ' * indents + thing + str(current))

def return_recursive_string(json):
	temp_list = []
	recursive_print(json, test_list = temp_list)
	return '\n'.join(temp_list)

print(return_recursive_string(y))
