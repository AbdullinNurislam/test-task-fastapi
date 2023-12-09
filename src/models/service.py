from typing import Set

from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, UniqueConstraint, Integer, ForeignKey


class Service(Base):
    __tablename__ = "services"
    __table_args__ = (
        UniqueConstraint("service_name", "path", name="_service_name__path"),
    )
    service_name: Mapped[str] = mapped_column(nullable=False)
    path: Mapped[str] = mapped_column(nullable=False)

    response_times: Mapped[Set["Metric"]] = relationship(
        back_populates="services", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Service {self.service_name} path {self.path}>"


class Metric(Base):
    __tablename__ = "metrics"
    service_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("services.id"), nullable=False
    )
    services: Mapped["Service"] = relationship(back_populates="response_times")
    response_time_ms: Mapped[float] = mapped_column(Numeric, nullable=False)

    def __repr__(self) -> str:
        return f"<Service {self.service_name} path {self.path}>"
