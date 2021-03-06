from ..factory import Type


class inputMessageText(Type):
    # A text message, @text Formatted text to be sent; 1-GetOption("message_text_length_max")
    # characters. Only Bold, Italic, Code, Pre, PreCode and TextUrl entities
    # are allowed to be specified manually

    text = None  # type: "formattedText"
    disable_web_page_preview = None  # type: "Bool"
    clear_draft = None  # type: "Bool"


class inputMessageAnimation(Type):
    # An animation message (GIF-style)., @animation Animation file to be sent
    # @thumbnail Animation thumbnail, if available, @duration Duration of the animation,
    # in seconds, @width Width of the animation; may be replaced
    # by the server, @height Height of the animation; may be
    # replaced by the server, @caption Animation caption; 0-GetOption("message_caption_length_max") characters

    animation = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    duration = None  # type: "int32"
    width = None  # type: "int32"
    height = None  # type: "int32"
    caption = None  # type: "formattedText"


class inputMessageAudio(Type):
    # An audio message, @audio Audio file to be sent, @album_cover_thumbnail
    # Thumbnail of the cover for the album, if available, @duration
    # Duration of the audio, in seconds; may be replaced by
    # the server, @title Title of the audio; 0-64 characters; may
    # be replaced by the server

    audio = None  # type: "InputFile"
    album_cover_thumbnail = None  # type: "inputThumbnail"
    duration = None  # type: "int32"
    title = None  # type: "string"
    performer = None  # type: "string"
    caption = None  # type: "formattedText"


class inputMessageDocument(Type):
    # A document message (general file), @document Document to be sent
    # @thumbnail Document thumbnail, if available, @caption Document caption; 0-GetOption("message_caption_length_max") characters

    document = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    caption = None  # type: "formattedText"


class inputMessagePhoto(Type):
    # A photo message, @photo Photo to send, @thumbnail Photo thumbnail
    # to be sent, this is sent to the other party
    # in secret chats only, @added_sticker_file_ids File identifiers of the stickers
    # added to the photo, if applicable, @width Photo width, @height
    # Photo height, @caption Photo caption; 0-GetOption("message_caption_length_max") characters

    photo = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    added_sticker_file_ids = None  # type: "vector<int32>"
    width = None  # type: "int32"
    height = None  # type: "int32"
    caption = None  # type: "formattedText"
    ttl = None  # type: "int32"


class inputMessageSticker(Type):
    # A sticker message, @sticker Sticker to be sent, @thumbnail Sticker
    # thumbnail, if available, @width Sticker width, @height Sticker height

    sticker = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    width = None  # type: "int32"
    height = None  # type: "int32"


class inputMessageVideo(Type):
    # A video message, @video Video to be sent, @thumbnail Video
    # thumbnail, if available, @added_sticker_file_ids File identifiers of the stickers added
    # to the video, if applicable

    video = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    added_sticker_file_ids = None  # type: "vector<int32>"
    duration = None  # type: "int32"
    width = None  # type: "int32"
    height = None  # type: "int32"
    supports_streaming = None  # type: "Bool"
    caption = None  # type: "formattedText"
    ttl = None  # type: "int32"


class inputMessageVideoNote(Type):
    # A video note message, @video_note Video note to be sent
    # @thumbnail Video thumbnail, if available, @duration Duration of the video,
    # in seconds, @length Video width and height; must be positive
    # and not greater than 640

    video_note = None  # type: "InputFile"
    thumbnail = None  # type: "inputThumbnail"
    duration = None  # type: "int32"
    length = None  # type: "int32"


class inputMessageVoiceNote(Type):
    # A voice note message, @voice_note Voice note to be sent
    # @duration Duration of the voice note, in seconds, @waveform Waveform
    # representation of the voice note, in 5-bit format, @caption Voice
    # note caption; 0-GetOption("message_caption_length_max") characters

    voice_note = None  # type: "InputFile"
    duration = None  # type: "int32"
    waveform = None  # type: "bytes"
    caption = None  # type: "formattedText"


class inputMessageLocation(Type):
    # A message with a location, @location Location to be sent
    # @live_period Period for which the location can be updated, in
    # seconds; should bebetween 60 and 86400 for a live location and 0 otherwise

    location = None  # type: "location"
    live_period = None  # type: "int32"


class inputMessageVenue(Type):
    # A message with information about a venue, @venue Venue to send

    venue = None  # type: "venue"


class inputMessageContact(Type):
    # A message containing a user contact, @contact Contact to send

    contact = None  # type: "contact"


class inputMessageGame(Type):
    # A message with a game; not supported for channels or
    # secret chats, @bot_user_id User identifier of the bot that owns
    # the game, @game_short_name Short name of the game

    bot_user_id = None  # type: "int32"
    game_short_name = None  # type: "string"


class inputMessageInvoice(Type):
    # A message with an invoice; can be used only by
    # bots and only in private chats, @invoice Invoice, @title Product
    # title; 1-32 characters, @param_description Product description; 0-255 characters, @photo_url Product
    # photo URL; optional, @photo_size Product photo size, @photo_width Product photo
    # width, @photo_height Product photo height

    invoice = None  # type: "invoice"
    title = None  # type: "string"
    description = None  # type: "string"
    photo_url = None  # type: "string"
    photo_size = None  # type: "int32"
    photo_width = None  # type: "int32"
    photo_height = None  # type: "int32"
    payload = None  # type: "bytes"
    provider_token = None  # type: "string"
    provider_data = None  # type: "string"
    start_parameter = None  # type: "string"


class inputMessageForwarded(Type):
    # A forwarded message, @from_chat_id Identifier for the chat this forwarded
    # message came from, @message_id Identifier of the message to forward
    # @in_game_share True, if a game message should be shared within
    # a launched game; applies only to game messages

    from_chat_id = None  # type: "int53"
    message_id = None  # type: "int53"
    in_game_share = None  # type: "Bool"
