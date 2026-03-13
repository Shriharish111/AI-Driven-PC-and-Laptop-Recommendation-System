from extensions import db



class CPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    cores = db.Column(db.Integer)
    threads = db.Column(db.Integer)
    benchmark_score = db.Column(db.Integer)
    socket = db.Column(db.String(20))
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, cores, threads, benchmark_score, socket, price, amazon_link):
        self.name = name
        self.cores = cores
        self.threads = threads
        self.benchmark_score = benchmark_score
        self.socket = socket
        self.price = price
        self.amazon_link = amazon_link


class GPU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    vram = db.Column(db.Integer)
    benchmark_score = db.Column(db.Integer)
    wattage = db.Column(db.Integer)
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, vram, benchmark_score, wattage, price, amazon_link):
        self.name = name
        self.vram = vram
        self.benchmark_score = benchmark_score
        self.wattage = wattage
        self.price = price
        self.amazon_link = amazon_link




class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    size = db.Column(db.Integer)
    type = db.Column(db.String(10))
    speed = db.Column(db.Integer)
    form_factor = db.Column(db.String(10))
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, size, type, speed, form_factor, price, amazon_link):
        self.name = name
        self.size = size
        self.type = type
        self.speed = speed
        self.form_factor = form_factor
        self.price = price
        self.amazon_link = amazon_link





class SSD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    interface = db.Column(db.String(50))
    capacity = db.Column(db.Integer)
    speed_score = db.Column(db.Integer)
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, interface, capacity, speed, price, amazon_link):
        self.name = name
        self.interface = interface
        self.capacity = capacity
        self.speed_score = speed
        self.price = price
        self.amazon_link = amazon_link


class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    socket = db.Column(db.String(20))
    chipset = db.Column(db.String(20))
    ram_type = db.Column(db.String(10))
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, socket, chipset, ram_type, price, amazon_link):
        self.name = name
        self.socket = socket
        self.chipset = chipset
        self.ram_type = ram_type
        self.price = price
        self.amazon_link = amazon_link





class PSU(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    wattage = db.Column(db.Integer)
    efficiency = db.Column(db.String(20))
    price = db.Column(db.Integer)
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, wattage, efficiency, price, amazon_link):
        self.name = name
        self.wattage = wattage
        self.efficiency = efficiency
        self.price = price
        self.amazon_link = amazon_link


class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cpu_score = db.Column(db.Integer)
    gpu_score = db.Column(db.Integer)
    ram = db.Column(db.Integer)
    storage = db.Column(db.Integer)
    price = db.Column(db.Integer)
    category = db.Column(db.String(50))
    amazon_link = db.Column(db.String(500))

    def __init__(self, name, cpu_score, gpu_score, ram, storage, price, category, amazon_link):
        self.name = name
        self.cpu_score = cpu_score
        self.gpu_score = gpu_score
        self.ram = ram
        self.storage = storage
        self.price = price
        self.category = category
        self.amazon_link = amazon_link

