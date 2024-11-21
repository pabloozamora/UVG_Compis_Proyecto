.data
newline: .asciiz "\n"
.text
.globl main
main:
li $a1, 0x10000008 # Cargar la direccion asignada para la variable 't15-3beb93e8-8d97-481f-8c45-d7208f508ce6' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t0, 12
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 't16-5ef2187a-f5ea-47bf-bb88-202706bb4ce5' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t1, 0x1000000c # La direccion del heap de la variable 't16-5ef2187a-f5ea-47bf-bb88-202706bb4ce5' se carga en $t1
move $a0, $t1 # Guardar el valor de la variable 't16-5ef2187a-f5ea-47bf-bb88-202706bb4ce5' en a0
move $a1, $t0 # Guardar el valor de la variable 't15-3beb93e8-8d97-481f-8c45-d7208f508ce6' en a1
jal L_CajaRegistradora_init_1
lw $t0, 0x1000000c # La direccion del heap de la instancia 't16-5ef2187a-f5ea-47bf-bb88-202706bb4ce5' se carga en $t0
li $t1, 0x10000010 # La direccion de memoria estatica de la variable 'caja' se carga en $t1
sw $t0, 0($t1) # Almacenar la direccion de memoria de la instancia 't16-5ef2187a-f5ea-47bf-bb88-202706bb4ce5' en la variable 'caja'
li $a1, 0x10000014 # Cargar la direccion asignada para la variable 't17-ce754a73-34f5-49cd-b23b-519af38473d9' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t2, 100
move $a0, $t0 # Guardar el valor de la variable 'caja' en a0
move $a1, $t2 # Guardar el valor de la variable 't17-ce754a73-34f5-49cd-b23b-519af38473d9' en a1
jal L_CajaRegistradora_agregarProducto_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000018 # Cargar la direccion asignada para la variable 't18-eb8e81f0-18ff-4410-8f5d-9c76f6f075af' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000001c # Cargar la direccion asignada para la variable 't19-a64d5508-ff26-481e-854f-c0044ec0c55e' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t1, 50
lw $t2, 0x10000010 # La direccion del heap de la variable 'caja' se carga en $t2
move $a0, $t2 # Guardar el valor de la variable 'caja' en a0
move $a1, $t1 # Guardar el valor de la variable 't19-a64d5508-ff26-481e-854f-c0044ec0c55e' en a1
jal L_CajaRegistradora_agregarProducto_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000020 # Cargar la direccion asignada para la variable 't20-b5bdeef3-b604-444b-8b83-0fb6c4dfb8e1' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x10000024 # Cargar la direccion asignada para la variable 't21-eb79abdf-70f5-43db-a9ce-f4d60b2abbdd' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t1, 25
lw $t2, 0x10000010 # La direccion del heap de la variable 'caja' se carga en $t2
move $a0, $t2 # Guardar el valor de la variable 'caja' en a0
move $a1, $t1 # Guardar el valor de la variable 't21-eb79abdf-70f5-43db-a9ce-f4d60b2abbdd' en a1
jal L_CajaRegistradora_agregarProducto_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000028 # Cargar la direccion asignada para la variable 't22-7db2c185-7343-4334-8f34-9482b3642b87' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000002c # Cargar la direccion asignada para la variable 't23-8da6efba-0119-4d65-9514-3a6fd87c6d0e' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t2, 0x1000002c # La direccion del heap de la variable 't23-8da6efba-0119-4d65-9514-3a6fd87c6d0e' se carga en $t2
li $t1, 69  # Cargar ASCII del caracter "E" en $t1
sb $t1, 0($t2)  # Guardar el caracter en la direccion 0(0x1000002c)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 1($t2)  # Guardar el caracter en la direccion 1(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 2($t2)  # Guardar el caracter en la direccion 2(0x1000002c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 3($t2)  # Guardar el caracter en la direccion 3(0x1000002c)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 4($t2)  # Guardar el caracter en la direccion 4(0x1000002c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 5($t2)  # Guardar el caracter en la direccion 5(0x1000002c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 6($t2)  # Guardar el caracter en la direccion 6(0x1000002c)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 7($t2)  # Guardar el caracter en la direccion 7(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 8($t2)  # Guardar el caracter en la direccion 8(0x1000002c)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 9($t2)  # Guardar el caracter en la direccion 9(0x1000002c)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 10($t2)  # Guardar el caracter en la direccion 10(0x1000002c)
li $t1, 110  # Cargar ASCII del caracter "n" en $t1
sb $t1, 11($t2)  # Guardar el caracter en la direccion 11(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 12($t2)  # Guardar el caracter en la direccion 12(0x1000002c)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 13($t2)  # Guardar el caracter en la direccion 13(0x1000002c)
li $t1, 109  # Cargar ASCII del caracter "m" en $t1
sb $t1, 14($t2)  # Guardar el caracter en la direccion 14(0x1000002c)
li $t1, 112  # Cargar ASCII del caracter "p" en $t1
sb $t1, 15($t2)  # Guardar el caracter en la direccion 15(0x1000002c)
li $t1, 117  # Cargar ASCII del caracter "u" en $t1
sb $t1, 16($t2)  # Guardar el caracter en la direccion 16(0x1000002c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 17($t2)  # Guardar el caracter en la direccion 17(0x1000002c)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 18($t2)  # Guardar el caracter en la direccion 18(0x1000002c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 19($t2)  # Guardar el caracter en la direccion 19(0x1000002c)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 20($t2)  # Guardar el caracter en la direccion 20(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 21($t2)  # Guardar el caracter en la direccion 21(0x1000002c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 22($t2)  # Guardar el caracter en la direccion 22(0x1000002c)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 23($t2)  # Guardar el caracter en la direccion 23(0x1000002c)
li $t1, 58  # Cargar ASCII del caracter ":" en $t1
sb $t1, 24($t2)  # Guardar el caracter en la direccion 24(0x1000002c)
li $t1, 0  # Terminador nulo
sb $t1, 25($t2)  # Guardar terminador nulo
lw $t1, 0($t2) # El valor de la variable 't23-8da6efba-0119-4d65-9514-3a6fd87c6d0e' en el heap se carga en $t1
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t2  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $a1, 0x10000030 # Cargar la direccion asignada para la variable 't24-cb45a5f6-ea3f-4ed9-8e7a-db578a862851' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t3, 0x10000010 # La direccion del heap de la variable 'caja' se carga en $t3
lw $t4, 4($t3) # Cargar el valor de la propiedad de la instancia 'caja' en $t3
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t4  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
move $a0, $t3 # Guardar el valor de la variable 'caja' en a0
jal L_CajaRegistradora_calcularTotalConImpuesto_0
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000034 # Cargar la direccion asignada para la variable 't25-b7b3f8e7-cc92-4131-926f-6c3938405eea' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
lw $t1, 0x10000010 # La direccion del heap de la variable 'caja' se carga en $t1
move $a0, $t1 # Guardar el valor de la variable 'caja' en a0
jal L_CajaRegistradora_reiniciar_0
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000038 # Cargar la direccion asignada para la variable 't26-e385fb12-ee59-4b5c-bc1a-fa848951b81e' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000003c # Cargar la direccion asignada para la variable 't27-033c9224-576d-4b4e-a4a1-5c160cbe8741' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t2, 0x1000003c # La direccion del heap de la variable 't27-033c9224-576d-4b4e-a4a1-5c160cbe8741' se carga en $t2
li $t1, 65  # Cargar ASCII del caracter "A" en $t1
sb $t1, 0($t2)  # Guardar el caracter en la direccion 0(0x1000003c)
li $t1, 104  # Cargar ASCII del caracter "h" en $t1
sb $t1, 1($t2)  # Guardar el caracter en la direccion 1(0x1000003c)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 2($t2)  # Guardar el caracter en la direccion 2(0x1000003c)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 3($t2)  # Guardar el caracter en la direccion 3(0x1000003c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 4($t2)  # Guardar el caracter en la direccion 4(0x1000003c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 5($t2)  # Guardar el caracter en la direccion 5(0x1000003c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 6($t2)  # Guardar el caracter en la direccion 6(0x1000003c)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 7($t2)  # Guardar el caracter en la direccion 7(0x1000003c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 8($t2)  # Guardar el caracter en la direccion 8(0x1000003c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 9($t2)  # Guardar el caracter en la direccion 9(0x1000003c)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 10($t2)  # Guardar el caracter en la direccion 10(0x1000003c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 11($t2)  # Guardar el caracter en la direccion 11(0x1000003c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 12($t2)  # Guardar el caracter en la direccion 12(0x1000003c)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 13($t2)  # Guardar el caracter en la direccion 13(0x1000003c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 14($t2)  # Guardar el caracter en la direccion 14(0x1000003c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 15($t2)  # Guardar el caracter en la direccion 15(0x1000003c)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 16($t2)  # Guardar el caracter en la direccion 16(0x1000003c)
li $t1, 58  # Cargar ASCII del caracter ":" en $t1
sb $t1, 17($t2)  # Guardar el caracter en la direccion 17(0x1000003c)
li $t1, 0  # Terminador nulo
sb $t1, 18($t2)  # Guardar terminador nulo
lw $t1, 0($t2) # El valor de la variable 't27-033c9224-576d-4b4e-a4a1-5c160cbe8741' en el heap se carga en $t1
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t2  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $a1, 0x10000040 # Cargar la direccion asignada para la variable 't28-7adc3506-009a-4a8f-9779-aca5d9608239' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t3, 0x10000010 # La direccion del heap de la variable 'caja' se carga en $t3
lw $t4, 4($t3) # Cargar el valor de la propiedad de la instancia 'caja' en $t3
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t4  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $v0, 10
syscall

