.data
newline: .asciiz "\n"
.text
.globl main
main:
li $a1, 0x10000010 # Cargar la direccion asignada para la variable 't25-d1b2b760-cf99-4fc0-8bcd-bbaec6e35317' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t1, 0x10000010 # La direccion del heap de la variable 't25-d1b2b760-cf99-4fc0-8bcd-bbaec6e35317' se carga en $t1
li $t0, 80  # Cargar ASCII del caracter "P" en $t0
sb $t0, 0($t1)  # Guardar el caracter en la direccion 0(0x10000010)
li $t0, 97  # Cargar ASCII del caracter "a" en $t0
sb $t0, 1($t1)  # Guardar el caracter en la direccion 1(0x10000010)
li $t0, 98  # Cargar ASCII del caracter "b" en $t0
sb $t0, 2($t1)  # Guardar el caracter en la direccion 2(0x10000010)
li $t0, 108  # Cargar ASCII del caracter "l" en $t0
sb $t0, 3($t1)  # Guardar el caracter en la direccion 3(0x10000010)
li $t0, 111  # Cargar ASCII del caracter "o" en $t0
sb $t0, 4($t1)  # Guardar el caracter en la direccion 4(0x10000010)
li $t0, 0  # Terminador nulo
sb $t0, 5($t1)  # Guardar terminador nulo
lw $t0, 0($t1) # El valor de la variable 't25-d1b2b760-cf99-4fc0-8bcd-bbaec6e35317' en el heap se carga en $t0
li $a1, 0x10000014 # Cargar la direccion asignada para la variable 'nombre' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000018 # Cargar la direccion asignada para la variable 't26-c1a9b04c-669b-419d-a550-9ed4059a1a04' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t2, 20
li $a1, 0x1000001c # Cargar la direccion asignada para la variable 't27-d4e03325-ed65-4de0-9440-3c092cb0443d' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t4, 0x1000001c # La direccion del heap de la variable 't27-d4e03325-ed65-4de0-9440-3c092cb0443d' se carga en $t4
li $t3, 51  # Cargar ASCII del caracter "3" en $t3
sb $t3, 0($t4)  # Guardar el caracter en la direccion 0(0x1000001c)
li $t3, 0  # Terminador nulo
sb $t3, 1($t4)  # Guardar terminador nulo
lw $t3, 0($t4) # El valor de la variable 't27-d4e03325-ed65-4de0-9440-3c092cb0443d' en el heap se carga en $t3
li $a1, 0x10000020 # Cargar la direccion asignada para la variable 't28-34ae3015-ff94-4860-8514-526e62adf7f2' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t5, 0x10000020 # La direccion del heap de la variable 't28-34ae3015-ff94-4860-8514-526e62adf7f2' se carga en $t5
move $a0, $t5 # Guardar el valor de la variable 't28-34ae3015-ff94-4860-8514-526e62adf7f2' en a0
move $a1, $t1 # Guardar el valor de la variable 'nombre' en a1
move $a2, $t2 # Guardar el valor de la variable 't26-c1a9b04c-669b-419d-a550-9ed4059a1a04' en a2
move $a3, $t4 # Guardar el valor de la variable 't27-d4e03325-ed65-4de0-9440-3c092cb0443d' en a3
jal L_Estudiante_init_3
lw $t0, 0x10000020 # La direccion del heap de la instancia 't28-34ae3015-ff94-4860-8514-526e62adf7f2' se carga en $t0
li $t1, 0x10000024 # La direccion de memoria estatica de la variable 'juan' se carga en $t1
sw $t0, 0($t1) # Almacenar la direccion de memoria de la instancia 't28-34ae3015-ff94-4860-8514-526e62adf7f2' en la variable 'juan'
move $a0, $t0 # Guardar el valor de la variable 'juan' en a0
jal L_Persona_saludar_0
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000028 # Cargar la direccion asignada para la variable 't29-7e03f30b-5b5f-4ce0-9408-1a9fc6392bbe' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x1000002c # Cargar la direccion asignada para la variable 't30-c9123bfa-749b-4c39-8324-c845042116e5' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t2, 0x1000002c # La direccion del heap de la variable 't30-c9123bfa-749b-4c39-8324-c845042116e5' se carga en $t2
li $t1, 77  # Cargar ASCII del caracter "M" en $t1
sb $t1, 0($t2)  # Guardar el caracter en la direccion 0(0x1000002c)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 1($t2)  # Guardar el caracter en la direccion 1(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 2($t2)  # Guardar el caracter en la direccion 2(0x1000002c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 3($t2)  # Guardar el caracter en la direccion 3(0x1000002c)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 4($t2)  # Guardar el caracter en la direccion 4(0x1000002c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 5($t2)  # Guardar el caracter en la direccion 5(0x1000002c)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 6($t2)  # Guardar el caracter en la direccion 6(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 7($t2)  # Guardar el caracter en la direccion 7(0x1000002c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 8($t2)  # Guardar el caracter en la direccion 8(0x1000002c)
li $t1, 99  # Cargar ASCII del caracter "c" en $t1
sb $t1, 9($t2)  # Guardar el caracter en la direccion 9(0x1000002c)
li $t1, 116  # Cargar ASCII del caracter "t" en $t1
sb $t1, 10($t2)  # Guardar el caracter en la direccion 10(0x1000002c)
li $t1, 117  # Cargar ASCII del caracter "u" en $t1
sb $t1, 11($t2)  # Guardar el caracter en la direccion 11(0x1000002c)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 12($t2)  # Guardar el caracter en la direccion 12(0x1000002c)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 13($t2)  # Guardar el caracter en la direccion 13(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 14($t2)  # Guardar el caracter en la direccion 14(0x1000002c)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 15($t2)  # Guardar el caracter en la direccion 15(0x1000002c)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 16($t2)  # Guardar el caracter en la direccion 16(0x1000002c)
li $t1, 58  # Cargar ASCII del caracter ":" en $t1
sb $t1, 17($t2)  # Guardar el caracter en la direccion 17(0x1000002c)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 18($t2)  # Guardar el caracter en la direccion 18(0x1000002c)
li $t1, 0  # Terminador nulo
sb $t1, 19($t2)  # Guardar terminador nulo
lw $t1, 0($t2) # El valor de la variable 't30-c9123bfa-749b-4c39-8324-c845042116e5' en el heap se carga en $t1
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t2  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
li $a1, 0x10000030 # Cargar la direccion asignada para la variable 't31-8851b76d-88f7-469d-923a-e713b167b370' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t3, 0x10000024 # La direccion del heap de la variable 'juan' se carga en $t3
lw $t4, 4($t3) # Cargar el valor de la propiedad de la instancia 'juan' en $t3
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t4  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
move $a0, $t3 # Guardar el valor de la variable 'juan' en a0
jal L_Estudiante_estudiar_0
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000034 # Cargar la direccion asignada para la variable 't32-7b217f15-fb18-49fe-bf76-cac65fe3a006' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x10000038 # Cargar la direccion asignada para la variable 't33-bf9feb39-985b-4458-9bdc-aca0f2576200' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t1, 5
lw $t2, 0x10000024 # La direccion del heap de la variable 'juan' se carga en $t2
move $a0, $t2 # Guardar el valor de la variable 'juan' en a0
move $a1, $t1 # Guardar el valor de la variable 't33-bf9feb39-985b-4458-9bdc-aca0f2576200' en a1
jal L_Persona_incrementarEdad_1
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x1000003c # Cargar la direccion asignada para la variable 't34-73ccf9c4-165c-4371-a70a-6c42d3e193a1' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x10000040 # Cargar la direccion asignada para la variable 't35-2b63a26b-5ae5-4f66-905f-9b41b056757e' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t1, 20
li $a1, 0x10000044 # Cargar la direccion asignada para la variable 't36-4b4878fb-8b5a-4cf6-8ec8-ba00cb9c31b9' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t2, 30
li $a1, 0x10000048 # Cargar la direccion asignada para la variable 't37-60e99630-a25b-4206-aabd-5462b0a2721c' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t3, 40
lw $t4, 0x10000024 # La direccion del heap de la variable 'juan' se carga en $t4
move $a0, $t4 # Guardar el valor de la variable 'juan' en a0
move $a1, $t1 # Guardar el valor de la variable 't35-2b63a26b-5ae5-4f66-905f-9b41b056757e' en a1
move $a2, $t2 # Guardar el valor de la variable 't36-4b4878fb-8b5a-4cf6-8ec8-ba00cb9c31b9' en a2
move $a3, $t3 # Guardar el valor de la variable 't37-60e99630-a25b-4206-aabd-5462b0a2721c' en a3
jal L_Estudiante_promedioNotas_3
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x1000004c # Cargar la direccion asignada para la variable 't38-9a57ce6d-91d0-4545-818c-9aad0a9b8e89' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x10000050 # Cargar la direccion asignada para la variable 't39-2ddcad4a-f029-4175-8620-1c0745c867f0' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t1, 0x10000024 # La direccion del heap de la variable 'juan' se carga en $t1
lw $t2, 4($t1) # Cargar el valor de la propiedad de la instancia 'juan' en $t1
li $a1, 0x10000054 # Cargar la direccion asignada para la variable 'edad' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000058 # Cargar la direccion asignada para la variable 't40-95f88225-fb80-49e8-8043-8464ed1f12a3' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t3, 2
mul $t4, $t2, $t3 # Multiplicar los valores de edad y t40-95f88225-fb80-49e8-8043-8464ed1f12a3
li $a1, 0x1000005c # Cargar la direccion asignada para la variable 't41-2914e0f0-84c6-4c02-a769-8f29214852fa' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000060 # Cargar la direccion asignada para la variable 't42-18bb5223-0589-4559-947c-2f51186daeae' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t5, 5
li $a1, 0x10000064 # Cargar la direccion asignada para la variable 't43-8a15fdfe-5a83-445d-86d5-ba6640af5817' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t6, 3
sub $t7, $t5, $t6 # Restar los valores de t42-18bb5223-0589-4559-947c-2f51186daeae y t43-8a15fdfe-5a83-445d-86d5-ba6640af5817
li $a1, 0x10000068 # Cargar la direccion asignada para la variable 't44-dee51538-1880-49f0-b374-4b939ec7c58b' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x1000006c # Cargar la direccion asignada para la variable 't45-e7969988-fc7f-4f02-a1b4-6befa7910158' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t3, 2
div $t7, $t3 # Dividir los valores de t44-dee51538-1880-49f0-b374-4b939ec7c58b y t45-e7969988-fc7f-4f02-a1b4-6befa7910158
mflo $t0 # Obtener el cociente de la división
li $a1, 0x10000070 # Cargar la direccion asignada para la variable 't46-2e12cfd6-9f1e-4c52-894e-322496b7ae19' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
add $t1, $t4, $t0 # Sumar los valores de t41-2914e0f0-84c6-4c02-a769-8f29214852fa y t46-2e12cfd6-9f1e-4c52-894e-322496b7ae19
li $a1, 0x10000074 # Cargar la direccion asignada para la variable 't47-22066a0d-abfe-42bf-a609-f9d8302b7dc0' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000078 # Cargar la direccion asignada para la variable 'resultado' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x1000007c # Cargar la direccion asignada para la variable 't48-53757b29-9ec5-48b7-9b3a-96fadc69107e' en memoria estatica
li $a2, 255 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t3, 0x1000007c # La direccion del heap de la variable 't48-53757b29-9ec5-48b7-9b3a-96fadc69107e' se carga en $t3
li $t2, 82  # Cargar ASCII del caracter "R" en $t2
sb $t2, 0($t3)  # Guardar el caracter en la direccion 0(0x1000007c)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 1($t3)  # Guardar el caracter en la direccion 1(0x1000007c)
li $t2, 115  # Cargar ASCII del caracter "s" en $t2
sb $t2, 2($t3)  # Guardar el caracter en la direccion 2(0x1000007c)
li $t2, 117  # Cargar ASCII del caracter "u" en $t2
sb $t2, 3($t3)  # Guardar el caracter en la direccion 3(0x1000007c)
li $t2, 108  # Cargar ASCII del caracter "l" en $t2
sb $t2, 4($t3)  # Guardar el caracter en la direccion 4(0x1000007c)
li $t2, 116  # Cargar ASCII del caracter "t" en $t2
sb $t2, 5($t3)  # Guardar el caracter en la direccion 5(0x1000007c)
li $t2, 97  # Cargar ASCII del caracter "a" en $t2
sb $t2, 6($t3)  # Guardar el caracter en la direccion 6(0x1000007c)
li $t2, 100  # Cargar ASCII del caracter "d" en $t2
sb $t2, 7($t3)  # Guardar el caracter en la direccion 7(0x1000007c)
li $t2, 111  # Cargar ASCII del caracter "o" en $t2
sb $t2, 8($t3)  # Guardar el caracter en la direccion 8(0x1000007c)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 9($t3)  # Guardar el caracter en la direccion 9(0x1000007c)
li $t2, 100  # Cargar ASCII del caracter "d" en $t2
sb $t2, 10($t3)  # Guardar el caracter en la direccion 10(0x1000007c)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 11($t3)  # Guardar el caracter en la direccion 11(0x1000007c)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 12($t3)  # Guardar el caracter en la direccion 12(0x1000007c)
li $t2, 108  # Cargar ASCII del caracter "l" en $t2
sb $t2, 13($t3)  # Guardar el caracter en la direccion 13(0x1000007c)
li $t2, 97  # Cargar ASCII del caracter "a" en $t2
sb $t2, 14($t3)  # Guardar el caracter en la direccion 14(0x1000007c)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 15($t3)  # Guardar el caracter en la direccion 15(0x1000007c)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 16($t3)  # Guardar el caracter en la direccion 16(0x1000007c)
li $t2, 120  # Cargar ASCII del caracter "x" en $t2
sb $t2, 17($t3)  # Guardar el caracter en la direccion 17(0x1000007c)
li $t2, 112  # Cargar ASCII del caracter "p" en $t2
sb $t2, 18($t3)  # Guardar el caracter en la direccion 18(0x1000007c)
li $t2, 114  # Cargar ASCII del caracter "r" en $t2
sb $t2, 19($t3)  # Guardar el caracter en la direccion 19(0x1000007c)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 20($t3)  # Guardar el caracter en la direccion 20(0x1000007c)
li $t2, 115  # Cargar ASCII del caracter "s" en $t2
sb $t2, 21($t3)  # Guardar el caracter en la direccion 21(0x1000007c)
li $t2, 105  # Cargar ASCII del caracter "i" en $t2
sb $t2, 22($t3)  # Guardar el caracter en la direccion 22(0x1000007c)
li $t2, 111  # Cargar ASCII del caracter "o" en $t2
sb $t2, 23($t3)  # Guardar el caracter en la direccion 23(0x1000007c)
li $t2, 110  # Cargar ASCII del caracter "n" en $t2
sb $t2, 24($t3)  # Guardar el caracter en la direccion 24(0x1000007c)
li $t2, 58  # Cargar ASCII del caracter ":" en $t2
sb $t2, 25($t3)  # Guardar el caracter en la direccion 25(0x1000007c)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 26($t3)  # Guardar el caracter en la direccion 26(0x1000007c)
li $t2, 0  # Terminador nulo
sb $t2, 27($t3)  # Guardar terminador nulo
lw $t2, 0($t3) # El valor de la variable 't48-53757b29-9ec5-48b7-9b3a-96fadc69107e' en el heap se carga en $t2
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t3  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t1  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
li $v0, 10
syscall

