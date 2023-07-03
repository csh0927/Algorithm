def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    for who in callings:
        rank = result[who]
        result[who] -= 1
        result[players[rank-1]] += 1
        players[rank-1], players[rank] = players[rank], players[rank-1]
    return players