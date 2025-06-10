# Project code structure and its functions meaning 

## main.py

## Initialize FastAPI application
app = FastAPI()

## Path to the Excel file containing multiple logical sections
excel_path = "./Data/capbudg.xlsx"

- Load Excel data into a dictionary structure:
- {
-  "SECTION_NAME_1": [ [row1], [row2], ... ],
-  "SECTION_NAME_2": [ ... ]
- }
- This is executed once at app startup


## def list_tables(): 
    """
    List all the logical table (section) names extracted from the Excel file.

    Returns:
        JSON response with the list of table/section names.
    
    Example response:
    {
        "tables": ["INITIAL INVESTMENT", "DISCOUNT RATE", "WORKING CAPITAL"]
    }
    """

## def get_table_details(table_name: str = Query(...)):
    """
    Return all the row names (first column values) from the specified table/section.

    Args:
        table_name (str): Name of the section/table as shown by `/list_tables`.

    Returns:
        JSON response containing:
            - table_name: Matched (case-insensitive) section name
            - row_names: List of first-column labels in that section

    Raises:
        HTTPException: If the table name doesn't match any loaded section
    """


## def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    """
    Return the sum of all numerical values in a given row of the specified table.

    Args:
        table_name (str): Name of the section/table 
        row_name (str): Exact name of the row (first column value) to sum

    Returns:
        JSON response containing:
            - table_name
            - row_name
            - sum: total of numeric values in that row

    Raises:
        HTTPException: If table or row is not found
    """



## utils.py


## def clean_value(val):
    """
    Cleans and converts a cell value to a float, if possible.

    Handles:
        - Strings with dollar signs ($), percent signs (%), or non-numeric characters
        - Empty cells or None values
        - Ignores text like "Do not enter"

    Args:
        val: Cell value (could be a string, number, or None)

    Returns:
        float: Parsed numeric value if valid, otherwise None
    """

## def load_excel_sections(path: str) -> Dict[str, List[List[str]]]:
    """
    Parses a loosely structured Excel file into named sections.

    Assumes:
        - The Excel file has labeled sections separated by headers.
        - Headers are detected based on uppercase names or labels ending with '='.
        - Each section consists of one or more rows following its header.

    Args:
        path (str): Path to the Excel file

    Returns:
        dict: A dictionary mapping section titles to lists of their row contents.

    Example:
        {
            "INITIAL INVESTMENT": [
                ["Initial Investment=", "$50,000"],
                ["Opportunity cost (if any)=", "$7,484"],
                ...
            ],
            ...
        }
    """

## def get_row_names(section_data: List[List[str]]) -> List[str]:
    """
    Extracts the row names (typically the first column values) from a section.

    Args:
        section_data (List[List[str]]): Rows belonging to one section

    Returns:
        List[str]: A list of all row labels in that section
    """


## def get_row_sum(section_data: List[List[str]], row_name: str) -> float:
    """
    Computes the sum of all numeric values in a given row of a section.

    Args:
        section_data (List[List[str]]): Rows of a particular section
        row_name (str): Name (first column) of the row to sum

    Returns:
        float: Sum of numeric values in that row

    Raises:
        ValueError: If the specified row is not found
    """