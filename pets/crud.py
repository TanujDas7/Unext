import psycopg2
from psycopg2 import OperationalError
from flask import render_template, redirect, url_for

class Crud:
    conn = psycopg2.connect(host="localhost",
        database="postgres",
        user='postgres',
        password='Finserv@2023')
    cur = conn.cursor()
    @classmethod
    def fetch(cls):
        cls.cur.execute("select * from pet;")
        return cls.cur.fetchall()
    @classmethod
    def create_table(cls):
        try:
            cls.cur.execute("create table if not exists pet (petid serial, petname varchar(20) not null, petbreed varchar(20), petowner varchar(20) not null);")
            cls.conn.commit()
        except OperationalError as oe:
            None

    @classmethod
    def insert_table(cls, name, breed, owner):
            cls.cur.execute(f"insert into pet (petname, petbreed, petowner) values('{name}', '{breed}', '{owner}');")
            cls.conn.commit()
            
    @classmethod
    def update_table(cls, pet_session, petid):
        try:
            for key in pet_session:
                if pet_session[key] != "" and key != "submit" and key != "csrf_token" and not pet_session[key].isdigit():
                    cls.cur.execute(f"update pet set {key}='{pet_session[key]}' where petid='{petid}';")
                    cls.conn.commit()
        except psycopg2.Error as er:
            return redirect(url_for("error", error=er))

    @classmethod
    def delete_entry(cls, id):
        try:
            cls.cur.execute(f"delete from pet where petid='{id}';")
            cls.conn.commit()
        except psycopg2.Error as er:
            return redirect(url_for("error", error=er))