import sys, os

if __name__ == "__main__":
 
    args = sys.argv

    if len(args) <= 1:
        print("ERROR: No argument specified\n")
        print("Please enter 'school' to connect to your eduroam")
        print("Or enter 'home' to connect to your home network")
        quit()

    else:
       args = sys.argv[1]

    if args.lower() == "school":
        print("Connecting to school network...")
        os.system("wpa_supplicant -Dnl80211 -iwlp3s0 -c school.conf -B")
        os.system("dhcpcd wlp3s0")
        
    elif args.lower() == "home":
        print("Connecting to home network...")
        os.system("wpa_supplicant -Dnl80211 -iwlp3s0 -c home.conf -B")
        os.system("dhcpcd wlp3s0")
