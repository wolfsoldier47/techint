
from fastapi import APIRouter,Request


from fastapi.responses import JSONResponse


from db.inmemoryDB import db as inMemDB
from model.notes import NoteCreate,NoteUpdate

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import Request

from core.config import settings
from logs.logging import Logger

router = APIRouter(prefix="/notes", tags=["notes"])


#adding rate limiter
limiter = Limiter(key_func=get_remote_address)


#adding logger
logg = Logger()


@router.get("/", summary="List all notes")
@limiter.limit(settings.RATE_LIMIT)
async def list_notes(request: Request, next_page: int = 0, limit: int = settings.PAGINATION_LIMIT):
  logg.log_info("Get with pagination")
  notes = inMemDB.list_notes()
  if not notes:
    return JSONResponse(status_code=404, content={"error": "no notes found"})
  notes_list = [ {"id": k, **v} for k, v in sorted(notes.items()) ]
  total = len(notes_list)
  total_pages = (total + limit - 1) // limit
    # Clamp next_page to valid range
  page = max(1, min(next_page, total_pages))
  start = (page - 1) * limit
  end = start + limit
  paginated = notes_list[start:end]
    # List of next pages (page numbers)
  next_pages = list(range(1, total_pages + 1)) if total_pages > 1 else []
  return JSONResponse(
      status_code=200,
      content={
        "total": total,
        "limit": limit,
        "total_pages": total_pages,
        "current_page": page,
        "next_page": next_pages,
        "data": paginated
      }
    )


@router.get("/{id}", summary="List single note")
@limiter.limit(settings.RATE_LIMIT)
async def get_note(request: Request, id: int):
  logg.log_info("Get by id")
  note = inMemDB.get_note(id)
  if note is None:
    return JSONResponse(status_code=404, content={"error": "no notes found"})
  else:
    return JSONResponse(status_code=200, content=note)

@router.post("/")
@limiter.limit(settings.RATE_LIMIT)
async def create_note(request:Request,note: NoteCreate):
  n_id = inMemDB.create_note(note.title, note.content)
  if n_id is None:
    return JSONResponse(status_code=400, content={"error": "note not created"})
  else:
    return JSONResponse(status_code=201, content={"id": n_id, "title": note.title, "content": note.content})

@router.put("/{n_id}")
@limiter.limit(settings.RATE_LIMIT)
async def update_note(request: Request,note: NoteUpdate,n_id: int, title: str = None, content: str = None):

  note = inMemDB.update_note(n_id, note.title, note.content)
  if note is None:
    return JSONResponse(status_code=404, content={"error": "no notes found"})
  else:
    return JSONResponse(status_code=200, content=note)

@router.delete("/{n_id}")
@limiter.limit(settings.RATE_LIMIT)
async def delete_note(request: Request,n_id: int):
  deleted = inMemDB.delete_note(n_id)
  if not deleted:
    return JSONResponse(status_code=404, content={"error": "no notes found"})
  else:
    return JSONResponse(status_code=200, content={"message": "note deleted"})
  