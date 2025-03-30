from datetime import datetime, timezone
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from src.database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False, unique=True, index=True)
    click_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    expire_at = Column(DateTime, nullable=False)
    link_owner_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id"),
        index=True,
        nullable=True
    )

    @declared_attr
    def author(cls) -> Mapped["User"]:
        from src.auth.models import User
        return relationship("User", back_populates="links", lazy="selectin")