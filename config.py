import json

class Config:

    #region GENERAL SETUP

    appid = 'c034a2bddc801c826b1a42ddfb919334'
    with open('ISO-3166.json', 'r') as file:
        iso_3166 = json.load(file)

    #endregion    

    #region GEOLOCATION SETUP

    geolocation_url = 'http://api.openweathermap.org/geo/1.0/direct?'

    #endregion

    #region WEATHER SETUP

    weather_url = 'https://api.openweathermap.org/data/3.0/onecall?'

    #endregion
    
    #region DATABSE SETUP

    local_db_host=''
    local_db=''
    local_db_user=''
    local_db_password=''
    
    development_db_host=''
    development_db=''
    development_db_user=''
    development_db_password=''
    
    homolog_db_host=''
    homolog_db=''
    homolog_db_user=''
    homolog_db_password=''
    
    production_db_host=''
    production_db=''
    production_db_user=''
    production_db_password=''

    #endregion

    #region EMAIL SETUP

    local_email_identifier = ''
    local_email_base_url = ''
    local_email_base_url_adm = ''
    local_email_sender = ''
    local_email_password = ''

    development_email_identifier = ''
    development_email_base_url = ''
    development_email_base_url_adm = ''
    development_email_sender = ''
    development_email_password = ''        
    
    homolog_email_identifier = ''
    homolog_email_base_url = ''
    homolog_email_base_url_adm = ''
    homolog_email_sender = ''
    homolog_email_password= '' 

    production_email_identifier = ''
    production_email_base_url = ''
    production_email_base_url_adm = ''
    production_email_sender = ''
    production_email_password= ''

    #endregion

    #region InfoData
    
    infodata_url_active = False
    local_infodata_url = 'http://127.0.0.1:5399/'
    development_infodata_url = ''
    homolog_infodata_url = ''
    production_infodata_url = ''

    #endregion