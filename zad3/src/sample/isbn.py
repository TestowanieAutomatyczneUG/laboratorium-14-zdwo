class ISBN:
    def alg(self, numb):
        newnumb = ''
        toadd = 0
        for i in range(len(numb)):
            if numb[i].isnumeric():
                newnumb+=numb[i]
        for i in range(len(newnumb)-1):
            if (i+1) % 2 == 0:
                toadd += int(newnumb[i])*3
            else:
                toadd += int(newnumb[i])
        if toadd % 10 == 0:
            contr = 0
        else:
            contr = 10 - (toadd % 10)

        return contr


i = ISBN()
i.alg('978-83-7181-510-2')
