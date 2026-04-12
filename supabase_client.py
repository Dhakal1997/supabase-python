import os
from dotenv import load_dotenv
load_dotenv()   
from supabase import create_client, Client

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]
def get_supabase() -> Client:
    return create_client(url, key)
# supabase: Client = create_client(url, key)


# name = str(input("Enter a todo"))
# insert = (
#     supabase.table("todo")
#     .insert({"id": 3, "todo-name": name})
#     .execute()
# )

# update = (
#     supabase.table("todo")
#     .update({"todo-name": "morefun"})
#     .eq("id",2)
#     .execute()
# )

# delete = (
#     supabase.table("todo")
#     .delete()
#     .eq("id",3)
#     .execute()

    
# )

# response = (
#     supabase.table("todo")
#     .select("*")
#     .execute()
# )


# print(type(response))
# print(response.data)
