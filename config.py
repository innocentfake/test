env_vars = {
  # Get From my.telegram.org
  "API_HASH": "",
  # Get From my.telegram.org
  "API_ID": "",
  #Get For @BotFather
  "BOT_TOKEN": "8118842825:AAHdTXuVtzc3Lm_UWbBr8hqfDHQq5UF56MY",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres:y4FYdvw7QPqGYdcK@cheekily-versed-houndshark.data-1.use1.tembo.io:5432/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "fuck_umanga",
  # Force Subs Channel username without @
  "CHANNEL": "Manga_Sect",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MS] [{chap_num}] {chap_name} @Manga_Sect"  

}
dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
