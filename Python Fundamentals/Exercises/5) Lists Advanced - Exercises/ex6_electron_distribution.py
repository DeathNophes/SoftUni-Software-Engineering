electrons = int(input())
electrons_list = []
shell = 0
while electrons > 0:
    shell += 1
    max_electrons_in_current_shell = 2 * (shell ** 2)
    if electrons - max_electrons_in_current_shell >= 0:
        electrons_list.append(max_electrons_in_current_shell)
    else:
        electrons_list.append(electrons)
    electrons -= max_electrons_in_current_shell
print(electrons_list)
