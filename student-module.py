def scholarship_qualification(name, years, gpa):
    """
    Determine scholarship qualification based on years of study and GPA
    
    Args:
    name (str): Student's name
    years (int): Years of study
    gpa (float): Student's GPA
    
    Returns:
    str: Qualification message
    """
    if years >= 2 and gpa >= 3.5:
        return f"{name}, you qualify for a scholarship in Rutgers university!"
    else:
        return f"{name}, you do not qualify for a scholarship in Rutgers university."
