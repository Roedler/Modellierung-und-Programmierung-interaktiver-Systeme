import random
import time

from Hausaufgaben.Aufgabe_2.Aufgabe_2_1.bubble_sort import bubble_sort
from Hausaufgaben.Aufgabe_2.Aufgabe_2_1.insertion_sort import insertion_sort
from Hausaufgaben.Aufgabe_2.Aufgabe_2_1.selection_sort import selection_sort
from Hausaufgaben.Aufgabe_3.Aufgabe_3_1.quicksort import quicksort, quicksortOptimized
from Hausaufgaben.Aufgabe_3.Aufgabe_3_4.Movie import Movie
from Vorlesungen.Vorlesung_2.fakultaet import fakultaet


def testFakultaet(number):
    print(f"Zahl:\t\t{number:_}")
    startTime = time.perf_counter()
    print(f"Fakultät:\t{fakultaet(number):_}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

def testQuicksort(max):
    print("======================== testQuicksort() =========================")

    array = [random.randint(0, max) for _ in range(max)]

    startTime = time.perf_counter()
    quicksort(array)
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden (Array)")

def testQuicksortOptimized(max):
    print("==================== testQuicksortOptimized() ====================")

    array = [random.randint(0, max) for _ in range(max)]

    startTime = time.perf_counter()
    quicksortOptimized(array, 0, len(array) - 1)
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden (Array)")

def testSelectionSort(max):
    print("==================== testSelectionSort() ====================")

    array = [random.randint(0, max) for _ in range(max)]

    startTime = time.perf_counter()
    selection_sort(array, len(array))
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden (Array)")

def testInsertionSort(max):
    print("==================== testInsertionSort() ====================")

    array = [random.randint(0, max) for _ in range(max)]

    startTime = time.perf_counter()
    insertion_sort(array)
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden (Array)")

def testBubbleSort(max):
    print("==================== testBubbleSort() ====================")

    array = [random.randint(0, max) for _ in range(max)]

    startTime = time.perf_counter()
    bubble_sort(array)
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden (Array)")

def testMovieDatabase(searchRequests: list[str]):
    print("==================== testFilmDatabase() ====================")

    movieDataBase = {
        "Die Verurteilten": Movie(
            name="Die Verurteilten",
            year=1994,
            directing=["Frank Darabont"],
            director=["Tim Robbins", "Morgan Freeman"],
            description="Zwei Häftlinge freunden sich über Jahre hinweg an und finden Trost und Erlösung durch grundlegende Menschlichkeit."
        ),
        "Der Pate": Movie(
            name="Der Pate",
            year=1972,
            directing=["Francis Ford Coppola"],
            director=["Marlon Brando", "Al Pacino", "James Caan"],
            description="Der alternde Patriarch einer organisierten Kriminaldynastie übergibt die Kontrolle über sein geheimes Imperium an seinen widerstrebenden Sohn."
        ),
        "The Dark Knight": Movie(
            name="The Dark Knight",
            year=2008,
            directing=["Christopher Nolan"],
            director=["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
            description="Als der Joker in Gotham auftaucht, muss Batman eine der größten psychologischen und physischen Prüfungen seiner Fähigkeit, Ungerechtigkeit zu bekämpfen, bestehen."
        ),
        "Pulp Fiction": Movie(
            name="Pulp Fiction",
            year=1994,
            directing=["Quentin Tarantino"],
            director=["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
            description="Die Leben von zwei Auftragskillern, einem Boxer, der Frau eines Gangsters und einem Paar Diner-Banditen verweben sich in vier Geschichten von Gewalt und Erlösung."
        ),
        "Inception": Movie(
            name="Inception",
            year=2010,
            directing=["Christopher Nolan"],
            director=["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
            description="Ein Dieb, der die Geheimnisse von Unternehmen stiehlt, indem er in die Träume anderer eindringt, erhält die umgekehrte Aufgabe, eine Idee in den Verstand eines CEOs einzupflanzen."
        ),
        "Forrest Gump": Movie(
            name="Forrest Gump",
            year=1994,
            directing=["Robert Zemeckis"],
            director=["Tom Hanks", "Robin Wright", "Gary Sinise"],
            description="Die Präsidentschaften von Kennedy und Johnson, der Vietnamkrieg, das Watergate und andere historische Ereignisse entfalten sich aus der Perspektive eines Mannes aus Alabama mit einem IQ von 75."
        ),
        "Parasite": Movie(
            name="Parasite",
            year=2019,
            directing=["Bong Joon Ho"],
            director=["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
            description="Gier und Klassendiskriminierung bedrohen die neu geschmiedete Beziehung zwischen der wohlhabenden Familie Park und dem mittellosen Clan der Kims."
        ),
        "Gladiator": Movie(
            name="Gladiator",
            year=2000,
            directing=["Ridley Scott"],
            director=["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
            description="Ein ehemaliger römischer General will sich rächen an dem korrupten Kaiser, der seine Familie ermordet und ihn in die Sklaverei geschickt hat."
        ),
        "Das Imperium schlägt zurück": Movie(
            name="Das Imperium schlägt zurück",
            year=1980,
            directing=["Irvin Kershner"],
            director=["Mark Hamill", "Harrison Ford", "Carrie Fisher"],
            description="Nachdem die Rebellen von einer Eiswelt vertrieben wurden, wird Luke Skywalker im Dagobah-System vom Jedi-Meister Yoda ausgebildet."
        ),
        "Interstellar": Movie(
            name="Interstellar",
            year=2014,
            directing=["Christopher Nolan"],
            director=["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
            description="Ein Team von Entdeckern reist durch ein Wurmloch im Weltraum, um das Überleben der Menschheit zu sichern."
        )
    }

    for title in searchRequests:
        print(f"Suche nach Film: '{title}'")
        movie = movieDataBase.get(title)
        if movie:
            print(movie)
        else:
            print(f"--- ERGEBNIS ---")
            print(f"   Film '{title}' nicht in der Datenbank gefunden.\n")


max = 900
# testFakultaet(5)
# testQuicksort(max)
# testSelectionSort(max)
# testInsertionSort(max)
# testBubbleSort(max)

suchanfragen = [
    "Inception",
    "Der Pate",
    "Alien",
    "Interstellar"
]

testMovieDatabase(suchanfragen)
