import aiohttp

from aiohttp_jinja2 import template
from sqlalchemy import select, insert, delete

from demo import db


@template("index.html")
async def index(request):
    site_name = request.app["config"].get("site_name")
    return {"site_name": site_name}


async def post(request):
    async with request.app["db"].acquire() as conn:
        query = select([db.post])
        result = await conn.fetch(query)

    return aiohttp.web.Response(body=str(result))


async def delete_by_id(request):
    params = request.rel_url.query
    if not "id" in params:
        return aiohttp.web.Response(body="")

    async with request.app["db"].acquire() as conn:
        stmt = delete(db.post).where(db.post.c.id == int(params["id"]))
        result = await conn.execute(stmt)
    return aiohttp.web.Response(body=str(result))


async def write_to_db(request):
    params = request.rel_url.query
    async with request.app["db"].acquire() as conn:
        stmt = insert(db.post).values(
            {
                "title": params.get("title", "default value"),
                "body": params.get("body"),
                "jsonb_field": params.get("jsonb_field"),
            }
        )
        result = await conn.execute(stmt)

    return aiohttp.web.Response(body=str(result))
