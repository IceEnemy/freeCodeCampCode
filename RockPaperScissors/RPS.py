def player(prev_play, opponent_history=[], play_order={}):
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)
    else:
        opponent_history.append('S')
    
    # Initialize the play_order dictionary if it's empty
    if not play_order:
        for move1 in ['R', 'P', 'S']:
            for move2 in ['R', 'P', 'S']:
                for move3 in ['R', 'P', 'S']:
                    for move4 in ['R', 'P', 'S']:
                        for move5 in ['R', 'P', 'S']:
                            play_order[move1 + move2 + move3 + move4 + move5] = 0
    
    # Handle cases where we don't have enough history
    if len(opponent_history) < 5:
        return "S"
    
    # Markov chain for predicting the opponent's next move
    last_five = "".join(opponent_history[-5:])
    if len(last_five) == 5:
        play_order[last_five] += 1

    # Predict the next move based on the highest frequency of the last five moves
    last_four = "".join(opponent_history[-4:])
    potential_plays = [last_four + "R", last_four + "P", last_four + "S"]
    sub_order = {k: play_order[k] for k in potential_plays}
    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1]
    else:
        prediction = "R"
    
    # Determine the ideal response to the predicted move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
