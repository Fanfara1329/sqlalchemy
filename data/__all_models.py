import datetime
import sqlalchemy as sa
from .db_session import ORMBase
from sqlalchemy import orm


class User(ORMBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                           primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String)
    speciality = sa.Column(sa.String)
    address = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String)
    modified_date = sa.Column(sa.DateTime)



class Jobs(ORMBase):
    __tablename__ = 'jobs'

    id = sa.Column(sa.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer)
    job = sa.Column(sa.String)
    work_size = sa.Column(sa.Integer)
    content = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime)
    end_date = sa.Column(sa.DateTime)
    is_finished = sa.Column(sa.Boolean)