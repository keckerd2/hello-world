from ctypes import *

# 为了清晰起见，让我们将Microsoft类型映射到ctypes
BYTE                            = c_ubyte
WORD                            = c_ushort
DWORD                           = c_ulong
LPBYTE                          = POINTER(c_ubyte)
LPTSTR                          = POINTER(c_char)
HANDLE                          = c_void_p

LONG = c_long
PVOID = c_void_p
ULONG_PTR =c_ulong
ULONG = c_ulong

DEBUG_PROCESS                   = 0x00000001
CREATE_NEW_CONSOLE              = 0x00000010

# 常量
PROCESS_ALL_ACCESS              = 0x001F0FFF
INFINITE                        = 0xFFFFFFFF

DBG_CONTINUE                    = 0x00010002
TH32CS_SNAPTHREAD               = 0x00000004    # 包括快照中系统中的所有线程。要枚举线程

# 线程常量
THREAD_ALL_ACCESS               = 0x001F03FF

# GetThreadContext()的上下文标志
CONTEXT_FULL                    = 0x00010007
CONTEXT_DEBUG_REGISTERS         = 0x00010010


class STARTUPINFO(Structure):
    _fields_=[
        ("cb",DWORD),
        ("lpReserved",LPTSTR),
        ("lpDesktop",LPTSTR),
        ("lpTitle",LPTSTR),
        ("dwX",DWORD),
        ("dwY",DWORD),
        ("dwXSize",DWORD),
        ("dwYSize",DWORD),
        ("dwXCountChars",DWORD),
        ("dwYCountChars",DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]

class PROCESS_INFORMATION(Structure):
    _fields_=[
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId",DWORD),
        ("dwThreadId", DWORD),
    ]

class EXCEPTION_RECORD(Structure):
    pass
EXCEPTION_RECORD._fields_ = [#这里之所以要这么设计，是因为ExceptionRecode调用了EXCEPTION_RECORD
        ("ExceptionCode",DWORD),
        ("ExceptionFlags",DWORD),
        ("ExceptionRecord",POINTER(EXCEPTION_RECORD)),
        ("ExceptionAddress",PVOID),
        ("NumberParameters",DWORD),
        ("ExceptionInfomation",ULONG_PTR * 15),
    ]


class EXCEPTION_DEBUG_INFO(Structure):
    _fields_ = [
        ("ExceptionRecord",EXCEPTION_RECORD),
        ('dwFistChance',DWORD),
    ]
class DEBUG_EVENT_UNION(Union):
    _fields_ = [
        ("Exception",EXCEPTION_DEBUG_INFO),
#        ("CreateThread",CREATE_THREAD_DEBUG_INFO),
#        ("CreateProcessInfo",CREATE_PROCESS_DEBUG_INFO),
#       ("ExitThread",EXIT_THREAD_DEBUG_INFO),
#       ("ExitProcess",EXIT_PROCESS_DEBUG_INFO),
#        ("LoadDll",LOAD_DLL_DEBUG_INFO),
#        ("UnloadDll",UNLOAD_DLL_DEBUG_INFO),
#        ("DebugString",OUTPUT_DEBUG_INFO),
#        ("RipInfo",RIP_INFO),
    ]
class DEBUG_EVENT(Structure):#定义DEBUG_EVENT处理事件
    _fields_ = [
        ("dwDebugEventCode",DWORD),#调试事件类型
        ("dwProcessId",DWORD),
        ("dwThreadId",DWORD),
        ("u",DEBUG_EVENT_UNION),
    ]

class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize",DWORD),
        ("cntUsage",DWORD),
        ("th32ThreadID",DWORD),
        ("th32OwnerProcessID",DWORD),
        ("tpBasePri",LONG),
        ("tpDeltaPri",LONG),
        ("dwFlags",DWORD),
    ]

# Used by the CONTEXT structure
class FLOATING_SAVE_AREA(Structure):
   _fields_ = [
        ("ControlWord", DWORD),
        ("StatusWord", DWORD),
        ("TagWord", DWORD),
        ("ErrorOffset", DWORD),
        ("ErrorSelector", DWORD),
        ("DataOffset", DWORD),
        ("DataSelector", DWORD),
        ("RegisterArea", BYTE * 80),
        ("Cr0NpxState", DWORD),
]

# The CONTEXT structure which holds all of the
# register values after a GetThreadContext() call
class CONTEXT(Structure):
    _fields_ = [
        ("ContextFlags", DWORD),
        ("Dr0", DWORD),
        ("Dr1", DWORD),
        ("Dr2", DWORD),
        ("Dr3", DWORD),
        ("Dr6", DWORD),
        ("Dr7", DWORD),
        ("FloatSave", FLOATING_SAVE_AREA),
        ("SegGs", DWORD),
        ("SegFs", DWORD),
        ("SegEs", DWORD),
        ("SegDs", DWORD),
        ("Edi", DWORD),
        ("Esi", DWORD),
        ("Ebx", DWORD),
        ("Edx", DWORD),
        ("Ecx", DWORD),
        ("Eax", DWORD),
        ("Ebp", DWORD),
        ("Eip", DWORD),
        ("SegCs", DWORD),
        ("EFlags", DWORD),
        ("Esp", DWORD),
        ("SegSs", DWORD),
        ("ExtendedRegisters", BYTE * 512),
]
