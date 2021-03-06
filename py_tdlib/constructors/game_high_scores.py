from ..factory import Method, Type


class gameHighScores(Type):
    # Contains a list of game high scores, @scores A list
    # of game high scores

    scores = None  # type: "vector<gameHighScore>"


class getGameHighScores(Method):
    # Returns the high scores for a game and some part
    # of the high score table in the range of the
    # specified user; for bots only, @chat_id The chat that contains
    # the message with the game, @message_id Identifier of the message, @user_id User identifier

    chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    user_id = None  # type: "int32"


class getInlineGameHighScores(Method):
    # Returns game high scores and some part of the high
    # score table in the range of the specified user; for
    # bots only, @inline_message_id Inline message identifier, @user_id User identifier

    inline_message_id = None  # type: "string"
    user_id = None  # type: "int32"
