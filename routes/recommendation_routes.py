from flask import Blueprint, request, jsonify, render_template, session, redirect
from models import Laptop

from services.feature_engineering import builds_to_matrix, laptops_to_matrix
from services.clustering_service import cluster_builds, cluster_laptops
from services.gemini_service import generate_pc_explanation, generate_laptop_explanation
from services.build_generator import generate_pc_builds

recommendation_bp = Blueprint("recommendation", __name__)


# ================= LANGUAGE =================

@recommendation_bp.route("/set-language/<lang>")
def set_language(lang):
    if lang in ["en", "ta", "hi"]:
        session["lang"] = lang
    return redirect(request.referrer or "/")


# ================= LANDING =================

@recommendation_bp.route("/")
def landing():
    if "user" in session:
        return redirect("/category")
    return render_template("landing.html")


# ================= CATEGORY =================

@recommendation_bp.route("/category", methods=["GET", "POST"])
def category():

    if request.method == "POST":
        data = request.get_json()
        session["category"] = data["category"]
        return "", 204

    return render_template("category.html")


# ================= BUDGET =================

@recommendation_bp.route("/budget", methods=["POST"])
def budget():
    category = request.form.get("category")
    return render_template("budget.html", category=category)


# ================= USE CASE =================

@recommendation_bp.route("/usecase", methods=["POST"])
def usecase():
    category = request.form.get("category")
    budget = request.form.get("budget")
    return render_template("usecase.html", category=category, budget=budget)


# ================= RESULTS (TEMPLATE FLOW) =================

@recommendation_bp.route("/results", methods=["POST"])
def results():

    category = request.form.get("category")
    budget = float(request.form.get("budget"))
    use_case = request.form.get("use_case")

    results = []
    metrics = {}

    # ================= PC FLOW =================
    if category == "pc":

        builds = generate_pc_builds(budget, use_case)

        if not builds:
            return render_template("recommendations.html", results=[])

        # Sort by value
        builds = sorted(builds, key=lambda x: x["value_score"], reverse=True)

        # Limit builds for clustering
        builds = builds[:500]

        feature_matrix = builds_to_matrix(builds)
        selected, metrics = cluster_builds(builds, feature_matrix)

        for build in selected:

            explanation = generate_pc_explanation(build, use_case)

            results.append({
                "type": "PC",

                "cpu": build["cpu"].name,
                "cpu_link": f"https://www.amazon.in/s?k={build['cpu'].name.replace(' ','+')}",

                "motherboard": build["motherboard"].name,
                "motherboard_link": f"https://www.amazon.in/s?k={build['motherboard'].name.replace(' ','+')}",

                "gpu": build["gpu"].name,
                "gpu_link": f"https://www.amazon.in/s?k={build['gpu'].name.replace(' ','+')}",

                "ram": f"{build['ram'].size}GB",
                "ram_link": f"https://www.amazon.in/s?k={build['ram'].name.replace(' ','+')}",

                "ssd": build["ssd"].name,
                "ssd_link": f"https://www.amazon.in/s?k={build['ssd'].name.replace(' ','+')}",

                "psu": build["psu"].name,
                "psu_link": f"https://www.amazon.in/s?k={build['psu'].name.replace(' ','+')}",

                "total_price": build["total_price"],
                "bottleneck_type": build["bottleneck"]["type"],
                "bottleneck_percentage": build["bottleneck"]["percentage"],

                "cluster": build.get("cluster"),
                "cluster_summary": build.get("cluster_summary"),

                "explanation": explanation
            })

    # ================= LAPTOP FLOW =================
    else:

        laptops = Laptop.query.filter(Laptop.price <= budget).all()

        if not laptops:
            return render_template("recommendations.html", results=[], metrics={})

        feature_matrix = laptops_to_matrix(laptops)
        selected, metrics = cluster_laptops(laptops, feature_matrix)

        for laptop in selected:

            explanation = generate_laptop_explanation(laptop, use_case)

            results.append({
                "type": "Laptop",
                "name": laptop.name,
                "ram": laptop.ram,
                "storage": laptop.storage,
                "price": laptop.price,

                "laptop_link": f"https://www.amazon.in/s?k={laptop.name.replace(' ','+')}",

                "cluster": getattr(laptop, "cluster", None),
                "cluster_summary": getattr(laptop, "cluster_summary", None),

                "explanation": explanation
            })

    return render_template("recommendations.html", results=results, metrics=metrics)


# ================= API FLOW =================

@recommendation_bp.route("/recommend", methods=["POST"])
def recommend():

    data = request.json
    budget = float(data.get("budget"))
    use_case = data.get("use_case")
    category = data.get("category")

    # ================= PC API =================
    if category == "pc":

        builds = generate_pc_builds(budget, use_case)

        if not builds:
            return jsonify({"message": "No PC builds found within budget"})

        feature_matrix = builds_to_matrix(builds)
        selected, metrics = cluster_builds(builds, feature_matrix)

        response = []

        for build in selected:

            explanation = generate_pc_explanation(build, use_case)

            response.append({
                "type": "PC",
                "cpu": build["cpu"].name,
                "gpu": build["gpu"].name,
                "ram": f"{build['ram'].size}GB",
                "total_price": build["total_price"],
                "cluster": build.get("cluster"),
                "cluster_summary": build.get("cluster_summary"),
                "explanation": explanation
            })

        return jsonify({
            "recommended": response,
            "metrics": metrics
        })

    # ================= LAPTOP API =================
    elif category == "laptop":

        laptops = Laptop.query.filter(Laptop.price <= budget).all()

        if not laptops:
            return jsonify({"message": "No laptops found within budget"})

        feature_matrix = laptops_to_matrix(laptops)
        selected, metrics = cluster_laptops(laptops, feature_matrix)

        response = []

        for laptop in selected:

            explanation = generate_laptop_explanation(laptop, use_case)

            response.append({
                "type": "Laptop",
                "name": laptop.name,
                "ram": laptop.ram,
                "price": laptop.price,
                "cluster": getattr(laptop, "cluster", None),
                "cluster_summary": getattr(laptop, "cluster_summary", None),
                "explanation": explanation
            })

        return jsonify({
            "recommended": response,
            "metrics": metrics
        })

    else:
        return jsonify({"message": "Invalid category"})