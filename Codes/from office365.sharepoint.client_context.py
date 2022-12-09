from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.system_object_type import FileSystemObjectType
from office365.sharepoint.listitems.listitem import ListItem
from office365.runtime.auth.user_credential import UserCredential


from dotenv import load_dotenv
import os

load_dotenv()


USERNAME = os.getenv('sharepoint_email')
PASSWORD = os.getenv('sharepoint_password')
SHAREPOINT_SITE = os.getenv('sharepoint_url_site')
SHAREPOINT_SITE_NAME = os.getenv('sharepoint_site_name')
SHAREPOINT_DOC = os.getenv('sharepoint_doc_library')

FOLDER_NAME = '1. ProjectLab'

target_folder_url = f'{SHAREPOINT_DOC}/{FOLDER_NAME}'

site_url = "https://metrixlab1.sharepoint.com/sites/DataScience-AA"
ctx = ClientContext(site_url).with_credentials(UserCredential("ruddi.garcia@metrixlab.com", "aeiouAEIOU1980#"))

# read documents from a folder 

folder = ctx.web.get_folder_by_server_relative_url(target_folder_url)
files = folder.files
ctx.load(files)
ctx.execute_query()
for file in files:
    print(file.properties['Name'])


# get the name of the folders in the site

folders = ctx.web.folders
ctx.load(folders)
ctx.execute_query()
for folder in folders:
    print(folder.properties['Name'])



# get a file by name.

file = ctx.web.get_file_by_server_relative_url("/sites/DataScience-AA/Shared Documents//AA_db.csv")
ctx.load(file)
ctx.execute_query()
print(file.properties['Name'])


doc_lib = ctx.web.lists.get_by_title("Sahred Documents")
items = doc_lib.items.select(["FileSystemObjectType"]).expand(["File", "Folder"]).get().execute_query()
for item in items:  # type: ListItem
    if item.file_system_object_type == FileSystemObjectType.Folder:
        print("(Folder): {0}".format(item.folder.serverRelativeUrl))
    else:
        print("(File): {0}".format(item.file.serverRelativeUrl))










    


