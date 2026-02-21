from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from add_book.db import get_db
from add_book.models import Address
from add_book.schemas import AddressCreate, AddressResponse
from add_book.utils import haversine_distance

router = APIRouter(prefix="/addresses", tags=["Addresses"])

@router.post("/", response_model=AddressResponse)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


# @router.get("/", response_model=list[AddressResponse])
# def list_addresses(db: Session = Depends(get_db)):
#     return db.query(Address).all()
@router.get("/", response_model=list[AddressResponse])
def list_addresses(
    name: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Address)

    if name:
        query = query.filter(Address.name.ilike(f"%{name}%"))

    if city:
        query = query.filter(Address.city.ilike(f"%{city}%"))

    return query.all()


@router.put("/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, data: AddressCreate, db: Session = Depends(get_db)):
    address = db.query(Address).get(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    for key, value in data.model_dump().items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)
    return address


@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(Address).get(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()
    return {"message": "Address deleted"}


@router.get("/nearby", response_model=list[AddressResponse])
def get_nearby_addresses(
    lat: float = Query(...),
    lon: float = Query(...),
    distance_km: float = Query(...),
    db: Session = Depends(get_db)
):
    addresses = db.query(Address).all()

    result = [
        addr for addr in addresses
        if haversine_distance(lat, lon, addr.latitude, addr.longitude) <= distance_km
    ]

    return result