from flask import Flask, jsonify, request
from pymongo import MongoClient
from rule_manager import RuleManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['rule_engine_db']
rule_collection = db['rules']

rule_manager = RuleManager()

@app.route('/api/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')
    if not rule_string:
        return jsonify({"error": "Rule string is required"}), 400
    try:
        rule_ast = rule_manager.create_rule(rule_string)
        rule_id = rule_collection.insert_one(rule_ast).inserted_id
        return jsonify({"message": "Rule created successfully", "rule_id": str(rule_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    
    if not rule_id or not data:
        return jsonify({"error": "rule_id and data are required"}), 400
    
    rule_ast = rule_collection.find_one({"_id": ObjectId(rule_id)})
    if not rule_ast:
        return jsonify({"error": "Rule not found"}), 404
    
    try:
        result = rule_manager.evaluate_rule(rule_ast, data)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
