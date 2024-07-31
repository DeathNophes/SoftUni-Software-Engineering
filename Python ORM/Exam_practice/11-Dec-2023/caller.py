import os

import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match

# Create queries within functions


def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ''

    if search_name is not None and search_country is not None:
        query = (Q(full_name__icontains=search_name) & Q(country__icontains=search_country))
    elif search_name is None:
        query = Q(country__icontains=search_country)
    else:
        query = Q(full_name__icontains=search_name)

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players:
        return ''

    result = []
    for p in players:
        result.append(
            f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}"
        )

    return '\n'.join(result)


def get_top_tennis_player():
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not top_player:
        return ''

    return f"Top Tennis Player: {top_player.full_name} with {top_player.wins_count} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects\
        .annotate(played_matches=Count('match_players'))\
        .filter(played_matches__gt=0)\
        .order_by('-played_matches', 'ranking')\
        .first()

    # We search for the player with most matches, therefore they should be greater than 0

    if not player:
        return ''

    return f"Tennis Player: {player.full_name} with {player.played_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ''

    tournaments = Tournament.objects\
        .annotate(matches_count=Count('match_tournament'))\
        .filter(surface_type__icontains=surface)\
        .order_by('-start_date')

    if not tournaments:
        return ''

    result = []
    for t in tournaments:
        result.append(
            f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.matches_count}"
        )

    return '\n'.join(result)


def get_latest_match_info():
    match = Match.objects.order_by('date_played').last()

    if not match:
        return ''

    players = match.players.order_by('full_name')

    winner = 'TBA' if match.winner is None else match.winner.full_name

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {players[0].full_name} vs {players[1].full_name}, "
            f"winner: {winner}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return 'No matches found.'

    matches = Match.objects\
        .prefetch_related('tournament')\
        .filter(tournament__name=tournament_name)\
        .order_by('-date_played')

    if not matches or not Tournament.objects.all():
        return 'No matches found.'

    result = []
    for m in matches:
        result.append(
            f"Match played on: {m.date_played}, "
            f"score: {m.score}, "
            f"winner: {m.winner.full_name if m.winner is not None else 'TBA'}"
        )

    return '\n'.join(result)
