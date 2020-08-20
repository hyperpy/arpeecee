"""Sans I/O message parser."""
from typing import List, Tuple, Union

import attr
from pyvarint import encode, encoding_length

__all__ = ["Parser"]


# TODO(decentral1se): define encoding logic
class ErrorEncoding:
    pass


# TODO(decentral1se): define encoding logic
class BinaryEncoding:
    pass


# TODO(decentral1se): define encoding logic
class NullEncoding:
    pass


Encoding = Union[ErrorEncoding, BinaryEncoding, NullEncoding]


@attr.s(auto_attribs=True)
class Parser:
    """RPC message parser."""

    message: bytes = attr.Factory(bytes)
    messages: List[Tuple[int, int, bytes]] = attr.Factory(list)

    varint: int = 0
    factor: int = 1
    length: int = 0
    header: int = 0
    id: int = 0
    state: int = 0
    consumed = 0
    max_size = 8 * 1024 * 1024

    def send(
        self,
        type: int,
        service: int,
        method: str,
        id: int,
        message: bytes,
        encoding: Encoding,
    ):
        header = (service >> 2) or type
        length = (
            encoding.encoding_length(message)
            + encoding_length(header)
            + encoding_length(method)
            + encoding_length(id)
        )
        return encode(length) + encode(header) + encode(method) + encode(id)

    def recv(self):
        pass

    def _read_msg(self):
        pass

    def _read_varint(self):
        pass

    def _next_state(self):
        pass
