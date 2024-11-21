.data
newline: .asciiz "\n"
.text
.globl main
main:
li $a1, 0x10000000 # Cargar la direccion asignada para la variable 't9-75348328-5371-4c57-8c14-1f6a9355d806' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t0, 5
li $a1, 0x10000004 # Cargar la direccion asignada para la variable 'numero' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $a0, $t0 # Guardar el valor de la variable 'numero' en a0
jal L_factorial_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000008 # Cargar la direccion asignada para la variable 't10-7cfc2909-edc9-4996-a7a7-51688093938a' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 'resultado' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000010 # Cargar la direccion asignada para la variable 't11-a6d69ac7-08a8-40b3-b691-e1404f07f23b' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t2, 0x10000010 # La direccion del heap de la variable 't11-a6d69ac7-08a8-40b3-b691-e1404f07f23b' se carga en $t2
li $t1, 69  # Cargar ASCII del caracter "E" en $t1
sb $t1, 0($t2)  # Guardar el caracter en la direccion 0(0x10000010)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 1($t2)  # Guardar el caracter en la direccion 1(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 2($t2)  # Guardar el caracter en la direccion 2(0x10000010)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 3($t2)  # Guardar el caracter en la direccion 3(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 4($t2)  # Guardar el caracter en la direccion 4(0x10000010)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 5($t2)  # Guardar el caracter en la direccion 5(0x10000010)
li $t1, 117  # Cargar ASCII del caracter "u" en $t1
sb $t1, 6($t2)  # Guardar el caracter en la direccion 6(0x10000010)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 7($t2)  # Guardar el caracter en la direccion 7(0x10000010)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 8($t2)  # Guardar el caracter en la direccion 8(0x10000010)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 9($t2)  # Guardar el caracter en la direccion 9(0x10000010)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 10($t2)  # Guardar el caracter en la direccion 10(0x10000010)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 11($t2)  # Guardar el caracter en la direccion 11(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 12($t2)  # Guardar el caracter en la direccion 12(0x10000010)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 13($t2)  # Guardar el caracter en la direccion 13(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 14($t2)  # Guardar el caracter en la direccion 14(0x10000010)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 15($t2)  # Guardar el caracter en la direccion 15(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 16($t2)  # Guardar el caracter en la direccion 16(0x10000010)
li $t1, 102  # Cargar ASCII del caracter "f" en $t1
sb $t1, 17($t2)  # Guardar el caracter en la direccion 17(0x10000010)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 18($t2)  # Guardar el caracter en la direccion 18(0x10000010)
li $t1, 99  # Cargar ASCII del caracter "c" en $t1
sb $t1, 19($t2)  # Guardar el caracter en la direccion 19(0x10000010)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 20($t2)  # Guardar el caracter en la direccion 20(0x10000010)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 21($t2)  # Guardar el caracter en la direccion 21(0x10000010)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 22($t2)  # Guardar el caracter en la direccion 22(0x10000010)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 23($t2)  # Guardar el caracter en la direccion 23(0x10000010)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 24($t2)  # Guardar el caracter en la direccion 24(0x10000010)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 25($t2)  # Guardar el caracter en la direccion 25(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 26($t2)  # Guardar el caracter en la direccion 26(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 27($t2)  # Guardar el caracter en la direccion 27(0x10000010)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 28($t2)  # Guardar el caracter en la direccion 28(0x10000010)
li $t1, 58  # Cargar ASCII del caracter ":" en $t1
sb $t1, 29($t2)  # Guardar el caracter en la direccion 29(0x10000010)
li $t1, 0  # Terminador nulo
sb $t1, 30($t2)  # Guardar terminador nulo
lw $t1, 0($t2) # El valor de la variable 't11-a6d69ac7-08a8-40b3-b691-e1404f07f23b' en el heap se carga en $t1
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t2  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t0  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $v0, 10
syscall

