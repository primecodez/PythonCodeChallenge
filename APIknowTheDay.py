#API TO KNOW THE EXACT DAY FOR A PARTICULAR DATE IN A PARTICULAR YEAR
#uvicorn APIknowTheDay:app --reload

from fastapi import FastAPI,HTTPException
from datetime import datetime

app = FastAPI()

@app.get("/day/{date_string}")
def get_day_of_week(date_string: str):
    # Create a list of all the formats you want to support
    supported_formats = ["%Y-%m-%d", "%d %B %Y", "%d %b %Y"]
    
    date_obj = None
    # Loop through the formats and try each one
    for fmt in supported_formats:
        try:
            date_obj = datetime.strptime(date_string, fmt)#strptime takes 2 values i.e strptime(val1,val2) 
            #here val 2 is blueprint to understand val 1
            break  # If it works, stop the loop immediately
        except ValueError:
            continue  # If it fails, just move on to the next format in the list

    # If no format worked, raise a proper 400 Bad Request error
    if date_obj is None:
        raise HTTPException(
            status_code=400, 
            detail="Invalid format. Try YYYY-MM-DD, DD Month YYYY, or DD Mon YYYY"
        )
            
    day_name = date_obj.strftime("%A")
    return {"date": date_string, "day_of_week": day_name}  