class Movie:
    def __init__(self, name: str, year: int, directing: list, director: list, description: str):
        self.name = name
        self.year = year
        self.directing = directing
        self.director = director
        self.description = description

    def __str__(self) -> str:
        """
        Erzeugt eine schön formatierte Zeichenkette für die Filmausgabe.
        """
        # Listen schön formatieren (z.B. "Christopher Nolan, Leonardo DiCaprio")
        directing_str = ", ".join(self.directing)
        director_str = ", ".join(self.director)

        return (
            f"--- {self.name.upper()} ({self.year}) ---\n"
            f"   Regie: {directing_str}\n"
            f"   Darsteller: {director_str}\n"
            f"   Handlung: {self.description}\n"
        )
