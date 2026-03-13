from models import CPU, GPU, RAM, SSD, Motherboard, PSU


def calculate_bottleneck(cpu_score, gpu_score):
    if gpu_score == 0:
        return {"type": "Balanced", "percentage": 0}

    ratio = cpu_score / gpu_score

    if ratio < 0.75:
        return {"type": "CPU Bottleneck", "percentage": round((1 - ratio) * 100, 2)}
    elif ratio > 1.35:
        return {"type": "GPU Bottleneck", "percentage": round((ratio - 1) * 100, 2)}
    else:
        return {"type": "Balanced", "percentage": 0}


def normalize_socket(socket_string):
    if not socket_string:
        return ""
    return socket_string.replace(" ", "").lower().strip()


def generate_pc_builds(budget, use_case):

    # 1️⃣ Pre-filter by realistic budget split
    cpus = CPU.query.filter(CPU.price <= budget * 0.35).all()
    gpus = GPU.query.filter(GPU.price <= budget * 0.45).all()
    rams = RAM.query.filter(RAM.price <= budget * 0.15).all()
    ssds = SSD.query.filter(SSD.price <= budget * 0.15).all()
    motherboards = Motherboard.query.filter(Motherboard.price <= budget * 0.20).all()
    psus = PSU.query.filter(PSU.price <= budget * 0.15).all()

    # 2️⃣ HARD LIMIT — keep only top 10 performance parts
    cpus = sorted(cpus, key=lambda x: x.benchmark_score, reverse=True)[:10]
    gpus = sorted(gpus, key=lambda x: x.benchmark_score, reverse=True)[:10]
    rams = sorted(rams, key=lambda x: x.size, reverse=True)[:6]
    ssds = sorted(ssds, key=lambda x: x.speed_score, reverse=True)[:6]

    builds = []

    for cpu in cpus:
        for gpu in gpus:

            # Avoid extreme mismatch
            if cpu.benchmark_score < gpu.benchmark_score * 0.5:
                continue

            compatible_mbs = [mb for mb in motherboards if mb.socket == cpu.socket]

            for mb in compatible_mbs:
                for ram in rams:
                    for ssd in ssds:
                        for psu in psus:

                            if gpu.wattage > psu.wattage:
                                continue

                            total_price = (
                                cpu.price +
                                gpu.price +
                                ram.price +
                                ssd.price +
                                mb.price +
                                psu.price
                            )

                            if total_price > budget:
                                continue

                            # ---------------- USE CASE SCORING ----------------
                            if use_case == "Gaming":
                                performance_score = (
                                    cpu.benchmark_score * 0.35 +
                                    gpu.benchmark_score * 0.45 +
                                    ram.size * 40 +
                                    ssd.speed_score * 0.01
                                )

                            elif use_case == "Video Editing":
                                performance_score = (
                                    cpu.benchmark_score * 0.45 +
                                    gpu.benchmark_score * 0.30 +
                                    ram.size * 70 +
                                    ssd.speed_score * 0.03
                                )

                            elif use_case == "Casual Use":
                                performance_score = (
                                    cpu.benchmark_score * 0.50 +
                                    ram.size * 60 +
                                    ssd.speed_score * 0.05
                                )

                            elif use_case == "Animation/VFX/Game Dev":
                                performance_score = (
                                    cpu.benchmark_score * 0.40 +
                                    gpu.benchmark_score * 0.40 +
                                    ram.size * 80 +
                                    ssd.speed_score * 0.03
                                )

                            else:
                                performance_score = (
                                    cpu.benchmark_score * 0.4 +
                                    gpu.benchmark_score * 0.4
                                )

                            value_score = performance_score / total_price

                            builds.append({
                                "cpu": cpu,
                                "gpu": gpu,
                                "ram": ram,
                                "ssd": ssd,
                                "motherboard": mb,
                                "psu": psu,
                                "total_price": total_price,
                                "performance_score": performance_score,
                                "value_score": value_score,
                                "bottleneck": calculate_bottleneck(
                                    cpu.benchmark_score,
                                    gpu.benchmark_score
                                )
                            })

    print("DEBUG: Total builds generated:", len(builds))
    return builds

