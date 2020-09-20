#Main script
#Run all the scripts


scripts = [
    "1.SaveLeads.py",
    "2.ConnectLeads.py",
    "3.1.ShuffleScriptInPendingList",
    "3.2.ShuffleScriptSlowLinkdinUNDPUserList",
    "3.ShuffleScript",
    "4.1.SendMessage",
    "4.SendMessage",
]

if __name__ == "__main__":

    # # Just change the name of the file, and this line of code will open another script
    for s in scripts:
        exec(open(s).read())
        time.sleep()
