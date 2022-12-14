from flask import Flask,jsonify,request

app = Flask(__name__)

tasks= [
    {
        "id" :1,
        "title":"wake up",
        "discription":"Wake up from sleeping",
        "done":False
    },
    {
         "id" :2,
        "title":"Brush Teeth",
        "discription":"Brush your teeth",
        "done":False
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the Data",
        },400)
    
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "discription":request.json.get("discription",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"succses",
        "message":"task added Succsesfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

    
@app.route("/")
def hello_world():
    return "hello world"

if(__name__=="__main__"):
    app.run(debug=True)