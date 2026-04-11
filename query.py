# from main import supabase
from supabase_client import supabase

# input = str(input("  Enter a todo!"))

# new_Todo = { "todo-name":input}
# new_res = supabase.table("todo").insert(new_Todo).execute()

response = supabase.table("todo").select("*").execute()

# Access the returned data
data = response.data
print(data)