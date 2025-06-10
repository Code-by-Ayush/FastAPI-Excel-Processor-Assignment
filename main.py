from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from utils import load_excel_sections, get_row_names, get_row_sum

app = FastAPI()
excel_path = "./Data/capbudg.xlsx"

# Load Excel data once
data = load_excel_sections(excel_path)

@app.get("/list_tables")
def list_tables():
    return {"tables": list(data.keys())}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    matched = next((k for k in data if k.lower() == table_name.lower()), None)
    if not matched:
        raise HTTPException(status_code=404, detail="Table not found")
    rows = get_row_names(data[matched])
    return {
        "table_name": matched,
        "row_names": rows
    }

@app.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    matched = next((k for k in data if k.lower() == table_name.lower()), None)
    if not matched:
        raise HTTPException(status_code=404, detail="Table not found")
    try:
        total = get_row_sum(data[matched], row_name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "table_name": matched,
        "row_name": row_name,
        "sum": total
    }

