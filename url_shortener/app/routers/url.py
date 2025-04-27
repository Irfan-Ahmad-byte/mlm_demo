from http.client import HTTPResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse, RedirectResponse

from app import schemas, crud
from app.database import get_db



router = APIRouter()


@router.post("/shorten", response_model=schemas.URLInfo)
def shorten_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, url)


@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    url_obj = crud.get_url_by_short_code(db, short_code)
    if not url_obj:
        raise HTTPException(status_code=404, detail="URL not found")
    return JSONResponse({"url":url_obj.original_url})
