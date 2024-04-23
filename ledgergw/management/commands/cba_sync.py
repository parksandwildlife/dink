from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from decimal import *
from ledgergw.emails import sendHtmlEmail
import json
import subprocess
import os
import shutil
from datetime import timedelta, datetime
from confy import env

class Command(BaseCommand):
    help = 'CBA Bpay file sync script'

    def handle(self, *args, **options):
            # today = datetime.today()# - timedelta(days=3)
            print ("Preparing to Sync CBA Files")
            local_bank_directory = env('LOCAL_BANK_DIRECTORY', "/tmp/bankfiles/")
            remote_bank_directory = env('REMOTE_BANK_DIRECTORY', "")
            sftp_username = env('SFTP_USERNAME', "")
            sftp_host = env('SFTP_HOST', "")
            sftp_key_location = env('SFTP_KEY_LOCATION', "")

            try:
                if len(sftp_username) > 0:
                     raise ValidationError("No username provided")
                if len(sftp_host) > 0:
                     raise ValidationError("No host provided")
                if len(sftp_key_location) > 0:
                     raise ValidationError("No key provided")


                local_bank_files = os.listdir(local_bank_directory)
                print (local_bank_files)
                for lbf in local_bank_files:
                    print ("removing "+lbf)
                    os.remove(local_bank_directory+lbf)
                
                result = subprocess.check_output('echo "ls '+remote_bank_directory+'" | sftp -i '+sftp_key_location+' '+sftp_username+'@'+sftp_host, shell=True, text=True)
                sftpfiles = result.split("\n")
                for file in sftpfiles:
                    sftp_file = file.strip()
                    if len(sftp_file) > 0:
                        file_only = sftp_file.replace(remote_bank_directory, "")
                        print ("'"+sftp_file+"'")    
                        print (file_only)

                        if os.path.isfile(local_bank_directory+file_only):
                            print ("File already exists not downloading "+file_only)
                        else:      
                            print ('downloading file '+file_only)
                            get_resp = subprocess.check_output('echo "get '+sftp_file+' '+local_bank_directory+'" | sftp -i '+sftp_key_location+' '+sftp_username+'@'+sftp_host, shell=True, text=True)
                            #print (get_resp)
                
            except Exception as e:
                print ("EXCEPTION:")
                print (e)
                print ("Sending Email Notification to: "+settings.NOTIFICATION_EMAIL)
                context = {'cba_error': str(e)}

                email_list = []
                for email_to in settings.NOTIFICATION_EMAIL.split(","):
                        email_list.append(email_to)
                sendHtmlEmail(tuple(email_list),"[LEDGER] Test Email",context,'ledgergw/email/cba_sync.html',None,None,settings.EMAIL_FROM,'system-oim',attachments=None)


