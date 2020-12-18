from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Matrix(BaseModel):
    matrix: list



@app.get("/")
def read_root():
    return "asdsdfsdg"

@app.get("/list/{item_id}")
def read_list(item_id: int):
    return [0,1,2,3,4,5][item_id]

@app.put("/transpose")
def make_order(matrixx: Matrix):
    return  '\n'.join([' '.join(['%d\t' % (matrixx.matrix[i][j]) for i in range(0, len(matrixx.matrix))]) for j in range(0,len(matrixx.matrix[0]))])

@app.put("/det")
def det(matrixx: Matrix):
    if (len(matrixx.matrix) != len(matrixx.matrix[0])): return None
    AM = matrixx.matrix

    for fd in range(len(matrixx.matrix)):
        for i in range(fd+1,len(matrixx.matrix)):
            if AM[fd][fd] == 0:
                AM[fd][fd] == 1.0e-18
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(len(matrixx.matrix)):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(len(matrixx.matrix)):
        product *= AM[i][i]

    return product
