from flask import Blueprint, render_template, request, url_for
from file_data import file_keywords

search_bp = Blueprint('search', __name__)

@search_bp.route('/')
def search():
    query = request.args.get("q","").lower()
    results = []

    for filename, keywords in file_keywords.items():
        for keyword in keywords:
            if query in keyword.lower():
                image_url = url_for( "static",filename=f'uploads/{filename}')
                results.append(image_url)

    # return jsonify({"url": results})
    return render_template("results.html", query=query, results=results)