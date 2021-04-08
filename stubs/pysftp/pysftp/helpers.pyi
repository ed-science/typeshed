from typing import Callable, ContextManager, Iterator, List, Optional

def known_hosts() -> str: ...
def st_mode_to_int(val: int) -> int: ...

class WTCallbacks:
    def __init__(self) -> None: ...
    def file_cb(self, pathname: str) -> None: ...
    def dir_cb(self, pathname: str) -> None: ...
    def unk_cb(self, pathname: str) -> None: ...
    @property
    def flist(self) -> List[str]: ...
    @flist.setter
    def flist(self, val: List[str]) -> None: ...
    @property
    def dlist(self) -> List[str]: ...
    @dlist.setter
    def dlist(self, val: List[str]) -> None: ...
    @property
    def ulist(self) -> List[str]: ...
    @ulist.setter
    def ulist(self, val: List[str]) -> None: ...

def path_advance(thepath: str, sep: str = ...) -> Iterator[str]: ...
def path_retreat(thepath: str, sep: str = ...) -> Iterator[str]: ...
def reparent(newparent: str, oldpath: str) -> str: ...

_PathCallback = Callable[[str], None]

def walktree(
    localpath: str, fcallback: _PathCallback, dcallback: _PathCallback, ucallback: _PathCallback, recurse: bool = ...
) -> None: ...
def cd(localpath: Optional[str] = ...) -> ContextManager[None]: ...