L_factorial_1:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -36   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'n' en el stack
li $t0, 1
sw $t0, 12($fp) # guardar el valor de la variable 't0-f5439cb1-0dc7-4be3-b557-36549aa1f250' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "t0-f5439cb1-0dc7-4be3-b557-36549aa1f250" del stack
blt $t1, $t2, L2 # Saltar a L2 si n < t0-f5439cb1-0dc7-4be3-b557-36549aa1f250
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "t0-f5439cb1-0dc7-4be3-b557-36549aa1f250" del stack
beq $t1, $t2, L2 # Saltar a L2 si n == t0-f5439cb1-0dc7-4be3-b557-36549aa1f250
li $t3, 0
sw $t3, 16($fp) # guardar el valor de la variable 't1-e58056ac-3e0f-4bc5-9fde-8f1ee8bc96d4' en el stack
j L1
L2:
li $t0, 1
sw $t0, 16($fp) # guardar el valor de la variable 't1-e58056ac-3e0f-4bc5-9fde-8f1ee8bc96d4' en el stack
L1:
lw $t0, 16($fp) # Obtener el valor de la variable "t1-e58056ac-3e0f-4bc5-9fde-8f1ee8bc96d4" del stack
li $t1, 0
beq $t0, $t1, L4 # Saltar a L4 si t1-e58056ac-3e0f-4bc5-9fde-8f1ee8bc96d4 == 0
li $t2, 1
sw $t2, 20($fp) # guardar el valor de la variable 't2-cac7b885-2eae-4e70-893f-702ac5c8dd51' en el stack
lw $t3, 20($fp) # Obtener el valor de la variable "t2-cac7b885-2eae-4e70-893f-702ac5c8dd51" del stack
sw $t3, 24($fp) # guardar el valor de la variable 't3-1be05c39-9db3-4a1b-9c66-1d4f2c9f6c02' en el stack
lw $v0, 24($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 36     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
j L3
L4:
li $t0, 1
sw $t0, 20($fp) # guardar el valor de la variable 't4-71b00de8-bf72-4464-864e-55e9f017787f' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 20($fp) # Obtener el valor de la variable "t4-71b00de8-bf72-4464-864e-55e9f017787f" del stack
sub $t3, $t1, $t2 # Restar los valores de n y t4-71b00de8-bf72-4464-864e-55e9f017787f
sw $t3, 24($fp) # Almacenar el resultado de la resta en t5-022a14ec-efeb-4813-bcd1-9dedfcf841c0
lw $t3, 24($fp) # Obtener el valor de la variable "t5-022a14ec-efeb-4813-bcd1-9dedfcf841c0" del stack
move $a0, $t3 # Guardar el valor de la variable 't5-022a14ec-efeb-4813-bcd1-9dedfcf841c0' en a0
jal L_factorial_1
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 28($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t0, 28($fp) # Obtener el valor de la variable "t6-4d12b59b-135d-45c5-ab41-2b1f0ba89669" del stack
mul $t2, $t1, $t0 # Multiplicar los valores de n y t6-4d12b59b-135d-45c5-ab41-2b1f0ba89669
sw $t2, 32($fp) # Almacenar el resultado de la multiplicacion en t7-c68285fb-1dbc-4c42-a4c4-5fb940d89de4
lw $t2, 32($fp) # Obtener el valor de la variable "t7-c68285fb-1dbc-4c42-a4c4-5fb940d89de4" del stack
sw $t2, 36($fp) # guardar el valor de la variable 't8-58387a17-7ca0-4f88-b84f-5395769c46f0' en el stack
lw $v0, 36($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 36     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
L3:

check_existing_variable:
lw $s0, 0($a1) # Cargar la direccion de la variable en memoria estatica
bnez $s0, end_check_existing_variable # Si la direccion (argumento 1) no es 0, regresar
save_variable:
li $v0, 9
move $a0, $a2 # Obtener el tamano de la variable del argumento 2
syscall
move $a2, $v0 # Guardar la direccion de memoria asignada en $a2
sw $a2, 0($a1) # Guardar la direccion de memoria asignada en la variable en memoria estatica
end_check_existing_variable:
jr $ra

alloc_memory:
li $v0, 9
move $a0, $s0
syscall
move $s1, $v0
jr $ra

copy_string:
copy_loop:
lb $s2, 0($s0)    # Leer caracter de la cadena fuente
beqz $s2, end_copy # Si el caracter es nulo, terminar
add $s4, $s3, $s1 # Calcular la direccion efectiva
sb $s2, 0($s4)    # Escribir el caracter en la cadena destino
addi $s0, $s0, 1  # Avanzar en la cadena fuente
addi $s1, $s1, 1  # Avanzar en la cadena destino
j copy_loop               # Continuar con el siguiente caracter
end_copy:
jr $ra
