from sqlalchemy import asc, desc
from models import Job

def parse_sort_param(sort_param):
    if sort_param == "posting_date_desc":
        return desc(Job.posting_date)
    elif sort_param == "posting_date_asc":
        return asc(Job.posting_date)
    return desc(Job.posting_date)
