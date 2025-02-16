
#imports - streamlit to display results - supabase for database information
import streamlit as st
import os
from supabase import create_client

#declare url and key from supabase
url = ""
key = ""

#connect supabase to local variables 
supabase = create_client(url,key)

#print out table 
response = supabase.table("test").select("*").execute()
print(response)

#print out just the name 
response =supabase.table("test").select("name").execute()
print(response)

#print out specific field data 
response = supabase.table("test").select("id","name").eq("name","slovakia").execute()
print(response)

#test search for things not in database 
response = supabase.table("test").select("id","name").eq("name","china").execute()
print(response)

#insert new data
response = supabase.table("test").insert({"id" : 12, "name" : "china"}).execute()
print(response)

#update existing fields
response = supabase.table("test").update({"name" : "texas"}).eq("id", "1").execute()
print(response)

#delete a field 
response = supabase.table("test").delete().eq("id","12").execute()
print(response)
