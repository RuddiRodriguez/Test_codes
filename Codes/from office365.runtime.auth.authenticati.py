from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 

####inputs########
# This will be the URL that points to your sharepoint site. 
# Make sure you change only the parts of the link that start with "Your"
url_shrpt = "https://metrixlab1.sharepoint.com/sites/DataScience-AA"
username_shrpt = "ruddi.garcia@metrixlab.com"
password_shrpt = "aeiouAEIOU1980#"
folder_url_shrpt = '/sites/DataScience-AA/Shared%20Documents/2E%20ProjectLab'

#######################


###Authentication###For authenticating into your sharepoint site###
ctx_auth = AuthenticationContext(url_shrpt)
if ctx_auth.acquire_token_for_user(username_shrpt, password_shrpt):
  ctx = ClientContext(url_shrpt, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print('Authenticated into sharepoint as: ',web.properties['Title'])

else:
  print(ctx_auth.get_last_error())
############################


###Function for extracting the file names of a folder in sharepoint###
###If you want to extract the folder names instead of file names, you have to change "sub_folders = folder.files" to "sub_folders = folder.folders" in the below function
global print_folder_contents
def print_folder_contents(ctx, folder_url):
    try:
       
        folder = ctx.web.get_folder_by_server_relative_url(folder_url)
        fold_names = []
        sub_folders = folder.files #Replace files with folders for getting list of folders
        ctx.load(sub_folders)
        ctx.execute_query()
     
        for s_folder in sub_folders:
            
            fold_names.append(s_folder.properties["Name"])

        return fold_names

    except Exception as e:
        print('Problem printing out library contents: ', e)
######################################################

# Call the function by giving your folder URL as input  
filelist_shrpt=print_folder_contents(ctx,folder_url_shrpt) 

#Print the list of files present in the folder
print(filelist_shrpt)