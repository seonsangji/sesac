from flask import Flask, jsonify, url_for
import random

app = Flask(__name__)

food_images = [
    "January.jpg",
    "July.png"
    "June.jpg",
    "May.jpg",
    "october.jpg",
    "September.jpg"
]

@app.route('/random-food')
def random_food():
    random_img = random.choice(food_images)
    # image_url = url_for('static', filename=f'img/{random_img}')
    image_url = url_for('static', filename=f'img/{random_img}', _external=True)
    return jsonify({"url": image_url})



if __name__ == "__main__":
    app.run(debug=True)