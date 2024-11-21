.data
newline: .asciiz "\n"
.text
.globl main
main:
li $a1, 0x10000000 # Cargar la direccion asignada para la variable 't11-ab8b3edd-33ac-4600-b0b7-2154c949d0f3' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t0, 10
li $a1, 0x10000004 # Cargar la direccion asignada para la variable 'numero' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $a0, $t0 # Guardar el valor de la variable 'numero' en a0
jal L_fibonacci_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000008 # Cargar la direccion asignada para la variable 't12-3c0807df-ee0f-4e4f-b857-3008a19ee51f' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 'resultado' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000010 # Cargar la direccion asignada para la variable 't13-0285ad61-84db-4849-98ea-8f73769dc373' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t2, 0x10000010 # La direccion del heap de la variable 't13-0285ad61-84db-4849-98ea-8f73769dc373' se carga en $t2
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
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 15($t2)  # Guardar el caracter en la direccion 15(0x10000010)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 16($t2)  # Guardar el caracter en la direccion 16(0x10000010)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 17($t2)  # Guardar el caracter en la direccion 17(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 18($t2)  # Guardar el caracter en la direccion 18(0x10000010)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 19($t2)  # Guardar el caracter en la direccion 19(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 20($t2)  # Guardar el caracter en la direccion 20(0x10000010)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 21($t2)  # Guardar el caracter en la direccion 21(0x10000010)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 22($t2)  # Guardar el caracter en la direccion 22(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 23($t2)  # Guardar el caracter en la direccion 23(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 24($t2)  # Guardar el caracter en la direccion 24(0x10000010)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 25($t2)  # Guardar el caracter en la direccion 25(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 26($t2)  # Guardar el caracter en la direccion 26(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 27($t2)  # Guardar el caracter en la direccion 27(0x10000010)
li $t1, 70  # Cargar ASCII del caracter "F" en $t1
sb $t1, 28($t2)  # Guardar el caracter en la direccion 28(0x10000010)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 29($t2)  # Guardar el caracter en la direccion 29(0x10000010)
li $t1, 98  # Cargar ASCII del caracter "b" en $t1
sb $t1, 30($t2)  # Guardar el caracter en la direccion 30(0x10000010)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 31($t2)  # Guardar el caracter en la direccion 31(0x10000010)
li $t1, 110  # Cargar ASCII del caracter "n" en $t1
sb $t1, 32($t2)  # Guardar el caracter en la direccion 32(0x10000010)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 33($t2)  # Guardar el caracter en la direccion 33(0x10000010)
li $t1, 99  # Cargar ASCII del caracter "c" en $t1
sb $t1, 34($t2)  # Guardar el caracter en la direccion 34(0x10000010)
li $t1, 99  # Cargar ASCII del caracter "c" en $t1
sb $t1, 35($t2)  # Guardar el caracter en la direccion 35(0x10000010)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 36($t2)  # Guardar el caracter en la direccion 36(0x10000010)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 37($t2)  # Guardar el caracter en la direccion 37(0x10000010)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 38($t2)  # Guardar el caracter en la direccion 38(0x10000010)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 39($t2)  # Guardar el caracter en la direccion 39(0x10000010)
li $t1, 58  # Cargar ASCII del caracter ":" en $t1
sb $t1, 40($t2)  # Guardar el caracter en la direccion 40(0x10000010)
li $t1, 0  # Terminador nulo
sb $t1, 41($t2)  # Guardar terminador nulo
lw $t1, 0($t2) # El valor de la variable 't13-0285ad61-84db-4849-98ea-8f73769dc373' en el heap se carga en $t1
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

