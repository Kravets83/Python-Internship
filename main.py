import os

import uvicorn as uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import utils

load_dotenv()
app = FastAPI(
    title="Python Internship by Maklai",
    description="Text generator\n\n"
                "Test tree from test task:\n\n"
                "tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) "
                "(NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) "
                "(VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) "
                "(CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )"
                "\n\n",

    version="0.0.1",
    contact={
            "name": "Kravets Olexandr",
            "email": "krava198383@gmail.com",
    },

)


'''start page redirect to docs swagger'''
@app.get("/", response_class=RedirectResponse)
async def root():
    # return {"message": "Hello World"} '''start page'''
    return '/docs'


@app.get("/paraphrase/{tree}")
async def tree_in(tree: str, limit: int = 20):
    return {"paraphrases": utils.create_list_tree(tree, limit)}


if __name__ == "__main__":
    uvicorn.run('main:app', host=str(os.getenv('LOCALHOST')), port=int(os.getenv('PORT')), reload=True)
