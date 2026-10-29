
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

SORT_OPTIONS = {
    "name_asc": ("Name (A-Z)", "name", False),
    "name_desc": ("Name (Z-A)", "name", True),
    "rating_desc": ("Rating (Highest first)", "rating", True),
    "rating_asc": ("Rating (Lowest first)", "rating", False),
    "price_asc": ("Price (Lowest first)", "price", False),
    "price_desc": ("Price (Highest first)", "price", True),
}

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Recommendation System - v3</title>
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
        .controls {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 18px;
            margin: 24px 0;
        }
        select, button {
            padding: 10px;
            margin: 8px 8px 0 0;
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
    <p class="version">Version 3 — Filter and Sort Results</p>

    <form class="controls" method="GET" action="/">
        <label for="category"><strong>Category:</strong></label><br>
        <select name="category" id="category">
            <option value="All"
                {% if selected_category == "All" %}selected{% endif %}>
                All Categories
            </option>
            {% for category in categories %}
            <option value="{{ category }}"
                {% if selected_category == category %}selected{% endif %}>
                {{ category }}
            </option>
            {% endfor %}
        </select>

        <br><br>

        <label for="sort"><strong>Sort by:</strong></label><br>
        <select name="sort" id="sort">
            {% for key, option in sort_options.items() %}
            <option value="{{ key }}"
                {% if selected_sort == key %}selected{% endif %}>
                {{ option[0] }}
            </option>
            {% endfor %}
        </select>

        <button type="submit">Apply</button>
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
    selected_category = request.args.get("category", "All").strip()
    selected_sort = request.args.get("sort", "name_asc").strip()

    if selected_category not in ["All"] + CATEGORIES:
        selected_category = "All"

    if selected_sort not in SORT_OPTIONS:
        selected_sort = "name_asc"

    if selected_category == "All":
        results = list(ITEMS)
    else:
        results = [
            item for item in ITEMS
            if item["category"] == selected_category
        ]

    _, sort_field, reverse = SORT_OPTIONS[selected_sort]
    results.sort(key=lambda item: item[sort_field], reverse=reverse)

    return render_template_string(
        PAGE,
        items=results,
        categories=CATEGORIES,
        sort_options=SORT_OPTIONS,
        selected_category=selected_category,
        selected_sort=selected_sort,
    )


@app.route("/api/health")
def health():
    return {
        "application": "recommendation-system",
        "version": "v3",
        "status": "healthy",
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
