import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


def cluster_builds(builds, feature_matrix):

    if len(builds) < 3:
        return builds, {}

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(feature_matrix)

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=15,
        algorithm="lloyd"
    )

    kmeans.fit(scaled_features)

    labels = kmeans.labels_
    inertia = kmeans.inertia_

    try:
        silhouette = silhouette_score(scaled_features, labels)
    except:
        silhouette = 0

    cluster_info = {}

    # Attach cluster labels + distance
    for i, build in enumerate(builds):
        build["cluster"] = int(labels[i])
        build["distance_to_center"] = float(
            np.linalg.norm(
                scaled_features[i] - kmeans.cluster_centers_[labels[i]]
            )
        )

    selected_builds = []

    for cluster_id in range(3):
        cluster_group = [b for b in builds if b["cluster"] == cluster_id]

        if cluster_group:

            # Select best by value_score
            best = max(cluster_group, key=lambda x: x["value_score"])

            best["cluster_summary"] = {
                "cluster_id": cluster_id,
                "total_builds_in_cluster": len(cluster_group),
                "avg_price": round(
                    np.mean([b["total_price"] for b in cluster_group]), 2
                ),
                "avg_performance": round(
                    np.mean([b["performance_score"] for b in cluster_group]), 2
                ),
            }

            selected_builds.append(best)

    metrics = {
        "inertia": round(inertia, 4),
        "silhouette_score": round(silhouette, 4),
        "total_builds_clustered": len(builds),
        "clusters": 3
    }

    return selected_builds, metrics


# ---------------------------------------
# LAPTOP CLUSTERING
# ---------------------------------------

def cluster_laptops(laptops, feature_matrix):

    if len(laptops) < 3:
        return laptops, {}

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(feature_matrix)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=15)
    kmeans.fit(scaled_features)

    labels = kmeans.labels_
    inertia = kmeans.inertia_

    try:
        silhouette = silhouette_score(scaled_features, labels)
    except:
        silhouette = 0

    for i, laptop in enumerate(laptops):
        laptop.cluster = int(labels[i])
        laptop.distance_to_center = float(
            np.linalg.norm(
                scaled_features[i] - kmeans.cluster_centers_[labels[i]]
            )
        )

    selected = []

    for cluster_id in range(3):
        cluster_group = [l for l in laptops if l.cluster == cluster_id]

        if cluster_group:
            best = min(cluster_group, key=lambda x: x.price)

            best.cluster_summary = {
                "cluster_id": cluster_id,
                "total_laptops_in_cluster": len(cluster_group),
                "avg_price": round(
                    np.mean([l.price for l in cluster_group]), 2
                ),
                "avg_cpu_score": round(
                    np.mean([l.cpu_score for l in cluster_group]), 2
                ),
                "avg_gpu_score": round(
                    np.mean([l.gpu_score for l in cluster_group]), 2
                )
            }

            selected.append(best)

    metrics = {
        "inertia": round(inertia, 4),
        "silhouette_score": round(silhouette, 4),
        "total_laptops_clustered": len(laptops),
        "clusters": 3
    }

    return selected, metrics
