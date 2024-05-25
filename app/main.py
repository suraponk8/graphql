from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
from app.db.database import prepare_database, Session
from app.db.models import Employer, Job
from app.gql.queries import Query
from app.gql.mutations import Mutation


schema = Schema(query=Query, mutation=Mutation)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    prepare_database()

@app.get("/employers")
def get_employee():
    session = Session()
    employers = session.query(Employer).all()
    session.close()
    return  employers

@app.get("/jobs")
def get_employee():
    with Session() as session:
        return session.query(Job).all()


app.mount("/graphql", GraphQLApp(
    schema=schema,
    on_get=make_playground_handler()
))