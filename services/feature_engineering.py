import numpy as np


def build_to_feature_vector(build):
    """
    Convert a single PC build to feature vector
    [CPU_score, GPU_score, RAM_size, SSD_speed_score, total_price]
    """

    return [
        build["cpu"].benchmark_score,
        build["gpu"].benchmark_score,
        build["ram"].size,
        build["ssd"].speed_score,
        build["total_price"]
    ]


def builds_to_matrix(builds):
    """
    Convert list of builds into 2D feature matrix
    """

    feature_list = []

    for build in builds:
        vector = build_to_feature_vector(build)
        feature_list.append(vector)

    return np.array(feature_list)

def laptops_to_matrix(laptops):
    matrix = []

    for laptop in laptops:

        # Convert storage (GB) into score
        if laptop.storage >= 2000:
            storage_score = 9000
        elif laptop.storage >= 1000:
            storage_score = 7000
        elif laptop.storage >= 512:
            storage_score = 5000
        else:
            storage_score = 3000

        matrix.append([
            laptop.cpu_score,
            laptop.gpu_score,
            laptop.ram,
            storage_score,
            laptop.price
        ])

    return np.array(matrix)

