
from flask import Flask, request, render_template_string

app = Flask(__name__)

ITEMS = [
    {"id": 1, "name": "Python Programming", "category": "Technology", "rating": 4.8, "price": 499},
    {"id": 2, "name": "Web Development", "category": "Technology", "rating": 4.6, "price": 699},
    {"id": 3, "name": "Machine Learning", "category": "AI", "rating": 4.9, "price": 999},
    {"id": 4, "name": "Data Science", "category": "AI", "rating": 4.7, "price": 799},
    {"id": 5, "name": "UI/UX Design", "category": "Design", "rating": 4.5, "price": 599},
]

CATEGORIES = ["Technology", "AI", "Design"]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Recommendation System - v2</title>
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
        .version { color: #555; }
        .filter {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 18px;
            margin: 24px 0;
        }
        select, button {
            padding: 10px;
            margin-top: 8px;
            font-size: 15px;
        }
        button {
            background: #173b65;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
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
    <p class="version">Version 2 — Filter Items by Category</p>

    <form class="filter" method="GET" action="/">
        <label for="category"><strong>Choose a category:</strong></label>
        <br>
        <select name="category" id="category">
            <option value="All"
                {% if selected == "All" %}selected{% endif %}>
                All Categories
            </option>
            {% for category in categories %}
            <option value="{{ category }}"
                {% if selected == category %}selected{% endif %}>
                {{ category }}
            </option>
            {% endfor %}
        </select>
        <button type="submit">Apply Filter</button>
    </form>

    <h2>Recommended Items</h2>

    {% for item in items %}
    <div class="item">
        <h3>{{ item.name }}</h3>
        <p class="details">
            Category: {{ item.category }} |
            Rating: {{ item.rating }}/5 |
            Price: ₹{{ item.price }}
        </p>
    </div>
    {% else %}
    <p>No items found for this category.</p>
    {% endfor %}

    <p>Total items displayed: {{ items|length }}</p>
</body>
</html>
"""


@app.route("/")
def home():
    selected = request.args.get("category", "All").strip()

    if selected not in ["All"] + CATEGORIES:
        selected = "All"

    if selected == "All":
        filtered_items = ITEMS
    else:
        filtered_items = [
            item for item in ITEMS
            if item["category"] == selected
        ]

    return render_template_string(
        PAGE,
        items=filtered_items,
        categories=CATEGORIES,
        selected=selected,
    )


@app.route("/api/health")
def health():
    return {
        "application": "recommendation-system",
        "version": "v2",
        "status": "healthy",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
