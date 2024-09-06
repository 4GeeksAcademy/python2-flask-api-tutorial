from flask import Flask, jsonify, request , abort
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    if not request.json or 'label' not in request.json or 'done' not in request.json:
        abort(400) 

    new_todo = {
        'done': request.json['done'],
        'label': request.json['label']
    }
    todos.append(new_todo)
    return jsonify(todos), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        abort(404)  

    del todos[position]
    return jsonify(todos), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)