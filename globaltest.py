variabel = "hallo"
def dette_er_en_funksjon(alfa):
    global variabel 
    variabel = variabel + "halloo"
    variabel1 = f"{alfa} til deg også"
    return(variabel1)
funker_dette = dette_er_en_funksjon(variabel)
print(funker_dette)
print(variabel)