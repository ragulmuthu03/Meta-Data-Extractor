import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def authenticate():
    # Set up OAuth 2.0 credentials
    creds = None
    token_path = 'token.json'  # Replace with the path to your token file

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',  # Replace with the path to your credentials file
            ['https://www.googleapis.com/auth/drive.metadata.readonly']
        )
        creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds

def get_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Define the fields you want to retrieve
    fields = "id,name,mimeType"

    # Get metadata for the file with specified fields
    file_metadata = drive_service.files().get(fileId=file_id, fields=fields).execute()

    return file_metadata

def get_version_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get version information for the file
    version_info = drive_service.files().get(fileId=file_id, fields="version").execute()

    return version_info

def get_link_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get link information for the file
    link_info = drive_service.files().get(fileId=file_id, fields="webViewLink").execute()

    return link_info

def get_size_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get size information for the file
    size_info = drive_service.files().get(fileId=file_id, fields="size").execute()

    return size_info

def get_owner_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get owner information for the file
    owner_info = drive_service.files().get(fileId=file_id, fields="owners").execute()

    return owner_info

def get_sharing_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get sharing information for the file
    sharing_info = drive_service.files().get(fileId=file_id, fields="shared,sharingUser").execute()

    return sharing_info

def get_parents_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get parents information for the file
    parents_info = drive_service.files().get(fileId=file_id, fields="parents").execute()
    
    return parents_info

def get_permissions_information(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get permissions information for the file
    permissions_info = drive_service.files().get(fileId=file_id, fields="permissions").execute()

    return permissions_info

def get_description(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get description for the file
    description_info = drive_service.files().get(fileId=file_id, fields="description").execute()

    return description_info

def get_image_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get image metadata for the file
    image_metadata = drive_service.files().get(fileId=file_id, fields="imageMediaMetadata").execute()

    return image_metadata

def get_video_metadata(file_id, creds):
    # Build the service object
    drive_service = build('drive', 'v3', credentials=creds)

    # Get video metadata for the file
    video_metadata = drive_service.files().get(fileId=file_id, fields="videoMediaMetadata").execute()

    return video_metadata


if __name__ == "__main__":
    # Authenticate and get credentials
    creds = authenticate()

    # Specify the file ID you want to retrieve metadata for
    file_id = '1mb7GVPRDzBlKKK-rKqIzRSqZog-muKSf'  # Replace with your file ID

    # Get and print extended metadata for the specified file
    metadata = get_metadata(file_id, creds)
    print("File ID,Name,Mime type:",metadata)
    link_info=get_link_information(file_id, creds)
    print("Link information:",link_info)
    size_info=get_size_information
    print("Size information:",size_info)
    owner_info=get_owner_information(file_id, creds)
    print("Owner information:",owner_info)
    sharing_info=get_sharing_information(file_id, creds)
    print("Sharing information:",sharing_info)
    parents_info=get_parents_information(file_id, creds)
    print("Parent information:",parents_info)
    description_info=get_description(file_id, creds)
    print("Description:",description_info)
    image_metadata=get_image_metadata(file_id, creds)
    print("Image Metadata:", image_metadata)
    video_metadata=get_video_metadata
    print("Video Metadata:",video_metadata)
