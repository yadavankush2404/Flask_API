from flask import Blueprint

bookmark = Blueprint("bookmarks",__name__,url_prefix="/api/v1/bookmarks")


@bookmark.get('/')
def get_all():
    return {"bookmarks":[]}


