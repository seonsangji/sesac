from flask import Flask, jsonify, url_for, render_template, request


app = Flask(__name__)

food_images = [
    {"filename":"January.jpg", "keywords" : ["food","healthy"]},
    {"filename":"July.png", "keywords" : ["food","fruit","sweet","bitter"]},
    {"filename":"June.jpg", "keywords" : ["food","crop","sweet","healthy"]},
    {"filename":"May.jpg", "keywords" : ["food","fruit","bitter"]},
    {"filename":"october.jpg", "keywords" : ["food","fruit","sweet"]},
    {"filename":"September.jpg", "keywords" : ["food","fruit","sweet"]}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q","").lower()
    results = []

    for i in food_images:
        found = False
        for keyword in i["keywords"]:
            if query in keyword:
                found = True

        if found:
            image_url = url_for('static', filename=f'img/{i["filename"]}')
            results.append(image_url)

    # return jsonify({"url": results})
    return render_template("results.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)