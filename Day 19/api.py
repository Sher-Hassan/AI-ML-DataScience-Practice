### Put and Delete -- HTTP Verbs
### Working with API's -- Json

## Mini Project (To-do App)

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}

]

@app.route('/')
def home():
    return "Welcome To the Sample To Do List App"


## Get: Retrieve all the items

@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

## Get: Retrieve specific Item by Id

@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

## Post: Create a new task

@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']

    }
    items.append(new_item)
    return jsonify(new_item)


## Put: Update an existing item

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item["name"] = request.json.get("name", item["name"])  # First argument ('name'): The key you are looking for in the incoming JSON. Second argument (item['name']): The default value. This is what the method returns if the key 'name' is missing from the request.
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item)


# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)


# PUT (The "Update" Method)
# Purpose: Replaces an existing resource or creates it if it doesn’t exist.

# Behavior: It is idempotent, meaning if you send the exact same PUT request multiple times, the result on the server will always be the same as the first time.

# Analogy: Overwriting a file on your computer with a new version of the same file.

# DELETE (The "Remove" Method)
# Purpose: Permanently removes a specific resource from the server.

# Behavior: Like PUT, it is also idempotent. Once a resource is deleted, sending the request again won't change anything (it's already gone).

# Analogy: Moving a file to the trash and emptying it.