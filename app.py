
from flask import Flask, render_template_string

app = Flask(__name__)

ITEMS = [
    {"id": 1, "name": "Python Programming", "category": "Technology", "rating": 4.8, "price": 499},
    {"id": 2, "name": "Web Development", "category": "Technology", "rating": 4.6, "price": 699},
    {"id": 3, "name": "Machine Learning", "category": "AI", "rating": 4.9, "price": 999},
    {"id": 4, "name": "Data Science", "category": "AI", "rating": 4.7, "price": 799},
    {"id": 5, "name": "UI/UX Design", "category": "Design", "rating": 4.5, "price": 599},
]


@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Recommendation System - v1</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 0 20px;
                background: #f5f7fa;
                color: #222;
            }
            h1 { color: #173b65; }
            .version { color: #555; margin-bottom: 24px; }
            .item {
                background: white;
                padding: 18px;
                margin-bottom: 12px;
                border-radius: 8px;
                border: 1px solid #ddd;
            }
            .details { color: #555; }
        </style>
    </head>
    <body>
        <h1>Recommendation System</h1>
        <p class="version">Version 1 — Show List</p>
        <h2>Available Items</h2>
        {% for item in items %}
        <div class="item">
            <h3>{{ item.name }}</h3>
            <p class="details">
                Category: {{ item.category }} |
                Rating: {{ item.rating }}/5 |
                Price: ₹{{ item.price }}
            </p>
        </div>
        {% endfor %}
        <p>Total items: {{ items|length }}</p>
    </body>
    </html>
    """
    return render_template_string(html, items=ITEMS)


@app.route("/api/health")
def health():
    return {"application": "recommendation-system", "version": "v1", "status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