L_CajaRegistradora_init_1:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -16   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'impuesto' en el stack
lw $t0, 12($fp) # Obtener el valor de la variable "impuesto" del stack
lw $t1, 8($fp) # La direccion del stack de la variable 'self' se carga en $t1
sw $t0, 0($t1) # Almacenar el valor de la variable 'self' en el heap
li $t2, 0
sw $t2, 16($fp) # guardar el valor de la variable 't0-69adcbe3-31d5-45e5-8e32-f61b3a3c7349' en el stack
lw $t3, 16($fp) # Obtener el valor de la variable "t0-69adcbe3-31d5-45e5-8e32-f61b3a3c7349" del stack
lw $t4, 8($fp) # La direccion del stack de la variable 'self' se carga en $t4
sw $t3, 4($t4) # Almacenar el valor de la variable 'self' en el heap
lw $v0, 16($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 16     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_CajaRegistradora_agregarProducto_1:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -24   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'precio' en el stack
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t0, 4($t0) # Obtener el valor de la propiedad 4 de la variable "self" del heap
sw $t0, 16($fp) # guardar el valor de la variable 't1-eec66bdf-dff9-477e-87d3-097038cd3a70' en el stack
lw $t1, 16($fp) # Obtener el valor de la variable "t1-eec66bdf-dff9-477e-87d3-097038cd3a70" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "precio" del stack
add $t3, $t1, $t2 # Sumar los valores de t1-eec66bdf-dff9-477e-87d3-097038cd3a70 y precio
sw $t3, 20($fp) # Almacenar el resultado de la suma en t2-1644ae7b-4980-4fad-ac69-d1d5b7434eb2
lw $t3, 20($fp) # Obtener el valor de la variable "t2-1644ae7b-4980-4fad-ac69-d1d5b7434eb2" del stack
lw $t4, 8($fp) # La direccion del stack de la variable 'self' se carga en $t4
sw $t3, 4($t4) # Almacenar el valor de la variable 'self' en el heap
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t5, $fp, 24 # La direccion del stack de la variable 't3-a99c81b3-78f2-4017-9069-db3bb2bdf52f' se carga en $t5
sw $s1, 0($t5) # Almacenar la direccion de memoria de la cadena 't3-a99c81b3-78f2-4017-9069-db3bb2bdf52f' en el stack
lw $t5, 0($t5) # La direccion de memoria de la cadena 't3-a99c81b3-78f2-4017-9069-db3bb2bdf52f' se carga en $t5
li $t6, 80  # Cargar ASCII del caracter "P" en $t6
sb $t6, 0($t5)  # Guardar el caracter en la direccion 0(24)
li $t6, 114  # Cargar ASCII del caracter "r" en $t6
sb $t6, 1($t5)  # Guardar el caracter en la direccion 1(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 2($t5)  # Guardar el caracter en la direccion 2(24)
li $t6, 100  # Cargar ASCII del caracter "d" en $t6
sb $t6, 3($t5)  # Guardar el caracter en la direccion 3(24)
li $t6, 117  # Cargar ASCII del caracter "u" en $t6
sb $t6, 4($t5)  # Guardar el caracter en la direccion 4(24)
li $t6, 99  # Cargar ASCII del caracter "c" en $t6
sb $t6, 5($t5)  # Guardar el caracter en la direccion 5(24)
li $t6, 116  # Cargar ASCII del caracter "t" en $t6
sb $t6, 6($t5)  # Guardar el caracter en la direccion 6(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 7($t5)  # Guardar el caracter en la direccion 7(24)
li $t6, 32  # Cargar ASCII del caracter " " en $t6
sb $t6, 8($t5)  # Guardar el caracter en la direccion 8(24)
li $t6, 97  # Cargar ASCII del caracter "a" en $t6
sb $t6, 9($t5)  # Guardar el caracter en la direccion 9(24)
li $t6, 110  # Cargar ASCII del caracter "n" en $t6
sb $t6, 10($t5)  # Guardar el caracter en la direccion 10(24)
li $t6, 97  # Cargar ASCII del caracter "a" en $t6
sb $t6, 11($t5)  # Guardar el caracter en la direccion 11(24)
li $t6, 100  # Cargar ASCII del caracter "d" en $t6
sb $t6, 12($t5)  # Guardar el caracter en la direccion 12(24)
li $t6, 105  # Cargar ASCII del caracter "i" en $t6
sb $t6, 13($t5)  # Guardar el caracter en la direccion 13(24)
li $t6, 100  # Cargar ASCII del caracter "d" en $t6
sb $t6, 14($t5)  # Guardar el caracter en la direccion 14(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 15($t5)  # Guardar el caracter en la direccion 15(24)
li $t6, 32  # Cargar ASCII del caracter " " en $t6
sb $t6, 16($t5)  # Guardar el caracter en la direccion 16(24)
li $t6, 99  # Cargar ASCII del caracter "c" en $t6
sb $t6, 17($t5)  # Guardar el caracter en la direccion 17(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 18($t5)  # Guardar el caracter en la direccion 18(24)
li $t6, 110  # Cargar ASCII del caracter "n" en $t6
sb $t6, 19($t5)  # Guardar el caracter en la direccion 19(24)
li $t6, 32  # Cargar ASCII del caracter " " en $t6
sb $t6, 20($t5)  # Guardar el caracter en la direccion 20(24)
li $t6, 112  # Cargar ASCII del caracter "p" en $t6
sb $t6, 21($t5)  # Guardar el caracter en la direccion 21(24)
li $t6, 114  # Cargar ASCII del caracter "r" en $t6
sb $t6, 22($t5)  # Guardar el caracter en la direccion 22(24)
li $t6, 101  # Cargar ASCII del caracter "e" en $t6
sb $t6, 23($t5)  # Guardar el caracter en la direccion 23(24)
li $t6, 99  # Cargar ASCII del caracter "c" en $t6
sb $t6, 24($t5)  # Guardar el caracter en la direccion 24(24)
li $t6, 105  # Cargar ASCII del caracter "i" en $t6
sb $t6, 25($t5)  # Guardar el caracter en la direccion 25(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 26($t5)  # Guardar el caracter en la direccion 26(24)
li $t6, 58  # Cargar ASCII del caracter ":" en $t6
sb $t6, 27($t5)  # Guardar el caracter en la direccion 27(24)
li $t6, 0  # Terminador nulo
sb $t6, 28($t5) # Guardar terminador nulo
lw $t7, 24($fp) # Cargar la dirección en el stack de la variable "t3-a99c81b3-78f2-4017-9069-db3bb2bdf52f"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t7  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
lw $t2, 12($fp) # Cargar la dirección en el stack de la variable "precio"
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t2  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
lw $v0, 16($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 24     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_CajaRegistradora_calcularTotalConImpuesto_0:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -48   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t0, 4($t0) # Obtener el valor de la propiedad 4 de la variable "self" del heap
sw $t0, 12($fp) # guardar el valor de la variable 't4-7d213d68-d4d3-47b0-9d43-56f821f4e45a' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t1, 4($t1) # Obtener el valor de la propiedad 4 de la variable "self" del heap
sw $t1, 16($fp) # guardar el valor de la variable 't5-c2835380-147f-4098-85d0-0cce5a132169' en el stack
lw $t2, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t2, 0($t2) # Obtener el valor de la propiedad 0 de la variable "self" del heap
sw $t2, 20($fp) # guardar el valor de la variable 't6-76db9e0c-6f30-4b4c-9f49-604d262e0707' en el stack
lw $t3, 16($fp) # Obtener el valor de la variable "t5-c2835380-147f-4098-85d0-0cce5a132169" del stack
lw $t4, 20($fp) # Obtener el valor de la variable "t6-76db9e0c-6f30-4b4c-9f49-604d262e0707" del stack
mul $t5, $t3, $t4 # Multiplicar los valores de t5-c2835380-147f-4098-85d0-0cce5a132169 y t6-76db9e0c-6f30-4b4c-9f49-604d262e0707
sw $t5, 24($fp) # Almacenar el resultado de la multiplicacion en t7-52bfb415-b06c-40a3-a732-8ed7aa8719b0
li $t6, 100
sw $t6, 28($fp) # guardar el valor de la variable 't8-9df37fb0-b978-43ed-8e08-9f0171385196' en el stack
lw $t5, 24($fp) # Obtener el valor de la variable "t7-52bfb415-b06c-40a3-a732-8ed7aa8719b0" del stack
lw $t7, 28($fp) # Obtener el valor de la variable "t8-9df37fb0-b978-43ed-8e08-9f0171385196" del stack
div $t5, $t7 # Dividir los valores de t7-52bfb415-b06c-40a3-a732-8ed7aa8719b0 y t8-9df37fb0-b978-43ed-8e08-9f0171385196
mflo $t0 # Obtener el cociente de la division
sw $t0, 32($fp) # Almacenar el resultado de la division en t9-05191296-cd04-416f-8753-7b93c6d63f8f
lw $t1, 12($fp) # Obtener el valor de la variable "t4-7d213d68-d4d3-47b0-9d43-56f821f4e45a" del stack
lw $t0, 32($fp) # Obtener el valor de la variable "t9-05191296-cd04-416f-8753-7b93c6d63f8f" del stack
add $t2, $t1, $t0 # Sumar los valores de t4-7d213d68-d4d3-47b0-9d43-56f821f4e45a y t9-05191296-cd04-416f-8753-7b93c6d63f8f
sw $t2, 36($fp) # Almacenar el resultado de la suma en t10-1e210785-525f-41b9-aecd-a597a2f2062c
lw $t2, 36($fp) # Obtener el valor de la variable "t10-1e210785-525f-41b9-aecd-a597a2f2062c" del stack
sw $t2, 40($fp) # guardar el valor de la variable 'totalConImpuesto' en el stack
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t3, $fp, 44 # La direccion del stack de la variable 't11-3b521ca4-155c-4eb3-ba1d-2032970a4f70' se carga en $t3
sw $s1, 0($t3) # Almacenar la direccion de memoria de la cadena 't11-3b521ca4-155c-4eb3-ba1d-2032970a4f70' en el stack
lw $t3, 0($t3) # La direccion de memoria de la cadena 't11-3b521ca4-155c-4eb3-ba1d-2032970a4f70' se carga en $t3
li $t4, 69  # Cargar ASCII del caracter "E" en $t4
sb $t4, 0($t3)  # Guardar el caracter en la direccion 0(44)
li $t4, 108  # Cargar ASCII del caracter "l" en $t4
sb $t4, 1($t3)  # Guardar el caracter en la direccion 1(44)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 2($t3)  # Guardar el caracter en la direccion 2(44)
li $t4, 116  # Cargar ASCII del caracter "t" en $t4
sb $t4, 3($t3)  # Guardar el caracter en la direccion 3(44)
li $t4, 111  # Cargar ASCII del caracter "o" en $t4
sb $t4, 4($t3)  # Guardar el caracter en la direccion 4(44)
li $t4, 116  # Cargar ASCII del caracter "t" en $t4
sb $t4, 5($t3)  # Guardar el caracter en la direccion 5(44)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 6($t3)  # Guardar el caracter en la direccion 6(44)
li $t4, 108  # Cargar ASCII del caracter "l" en $t4
sb $t4, 7($t3)  # Guardar el caracter en la direccion 7(44)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 8($t3)  # Guardar el caracter en la direccion 8(44)
li $t4, 99  # Cargar ASCII del caracter "c" en $t4
sb $t4, 9($t3)  # Guardar el caracter en la direccion 9(44)
li $t4, 111  # Cargar ASCII del caracter "o" en $t4
sb $t4, 10($t3)  # Guardar el caracter en la direccion 10(44)
li $t4, 110  # Cargar ASCII del caracter "n" en $t4
sb $t4, 11($t3)  # Guardar el caracter en la direccion 11(44)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 12($t3)  # Guardar el caracter en la direccion 12(44)
li $t4, 105  # Cargar ASCII del caracter "i" en $t4
sb $t4, 13($t3)  # Guardar el caracter en la direccion 13(44)
li $t4, 109  # Cargar ASCII del caracter "m" en $t4
sb $t4, 14($t3)  # Guardar el caracter en la direccion 14(44)
li $t4, 112  # Cargar ASCII del caracter "p" en $t4
sb $t4, 15($t3)  # Guardar el caracter en la direccion 15(44)
li $t4, 117  # Cargar ASCII del caracter "u" en $t4
sb $t4, 16($t3)  # Guardar el caracter en la direccion 16(44)
li $t4, 101  # Cargar ASCII del caracter "e" en $t4
sb $t4, 17($t3)  # Guardar el caracter en la direccion 17(44)
li $t4, 115  # Cargar ASCII del caracter "s" en $t4
sb $t4, 18($t3)  # Guardar el caracter en la direccion 18(44)
li $t4, 116  # Cargar ASCII del caracter "t" en $t4
sb $t4, 19($t3)  # Guardar el caracter en la direccion 19(44)
li $t4, 111  # Cargar ASCII del caracter "o" en $t4
sb $t4, 20($t3)  # Guardar el caracter en la direccion 20(44)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 21($t3)  # Guardar el caracter en la direccion 21(44)
li $t4, 101  # Cargar ASCII del caracter "e" en $t4
sb $t4, 22($t3)  # Guardar el caracter en la direccion 22(44)
li $t4, 115  # Cargar ASCII del caracter "s" en $t4
sb $t4, 23($t3)  # Guardar el caracter en la direccion 23(44)
li $t4, 58  # Cargar ASCII del caracter ":" en $t4
sb $t4, 24($t3)  # Guardar el caracter en la direccion 24(44)
li $t4, 0  # Terminador nulo
sb $t4, 25($t3) # Guardar terminador nulo
lw $t5, 44($fp) # Cargar la dirección en el stack de la variable "t11-3b521ca4-155c-4eb3-ba1d-2032970a4f70"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t5  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
lw $t6, 40($fp) # Cargar la dirección en el stack de la variable "totalConImpuesto"
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t6  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
lw $t6, 40($fp) # Obtener el valor de la variable "totalConImpuesto" del stack
sw $t6, 48($fp) # guardar el valor de la variable 't12-9b5de01e-531b-4046-9563-9a05a331030b' en el stack
lw $v0, 48($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 48     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_CajaRegistradora_reiniciar_0:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -16   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
li $t0, 0
sw $t0, 12($fp) # guardar el valor de la variable 't13-d67dae76-82bf-414f-9ab9-cb377d9dcabb' en el stack
lw $t1, 12($fp) # Obtener el valor de la variable "t13-d67dae76-82bf-414f-9ab9-cb377d9dcabb" del stack
lw $t2, 8($fp) # La direccion del stack de la variable 'self' se carga en $t2
sw $t1, 4($t2) # Almacenar el valor de la variable 'self' en el heap
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t3, $fp, 16 # La direccion del stack de la variable 't14-f834b064-73b2-4c61-9403-b2533fa0ece8' se carga en $t3
sw $s1, 0($t3) # Almacenar la direccion de memoria de la cadena 't14-f834b064-73b2-4c61-9403-b2533fa0ece8' en el stack
lw $t3, 0($t3) # La direccion de memoria de la cadena 't14-f834b064-73b2-4c61-9403-b2533fa0ece8' se carga en $t3
li $t4, 76  # Cargar ASCII del caracter "L" en $t4
sb $t4, 0($t3)  # Guardar el caracter en la direccion 0(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 1($t3)  # Guardar el caracter en la direccion 1(16)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 2($t3)  # Guardar el caracter en la direccion 2(16)
li $t4, 99  # Cargar ASCII del caracter "c" en $t4
sb $t4, 3($t3)  # Guardar el caracter en la direccion 3(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 4($t3)  # Guardar el caracter en la direccion 4(16)
li $t4, 106  # Cargar ASCII del caracter "j" en $t4
sb $t4, 5($t3)  # Guardar el caracter en la direccion 5(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 6($t3)  # Guardar el caracter en la direccion 6(16)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 7($t3)  # Guardar el caracter en la direccion 7(16)
li $t4, 114  # Cargar ASCII del caracter "r" en $t4
sb $t4, 8($t3)  # Guardar el caracter en la direccion 8(16)
li $t4, 101  # Cargar ASCII del caracter "e" en $t4
sb $t4, 9($t3)  # Guardar el caracter en la direccion 9(16)
li $t4, 103  # Cargar ASCII del caracter "g" en $t4
sb $t4, 10($t3)  # Guardar el caracter en la direccion 10(16)
li $t4, 105  # Cargar ASCII del caracter "i" en $t4
sb $t4, 11($t3)  # Guardar el caracter en la direccion 11(16)
li $t4, 115  # Cargar ASCII del caracter "s" en $t4
sb $t4, 12($t3)  # Guardar el caracter en la direccion 12(16)
li $t4, 116  # Cargar ASCII del caracter "t" en $t4
sb $t4, 13($t3)  # Guardar el caracter en la direccion 13(16)
li $t4, 114  # Cargar ASCII del caracter "r" en $t4
sb $t4, 14($t3)  # Guardar el caracter en la direccion 14(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 15($t3)  # Guardar el caracter en la direccion 15(16)
li $t4, 100  # Cargar ASCII del caracter "d" en $t4
sb $t4, 16($t3)  # Guardar el caracter en la direccion 16(16)
li $t4, 111  # Cargar ASCII del caracter "o" en $t4
sb $t4, 17($t3)  # Guardar el caracter en la direccion 17(16)
li $t4, 114  # Cargar ASCII del caracter "r" en $t4
sb $t4, 18($t3)  # Guardar el caracter en la direccion 18(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 19($t3)  # Guardar el caracter en la direccion 19(16)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 20($t3)  # Guardar el caracter en la direccion 20(16)
li $t4, 115  # Cargar ASCII del caracter "s" en $t4
sb $t4, 21($t3)  # Guardar el caracter en la direccion 21(16)
li $t4, 101  # Cargar ASCII del caracter "e" en $t4
sb $t4, 22($t3)  # Guardar el caracter en la direccion 22(16)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 23($t3)  # Guardar el caracter en la direccion 23(16)
li $t4, 104  # Cargar ASCII del caracter "h" en $t4
sb $t4, 24($t3)  # Guardar el caracter en la direccion 24(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 25($t3)  # Guardar el caracter en la direccion 25(16)
li $t4, 32  # Cargar ASCII del caracter " " en $t4
sb $t4, 26($t3)  # Guardar el caracter en la direccion 26(16)
li $t4, 114  # Cargar ASCII del caracter "r" en $t4
sb $t4, 27($t3)  # Guardar el caracter en la direccion 27(16)
li $t4, 101  # Cargar ASCII del caracter "e" en $t4
sb $t4, 28($t3)  # Guardar el caracter en la direccion 28(16)
li $t4, 105  # Cargar ASCII del caracter "i" en $t4
sb $t4, 29($t3)  # Guardar el caracter en la direccion 29(16)
li $t4, 110  # Cargar ASCII del caracter "n" en $t4
sb $t4, 30($t3)  # Guardar el caracter en la direccion 30(16)
li $t4, 105  # Cargar ASCII del caracter "i" en $t4
sb $t4, 31($t3)  # Guardar el caracter en la direccion 31(16)
li $t4, 99  # Cargar ASCII del caracter "c" en $t4
sb $t4, 32($t3)  # Guardar el caracter en la direccion 32(16)
li $t4, 105  # Cargar ASCII del caracter "i" en $t4
sb $t4, 33($t3)  # Guardar el caracter en la direccion 33(16)
li $t4, 97  # Cargar ASCII del caracter "a" en $t4
sb $t4, 34($t3)  # Guardar el caracter en la direccion 34(16)
li $t4, 100  # Cargar ASCII del caracter "d" en $t4
sb $t4, 35($t3)  # Guardar el caracter en la direccion 35(16)
li $t4, 111  # Cargar ASCII del caracter "o" en $t4
sb $t4, 36($t3)  # Guardar el caracter en la direccion 36(16)
li $t4, 0  # Terminador nulo
sb $t4, 37($t3) # Guardar terminador nulo
lw $t5, 16($fp) # Cargar la dirección en el stack de la variable "t14-f834b064-73b2-4c61-9403-b2533fa0ece8"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t5  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
lw $v0, 12($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 16     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

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
