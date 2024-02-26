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

    # Get metadata for the file
    file_metadata = drive_service.files().get(fileId=file_id).execute()

    return file_metadata

if __name__ == "__main__":
    # Authenticate and get credentials
    creds = authenticate()

    # Specify the file ID you want to retrieve metadata for
    file_id = '1mb7GVPRDzBlKKK-rKqIzRSqZog-muKSf'

    # Get and print metadata for the specified file
    metadata = get_metadata(file_id, creds)
    print(metadata)
    
