import aiosqlite

async def make_tag(name, content):
  async with aiosqlite.connect('data.db') as con:
    await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    await con.execute(f"INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
    await con.commit()
    print("done")

async def get_tag(name):
  async with aiosqlite.connect('data.db') as con:
    await con.execute("CREATE TABLE IF NOT EXISTS tags(title TEXT, content TEXT)")
    async with con.execute("SELECT content FROM tags WHERE title=?", [name.lower()]) as cur:
      result = await cur.fetchone()
      return result[0]
      print("done")

async def delete_tag(name):
  async with aiosqlite.connect('data.db') as con:
    await con.execute("CREATE TABLE IF NOT EXISTS tags (title TEXT, content TEXT)")
    await con.execute("DELETE FROM tags WHERE title=?", [name.lower()])
    await con.commit()
    print("done")

class dbOps:
  def __init__(self):
    print("Ready!")

  async def make_table(self):
    async with aiosqlite.connect('data.db') as con:
      await con.execute

  async def make_tag(self, name, content):
    async with aiosqlite.connect('data.db') as con:
      await con.execute("INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
