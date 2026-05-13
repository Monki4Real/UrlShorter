from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session
from datetime import datetime

from app.utils.code_generator import generate_short_code 
from app.database import get_db  
from app import schemas 
from app.models import UrlsBase
from starlette.responses import RedirectResponse


router = APIRouter(
    prefix="/api",
    tags=['urls']
) 


@router.post('/shorten', response_model=schemas.GetUrl)
def create_short_url(
    url_data: schemas.CreateUrl,
    db: Session = Depends(get_db)
):
    short_code = generate_short_code(db)

    new_url = UrlsBase(
        short_code = short_code,
        original_url = str(url_data.original_url),
        created_at=datetime.now(),
        clicks=0,
        last_accessed = None
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return schemas.GetUrl(
        short_code=new_url.short_code,
        original_url=url_data.original_url,
        created_at=new_url.created_at
    )
    

@router.get('/{short_code}')
def redirect_to_original(
    short_code:str,
    db: Session = Depends(get_db)
):
    
    find_url = db.query(UrlsBase).filter(UrlsBase.short_code == short_code).first()

    if not find_url:
        raise HTTPException(status_code=404, detail='Short URL not found')
    
    find_url.clicks += 1
    find_url.last_accessed = datetime.now()
    db.commit()

    return RedirectResponse(url=find_url.original_url, status_code=307)

@router.get('stats/{short_code}')
def get_stats_shortcode(
    short_code:str,
    db: Session = Depends(get_db)
):
    get_stats = db.query(UrlsBase).filter(UrlsBase.short_code == short_code).first()

    if not get_stats:
        raise HTTPException(status_code=404, detail='Short URL not found')
    
    return schemas.Statistics(
        short_code=get_stats.short_code,
        original_url=get_stats.original_url,
        created_at=get_stats.created_at,
        clicks=get_stats.clicks
    )