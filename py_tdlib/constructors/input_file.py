from ..factory import Type


class inputFileId(Type):
    # A file defined by its unique ID, @id Unique file identifier

    id = None  # type: "int32"


class inputFileRemote(Type):
    # A file defined by its remote ID, @id Remote file identifier

    id = None  # type: "string"


class inputFileLocal(Type):
    # A file defined by a local path, @path Local path to the file

    path = None  # type: "string"


class inputFileGenerated(Type):
    # A file generated by the client, @original_path Local path to
    # a file from which the file is generated; may be
    # empty if there is no such file, @conversion String specifying
    # the conversion applied to the original file; should be persistent
    # across application restarts, @expected_size Expected size of the generated file; 0 if unknown

    original_path = None  # type: "string"
    conversion = None  # type: "string"
    expected_size = None  # type: "int32"
