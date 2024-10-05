import random

def selecccion_palabra():
    palabras = [
        "abismo", "acento", "acopio", "acuoso", "adepto", "afable", "afecto", "agotar", "ajuste", "alegre",
        "algido", "altivo", "aludido", "amaner", "amparo", "anotar", "ansias", "apilar", "apogeo", "aprove",
        "ardido", "aromar", "asomar", "atador", "atizar", "auguro", "aurora", "avidez", "avivar", "báculo",
        "bahía", "bambú", "banco", "barril", "batido", "bebida", "bifido", "blando", "bocado", "borrar",
        "bovino", "brecha", "bribón", "bronce", "bucear", "bufón", "burdo", "cabina", "cadete", "calabo",
        "calder", "caliza", "callar", "camino", "camote", "canope", "capote", "caribe", "carita", "carnero",
        "castor", "celoso", "cerveo", "cesión", "chanza", "chicle", "chirla", "ciego", "clavó", "coágulo",
        "cobijo", "colina", "collar", "comida", "copete", "corona", "cosmos", "cresta", "crisol", "cuadra",
        "curado", "curioso", "cutres", "deberá", "delito", "delujo", "dentil", "derrum", "despido", "dicho",
        "diurno", "docena", "donoso", "dorado", "drama", "drogas", "druida", "duelo", "dulzor", "ebano",
        "eclipse", "edición", "egoísmo", "elevar", "embate", "empero", "enanos", "enfado", "enigma", "envase",
        "epopey", "equipo", "errante", "esbozo", "escalar", "esclus", "esmero", "espeso", "estepa", "estoic",
        "estrof", "eterno", "evadir", "fábula", "faceta", "fallo", "faraón", "farina", "fatal", "felina",
        "feo", "feroz", "fiable", "fibras", "fijado", "fijate", "fluir", "fonema", "fondo", "forjar", 
        "fragil", "fresco", "friso", "frugal", "fuerza", "furor", "fusil", "gacela", "galeno", "gama", 
        "gemelo", "genoma", "gestar", "girar", "golear", "gremio", "gritar", "guinda", "gustar", "habano", 
        "hacina", "hacha", "hebreo", "heder", "helena", "heroico", "hermos", "hojear", "hollar", "hombro",
        "honesto", "honor", "horno", "humano", "húmedo", "ibérico", "iconos", "ideado", "ideal", "ídolo", 
        "igual", "impact", "impera", "impulso", "inciso", "indigo", "indómit", "infiel", "ingente", "inicia",
        "injuri", "inmune", "intern", "iridio", "jardín", "jirafa", "jovial", "joyero", "judío", "juicio",
        "junior", "labial", "labrado", "lactea", "laguna", "laico", "lámine", "lancer", "latido", "legal",
        "leñoso", "lepido", "libelo", "ligero", "litoral", "lodo", "lucha", "lumbar", "lúcido", "maceta", 
        "madera", "magnet", "maleza", "malta", "manc", "manto", "marina", "masaje", "medrar", "menudo",
        "mesura", "mestiz", "método", "militar", "misiva", "modulo", "mojito", "molino", "morada", "moreno",
        "mosca", "mucha", "muda", "mujer", "multa", "murmul", "nacar", "nacional", "nave", "neutro", 
        "nicho", "ninfa", "nombrar", "novela", "nuboso", "núcleo", "obispo", "oído", "ojalá", "olvido",
        "ómnibus", "ópalo", "órbita", "orígenes", "osado", "pacífico", "padecer", "pagoda", "pálida", 
        "paliza", "pámpano", "pánico", "paquete", "parado", "pasado", "pávido", "pedazo", "peinado", 
        "perder", "pesada", "pétalo", "picara", "piedra", "pienso", "pirata", "placido", "plaza", "plegar",
        "pluma", "pobre", "poeta", "polaco", "polen", "ponder", "póquer", "postal", "prado", "premio",
        "prensa", "prisma", "proa", "probar", "púa", "pueblo", "puñado", "pulido", "pulso", "puntual",
        "quedar", "químico", "quitar", "radial", "rápido", "raudal", "razonar", "recio", "reino", "reja", 
        "relato", "remate", "renal", "renovar", "retoño", "rever", "ríe", "rifar", "risueño", "robar",
        "rodeo", "romero", "rumbo", "sabana", "saber", "saciar", "sala", "salida", "salino", "saltar",
        "salud", "sanar", "satín", "secador", "seco", "segado", "señal", "senda", "sereno", "serio",
        "siembra", "siglo", "silbar", "simio", "soga", "solar", "sombra", "soplar", "sorda", "sufrir",
        "tahona", "tajo", "talar", "talón", "tándem", "tarde", "temor", "tenaz", "tensa", "teoría", 
        "terco", "termo", "tesoro", "tiempo", "tierra", "tirano", "toldo", "tórax", "tostar", "tóxico", 
        "trabajo", "traer", "trama", "trazar", "trofeo", "trompa", "trueno", "tulipa", "tumba", "tutor", 
        "ubicar", "úlcera", "ungido", "urgente", "usar", "utopía", "vaciar", "vago", "válido", "veloz",
        "vencer", "venero", "verano", "verde", "verso", "vestir", "víbora", "vídeo", "vigor", "virgen",
        "visto", "viudo", "volar", "volcán", "volver", "yegua", "yermo", "yerno", "yodado", "yunta",
        "zafar", "zanja", "zapato", "zarpa", "zodíaco", "zona", "zorro"
    ]


    palabra_oculta = random.choice(palabras)
    return palabra_oculta


def mostrar_final_juego():
    print("\n═════════════════════════════════════")
    print(" Elija una opción:")
    print("   1. Volver a jugar")
    print("   2. Volver al menú principal")
    print("   3. Salir")
    seleccion_final = int(input("👉 Tu opción: "))
    print("═════════════════════════════════════")
    return seleccion_final