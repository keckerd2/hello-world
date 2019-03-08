from my_debugger import debugger
debugger = debugger()

pid = input("输入需要依附的程序的pid：")
debugger.attach(int(pid))

list = debugger.enumerate_threads()
for thread in list:
    thread_context = debugger.get_thread_context(thread)
    print("[*] 线程id：0x%08x" % thread)
    print("[*] EIP:0x%08x" % thread_context.Eip)
    print("[*] ESP:0x%08x" % thread_context.Esp)
    print("[*] EBP:0x%08x" % thread_context.Ebp)
    print("[*] EAX:0x%08x" % thread_context.Eax)
    print("[*] EBX:0x%08x" % thread_context.Ebx)
    print("[*] ECX:0x%08x" % thread_context.Ecx)
    print("[*] EDX:0x%08x" % thread_context.Edx)

debugger.detach()
