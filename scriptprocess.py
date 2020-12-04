for i in range(1, 9):
    if i < 10:
        OpenFile = 'S2/S2E'+str(i)+'/'+ 'Dark.S02E0' + str(i) + '.srt'
        WriteFile = 'S2/S2E'+str(i)+'/'+ 'Dark.S02E0' + str(i) + '_cleaned.txt'
    else:
        OpenFile = 'S2/S2E'+str(i)+'/'+ 'Dark.S02E' + str(i) + '.srt'
        WriteFile = 'S2/S2E'+str(i)+'/'+ 'Dark.S02E' + str(i) + '_cleaned.txt'
    f = open(OpenFile, 'r')
    fw = open(WriteFile, 'w')
    FileContent = f.readlines()
    for line in FileContent:
        if line == '\n' or '-->' in line or 'WWW.MY-SUBS.COM' in line or line == '\ufeff1\n':
            continue
        else:
            try:
                int(line.lstrip())
                print(line)
            except ValueError:
                fw.write(line)
    fw.close()