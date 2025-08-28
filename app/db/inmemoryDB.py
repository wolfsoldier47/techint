from typing import Dict, Optional



class InMemDB:
  def __init__(self):
    self.notes: Dict[int, dict] = {}
    self.n_id: int = 0

  def create_note(self, title:str,content:str) -> int:
    n_id = self.n_id
    self.notes[n_id] = {"title": title, "content": content}
    self.n_id += 1
    return n_id
  
  def get_note(self, n_id: int) -> Optional[dict]:
    notes = ""
    try:
      notes = self.notes.get(n_id)
    except KeyError:
      notes = {"error":"no notes found"}
    return notes

  def update_note(self, n_id:int,title:Optional[str]=None,content:Optional[str]=None) -> Optional[dict]:
    note = self.notes.get(n_id)
    if note is None:
      return None
    if title is not None:
      note["title"] = title
    if content is not None:
      note["content"] = content
    self.notes[n_id] = note
    return note

  def delete_note(self,n_id:int) ->bool:
    if n_id in self.notes:
      del self.notes[n_id]
      return True
    return False
  
  def list_notes(self) -> Dict[int, dict]:
    return self.notes

db = InMemDB()
