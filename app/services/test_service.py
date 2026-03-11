from datetime import datetime
from sqlalchemy.orm import Session

from models.test import Test

def get_test_service(db: Session):
    data = db.query(Test).first()

    if data:
        status = "OK"
    else:
        status = "No data"

    return {
        "status": status,
        "received_at": datetime.now()
    }
        