import sqlite3



class db:
  def __init__(self):
    self.con = sqlite3.connect('data.db')
    self.cur = self.con.cursor()
  
  async def make_table(self):
    self.cur.execute("CREATE TABLE IF NOT EXISTS tags (title TEXT, content TEXT)")
    self.con.commit()
    print('done')
  
  async def make_tag(self, name, content):
    await self.make_table()
    self.cur.execute("INSERT INTO tags VALUES(?, ?)", (name.lower(), content))
    self.con.commit()
    print('done')
  
  async def get_tag(self, name):
    await self.make_table()
    self.cur.execute("SELECT content FROM tags WHERE title=?", [name.lower()])
    result = self.cur.fetchone()
    return result[0]
    print('done')
  
  async def delete_tag(self, name):
    await self.make_table()
    self.cur.execute("DELETE FROM tags WHERE title=?", [name.lower()])
    self.con.commit()
