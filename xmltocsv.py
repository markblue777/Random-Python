import xml.etree.ElementTree as Xet 
import pandas as pd 
  
cols = ["iana_timezone", "sql_timezone"] 
rows = [] 
  
# Parsing the XML file 
xmlparse = Xet.parse('timezones.xml') 
root = xmlparse.getroot() 
for i in root.findall('.//mapZone'): 
    iana_timezone = i.get("type") 
    sql_timezone = i.get("other")
    
    rows.append({"iana_timezone": iana_timezone, 
                 "sql_timezone": sql_timezone}) 
  
df = pd.DataFrame(rows, columns=cols) 
  
# Writing dataframe to csv 
df.to_csv('output.csv') 