L_fibonacci_1:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -56   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'n' en el stack
li $t0, 1
sw $t0, 12($fp) # guardar el valor de la variable 't0-415e6966-9535-477e-b8b9-0bd86f520e05' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "t0-415e6966-9535-477e-b8b9-0bd86f520e05" del stack
blt $t1, $t2, L2 # Saltar a L2 si n < t0-415e6966-9535-477e-b8b9-0bd86f520e05
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "t0-415e6966-9535-477e-b8b9-0bd86f520e05" del stack
beq $t1, $t2, L2 # Saltar a L2 si n == t0-415e6966-9535-477e-b8b9-0bd86f520e05
li $t3, 0
sw $t3, 16($fp) # guardar el valor de la variable 't1-0bff216f-3ffb-4cf6-9234-709806894e1c' en el stack
j L1
L2:
li $t0, 1
sw $t0, 16($fp) # guardar el valor de la variable 't1-0bff216f-3ffb-4cf6-9234-709806894e1c' en el stack
L1:
lw $t0, 16($fp) # Obtener el valor de la variable "t1-0bff216f-3ffb-4cf6-9234-709806894e1c" del stack
li $t1, 0
beq $t0, $t1, L4 # Saltar a L4 si t1-0bff216f-3ffb-4cf6-9234-709806894e1c == 0
lw $t2, 8($fp) # Obtener el valor de la variable "n" del stack
sw $t2, 20($fp) # guardar el valor de la variable 't2-a8824e37-c702-4e13-a1ff-fff1ab277bc1' en el stack
lw $v0, 20($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 56     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
j L3
L4:
li $t0, 1
sw $t0, 20($fp) # guardar el valor de la variable 't3-46695ba1-35a9-407c-afd0-d78b41b40cea' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t2, 20($fp) # Obtener el valor de la variable "t3-46695ba1-35a9-407c-afd0-d78b41b40cea" del stack
sub $t3, $t1, $t2 # Restar los valores de n y t3-46695ba1-35a9-407c-afd0-d78b41b40cea
sw $t3, 24($fp) # Almacenar el resultado de la resta en t4-a4e0f707-a73b-4c6c-8047-eb601538e791
lw $t3, 24($fp) # Obtener el valor de la variable "t4-a4e0f707-a73b-4c6c-8047-eb601538e791" del stack
move $a0, $t3 # Guardar el valor de la variable 't4-a4e0f707-a73b-4c6c-8047-eb601538e791' en a0
jal L_fibonacci_1
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 28($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t0, 28($fp) # Obtener el valor de la variable "t5-2eff10c5-44ad-4bc7-a008-9df0d730c405" del stack
sw $t0, 32($fp) # guardar el valor de la variable 'a' en el stack
li $t1, 2
sw $t1, 36($fp) # guardar el valor de la variable 't6-2e5fae90-9919-47e8-8024-5e20b29fbfd6' en el stack
lw $t2, 8($fp) # Obtener el valor de la variable "n" del stack
lw $t3, 36($fp) # Obtener el valor de la variable "t6-2e5fae90-9919-47e8-8024-5e20b29fbfd6" del stack
sub $t4, $t2, $t3 # Restar los valores de n y t6-2e5fae90-9919-47e8-8024-5e20b29fbfd6
sw $t4, 40($fp) # Almacenar el resultado de la resta en t7-afef87be-6560-43c8-a99c-770cdef49ed0
lw $t4, 40($fp) # Obtener el valor de la variable "t7-afef87be-6560-43c8-a99c-770cdef49ed0" del stack
move $a0, $t4 # Guardar el valor de la variable 't7-afef87be-6560-43c8-a99c-770cdef49ed0' en a0
jal L_fibonacci_1
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 44($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t0, 44($fp) # Obtener el valor de la variable "t8-8bc58258-dbed-4e76-8abf-3ef0876ee25e" del stack
sw $t0, 48($fp) # guardar el valor de la variable 'b' en el stack
lw $t1, 32($fp) # Obtener el valor de la variable "a" del stack
lw $t2, 48($fp) # Obtener el valor de la variable "b" del stack
add $t3, $t1, $t2 # Sumar los valores de a y b
sw $t3, 52($fp) # Almacenar el resultado de la suma en t9-c7150ee5-1c46-4097-b7d8-4a7d3231a79e
lw $t3, 52($fp) # Obtener el valor de la variable "t9-c7150ee5-1c46-4097-b7d8-4a7d3231a79e" del stack
sw $t3, 56($fp) # guardar el valor de la variable 't10-b6a82aff-67b0-4d81-9d95-d2431e6a7747' en el stack
lw $v0, 56($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 56     # Limpiar espacio de variables locales
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
