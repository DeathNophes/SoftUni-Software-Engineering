from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        try:
            musician = self.VALID_MUSICIANS[musician_type](name, age)
        except KeyError:
            raise ValueError("Invalid musician type!")

        for m in self.musicians:
            if m.name == name:
                raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]

        if not self.is_one_member_of_each_type(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            if not self.can_the_band_play_rock_concert(band):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            if not self.can_the_band_play_metal_concert(band):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            if not self.can_the_band_play_jazz_concert(band):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = self.calculate_profit(band, concert)

        return profit

    def is_one_member_of_each_type(self, band):
        guitarists = 0
        drummers = 0
        singers = 0

        for member in band.members:
            if member.__class__.__name__ == 'Guitarist':
                guitarists += 1
            elif member.__class__.__name__ == 'Drummer':
                drummers += 1
            elif member.__class__.__name__ == 'Singer':
                singers += 1

        if guitarists > 0 and drummers > 0 and singers > 0:
            return True
        return False

    def can_the_band_play_rock_concert(self, band):
        required_skills = [
            'play the drums with drumsticks',
            'sing high pitch notes',
            'play rock'
        ]

        skills = set()

        for musician in band.members:
            for skill in musician.skills:
                if skill in required_skills:
                    skills.add(skill)

        if len(skills) == len(required_skills):
            return True
        return False

    def can_the_band_play_metal_concert(self, band):
        required_skills = [
            'play the drums with drumsticks',
            'sing low pitch notes',
            'play metal'
        ]

        skills = set()

        for musician in band.members:
            for skill in musician.skills:
                if skill in required_skills:
                    skills.add(skill)

        if len(skills) == len(required_skills):
            return True
        return False

    def can_the_band_play_jazz_concert(self, band):
        required_skills = [
            'play the drums with drum brushes',
            'sing high pitch notes',
            'sing low pitch notes',
            'play jazz'
        ]

        skills = set()

        for musician in band.members:
            for skill in musician.skills:
                if skill in required_skills:
                    skills.add(skill)

        if len(skills) == len(required_skills):
            return True
        return False

    def calculate_profit(self, band, concert):
        total_profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {total_profit:.2f}$ from the {concert.genre} concert in {concert.place}."

