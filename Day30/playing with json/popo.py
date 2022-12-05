# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome10_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Datum:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    def __init__(self, id: int, email: str, first_name: str, last_name: str, avatar: str) -> None:
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        email = from_str(obj.get("email"))
        first_name = from_str(obj.get("first_name"))
        last_name = from_str(obj.get("last_name"))
        avatar = from_str(obj.get("avatar"))
        return Datum(id, email, first_name, last_name, avatar)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["email"] = from_str(self.email)
        result["first_name"] = from_str(self.first_name)
        result["last_name"] = from_str(self.last_name)
        result["avatar"] = from_str(self.avatar)
        return result


class Support:
    url: str
    text: str

    def __init__(self, url: str, text: str) -> None:
        self.url = url
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'Support':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        text = from_str(obj.get("text"))
        return Support(url, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["text"] = from_str(self.text)
        return result


class Welcome10:
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Datum]
    support: Support

    def __init__(self, page: int, per_page: int, total: int, total_pages: int, data: List[Datum], support: Support) -> None:
        self.page = page
        self.per_page = per_page
        self.total = total
        self.total_pages = total_pages
        self.data = data
        self.support = support

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome10':
        assert isinstance(obj, dict)
        page = from_int(obj.get("page"))
        per_page = from_int(obj.get("per_page"))
        total = from_int(obj.get("total"))
        total_pages = from_int(obj.get("total_pages"))
        data = from_list(Datum.from_dict, obj.get("data"))
        support = Support.from_dict(obj.get("support"))
        return Welcome10(page, per_page, total, total_pages, data, support)

    def to_dict(self) -> dict:
        result: dict = {}
        result["page"] = from_int(self.page)
        result["per_page"] = from_int(self.per_page)
        result["total"] = from_int(self.total)
        result["total_pages"] = from_int(self.total_pages)
        result["data"] = from_list(lambda x: to_class(Datum, x), self.data)
        result["support"] = to_class(Support, self.support)
        return result


def welcome10_from_dict(s: Any) -> Welcome10:
    return Welcome10.from_dict(s)


def welcome10_to_dict(x: Welcome10) -> Any:
    return to_class(Welcome10, x)
