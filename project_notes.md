
# Project Insights & Improvements

## Insight on the Project

This project transforms structured Excel data into a RESTful API using FastAPI. It’s particularly useful for:
- Financial budgeting tools where Excel is used as the source of data.
- Quick access to structured spreadsheet data.
The project is well-structured and uses a clean, maintainable approach.

---

## Potential Improvements

1. **Handle Multiple Excel Sheets**  
   Allow querying specific sheets via a parameter.

2. **Dynamic Excel Upload**  
   Add a POST endpoint to upload new Excel files without restarting the server.

3. **Frontend Dashboard**  
   Build a UI using Streamlit for ease of use and visualization.

---

## Missed Edge Cases

1. **Empty Excel Files**  
   Need checks for empty or invalid files with proper error messages.

2. **Duplicate Row Names**  
   Handle or prevent non-unique row names in the same section.

3. **Non-Numeric Rows**  
   Warn when a row has no numeric data instead of returning zero silently.

3. **Missing/Corrupted Excel Files**  
   Provide clearer errors if the Excel file is missing or unreadable.

---

