from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('mysql://root:123@127.0.0.1/sdo?charset=utf8', echo=True)

Session = sessionmaker(bind=engine)


class Tests(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True)
    course_id = Column(
        Integer,
        ForeignKey('courses.id'),
        nullable=False,
    )
    problems = Column(String(300))
    owner = Column(Integer)
    duration = Column(Integer)
    created_date = Column(DateTime(timezone=True), server_default=func.now())



Base.metadata.create_all(bind=engine)
