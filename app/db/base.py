from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):  # 이 방식이 SQLAlchemy 2.0에서 권장되는 방식임.
    pass
