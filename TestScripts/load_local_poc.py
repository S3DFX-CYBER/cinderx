import dis
import types

print("=" * 60)
print("LOAD_LOCAL RESEARCH POC")
print("=" * 60)

# Placeholder function until we wire in actual static compilation
def testfunc():
    i = 0
    while i < 100:
        i += 1
    return i

print("\n[+] Bytecode")
dis.dis(testfunc)

print("\n[+] Constants")
for idx, c in enumerate(testfunc.__code__.co_consts):
    print(f"{idx}: {repr(c)}")

print("\n[+] Code Object Info")
print("co_argcount =", testfunc.__code__.co_argcount)
print("co_nlocals =", testfunc.__code__.co_nlocals)
print("co_stacksize =", testfunc.__code__.co_stacksize)

print("\n[+] Validation Complete")
