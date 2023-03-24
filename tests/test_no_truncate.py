from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_no_truncate():
    datasette = Datasette(memory=True)
    db = datasette.add_memory_database("test")
    bigstring = "a" * 10000
    await db.execute_write("create table t (x text)")
    await db.execute_write("insert into t (x) values (?)", (bigstring,))
    response = await datasette.client.get("/test/t")
    assert response.status_code == 200
    assert bigstring in response.text
