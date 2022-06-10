import requests
import json

url = "https://pokeapi.co/api/v2/pokemon"
JSONContent = requests.get(url).json()
pokemon = json.dumps(JSONContent, indent = 4, sort_keys=True)
print(pokemon)

url2 = "https://pokeapi.co/api/v2/pokemon/3"
JSONContent = requests.get(url2).json()
pokemon3 = json.dumps(JSONContent, indent = 4, sort_keys=True)
print(pokemon3)


##best practices:
##1. Load all imports at the top of script
##2. Use same text naming convention all throughout(i.e. underscores, camelcase, snake case)
##3. When applicable, create appropriate doccumentation
##4. Use comments sparingle
##5. New lines for when code gets too long