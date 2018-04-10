import sys
loopcount=1

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

def status_scan(files_scanned,folders_scanned,threats_detected,threats_cleaned):
    # print('Total Files Scanned : ' + str(files_scanned) + "\n")
    # print('Total Files Scanned : ' + str(files_scanned) + "\n" , end = '\r')
    if files_scanned == 1:
        sys.stdout.write('Total Files Scanned        : ' + str(files_scanned) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Total Folders Scanned      : ' + str(folders_scanned) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Threats Detected           : ' + str(threats_detected) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Threats Cleaned            : ' + str(threats_cleaned) + "\n")
        sys.stdout.flush()
        # restart_line()

    else:
        sys.stdout.write('Total Files Scanned        : ' + str(files_scanned) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Total Folders Scanned      : ' + str(folders_scanned) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Threats Detected           : ' + str(threats_detected) + "\n")
        sys.stdout.flush()
        restart_line()
        sys.stdout.write('Threats Cleaned            : ' + str(threats_cleaned) + "\n")
        sys.stdout.flush()
        # restart_line()

def current_scan(file_loc):
    global loopcount
    if loopcount == 1:
        sys.stdout.write('Currently Scanning         : ' + str(file_loc)  + "\n")
        sys.stdout.flush()
        restart_line()
        loopcount += 1
    else :
        sys.stdout.write('\033[F\033[F\033[F\033[F\033[FCurrently Scanning         : ' + str(file_loc)  + "\n")
        sys.stdout.flush()
        restart_line()
