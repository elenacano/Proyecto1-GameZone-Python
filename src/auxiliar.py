import random

def selecccion_palabra():
    """Selecciona una palabra de una lista de 500 palabras.

    Returns:
        str: palabra seleccionada de forma aleatoria.
    """
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

def seleccion_pregunta_preguntados():
    """Declara preguntas para 5 categorias dstintas y devuelve una categoría aleatoria y una pregunta aleatoria de dicha categoría.

    Returns:
        str: categoría de la pregunta.
        dict: donde hay dos elementos, la pregunta y las respuestas cuyo valor es una lista.
    """

    preguntas_geografia = [
        {"Pregunta": "¿Cuál es la capital de Cantabria?", "Respuestas": {"Santander": True, "Lugo": False, "Antequera": False, "Oviedo": False}},
        {"Pregunta": "¿Cuál es la capital de Navarra?", "Respuestas": {"Alcalá de Henares": False, "Logroño": False, "Pamplona": True, "Zaragoza": False}},
        {"Pregunta": "¿Cuál es el país más grande del mundo?", "Respuestas": {"Canadá": False, "China": False, "Rusia": True, "EE.UU.": False}},
        {"Pregunta": "¿Qué océano es el más grande?", "Respuestas": {"Atlántico": False, "Índico": False, "Pacífico": True, "Ártico": False}},
        {"Pregunta": "¿Cuál es el río más largo del mundo?", "Respuestas": {"Nilo": False, "Amazonas": True, "Yangtsé": False, "Misisipi": False}},
        {"Pregunta": "¿Cuál es el país más pequeño del mundo?", "Respuestas": {"San Marino": False, "Mónaco": False, "Ciudad del Vaticano": True, "Liechtenstein": False}},
        {"Pregunta": "¿En qué continente se encuentra Egipto?", "Respuestas": {"Asia": False, "Europa": False, "África": True, "América": False}},
        {"Pregunta": "¿Cuál es el desierto más grande del mundo?", "Respuestas": {"Sáhara": False, "Gobi": False, "Antártico": True, "Kalahari": False}},
        {"Pregunta": "¿Qué país tiene más habitantes?", "Respuestas": {"India": False, "EE.UU.": False, "China": True, "Rusia": False}},
        {"Pregunta": "¿Cuál es la montaña más alta del mundo?", "Respuestas": {"Mont Blanc": False, "K2": False, "Monte Everest": True, "Kilimanjaro": False}},
        {"Pregunta": "¿Cuál es la capital de Australia?", "Respuestas": {"Sídney": False, "Melbourne": False, "Canberra": True, "Perth": False}},
        {"Pregunta": "¿Cuál es la isla más grande del mundo?", "Respuestas": {"Madagascar": False, "Groenlandia": True, "Nueva Guinea": False, "Borneo": False}},
        {"Pregunta": "¿Cuál es la capital de Japón?", "Respuestas": {"Seúl": False, "Pekín": False, "Tokio": True, "Bangkok": False}},
        {"Pregunta": "¿Qué mar separa Europa de África?", "Respuestas": {"Mar del Norte": False, "Mar Mediterráneo": True, "Mar Rojo": False, "Mar Caspio": False}},
        {"Pregunta": "¿En qué país está el río Támesis?", "Respuestas": {"Francia": False, "España": False, "Reino Unido": True, "Italia": False}},
        {"Pregunta": "¿Qué país tiene la forma de una bota?", "Respuestas": {"España": False, "Italia": True, "Grecia": False, "Portugal": False}},
        {"Pregunta": "¿En qué país se encuentra la Torre Eiffel?", "Respuestas": {"Italia": False, "Alemania": False, "Francia": True, "Bélgica": False}},
        {"Pregunta": "¿Qué país limita con España al oeste?", "Respuestas": {"Francia": False, "Italia": False, "Portugal": True, "Marruecos": False}},
        {"Pregunta": "¿Cuál es la capital de Canadá?", "Respuestas": {"Toronto": False, "Vancouver": False, "Ottawa": True, "Montreal": False}},
        {"Pregunta": "¿En qué país se encuentra el desierto de Atacama?", "Respuestas": {"Argentina": False, "Chile": True, "Perú": False, "Bolivia": False}},
        {"Pregunta": "¿Cuál es la capital de México?", "Respuestas": {"Guadalajara": False, "Ciudad de México": True, "Monterrey": False, "Cancún": False}},
        {"Pregunta": "¿Qué cordillera atraviesa Sudamérica de norte a sur?", "Respuestas": {"Montañas Rocosas": False, "Alpes": False, "Andes": True, "Cáucaso": False}},
        {"Pregunta": "¿Cuál es la capital de Argentina?", "Respuestas": {"Lima": False, "Buenos Aires": True, "Montevideo": False, "Santiago": False}},
        {"Pregunta": "¿En qué océano se encuentra Hawái?", "Respuestas": {"Atlántico": False, "Pacífico": True, "Índico": False, "Ártico": False}},
        {"Pregunta": "¿Cuál es la capital de Brasil?", "Respuestas": {"São Paulo": False, "Brasilia": True, "Río de Janeiro": False, "Salvador": False}},
        {"Pregunta": "¿Cuál es el país más poblado de África?", "Respuestas": {"Sudáfrica": False, "Egipto": False, "Nigeria": True, "Argelia": False}},
        {"Pregunta": "¿Qué país tiene más lagos?", "Respuestas": {"Suecia": False, "Estados Unidos": False, "Canadá": True, "Finlandia": False}},
        {"Pregunta": "¿En qué continente está el río Amazonas?", "Respuestas": {"África": False, "Asia": False, "Sudamérica": True, "Europa": False}},
        {"Pregunta": "¿Cuál es el lago más grande del mundo?", "Respuestas": {"Lago Victoria": False, "Lago Superior": False, "Mar Caspio": True, "Lago Baikal": False}},
        {"Pregunta": "¿Cuál es la capital de Alemania?", "Respuestas": {"Múnich": False, "Berlín": True, "Frankfurt": False, "Hamburgo": False}},
    ]
    preguntas_historia = [
        {"Pregunta": "¿En qué año se descubrió América?", "Respuestas": {"1234": False, "1492": True, "1482": False, "1111": False}},
        {"Pregunta": "¿Quién fue el inventor del teléfono?", "Respuestas": {"Einstein": False, "Marie Curie": False, "Alexander Graham Bell": True, "Nicola Tesla": False}},
        {"Pregunta": "¿En qué año comenzó la Primera Guerra Mundial?", "Respuestas": {"1901": False, "1914": True, "1939": False, "1812": False}},
        {"Pregunta": "¿En qué año fue la Revolución Francesa?", "Respuestas": {"1812": False, "1789": True, "1804": False, "1756": False}},
        {"Pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "Respuestas": {"Thomas Jefferson": False, "George Washington": True, "Abraham Lincoln": False, "John Adams": False}},
        {"Pregunta": "¿En qué año cayó el Muro de Berlín?", "Respuestas": {"1961": False, "1989": True, "1991": False, "1979": False}},
        {"Pregunta": "¿Qué faraón ordenó construir la Gran Pirámide de Giza?", "Respuestas": {"Tutankamón": False, "Ramsés II": False, "Keops": True, "Cleopatra": False}},
        {"Pregunta": "¿Quién fue el líder de la Revolución Cubana?", "Respuestas": {"Ernesto Che Guevara": False, "Fidel Castro": True, "Raúl Castro": False, "Camilo Cienfuegos": False}},
        {"Pregunta": "¿Quién fue el emperador romano durante la crucifixión de Jesús?", "Respuestas": {"Nerón": False, "Tiberio": True, "Julio César": False, "Calígula": False}},
        {"Pregunta": "¿Cuál fue el último faraón de Egipto?", "Respuestas": {"Ramsés II": False, "Cleopatra VII": True, "Tutankamón": False, "Akenatón": False}},
        {"Pregunta": "¿Qué imperio construyó el Coliseo?", "Respuestas": {"Griego": False, "Romano": True, "Egipcio": False, "Persa": False}},
        {"Pregunta": "¿Qué conflicto bélico finalizó en 1945?", "Respuestas": {"Primera Guerra Mundial": False, "Segunda Guerra Mundial": True, "Guerra de Vietnam": False, "Guerra Civil Española": False}},
        {"Pregunta": "¿Quién fue el primer hombre en pisar la luna?", "Respuestas": {"Buzz Aldrin": False, "Neil Armstrong": True, "Yuri Gagarin": False, "Michael Collins": False}},
        {"Pregunta": "¿Qué acontecimiento histórico tuvo lugar el 6 de junio de 1944?", "Respuestas": {"La batalla de Stalingrado": False, "El Desembarco de Normandía": True, "La caída de Berlín": False, "El ataque a Pearl Harbor": False}},
        {"Pregunta": "¿Qué emperador romano legalizó el cristianismo?", "Respuestas": {"Nerón": False, "Constantino I": True, "Julio César": False, "Marco Aurelio": False}},
        {"Pregunta": "¿Qué país utilizó por primera vez armas nucleares en la guerra?", "Respuestas": {"Alemania": False, "Estados Unidos": True, "Rusia": False, "Japón": False}},
        {"Pregunta": "¿En qué país tuvo lugar la Revolución Industrial?", "Respuestas": {"Francia": False, "Inglaterra": True, "Alemania": False, "Italia": False}},
        {"Pregunta": "¿En qué año comenzó la Guerra Civil Española?", "Respuestas": {"1923": False, "1936": True, "1939": False, "1914": False}},
        {"Pregunta": "¿Quién escribió 'El Príncipe'?", "Respuestas": {"Platón": False, "Maquiavelo": True, "Aristóteles": False, "Rousseau": False}},
        {"Pregunta": "¿Qué civilización construyó Machu Picchu?", "Respuestas": {"Azteca": False, "Inca": True, "Maya": False, "Tolteca": False}},
        {"Pregunta": "¿En qué país tuvo lugar la Revolución Mexicana?", "Respuestas": {"Argentina": False, "México": True, "Brasil": False, "Perú": False}},
        {"Pregunta": "¿Quién pintó la Mona Lisa?", "Respuestas": {"Picasso": False, "Da Vinci": True, "Van Gogh": False, "Miguel Ángel": False}},
        {"Pregunta": "¿Qué civilización inventó la escritura?", "Respuestas": {"Griegos": False, "Sumerios": True, "Romanos": False, "Egipcios": False}},
        {"Pregunta": "¿En qué año cayó Constantinopla?", "Respuestas": {"1453": True, "1492": False, "1402": False, "1543": False}},
        {"Pregunta": "¿Qué evento se considera el inicio de la Edad Media?", "Respuestas": {"Caída del Imperio Romano": True, "Descubrimiento de América": False, "Revolución Francesa": False, "Fundación de Roma": False}},
        {"Pregunta": "¿Qué líder revolucionario dijo: 'La historia me absolverá'?", "Respuestas": {"Mao Zedong": False, "Fidel Castro": True, "Simón Bolívar": False, "Pancho Villa": False}},
        {"Pregunta": "¿Qué civilización construyó las pirámides de Egipto?", "Respuestas": {"Egipcios": True, "Griegos": False, "Romanos": False, "Fenicios": False}},
        {"Pregunta": "¿En qué país tuvo lugar el Renacimiento?", "Respuestas": {"Francia": False, "Italia": True, "España": False, "Alemania": False}},
        {"Pregunta": "¿En qué año comenzó la Revolución Francesa?", "Respuestas": {"1799": False, "1789": True, "1801": False, "1776": False}},
        {"Pregunta": "¿Qué filósofo escribió 'La República'?", "Respuestas": {"Sócrates": False, "Platón": True, "Aristóteles": False, "Descartes": False}},
        {"Pregunta": "¿Quién fue el último zar de Rusia?", "Respuestas": {"Pedro el Grande": False, "Nicolás II": True, "Iván el Terrible": False, "Alejandro II": False}},
    ]
    preguntas_entretenimiento = [
        {"Pregunta": "¿Qué famoso programador apareció en Master Chef?", "Respuestas": {"James Gosling": False, "Jean-Charles": True, "Guido Van Rossum": False, "Dennis Ritchie": False}},
        {"Pregunta": "¿Qué serie protagoniza Hugh Laurie?", "Respuestas": {"Ricky n' Morty": False, "Suits": False, "La Que Se Avecina": False, "House": True}},
        {"Pregunta": "¿En qué año se estrenó la película 'Titanic'?", "Respuestas": {"1990": False, "1997": True, "2000": False, "1985": False}},
        {"Pregunta": "¿Qué actor interpretó a Jack Sparrow en 'Piratas del Caribe'?", "Respuestas": {"Brad Pitt": False, "Johnny Depp": True, "Leonardo DiCaprio": False, "Tom Cruise": False}},
        {"Pregunta": "¿Qué grupo musical popularizó la canción 'Bohemian Rhapsody'?", "Respuestas": {"The Beatles": False, "Queen": True, "Led Zeppelin": False, "The Rolling Stones": False}},
        {"Pregunta": "¿Quién dirigió la película 'El Padrino'?", "Respuestas": {"Steven Spielberg": False, "Francis Ford Coppola": True, "Martin Scorsese": False, "Stanley Kubrick": False}},
        {"Pregunta": "¿Qué saga de películas es famosa por sus anillos?", "Respuestas": {"Star Wars": False, "Harry Potter": False, "El Señor de los Anillos": True, "Indiana Jones": False}},
        {"Pregunta": "¿En qué serie aparece el personaje Walter White?", "Respuestas": {"Breaking Bad": True, "The Wire": False, "Narcos": False, "Better Call Saul": False}},
        {"Pregunta": "¿Qué actriz protagoniza la película 'Gravity'?", "Respuestas": {"Julia Roberts": False, "Sandra Bullock": True, "Angelina Jolie": False, "Meryl Streep": False}},
        {"Pregunta": "¿Cuál es el nombre de la heroína en 'Los Juegos del Hambre'?", "Respuestas": {"Hermione Granger": False, "Katniss Everdeen": True, "Bella Swan": False, "Arya Stark": False}},
        {"Pregunta": "¿Qué película ganó el Oscar a la Mejor Película en 2020?", "Respuestas": {"Joker": False, "1917": False, "Parásitos": True, "Once Upon a Time in Hollywood": False}},
        {"Pregunta": "¿Quién es el creador de la serie 'Los Simpson'?", "Respuestas": {"Seth MacFarlane": False, "Matt Groening": True, "Trey Parker": False, "Hank Azaria": False}},
        {"Pregunta": "¿Qué banda sonora compuso John Williams?", "Respuestas": {"Star Wars": True, "El Señor de los Anillos": False, "Harry Potter": False, "Jurassic Park": False}},
        {"Pregunta": "¿Qué personaje de cine dice 'I'll be back'?", "Respuestas": {"Rocky Balboa": False, "Darth Vader": False, "Terminator": True, "Rambo": False}},
        {"Pregunta": "¿Qué serie se desarrolla en la ficticia ciudad de Gotham?", "Respuestas": {"The Flash": False, "Superman": False, "Batman": True, "Wonder Woman": False}},
        {"Pregunta": "¿Qué famoso grupo musical fue conocido como 'Los Cuatro de Liverpool'?", "Respuestas": {"The Rolling Stones": False, "The Beatles": True, "The Who": False, "Queen": False}},
        {"Pregunta": "¿Qué actor protagonizó la película 'Forrest Gump'?", "Respuestas": {"Tom Cruise": False, "Tom Hanks": True, "Brad Pitt": False, "Leonardo DiCaprio": False}},
        {"Pregunta": "¿Qué película tiene la famosa frase 'Hasta el infinito y más allá'?", "Respuestas": {"Shrek": False, "Toy Story": True, "Monsters Inc.": False, "Cars": False}},
        {"Pregunta": "¿Qué serie protagonizó Jennifer Aniston?", "Respuestas": {"Breaking Bad": False, "Friends": True, "The Office": False, "How I Met Your Mother": False}},
        {"Pregunta": "¿Qué director es famoso por la película 'Pulp Fiction'?", "Respuestas": {"Christopher Nolan": False, "Martin Scorsese": False, "Quentin Tarantino": True, "Alfred Hitchcock": False}},
        {"Pregunta": "¿Qué personaje interpretó Leonardo DiCaprio en 'El Lobo de Wall Street'?", "Respuestas": {"Tony Montana": False, "Jordan Belfort": True, "Jay Gatsby": False, "Jack Dawson": False}},
        {"Pregunta": "¿Qué superhéroe pertenece a DC Comics?", "Respuestas": {"Spiderman": False, "Iron Man": False, "Batman": True, "Capitán América": False}},
        {"Pregunta": "¿Quién dirigió la trilogía de 'El Señor de los Anillos'?", "Respuestas": {"George Lucas": False, "Steven Spielberg": False, "Peter Jackson": True, "James Cameron": False}},
        {"Pregunta": "¿En qué ciudad está ambientada la serie 'Friends'?", "Respuestas": {"Los Ángeles": False, "Nueva York": True, "Chicago": False, "San Francisco": False}},
        {"Pregunta": "¿Qué personaje de dibujos animados tiene un amigo llamado Patricio?", "Respuestas": {"Bob Esponja": True, "Mickey Mouse": False, "Scooby-Doo": False, "Dora la Exploradora": False}},
        {"Pregunta": "¿Qué cantante es conocido como 'El Rey del Pop'?", "Respuestas": {"Prince": False, "Michael Jackson": True, "Elvis Presley": False, "David Bowie": False}},
        {"Pregunta": "¿Qué película está basada en la novela de J.R.R. Tolkien?", "Respuestas": {"Harry Potter": False, "El Señor de los Anillos": True, "Narnia": False, "Divergente": False}},
        {"Pregunta": "¿Qué actor interpretó a Indiana Jones?", "Respuestas": {"Tom Hanks": False, "Harrison Ford": True, "Mel Gibson": False, "Bruce Willis": False}},
        {"Pregunta": "¿Qué película animada tiene como protagonista a un panda llamado Po?", "Respuestas": {"Kung Fu Panda": True, "Shrek": False, "Los Increíbles": False, "Ratatouille": False}},
        {"Pregunta": "¿Qué director es conocido por las películas 'Inception' y 'The Dark Knight'?", "Respuestas": {"Steven Spielberg": False, "Christopher Nolan": True, "James Cameron": False, "Tim Burton": False}},
    ]
    preguntas_ciencia = [
        {"Pregunta": "¿Qué planeta es el más cercano al sol?", "Respuestas": {"Tierra": False, "Venus": False, "Mercurio": True, "Marte": False}},
        {"Pregunta": "¿Quién desarrolló la teoría de la relatividad?", "Respuestas": {"Isaac Newton": False, "Albert Einstein": True, "Nikola Tesla": False, "Galileo Galilei": False}},
        {"Pregunta": "¿Cuál es el gas más abundante en la atmósfera?", "Respuestas": {"Oxígeno": False, "Nitrógeno": True, "Dióxido de carbono": False, "Helio": False}},
        {"Pregunta": "¿Qué partícula subatómica tiene carga negativa?", "Respuestas": {"Protones": False, "Electrones": True, "Neutrones": False, "Quarks": False}},
        {"Pregunta": "¿Cómo se llama el proceso por el cual las plantas producen su alimento?", "Respuestas": {"Respiración": False, "Fotosíntesis": True, "Metabolismo": False, "Fermentación": False}},
        {"Pregunta": "¿Quién es conocido como el padre de la medicina moderna?", "Respuestas": {"Hipócrates": True, "Aristóteles": False, "Galileo": False, "Marie Curie": False}},
        {"Pregunta": "¿Qué planeta es conocido como el planeta rojo?", "Respuestas": {"Venus": False, "Marte": True, "Júpiter": False, "Saturno": False}},
        {"Pregunta": "¿Qué órgano humano produce la insulina?", "Respuestas": {"Hígado": False, "Páncreas": True, "Riñón": False, "Corazón": False}},
        {"Pregunta": "¿Qué elemento químico tiene como símbolo O?", "Respuestas": {"Hidrógeno": False, "Oxígeno": True, "Carbono": False, "Nitrógeno": False}},
        {"Pregunta": "¿Qué científico propuso las leyes del movimiento?", "Respuestas": {"Albert Einstein": False, "Isaac Newton": True, "Galileo Galilei": False, "Stephen Hawking": False}},
        {"Pregunta": "¿Cuál es el animal más grande del mundo?", "Respuestas": {"Elefante": False, "Ballena azul": True, "Tiburón blanco": False, "Jirafa": False}},
        {"Pregunta": "¿Qué planeta tiene los anillos más visibles?", "Respuestas": {"Júpiter": False, "Urano": False, "Saturno": True, "Neptuno": False}},
        {"Pregunta": "¿Cómo se llama la fuerza que nos mantiene en la Tierra?", "Respuestas": {"Electromagnetismo": False, "Gravedad": True, "Inercia": False, "Fricción": False}},
        {"Pregunta": "¿Cuál es el elemento más abundante en el universo?", "Respuestas": {"Helio": False, "Oxígeno": False, "Hidrógeno": True, "Carbono": False}},
        {"Pregunta": "¿Qué parte del cuerpo humano está compuesta de más huesos?", "Respuestas": {"Cabeza": False, "Mano": True, "Pierna": False, "Espalda": False}},
        {"Pregunta": "¿Qué tipo de sangre es considerado donante universal?", "Respuestas": {"A+": False, "B+": False, "O-": True, "AB+": False}},
        {"Pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", "Respuestas": {"Fémur": True, "Húmero": False, "Tibia": False, "Columna vertebral": False}},
        {"Pregunta": "¿Qué científico descubrió la penicilina?", "Respuestas": {"Louis Pasteur": False, "Alexander Fleming": True, "Marie Curie": False, "Isaac Newton": False}},
        {"Pregunta": "¿Qué tipo de energía es producida por el movimiento?", "Respuestas": {"Energía térmica": False, "Energía cinética": True, "Energía química": False, "Energía nuclear": False}},
        {"Pregunta": "¿Qué planeta es conocido por sus lunas gigantes?", "Respuestas": {"Saturno": False, "Júpiter": True, "Marte": False, "Neptuno": False}},
        {"Pregunta": "¿Qué proceso convierte el agua en vapor?", "Respuestas": {"Condensación": False, "Evaporación": True, "Sublimación": False, "Fusión": False}},
        {"Pregunta": "¿Cuál es el metal más ligero?", "Respuestas": {"Aluminio": False, "Litio": True, "Magnesio": False, "Oro": False}},
        {"Pregunta": "¿Qué animal es conocido como el más rápido del mundo?", "Respuestas": {"Leopardo": False, "Halcón peregrino": True, "Guepardo": False, "León": False}},
        {"Pregunta": "¿Qué planeta es el más grande del sistema solar?", "Respuestas": {"Saturno": False, "Júpiter": True, "Neptuno": False, "Tierra": False}},
        {"Pregunta": "¿Cuál es la unidad de medida de la corriente eléctrica?", "Respuestas": {"Voltios": False, "Amperios": True, "Ohmios": False, "Vatios": False}},
        {"Pregunta": "¿Qué tipo de célula transporta oxígeno por el cuerpo?", "Respuestas": {"Células nerviosas": False, "Glóbulos rojos": True, "Plaquetas": False, "Glóbulos blancos": False}},
        {"Pregunta": "¿Cómo se llama la capa más externa de la Tierra?", "Respuestas": {"Núcleo": False, "Manto": False, "Corteza": True, "Litosfera": False}},
        {"Pregunta": "¿Qué gas es fundamental para la respiración de los seres humanos?", "Respuestas": {"Nitrógeno": False, "Oxígeno": True, "Dióxido de carbono": False, "Hidrógeno": False}},
        {"Pregunta": "¿Qué instrumento se usa para medir la temperatura?", "Respuestas": {"Barómetro": False, "Termómetro": True, "Microscopio": False, "Anemómetro": False}},
        {"Pregunta": "¿Qué elemento tiene el símbolo H?", "Respuestas": {"Hidrógeno": True, "Helio": False, "Oro": False, "Carbono": False}},
        {"Pregunta": "¿Qué animal se considera el rey de la selva?", "Respuestas": {"Tigre": False, "León": True, "Elefante": False, "Oso": False}},
    ]
    preguntas_deporte = [
        {"Pregunta": "¿En qué deporte se usa una red alta y una pelota?", "Respuestas": {"Baloncesto": False, "Tenis": True, "Fútbol": False, "Béisbol": False}},
        {"Pregunta": "¿Qué deporte practica Lionel Messi?", "Respuestas": {"Tenis": False, "Fútbol": True, "Baloncesto": False, "Natación": False}},
        {"Pregunta": "¿Qué país ganó la Copa del Mundo en 2018?", "Respuestas": {"Brasil": False, "Francia": True, "Argentina": False, "Alemania": False}},
        {"Pregunta": "¿Cuántos jugadores hay en un equipo de baloncesto?", "Respuestas": {"6": False, "5": True, "7": False, "11": False}},
        {"Pregunta": "¿Qué deportista tiene el récord de más medallas olímpicas?", "Respuestas": {"Usain Bolt": False, "Michael Phelps": True, "Carl Lewis": False, "Simone Biles": False}},
        {"Pregunta": "¿En qué deporte se utiliza un bate?", "Respuestas": {"Baloncesto": False, "Fútbol": False, "Béisbol": True, "Hockey": False}},
        {"Pregunta": "¿Qué país es famoso por su equipo de rugby llamado los All Blacks?", "Respuestas": {"Sudáfrica": False, "Nueva Zelanda": True, "Australia": False, "Inglaterra": False}},
        {"Pregunta": "¿Quién es conocido como 'El Rey del Fútbol'?", "Respuestas": {"Cristiano Ronaldo": False, "Pelé": True, "Lionel Messi": False, "Diego Maradona": False}},
        {"Pregunta": "¿Qué deporte se juega en Wimbledon?", "Respuestas": {"Fútbol": False, "Tenis": True, "Golf": False, "Baloncesto": False}},
        {"Pregunta": "¿En qué año ganó Argentina la Copa del Mundo de Fútbol por primera vez?", "Respuestas": {"1986": True, "1978": True, "1998": False, "2014": False}},
        {"Pregunta": "¿Quién tiene el récord de más títulos de Grand Slam en tenis?", "Respuestas": {"Roger Federer": False, "Rafael Nadal": False, "Novak Djokovic": True, "Pete Sampras": False}},
        {"Pregunta": "¿Qué jugador de baloncesto es conocido por el apodo 'Air Jordan'?", "Respuestas": {"LeBron James": False, "Kobe Bryant": False, "Michael Jordan": True, "Shaquille O'Neal": False}},
        {"Pregunta": "¿En qué deporte se lanzan discos?", "Respuestas": {"Lanzamiento de peso": False, "Lanzamiento de jabalina": False, "Lanzamiento de disco": True, "Salto de longitud": False}},
        {"Pregunta": "¿Qué país ganó la Copa América en 2021?", "Respuestas": {"Brasil": False, "Argentina": True, "Uruguay": False, "Chile": False}},
        {"Pregunta": "¿En qué deporte se utilizan los términos 'birdie' y 'eagle'?", "Respuestas": {"Fútbol": False, "Golf": True, "Cricket": False, "Tenis": False}},
        {"Pregunta": "¿Qué deportista fue apodado 'El Rayo'?", "Respuestas": {"Carl Lewis": False, "Usain Bolt": True, "Michael Johnson": False, "Mo Farah": False}},
        {"Pregunta": "¿Qué deporte tiene como objetivo derribar bolos?", "Respuestas": {"Cricket": False, "Tenis": False, "Bolos": True, "Hockey": False}},
        {"Pregunta": "¿Qué deporte se juega en el Super Bowl?", "Respuestas": {"Béisbol": False, "Baloncesto": False, "Fútbol americano": True, "Hockey": False}},
        {"Pregunta": "¿En qué país se originó el judo?", "Respuestas": {"China": False, "Japón": True, "Corea del Sur": False, "Brasil": False}},
        {"Pregunta": "¿Qué tenista ha ganado más títulos de Grand Slam en la historia?", "Respuestas": {"Serena Williams": True, "Steffi Graf": False, "Margaret Court": False, "Martina Navratilova": False}},
        {"Pregunta": "¿Qué equipo de fútbol tiene más títulos de la Champions League?", "Respuestas": {"Barcelona": False, "Real Madrid": True, "Manchester United": False, "Bayern Múnich": False}},
        {"Pregunta": "¿Qué país es conocido por el sumo?", "Respuestas": {"China": False, "Corea del Sur": False, "Japón": True, "India": False}},
        {"Pregunta": "¿Qué atleta ha ganado más medallas en un solo evento olímpico?", "Respuestas": {"Michael Phelps": True, "Usain Bolt": False, "Simone Biles": False, "Carl Lewis": False}},
        {"Pregunta": "¿Quién es el futbolista conocido como 'La Pulga'?", "Respuestas": {"Cristiano Ronaldo": False, "Pelé": False, "Lionel Messi": True, "Diego Maradona": False}},
        {"Pregunta": "¿Qué país organizó los Juegos Olímpicos de 2021?", "Respuestas": {"China": False, "Japón": True, "Brasil": False, "Rusia": False}},
        {"Pregunta": "¿En qué deporte se juega con una pelota ovalada?", "Respuestas": {"Fútbol americano": True, "Béisbol": False, "Tenis": False, "Baloncesto": False}},
        {"Pregunta": "¿Qué ciclista ha ganado el Tour de Francia más veces?", "Respuestas": {"Eddy Merckx": False, "Chris Froome": False, "Lance Armstrong": True, "Miguel Induráin": False}},
        {"Pregunta": "¿En qué país se celebró el Mundial de Fútbol de 2010?", "Respuestas": {"Alemania": False, "Sudáfrica": True, "Brasil": False, "Rusia": False}},
        {"Pregunta": "¿Qué deporte se juega en el US Open?", "Respuestas": {"Golf": False, "Tenis": True, "Fútbol americano": False, "Baloncesto": False}},
        {"Pregunta": "¿Qué país es famoso por la lucha libre conocida como 'Lucha Libre'?", "Respuestas": {"Brasil": False, "México": True, "Japón": False, "Estados Unidos": False}},
        {"Pregunta": "¿Qué selección de fútbol ganó el Mundial en 2010?", "Respuestas": {"España": True, "Alemania": False, "Brasil": False, "Francia": False}},
    ]

    categorias = {
        "Geografía": preguntas_geografia,
        "Historia": preguntas_historia,
        "Entretenimiento": preguntas_entretenimiento,
        "Ciencia": preguntas_ciencia,
        "Deporte": preguntas_deporte,
    }

    categoria_aleatoria = random.choice(list(categorias.keys()))
    preguntas_categoria = categorias[categoria_aleatoria]
    pregunta_aleatoria = random.choice(preguntas_categoria)

    return categoria_aleatoria, pregunta_aleatoria




def mostrar_final_juego():
    """Instrucciones que se muestran tras finalizar un juego.

    Returns:
        int: devuelve un 1,2,o3 dependiendo de la opción seleccionada.
    """
    print("\n═════════════════════════════════════")
    print(" Elija una opción:")
    print("   1. Volver a jugar")
    print("   2. Volver al menú principal")
    print("   3. Salir")
    while True:
        try:
            seleccion_final = int(input("👉 Tu opción: "))
            if seleccion_final not in [1,2,3]:
                print("\nPor favor introduzca un 1, 2 o 3.")
            else:
                break
        except ValueError:
            print("\nPor favor introduzca un 1, 2 o 3.")
    print("═════════════════════════════════════\n")
    return seleccion_final