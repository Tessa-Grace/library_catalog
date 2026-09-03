# test_ol_client.py
import asyncio
from src.library_catalog.external.openlibrary.client import OpenLibraryClient


async def test():
    client = OpenLibraryClient()
    
    # Тест по ISBN
    print("🔍 Поиск по ISBN...")
    data = await client.search_by_isbn("9780132350884")
    print(f"✅ По ISBN найдено: {data}")
    
    # Тест по title+author
    print("🔍 Поиск по названию и автору...")
    data = await client.search_by_title_author(
        "Clean Code",
        "Robert Martin"
    )
    print(f"✅ По названию/автору найдено: {data}")
    
    await client.close()


if __name__ == "__main__":
    asyncio.run(test())