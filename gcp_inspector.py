from optparse import OptionParser
import subprocess
import sys
from termcolor import colored


#data="/myfile.txt"

def main():
    global data
    parser = OptionParser(usage="Usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-r",
                      action="store_true",
                      help="Provide file as an input with google bucket names")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("Incorrect number of arguments, use -h for help")

    data= args[0]
    count = 0
    # Using readlines()
    file_read = open(data, 'r')
    read_lines = file_read.readlines()
    # Strips the newline character
    print(colored("Run gsutil config. Ignore if already installed.\n", 'cyan', attrs=['bold']))
    print(colored("Starting GCP Bucket Enumeration: ", 'cyan', attrs=['bold']))

    for val in read_lines:
        count += 1
        try:
            if "gs://" in val:
                getVersion = subprocess.Popen("gsutil ls " + val.strip(), shell=True, stderr=subprocess.STDOUT,
                                              stdout=subprocess.PIPE).stdout
                version = getVersion.read()
            else:
                getVersion = subprocess.Popen("gsutil ls gs://" + val.strip(), shell=True, stderr=subprocess.STDOUT,
                                              stdout=subprocess.PIPE).stdout
                version = getVersion.read()

            #print(version.decode())
            #checking exceptions
            if "credentials are invalid" in version.decode():
                print(colored("Credentials are invalid. Authenticate again.", 'yellow'))
                sys.exit()

            elif "ServiceException" in version.decode():
                print(colored("Error While Running \'gsutil\', Run The Command Manually", "yellow"))
                sys.exit()

            elif "bash:" in version.decode() or "command not found" in version.decode():
                print(colored("\'gsutil\' Command Not Found", "yellow"))
                sys.exit()

            elif "bucket does not exist" in version.decode():
                print(colored(f'Result {count}. Bucket {val.strip()} Does Not Exist', 'yellow'))

            elif "AccessDeniedException" in version.decode():
                print(colored(f'Result {count}. Bucket {val.strip()} Publicly Not Accessible.', 'red'))

            else:
                print(colored(f'\nResult {count}. Bucket {val.strip()} Publicly Accessible. Visit http://storage.googleapis.com/{val.strip("gs://")} Via Public Endpoint.\n', 'green'))

        except:
            #exit program gracefully
            print(colored('Error: ' + str(sys.exc_info()) + '\n', 'yellow'))
            print ("Program Exited.")
            sys.exit()


if __name__ == '__main__':
    print("""
 ██████╗  ██████╗██████╗     ██╗███╗   ██╗███████╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗██║     ██████╔╝    ██║██╔██╗ ██║███████╗██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
██║   ██║██║     ██╔═══╝     ██║██║╚██╗██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
╚██████╔╝╚██████╗██║         ██║██║ ╚████║███████║██║     ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚═════╝  ╚═════╝╚═╝         ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                            Author - Divyanshu Shukla(twitter.com/justm0rph3u5)
    """)
    main()
