import os



project_path = os.path.dirname(os.path.realpath(__name__))
file_to_modify = "youtube-all"
hostsfile_description = """
! Title: b3nchas hosts file with all youtube-urls
!
! Description: 
! The original blocklist file come from https://github.com/jmdugan/blocklists/
! and was modified with my python script file to make it compatible for AdGuard.
! 
! Project Homepage: https://github.com/b3ncha/blocklist
! Python Script:    https://github.com/b3ncha/blocklist/AdGuarts/modhostsfile.py
"""
__hostsfile_description = """
! Title: b3nchas hosts files 
!
! Description: 
! The file was created from many blocklists with the 
! project https://github.com/StevenBlack/hosts and was modified 
! with my python script file to make it compatible for AdGuard.
! 
! Project Homepage: https://github.com/b3ncha/blocklist
! Python Script:    https://github.com/b3ncha/blocklist/smartphone-hosts/modhostsfile.py
"""

def mod_url(url = ""):
    """ This function modifies one url entry of the hosts file
        Example:
        Input:  0.0.0.0 google.de # Germany
        Output: ||google.de^

        For more filter option see https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters#for_maintainers
    """
    if url == "":
        print("An empty url strings cannot be processed.")
        return None

    new_url = url.split(" ")[1].replace("\n", "")         # we need only the url

    return "||" + new_url + "^" + "\n"

def filter_hosts(hosts = ""):
    """ We need only the lines with the urls but
        we get:
        1. Comments, beginning with #. The comments are not compatible with AdGuard
        2. emty lines. We don't need
        3. url lines like 0.0.0.0 google.de # Germany. That is was we need

        Parameters
        ----------
        hosts : str
            path to hosts file
        return: str
            String object with all new urls
    """
    if hosts == "":
        Print("An empty file path cannot be processed.")
        return None
    
    with open(hosts) as file:
        new_hosts_file = ""

        for line in file:
            if line.find("0.0.0.0") == 0:
                new_hosts_file += mod_url(line)

    file.close()
    return new_hosts_file

def main():
    print("Start to modify the hosts file.")
    current_hosts_file = project_path + "/" + file_to_modify
    new_hosts_file = hostsfile_description + "\n"

    file_exists = os.path.exists(current_hosts_file)
    if file_exists == False:
        print("The hosts file does not exist")
        return None
    print("Hosts file exists.")
    new_hosts_file += filter_hosts(current_hosts_file)

    with open(current_hosts_file, "w") as file:
        file.write(new_hosts_file)

    file.close()

if __name__ == "__main__":
    main()