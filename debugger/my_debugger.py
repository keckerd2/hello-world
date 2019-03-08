from ctypes import *
from my_debugger_defines import *
kernel32 = windll.kernel32
class debugger():
    def __init__(self):
        self.h_process              = None          # 进程句柄
        self.pid                    = None          # 进程pid
        self.debugger_active        = False         # 进程活跃状态
        self.h_thread               = None          # 线程id
        self.context                = None          # 寄存器内容
        pass
    def load(self,path_to_exe):
        creation_flags              = DEBUG_PROCESS
        startupinfo                 = STARTUPINFO()
        process_information         = PROCESS_INFORMATION()
        startupinfo.dwFlags         = 0x1
        startupinfo.wShowWindow     = 0x0
        startupinfo.cb=sizeof(startupinfo)
        if kernel32.CreateProcessA(path_to_exe,
                                None,
                                None,
                                None,
                                None,
                                creation_flags,
                                None,
                                None,
                                byref(startupinfo),
                                byref(process_information)):
            print("[*] 我们成功启动目标程序!")
            print("[*] PID:%d"%process_information.dwProcessId)
        else:
            print("[*] Error:0x%08x."%kernel32.GetLastError())

    def open_process(self,pid):
        """
        打开进程权限
        :param pid 进程pid
        return 进程句柄
        """
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,pid,False)
        return h_process

    def attach(self,pid):
        """
        附加程序
        """
        self.h_process = self.open_process(pid)
        # 试图附加到目标程序，若附加操作失败
        # 则在输出提示信息后返回
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            self.run()
        else:
            print("[*] 错误码:0x%08x." % kernel32.GetLastError())
            print("[*] 无法附加到进程.")

    def run(self):
        """
        不断轮询调试事件
        """
        # 我们等待发生在debug进程中的调试事件
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        """
        获得调试事件
        """
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE

        if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
            # 我们现在不打算构建任何处理程序
            # 这里简单的操作就可以恢复执行目标进程

            # input("按下任意键....")
            # self.debugger_active = False

            kernel32.ContinueDebugEvent(\
                    debug_event.dwProcessId,\
                    debug_event.dwThreadId,\
                    continue_status)
    def detach(self):
        """
        停止调试
        """
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] 完成调试，退出....")
            return True
        else:
            print("这里有一个错误")
            return False

    def enumerate_threads(self):
        """
        枚举线程
        """
        thread_entry                = THREADENTRY32()
        thread_list                 = []                        # 线程列表
        # 获取指定进程的快照，以及这些进程使用的堆，模块和线程
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD,self.pid)
        if snapshot is not None:
            thread_entry.dwSize     = sizeof(thread_entry)
            # 通过Thread32First列举出线程
            success = kernel32.Thread32First(snapshot,byref((thread_entry)))
            while success:
                # 线程拥有的进程id必须与我们输入的pid相同
                if thread_entry.th32OwnerProcessID == self.pid:
                    thread_list.append(thread_entry.th32ThreadID)
                success = kernel32.Thread32Next(snapshot,byref(thread_entry))
            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            return False
    def get_thread_context(self,thread_id):
        """
        获取寄存器内容
        """
        context                 = CONTEXT()
        context.ContextFlags    = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        # 获得一个线程句柄
        h_thread = self.open_thread(thread_id)
        if kernel32.GetThreadContext(h_thread,byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            return False

    def open_thread(self,thread_id):
        """
        打开线程，获取线程句柄
        :param thread_id 线程id类似进程pid
        :return 线程句柄
        """
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS,None,thread_id)
        if h_thread is not None:
            return h_thread
        else:
            print("[*] 无法获得有效的线程句柄")
            return False

