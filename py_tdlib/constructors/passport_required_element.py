from ..factory import Type


class passportRequiredElement(Type):
    # Contains a description of the required Telegram Passport element that
    # was requested by a service, @suitable_elements List of Telegram Passport
    # elements any of which is enough to provide

    suitable_elements = None  # type: "vector<passportSuitableElement>"
