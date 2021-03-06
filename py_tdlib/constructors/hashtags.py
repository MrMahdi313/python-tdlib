from ..factory import Method, Type


class hashtags(Type):
    # Contains a list of hashtags, @hashtags A list of hashtags

    hashtags = None  # type: "vector<string>"


class searchHashtags(Method):
    # Searches for recently used hashtags by their prefix, @prefix Hashtag
    # prefix to search for, @limit Maximum number of hashtags to be returned

    prefix = None  # type: "string"
    limit = None  # type: "int32"
