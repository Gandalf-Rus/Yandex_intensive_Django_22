import sys
import requests

terminal = sys.argv[1:]
host = None
port = None
plants = []
height = 200
name = "a"

for i in range(len(terminal)):
    if "--height" == terminal[i]:
        height = int(terminal[i + 1])

    elif "--name" == terminal[i]:
        name = terminal[i + 1]

    elif i == 0:
        host = terminal[i]
    elif i == 1:
        port = terminal[i]
    else:
        plants.append(terminal[i])


response = requests.get(f"http://{host}:{port}")
if not response:
    print("error")
    pass
json_response = response.json()

new_json = {}

for obj in json_response:
    if obj["kind"] in plants:
        if obj["height"] <= height:
            if name in obj["name"]:
                if obj["kind"] in new_json.keys():
                    new_json[obj["kind"]].append([obj["name"], obj["hardiness"]])
                else:
                    new_json[obj["kind"]] = [[obj["name"], obj["hardiness"]]]

for key in new_json.keys():
    new_json[key] = sorted(new_json[key], key=lambda x: (-x[1], x[0]))

with open("tundra.json", "w") as file:
    file.write(f"{new_json}")
# python ex_3.py 127.0.0.1 5000 grass tree --height 82