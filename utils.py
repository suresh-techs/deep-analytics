def capitalize(name:str):
    return name.upper()
    
def analyse():
    """This method is used to analyse the data"""
    languages = ["html","css","js"]
    return list(map(capitalize,languages))
