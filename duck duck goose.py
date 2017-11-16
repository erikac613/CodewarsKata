def duck_duck_goose(players, goose):
    goose -= 1
    goose %= len(players)
    return players[goose].name
