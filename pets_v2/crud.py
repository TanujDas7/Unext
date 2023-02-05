import psycopg2
from psycopg2 import OperationalError
from flask import render_template, redirect, url_for, flash
from app import logger

from config import dbsettings

class Crud:
    conn = None
    cur = None
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Crud, cls).__new__(cls)
        return cls._instance

    @classmethod
    def connect(cls):
        # from config.py
        conn = psycopg2.connect(
            host=dbsettings['host'],
            database=dbsettings['database'],
            user=dbsettings['user'],
            password=dbsettings['password'])
        return conn
    @classmethod
    def fetch(cls, cur):
        cur.execute("select * from pet;")
        return cur.fetchall()
    @classmethod
    def create_table(cls, cur, conn):
        try:
            cur.execute("create table if not exists pet (petid serial, petname varchar(20) not null, petbreed varchar(20), petowner varchar(20) not null);")
            conn.commit()
        except OperationalError as oe:
            logger.exception(f"{oe}")
            None

    @classmethod
    def insert_table(cls, name, breed, owner, cur, conn):
            cur.execute(f"insert into pet (petname, petbreed, petowner) values('{name}', '{breed}', '{owner}');")
            conn.commit()
            flash(f"new pet entry recorded for owner: {owner}", "success")
            
    @classmethod
    def update_table(cls, pet_session, petid, cur, conn):
        try:
            cur.execute(f"select petname from pet where petid={petid}")
            x = cur.fetchall()
            for key in pet_session:
                if pet_session[key] != "" and key != "submit" and key != "csrf_token" and not pet_session[key].isdigit():
                    cur.execute(f"update pet set {key}='{pet_session[key]}' where petid='{petid}';")
                    conn.commit()
            flash(f"entry edited for : {x[0][0]}", "success")
        except psycopg2.Error as er:
            logger.exception(f"{er}")
            flash(f"could not update entry", "error")
            return redirect(url_for("error", error=er))

    @classmethod
    def delete_entry(cls, id, cur, conn):
        try:
            cur.execute(f"select petname from pet where petid={id}")
            x=cur.fetchall()
            cur.execute(f"delete from pet where petid='{id}';")
            conn.commit()
            flash(f"entry deleted for : {x[0][0]}", "success")
        except psycopg2.Error as er:
            logger.exception(f"{er}")
            flash(f"could not delete entry", "error")
            return redirect(url_for("error", error=er))