from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connector import get_db
from schemas.test_schema import TestResponse
from services.test_service import get_test_service

router = APIRouter()

@router.get("/", response_model=TestResponse)
def get_test(db: Session = Depends(get_db)):
    try:
        data = get_test_service(db)

        return data
    
    except Exception:
        raise HTTPException(status_code=500, detail="Error in server.")
    
