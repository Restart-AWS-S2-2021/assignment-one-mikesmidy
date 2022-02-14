from fastapi import FastAPI

import queries

my_querie_app = FastAPI()
"""
FastAPI
uvicorn main:my_querie_app --reload
"""


# Add your 20 views/routes below.
@my_querie_app.get("/1")
async def root():
    # SELECT & ORDER BY
    return {queries.one_query_order_by()}


@my_querie_app.get("/2")
async def root():
    return {queries.two_query_order_by()}


@my_querie_app.get("/3")
async def root():
    return {queries.three_query_order_by()}


@my_querie_app.get("/4")
async def root():
    return {queries.four_query_where()}


@my_querie_app.get("/5")
async def root():
    return {queries.five_query_where()}


@my_querie_app.get("/6")
async def root():
    return {queries.six_query_where()}


@my_querie_app.delete("/7")
async def root():
    return {queries.seven_query_delete()}


@my_querie_app.put("/8")
async def root():
    return {queries.eight_query_update()}


@my_querie_app.put("/9")
async def root():
    return {queries.nine_query_update()}


@my_querie_app.put("/10")
async def root():
    return {queries.ten_query_update()}


@my_querie_app.post("/11")
async def root():
    return {queries.eleven_query_insert_into()}


@my_querie_app.post("/12")
async def root():
    return {queries.twelfth_query_insert_into()}


@my_querie_app.post("/13")
async def root():
    return {queries.thirteen_query_insert_into()}


@my_querie_app.post("/14")
async def root():
    return {queries.fourteen_query_insert_into()}


@my_querie_app.post("/15")
async def root():
    return {queries.fifthteen_query_insert_into()}


@my_querie_app.get("/16")
async def root():
    # SELECT & ORDER BY
    return {queries.sixteen_query_inner_join()}


@my_querie_app.get("/17")
async def root():
    # SELECT & ORDER BY
    return {queries.seventeen_query_inner_join()}


@my_querie_app.get("/18")
async def root():
    # SELECT & ORDER BY
    return {queries.eighteen_query_self_join()}


@my_querie_app.get("/19")
async def root():
    # SELECT & ORDER BY
    return {queries.nineteen_query_left_join()}


@my_querie_app.get("/20")
async def root():
    # SELECT & ORDER BY
    return {queries.twenty_query_self_join()}


# f)
import hashlib

@my_querie_app.post("/hash_password/{password}")
async def read_item(password: str):
    return {"Hashed password is": hashlib.sha256(password.encode('utf8')).hexdigest()}