L_Persona_init_2:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -20   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'nombre' en el stack
sw $a2, 16($fp) # Guardar el valor de la variable 'edad' en el stack
lw $t0, 12($fp) # Obtener el valor de la variable "nombre" del stack
lw $t1, 8($fp) # La direccion del stack de la variable 'self' se carga en $t1
sw $t0, 0($t1) # Almacenar el valor de la variable 'self' en el heap
lw $t2, 16($fp) # Obtener el valor de la variable "edad" del stack
lw $t3, 8($fp) # La direccion del stack de la variable 'self' se carga en $t3
sw $t2, 4($t3) # Almacenar el valor de la variable 'self' en el heap
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t4, $fp, 20 # La direccion del stack de la variable 't0-3c72176e-6c80-4d1c-bfa3-2b4cc5788706' se carga en $t4
sw $s1, 0($t4) # Almacenar la direccion de memoria de la cadena 't0-3c72176e-6c80-4d1c-bfa3-2b4cc5788706' en el stack
lw $t4, 0($t4) # La direccion de memoria de la cadena 't0-3c72176e-6c80-4d1c-bfa3-2b4cc5788706' se carga en $t4
li $t5, 114  # Cargar ASCII del caracter "r" en $t5
sb $t5, 0($t4)  # Guardar el caracter en la direccion 0(20)
li $t5, 111  # Cargar ASCII del caracter "o" en $t5
sb $t5, 1($t4)  # Guardar el caracter en la direccion 1(20)
li $t5, 106  # Cargar ASCII del caracter "j" en $t5
sb $t5, 2($t4)  # Guardar el caracter en la direccion 2(20)
li $t5, 111  # Cargar ASCII del caracter "o" en $t5
sb $t5, 3($t4)  # Guardar el caracter en la direccion 3(20)
li $t5, 0  # Terminador nulo
sb $t5, 4($t4) # Guardar terminador nulo
lw $t6, 20($fp) # Obtener el valor de la variable "t0-3c72176e-6c80-4d1c-bfa3-2b4cc5788706" del stack
lw $t7, 8($fp) # La direccion del stack de la variable 'self' se carga en $t7
sw $t6, 8($t7) # Almacenar el valor de la variable 'self' en el heap
addi $sp, $sp, 20     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_Persona_saludar_0:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -20   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t0, $fp, 12 # La direccion del stack de la variable 't1-2059211d-4763-4d74-bd57-e68e1a4973cc' se carga en $t0
sw $s1, 0($t0) # Almacenar la direccion de memoria de la cadena 't1-2059211d-4763-4d74-bd57-e68e1a4973cc' en el stack
lw $t0, 0($t0) # La direccion de memoria de la cadena 't1-2059211d-4763-4d74-bd57-e68e1a4973cc' se carga en $t0
li $t1, 72  # Cargar ASCII del caracter "H" en $t1
sb $t1, 0($t0)  # Guardar el caracter en la direccion 0(12)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 1($t0)  # Guardar el caracter en la direccion 1(12)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 2($t0)  # Guardar el caracter en la direccion 2(12)
li $t1, 97  # Cargar ASCII del caracter "a" en $t1
sb $t1, 3($t0)  # Guardar el caracter en la direccion 3(12)
li $t1, 44  # Cargar ASCII del caracter "," en $t1
sb $t1, 4($t0)  # Guardar el caracter en la direccion 4(12)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 5($t0)  # Guardar el caracter en la direccion 5(12)
li $t1, 109  # Cargar ASCII del caracter "m" en $t1
sb $t1, 6($t0)  # Guardar el caracter en la direccion 6(12)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 7($t0)  # Guardar el caracter en la direccion 7(12)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 8($t0)  # Guardar el caracter en la direccion 8(12)
li $t1, 110  # Cargar ASCII del caracter "n" en $t1
sb $t1, 9($t0)  # Guardar el caracter en la direccion 9(12)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 10($t0)  # Guardar el caracter en la direccion 10(12)
li $t1, 109  # Cargar ASCII del caracter "m" en $t1
sb $t1, 11($t0)  # Guardar el caracter en la direccion 11(12)
li $t1, 98  # Cargar ASCII del caracter "b" en $t1
sb $t1, 12($t0)  # Guardar el caracter en la direccion 12(12)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 13($t0)  # Guardar el caracter en la direccion 13(12)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 14($t0)  # Guardar el caracter en la direccion 14(12)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 15($t0)  # Guardar el caracter en la direccion 15(12)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 16($t0)  # Guardar el caracter en la direccion 16(12)
li $t1, 115  # Cargar ASCII del caracter "s" en $t1
sb $t1, 17($t0)  # Guardar el caracter en la direccion 17(12)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 18($t0)  # Guardar el caracter en la direccion 18(12)
li $t1, 0  # Terminador nulo
sb $t1, 19($t0) # Guardar terminador nulo
lw $t2, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t2, 0($t2) # Obtener el valor de la propiedad 0 de la variable "self" del heap
sw $t2, 16($fp) # guardar el valor de la variable 't2-1cedcf8b-ee63-4817-b618-62a2d2edd8b9' en el stack
lw $t3, 12($fp) # La direccion del heap de la variable 't1-2059211d-4763-4d74-bd57-e68e1a4973cc' se carga en $t3
lw $t4, 16($fp) # La direccion del heap de la variable 't2-1cedcf8b-ee63-4817-b618-62a2d2edd8b9' se carga en $t4
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t5, $fp, 20 # La direccion del stack de la variable 't3-ce4365ae-d3cb-4dc5-9239-cfd889ea2a6c' se carga en $t5
sw $s1, 0($t5) # Almacenar la direccion de memoria de la cadena 't3-ce4365ae-d3cb-4dc5-9239-cfd889ea2a6c' en el stack
lw $t5, 0($t5) # La direccion de memoria de la cadena 't3-ce4365ae-d3cb-4dc5-9239-cfd889ea2a6c' se carga en $t5
move $s0, $t3 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t4 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
lw $t6, 20($fp) # Cargar la dirección en el stack de la variable "t3-ce4365ae-d3cb-4dc5-9239-cfd889ea2a6c"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t6  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $v0, 16($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 20     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_Persona_incrementarEdad_1:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -28   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'anos' en el stack
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t0, 4($t0) # Obtener el valor de la propiedad 4 de la variable "self" del heap
sw $t0, 16($fp) # guardar el valor de la variable 't4-b4e31c2f-5361-4139-876f-2cbac597d8d4' en el stack
lw $t1, 16($fp) # Obtener el valor de la variable "t4-b4e31c2f-5361-4139-876f-2cbac597d8d4" del stack
lw $t2, 12($fp) # Obtener el valor de la variable "anos" del stack
add $t3, $t1, $t2 # Sumar los valores de t4-b4e31c2f-5361-4139-876f-2cbac597d8d4 y anos
sw $t3, 20($fp) # Almacenar el resultado de la suma en t5-a78fc5ec-5ead-4fdd-9fe6-6b275b4f5056
lw $t3, 20($fp) # Obtener el valor de la variable "t5-a78fc5ec-5ead-4fdd-9fe6-6b275b4f5056" del stack
lw $t4, 8($fp) # La direccion del stack de la variable 'self' se carga en $t4
sw $t3, 4($t4) # Almacenar el valor de la variable 'self' en el heap
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t5, $fp, 24 # La direccion del stack de la variable 't6-08f93921-965d-438d-bc5d-418dbc7d0072' se carga en $t5
sw $s1, 0($t5) # Almacenar la direccion de memoria de la cadena 't6-08f93921-965d-438d-bc5d-418dbc7d0072' en el stack
lw $t5, 0($t5) # La direccion de memoria de la cadena 't6-08f93921-965d-438d-bc5d-418dbc7d0072' se carga en $t5
li $t6, 65  # Cargar ASCII del caracter "A" en $t6
sb $t6, 0($t5)  # Guardar el caracter en la direccion 0(24)
li $t6, 104  # Cargar ASCII del caracter "h" en $t6
sb $t6, 1($t5)  # Guardar el caracter en la direccion 1(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 2($t5)  # Guardar el caracter en la direccion 2(24)
li $t6, 114  # Cargar ASCII del caracter "r" en $t6
sb $t6, 3($t5)  # Guardar el caracter en la direccion 3(24)
li $t6, 97  # Cargar ASCII del caracter "a" en $t6
sb $t6, 4($t5)  # Guardar el caracter en la direccion 4(24)
li $t6, 32  # Cargar ASCII del caracter " " en $t6
sb $t6, 5($t5)  # Guardar el caracter en la direccion 5(24)
li $t6, 116  # Cargar ASCII del caracter "t" en $t6
sb $t6, 6($t5)  # Guardar el caracter en la direccion 6(24)
li $t6, 101  # Cargar ASCII del caracter "e" en $t6
sb $t6, 7($t5)  # Guardar el caracter en la direccion 7(24)
li $t6, 110  # Cargar ASCII del caracter "n" en $t6
sb $t6, 8($t5)  # Guardar el caracter en la direccion 8(24)
li $t6, 103  # Cargar ASCII del caracter "g" en $t6
sb $t6, 9($t5)  # Guardar el caracter en la direccion 9(24)
li $t6, 111  # Cargar ASCII del caracter "o" en $t6
sb $t6, 10($t5)  # Guardar el caracter en la direccion 10(24)
li $t6, 32  # Cargar ASCII del caracter " " en $t6
sb $t6, 11($t5)  # Guardar el caracter en la direccion 11(24)
li $t6, 58  # Cargar ASCII del caracter ":" en $t6
sb $t6, 12($t5)  # Guardar el caracter en la direccion 12(24)
li $t6, 0  # Terminador nulo
sb $t6, 13($t5) # Guardar terminador nulo
lw $t7, 24($fp) # Cargar la dirección en el stack de la variable "t6-08f93921-965d-438d-bc5d-418dbc7d0072"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t7  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t0, 4($t0) # Obtener el valor de la propiedad 4 de la variable "self" del heap
sw $t0, 28($fp) # guardar el valor de la variable 't7-70ede31e-3008-4f30-ae12-0672e55be864' en el stack
lw $t1, 28($fp) # Cargar la dirección en el stack de la variable "t7-70ede31e-3008-4f30-ae12-0672e55be864"
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t1  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $v0, 28($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 28     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_Estudiante_init_3:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -24   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'nombre' en el stack
sw $a2, 16($fp) # Guardar el valor de la variable 'edad' en el stack
sw $a3, 20($fp) # Guardar el valor de la variable 'grado' en el stack
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
move $a0, $t0 # Guardar el valor de la variable 'self' en a0
lw $t1, 12($fp) # Obtener el valor de la variable "nombre" del stack
move $a1, $t1 # Guardar el valor de la variable 'nombre' en a1
lw $t2, 16($fp) # Obtener el valor de la variable "edad" del stack
move $a2, $t2 # Guardar el valor de la variable 'edad' en a2
jal L_Persona_init_2
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 24($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t1, 20($fp) # Obtener el valor de la variable "grado" del stack
lw $t2, 8($fp) # La direccion del stack de la variable 'self' se carga en $t2
sw $t1, 12($t2) # Almacenar el valor de la variable 'self' en el heap
lw $v0, 28($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 24     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_Estudiante_estudiar_0:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -36   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
lw $t0, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t0, 0($t0) # Obtener el valor de la propiedad 0 de la variable "self" del heap
sw $t0, 12($fp) # guardar el valor de la variable 't9-1537391b-ca19-499d-ad60-6ab525735334' en el stack
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t1, $fp, 16 # La direccion del stack de la variable 't10-aac45f5f-350f-42c5-881f-273bcfb65251' se carga en $t1
sw $s1, 0($t1) # Almacenar la direccion de memoria de la cadena 't10-aac45f5f-350f-42c5-881f-273bcfb65251' en el stack
lw $t1, 0($t1) # La direccion de memoria de la cadena 't10-aac45f5f-350f-42c5-881f-273bcfb65251' se carga en $t1
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 0($t1)  # Guardar el caracter en la direccion 0(16)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 1($t1)  # Guardar el caracter en la direccion 1(16)
li $t2, 115  # Cargar ASCII del caracter "s" en $t2
sb $t2, 2($t1)  # Guardar el caracter en la direccion 2(16)
li $t2, 116  # Cargar ASCII del caracter "t" en $t2
sb $t2, 3($t1)  # Guardar el caracter en la direccion 3(16)
li $t2, 97  # Cargar ASCII del caracter "a" en $t2
sb $t2, 4($t1)  # Guardar el caracter en la direccion 4(16)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 5($t1)  # Guardar el caracter en la direccion 5(16)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 6($t1)  # Guardar el caracter en la direccion 6(16)
li $t2, 115  # Cargar ASCII del caracter "s" en $t2
sb $t2, 7($t1)  # Guardar el caracter en la direccion 7(16)
li $t2, 116  # Cargar ASCII del caracter "t" en $t2
sb $t2, 8($t1)  # Guardar el caracter en la direccion 8(16)
li $t2, 117  # Cargar ASCII del caracter "u" en $t2
sb $t2, 9($t1)  # Guardar el caracter en la direccion 9(16)
li $t2, 100  # Cargar ASCII del caracter "d" en $t2
sb $t2, 10($t1)  # Guardar el caracter en la direccion 10(16)
li $t2, 105  # Cargar ASCII del caracter "i" en $t2
sb $t2, 11($t1)  # Guardar el caracter en la direccion 11(16)
li $t2, 97  # Cargar ASCII del caracter "a" en $t2
sb $t2, 12($t1)  # Guardar el caracter en la direccion 12(16)
li $t2, 110  # Cargar ASCII del caracter "n" en $t2
sb $t2, 13($t1)  # Guardar el caracter en la direccion 13(16)
li $t2, 100  # Cargar ASCII del caracter "d" en $t2
sb $t2, 14($t1)  # Guardar el caracter en la direccion 14(16)
li $t2, 111  # Cargar ASCII del caracter "o" en $t2
sb $t2, 15($t1)  # Guardar el caracter en la direccion 15(16)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 16($t1)  # Guardar el caracter en la direccion 16(16)
li $t2, 101  # Cargar ASCII del caracter "e" en $t2
sb $t2, 17($t1)  # Guardar el caracter en la direccion 17(16)
li $t2, 110  # Cargar ASCII del caracter "n" en $t2
sb $t2, 18($t1)  # Guardar el caracter en la direccion 18(16)
li $t2, 32  # Cargar ASCII del caracter " " en $t2
sb $t2, 19($t1)  # Guardar el caracter en la direccion 19(16)
li $t2, 0  # Terminador nulo
sb $t2, 20($t1) # Guardar terminador nulo
lw $t3, 12($fp) # La direccion del heap de la variable 't9-1537391b-ca19-499d-ad60-6ab525735334' se carga en $t3
lw $t4, 16($fp) # La direccion del heap de la variable 't10-aac45f5f-350f-42c5-881f-273bcfb65251' se carga en $t4
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t5, $fp, 20 # La direccion del stack de la variable 't11-2bedd911-749d-493e-8635-28e63796fcca' se carga en $t5
sw $s1, 0($t5) # Almacenar la direccion de memoria de la cadena 't11-2bedd911-749d-493e-8635-28e63796fcca' en el stack
lw $t5, 0($t5) # La direccion de memoria de la cadena 't11-2bedd911-749d-493e-8635-28e63796fcca' se carga en $t5
move $s0, $t3 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t4 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
lw $t6, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t6, 12($t6) # Obtener el valor de la propiedad 12 de la variable "self" del heap
sw $t6, 24($fp) # guardar el valor de la variable 't12-dd4ee8c4-db11-4f02-9224-ca5148dec4a3' en el stack
lw $t7, 20($fp) # La direccion del heap de la variable 't11-2bedd911-749d-493e-8635-28e63796fcca' se carga en $t7
lw $t0, 24($fp) # La direccion del heap de la variable 't12-dd4ee8c4-db11-4f02-9224-ca5148dec4a3' se carga en $t0
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t1, $fp, 28 # La direccion del stack de la variable 't13-71cdf36e-83db-4d4f-86e2-8e7448670588' se carga en $t1
sw $s1, 0($t1) # Almacenar la direccion de memoria de la cadena 't13-71cdf36e-83db-4d4f-86e2-8e7448670588' en el stack
lw $t1, 0($t1) # La direccion de memoria de la cadena 't13-71cdf36e-83db-4d4f-86e2-8e7448670588' se carga en $t1
move $s0, $t7 # Direccion de la cadena a copiar
move $s3, $t1 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t0 # Direccion de la cadena a copiar
move $s3, $t1 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t2, $fp, 32 # La direccion del stack de la variable 't14-770c4d8e-2229-43f1-b57c-4c2118e56ab6' se carga en $t2
sw $s1, 0($t2) # Almacenar la direccion de memoria de la cadena 't14-770c4d8e-2229-43f1-b57c-4c2118e56ab6' en el stack
lw $t2, 0($t2) # La direccion de memoria de la cadena 't14-770c4d8e-2229-43f1-b57c-4c2118e56ab6' se carga en $t2
li $t3, 32  # Cargar ASCII del caracter " " en $t3
sb $t3, 0($t2)  # Guardar el caracter en la direccion 0(32)
li $t3, 103  # Cargar ASCII del caracter "g" en $t3
sb $t3, 1($t2)  # Guardar el caracter en la direccion 1(32)
li $t3, 114  # Cargar ASCII del caracter "r" en $t3
sb $t3, 2($t2)  # Guardar el caracter en la direccion 2(32)
li $t3, 97  # Cargar ASCII del caracter "a" en $t3
sb $t3, 3($t2)  # Guardar el caracter en la direccion 3(32)
li $t3, 100  # Cargar ASCII del caracter "d" en $t3
sb $t3, 4($t2)  # Guardar el caracter en la direccion 4(32)
li $t3, 111  # Cargar ASCII del caracter "o" en $t3
sb $t3, 5($t2)  # Guardar el caracter en la direccion 5(32)
li $t3, 0  # Terminador nulo
sb $t3, 6($t2) # Guardar terminador nulo
lw $t4, 28($fp) # La direccion del heap de la variable 't13-71cdf36e-83db-4d4f-86e2-8e7448670588' se carga en $t4
lw $t5, 32($fp) # La direccion del heap de la variable 't14-770c4d8e-2229-43f1-b57c-4c2118e56ab6' se carga en $t5
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t6, $fp, 36 # La direccion del stack de la variable 't15-653bfa13-b1ae-4f4f-a4ee-7b69c71155f6' se carga en $t6
sw $s1, 0($t6) # Almacenar la direccion de memoria de la cadena 't15-653bfa13-b1ae-4f4f-a4ee-7b69c71155f6' en el stack
lw $t6, 0($t6) # La direccion de memoria de la cadena 't15-653bfa13-b1ae-4f4f-a4ee-7b69c71155f6' se carga en $t6
move $s0, $t4 # Direccion de la cadena a copiar
move $s3, $t6 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t5 # Direccion de la cadena a copiar
move $s3, $t6 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
lw $t0, 36($fp) # Cargar la dirección en el stack de la variable "t15-653bfa13-b1ae-4f4f-a4ee-7b69c71155f6"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t0  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $v0, 24($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 36     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador

L_Estudiante_promedioNotas_3:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -60   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'self' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'nota1' en el stack
sw $a2, 16($fp) # Guardar el valor de la variable 'nota2' en el stack
sw $a3, 20($fp) # Guardar el valor de la variable 'nota3' en el stack
lw $t0, 12($fp) # Obtener el valor de la variable "nota1" del stack
lw $t1, 16($fp) # Obtener el valor de la variable "nota2" del stack
add $t2, $t0, $t1 # Sumar los valores de nota1 y nota2
sw $t2, 24($fp) # Almacenar el resultado de la suma en t16-4f91cf82-36ce-4a34-a245-c5fae9e55ecf
lw $t2, 24($fp) # Obtener el valor de la variable "t16-4f91cf82-36ce-4a34-a245-c5fae9e55ecf" del stack
lw $t3, 20($fp) # Obtener el valor de la variable "nota3" del stack
add $t4, $t2, $t3 # Sumar los valores de t16-4f91cf82-36ce-4a34-a245-c5fae9e55ecf y nota3
sw $t4, 28($fp) # Almacenar el resultado de la suma en t17-ff80b68a-2254-4094-a55c-760c4a6bd7bd
li $t5, 3
sw $t5, 32($fp) # guardar el valor de la variable 't18-590e16bd-ae15-4a71-a742-98efd7c12a37' en el stack
lw $t4, 28($fp) # Obtener el valor de la variable "t17-ff80b68a-2254-4094-a55c-760c4a6bd7bd" del stack
lw $t6, 32($fp) # Obtener el valor de la variable "t18-590e16bd-ae15-4a71-a742-98efd7c12a37" del stack
div $t4, $t6 # Dividir los valores de t17-ff80b68a-2254-4094-a55c-760c4a6bd7bd y t18-590e16bd-ae15-4a71-a742-98efd7c12a37
mflo $t7 # Obtener el cociente de la división
sw $t7, 36($fp) # Almacenar el resultado de la multiplicación en t19-e4103fe6-f2b1-4715-b71c-22058fca286e
lw $t7, 36($fp) # Obtener el valor de la variable "t19-e4103fe6-f2b1-4715-b71c-22058fca286e" del stack
sw $t7, 40($fp) # guardar el valor de la variable 'promedio' en el stack
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t0, $fp, 44 # La direccion del stack de la variable 't20-ceff61f3-a679-4f63-b886-9ed0bb265d1a' se carga en $t0
sw $s1, 0($t0) # Almacenar la direccion de memoria de la cadena 't20-ceff61f3-a679-4f63-b886-9ed0bb265d1a' en el stack
lw $t0, 0($t0) # La direccion de memoria de la cadena 't20-ceff61f3-a679-4f63-b886-9ed0bb265d1a' se carga en $t0
li $t1, 69  # Cargar ASCII del caracter "E" en $t1
sb $t1, 0($t0)  # Guardar el caracter en la direccion 0(44)
li $t1, 108  # Cargar ASCII del caracter "l" en $t1
sb $t1, 1($t0)  # Guardar el caracter en la direccion 1(44)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 2($t0)  # Guardar el caracter en la direccion 2(44)
li $t1, 112  # Cargar ASCII del caracter "p" en $t1
sb $t1, 3($t0)  # Guardar el caracter en la direccion 3(44)
li $t1, 114  # Cargar ASCII del caracter "r" en $t1
sb $t1, 4($t0)  # Guardar el caracter en la direccion 4(44)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 5($t0)  # Guardar el caracter en la direccion 5(44)
li $t1, 109  # Cargar ASCII del caracter "m" en $t1
sb $t1, 6($t0)  # Guardar el caracter en la direccion 6(44)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 7($t0)  # Guardar el caracter en la direccion 7(44)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 8($t0)  # Guardar el caracter en la direccion 8(44)
li $t1, 105  # Cargar ASCII del caracter "i" en $t1
sb $t1, 9($t0)  # Guardar el caracter en la direccion 9(44)
li $t1, 111  # Cargar ASCII del caracter "o" en $t1
sb $t1, 10($t0)  # Guardar el caracter en la direccion 10(44)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 11($t0)  # Guardar el caracter en la direccion 11(44)
li $t1, 100  # Cargar ASCII del caracter "d" en $t1
sb $t1, 12($t0)  # Guardar el caracter en la direccion 12(44)
li $t1, 101  # Cargar ASCII del caracter "e" en $t1
sb $t1, 13($t0)  # Guardar el caracter en la direccion 13(44)
li $t1, 32  # Cargar ASCII del caracter " " en $t1
sb $t1, 14($t0)  # Guardar el caracter en la direccion 14(44)
li $t1, 0  # Terminador nulo
sb $t1, 15($t0) # Guardar terminador nulo
lw $t2, 8($fp) # Obtener el valor de la variable "self" del stack
lw $t2, 0($t2) # Obtener el valor de la propiedad 0 de la variable "self" del heap
sw $t2, 48($fp) # guardar el valor de la variable 't21-5638ea57-3700-42c9-bf97-e1c629955280' en el stack
lw $t3, 44($fp) # La direccion del heap de la variable 't20-ceff61f3-a679-4f63-b886-9ed0bb265d1a' se carga en $t3
lw $t4, 48($fp) # La direccion del heap de la variable 't21-5638ea57-3700-42c9-bf97-e1c629955280' se carga en $t4
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t5, $fp, 52 # La direccion del stack de la variable 't22-dc6ab805-b833-4646-ae27-69f70054a0c8' se carga en $t5
sw $s1, 0($t5) # Almacenar la direccion de memoria de la cadena 't22-dc6ab805-b833-4646-ae27-69f70054a0c8' en el stack
lw $t5, 0($t5) # La direccion de memoria de la cadena 't22-dc6ab805-b833-4646-ae27-69f70054a0c8' se carga en $t5
move $s0, $t3 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t4 # Direccion de la cadena a copiar
move $s3, $t5 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t6, $fp, 56 # La direccion del stack de la variable 't23-8d6547e3-de42-4d02-8b45-a8fc611642be' se carga en $t6
sw $s1, 0($t6) # Almacenar la direccion de memoria de la cadena 't23-8d6547e3-de42-4d02-8b45-a8fc611642be' en el stack
lw $t6, 0($t6) # La direccion de memoria de la cadena 't23-8d6547e3-de42-4d02-8b45-a8fc611642be' se carga en $t6
li $t7, 32  # Cargar ASCII del caracter " " en $t7
sb $t7, 0($t6)  # Guardar el caracter en la direccion 0(56)
li $t7, 101  # Cargar ASCII del caracter "e" en $t7
sb $t7, 1($t6)  # Guardar el caracter en la direccion 1(56)
li $t7, 115  # Cargar ASCII del caracter "s" en $t7
sb $t7, 2($t6)  # Guardar el caracter en la direccion 2(56)
li $t7, 58  # Cargar ASCII del caracter ":" en $t7
sb $t7, 3($t6)  # Guardar el caracter en la direccion 3(56)
li $t7, 32  # Cargar ASCII del caracter " " en $t7
sb $t7, 4($t6)  # Guardar el caracter en la direccion 4(56)
li $t7, 0  # Terminador nulo
sb $t7, 5($t6) # Guardar terminador nulo
lw $t0, 52($fp) # La direccion del heap de la variable 't22-dc6ab805-b833-4646-ae27-69f70054a0c8' se carga en $t0
lw $t1, 56($fp) # La direccion del heap de la variable 't23-8d6547e3-de42-4d02-8b45-a8fc611642be' se carga en $t1
li $s0, 255 # Tamano de la cadena a copiar
jal alloc_memory # Reservar espacio en el heap para la cadena
addi $t2, $fp, 60 # La direccion del stack de la variable 't24-21fadd49-f43a-436b-8944-ca5d81babf44' se carga en $t2
sw $s1, 0($t2) # Almacenar la direccion de memoria de la cadena 't24-21fadd49-f43a-436b-8944-ca5d81babf44' en el stack
lw $t2, 0($t2) # La direccion de memoria de la cadena 't24-21fadd49-f43a-436b-8944-ca5d81babf44' se carga en $t2
move $s0, $t0 # Direccion de la cadena a copiar
move $s3, $t2 # Direccion de la cadena destino
li $s1, 0 # Offset inicial para la copia
jal copy_string # Concatenar cadenas
move $s0, $t1 # Direccion de la cadena a copiar
move $s3, $t2 # Direccion de la cadena destino
jal copy_string # Concatenar cadenas
lw $t3, 60($fp) # Cargar la dirección en el stack de la variable "t24-21fadd49-f43a-436b-8944-ca5d81babf44"
li $v0, 4       # Codigo de syscall para imprimir cadenas
move $a0, $t3  # Mover el valor de la cadena al registro $a0
syscall         # Imprimir la cadena
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $t4, 40($fp) # Cargar la dirección en el stack de la variable "promedio"
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t4  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la dirección de la cadena '\n'
li $v0, 4       # Código de syscall para imprimir cadenas
syscall         # Imprimir salto de línea
lw $v0, 48($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 60     # Limpiar espacio de variables locales
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
add $s4, $s3, $s1 # Calcular la dirección efectiva
sb $s2, 0($s4)    # Escribir el caracter en la cadena destino
addi $s0, $s0, 1  # Avanzar en la cadena fuente
addi $s1, $s1, 1  # Avanzar en la cadena destino
j copy_loop               # Continuar con el siguiente caracter
end_copy:
jr $ra
