import httpx
import pytest
import respx

from library_catalog.domain.exceptions import (
    OpenLibraryException,
    OpenLibraryTimeoutException,
)
from library_catalog.external.openlibrary.client import OpenLibraryClient

URL = "https://openlibrary.org/search.json"


@pytest.fixture
async def client():
    client = OpenLibraryClient()
    yield client
    await client.close()


@respx.mock
async def test_search_by_isbn_returns_cover_and_subjects(client):
    respx.get(URL).mock(
        return_value=httpx.Response(
            200,
            json={"docs": [{"cover_i": 123, "subject": ["Fantasy"]}]},
        )
    )

    result = await client.search_by_isbn("9780000000000")

    assert result["cover_url"] == "https://covers.openlibrary.org/b/id/123-L.jpg"
    assert result["subjects"] == ["Fantasy"]


@respx.mock
async def test_timeout_becomes_domain_exception(client):
    respx.get(URL).mock(side_effect=httpx.ReadTimeout("slow"))

    with pytest.raises(OpenLibraryTimeoutException):
        await client.search_by_isbn("0")


@respx.mock
async def test_connection_error_becomes_domain_exception(client):
    respx.get(URL).mock(side_effect=httpx.ConnectError("down"))

    with pytest.raises(OpenLibraryException):
        await client.search_by_isbn("0")
