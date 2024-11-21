.data
newline: .asciiz "\n"
.text
.globl main
main:
li $a1, 0x10000000 # Cargar la direccion asignada para la variable 't27-8ce8aca3-da5d-455a-b519-c46aba9e3513' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t0, 2
li $a1, 0x10000004 # Cargar la direccion asignada para la variable 'm' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000008 # Cargar la direccion asignada para la variable 't28-baab294b-4ac3-4cac-934a-536d3d7dd0f5' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $t1, 3
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 'n' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $a0, $t0 # Guardar el valor de la variable 'm' en a0
move $a1, $t1 # Guardar el valor de la variable 'n' en a1
jal L_ackermann_2
move $t0, $v0  # Leer el valor de retorno desde la ultima posicion
li $a1, 0x10000010 # Cargar la direccion asignada para la variable 't29-d463cc2c-0ed9-4c08-acde-838991ede39c' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
move $fp, $sp # Liberar espacio de variables locales y $ra
li $a1, 0x10000014 # Cargar la direccion asignada para la variable 'result' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $v0, 1       # Codigo de syscall para imprimir enteros
move $a0, $t0  # Mover el valor del entero al registro $a0
syscall         # Imprimir el valor en $a0
la $a0, newline # Cargar la direccion de la cadena '\n'
li $v0, 4       # Codigo de syscall para imprimir cadenas
syscall         # Imprimir salto de linea
li $v0, 10
syscall

L_ackermann_2:
addi $sp, $sp, -8   # Reservar espacio para $ra, $fp
sw $ra, 0($sp)      # Guardar $ra
sw $fp, 4($sp)      # Guardar $fp
move $fp, $sp       # Establecer nuevo frame pointer
addi $sp, $sp, -88   # Reservar espacio para variables locales
sw $a0, 8($fp) # Guardar el valor de la variable 'm' en el stack
sw $a1, 12($fp) # Guardar el valor de la variable 'n' en el stack
li $t0, 0
sw $t0, 16($fp) # guardar el valor de la variable 't0-dfbfd646-d597-4a2c-bb5b-f1122dbc60a5' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "m" del stack
lw $t2, 16($fp) # Obtener el valor de la variable "t0-dfbfd646-d597-4a2c-bb5b-f1122dbc60a5" del stack
beq $t1, $t2, L1 # Saltar a L1 si m == t0-dfbfd646-d597-4a2c-bb5b-f1122dbc60a5
li $t0, 0
sw $t0, 20($fp) # guardar el valor de la variable 't1-1ff538c7-393c-4142-a619-b7724d6db696' en el stack
j L2
L1:
li $t0, 1
sw $t0, 20($fp) # guardar el valor de la variable 't1-1ff538c7-393c-4142-a619-b7724d6db696' en el stack
L2:
lw $t0, 20($fp) # Obtener el valor de la variable "t1-1ff538c7-393c-4142-a619-b7724d6db696" del stack
li $t1, 0
beq $t0, $t1, L4 # Saltar a L4 si t1-1ff538c7-393c-4142-a619-b7724d6db696 == 0
li $t2, 1
sw $t2, 24($fp) # guardar el valor de la variable 't2-d56d5774-c965-4f74-bd87-1ccbc186be7b' en el stack
lw $t3, 12($fp) # Obtener el valor de la variable "n" del stack
lw $t4, 24($fp) # Obtener el valor de la variable "t2-d56d5774-c965-4f74-bd87-1ccbc186be7b" del stack
add $t5, $t3, $t4 # Sumar los valores de n y t2-d56d5774-c965-4f74-bd87-1ccbc186be7b
sw $t5, 28($fp) # Almacenar el resultado de la suma en t3-1752144a-5f48-43b5-be99-dce1e02568c5
lw $t5, 28($fp) # Obtener el valor de la variable "t3-1752144a-5f48-43b5-be99-dce1e02568c5" del stack
sw $t5, 32($fp) # guardar el valor de la variable 't4-ba97e245-d271-4843-8306-2cc34e6507fd' en el stack
lw $v0, 32($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 88     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
j L3
L4:
L3:
li $t0, 0
sw $t0, 24($fp) # guardar el valor de la variable 't5-c7f63e94-7ed2-41d7-8cb7-dae9c0d83a53' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "m" del stack
lw $t2, 24($fp) # Obtener el valor de la variable "t5-c7f63e94-7ed2-41d7-8cb7-dae9c0d83a53" del stack
bgt $t1, $t2, L6 # Saltar a L6 si m > t5-c7f63e94-7ed2-41d7-8cb7-dae9c0d83a53
li $t0, 0
sw $t0, 28($fp) # guardar el valor de la variable 't6-43483615-06c8-4e32-9f62-e60d607e90f8' en el stack
j L5
L6:
li $t0, 1
sw $t0, 28($fp) # guardar el valor de la variable 't6-43483615-06c8-4e32-9f62-e60d607e90f8' en el stack
L5:
lw $t0, 28($fp) # Obtener el valor de la variable "t6-43483615-06c8-4e32-9f62-e60d607e90f8" del stack
li $t1, 0
beq $t0, $t1, L7 # Saltar a L7 si t6-43483615-06c8-4e32-9f62-e60d607e90f8 == 0
li $t1, 0
sw $t1, 32($fp) # guardar el valor de la variable 't7-7adb0454-8124-40af-81b2-2c80dbbf5332' en el stack
lw $t2, 12($fp) # Obtener el valor de la variable "n" del stack
lw $t3, 32($fp) # Obtener el valor de la variable "t7-7adb0454-8124-40af-81b2-2c80dbbf5332" del stack
beq $t2, $t3, L8 # Saltar a L8 si n == t7-7adb0454-8124-40af-81b2-2c80dbbf5332
li $t1, 0
sw $t1, 36($fp) # guardar el valor de la variable 't8-5a1f3f8d-b6c5-49c3-bd48-1e9a30b7872f' en el stack
j L9
L8:
li $t0, 1
sw $t0, 36($fp) # guardar el valor de la variable 't8-5a1f3f8d-b6c5-49c3-bd48-1e9a30b7872f' en el stack
L9:
lw $t0, 36($fp) # Obtener el valor de la variable "t8-5a1f3f8d-b6c5-49c3-bd48-1e9a30b7872f" del stack
li $t1, 0
beq $t0, $t1, L7 # Saltar a L7 si t8-5a1f3f8d-b6c5-49c3-bd48-1e9a30b7872f == 0
li $t2, 1
sw $t2, 40($fp) # guardar el valor de la variable 't9-57f4dd08-2670-4521-8bc9-4947718eecf1' en el stack
j L10
L7:
li $t0, 0
sw $t0, 40($fp) # guardar el valor de la variable 't9-57f4dd08-2670-4521-8bc9-4947718eecf1' en el stack
L10:
lw $t0, 40($fp) # Obtener el valor de la variable "t9-57f4dd08-2670-4521-8bc9-4947718eecf1" del stack
li $t1, 0
beq $t0, $t1, L12 # Saltar a L12 si t9-57f4dd08-2670-4521-8bc9-4947718eecf1 == 0
li $t2, 1
sw $t2, 44($fp) # guardar el valor de la variable 't10-8f132f08-68b8-490c-af21-cf0502e72a10' en el stack
lw $t3, 8($fp) # Obtener el valor de la variable "m" del stack
lw $t4, 44($fp) # Obtener el valor de la variable "t10-8f132f08-68b8-490c-af21-cf0502e72a10" del stack
sub $t5, $t3, $t4 # Restar los valores de m y t10-8f132f08-68b8-490c-af21-cf0502e72a10
sw $t5, 48($fp) # Almacenar el resultado de la resta en t11-b7d31379-ee84-4336-b6d7-d15e2b49a7a5
li $t2, 1
sw $t2, 52($fp) # guardar el valor de la variable 't12-6bd09480-cd6a-41a0-968e-cf77692b772f' en el stack
lw $t5, 48($fp) # Obtener el valor de la variable "t11-b7d31379-ee84-4336-b6d7-d15e2b49a7a5" del stack
move $a0, $t5 # Guardar el valor de la variable 't11-b7d31379-ee84-4336-b6d7-d15e2b49a7a5' en a0
lw $t6, 52($fp) # Obtener el valor de la variable "t12-6bd09480-cd6a-41a0-968e-cf77692b772f" del stack
move $a1, $t6 # Guardar el valor de la variable 't12-6bd09480-cd6a-41a0-968e-cf77692b772f' en a1
jal L_ackermann_2
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 56($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t0, 56($fp) # Obtener el valor de la variable "t13-b050f2d5-94d7-4d09-96ea-caf87fc167b4" del stack
sw $t0, 60($fp) # guardar el valor de la variable 't14-dc0763e6-8c6b-4818-9267-98c16696cac9' en el stack
lw $v0, 60($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 88     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
j L11
L12:
L11:
li $t0, 0
sw $t0, 44($fp) # guardar el valor de la variable 't15-0e525656-95d2-44c4-b85b-8ee22a2220c2' en el stack
lw $t1, 8($fp) # Obtener el valor de la variable "m" del stack
lw $t2, 44($fp) # Obtener el valor de la variable "t15-0e525656-95d2-44c4-b85b-8ee22a2220c2" del stack
bgt $t1, $t2, L14 # Saltar a L14 si m > t15-0e525656-95d2-44c4-b85b-8ee22a2220c2
li $t0, 0
sw $t0, 48($fp) # guardar el valor de la variable 't16-6ad776cc-f6d5-4702-9b7a-92aaaff9e99d' en el stack
j L13
L14:
li $t0, 1
sw $t0, 48($fp) # guardar el valor de la variable 't16-6ad776cc-f6d5-4702-9b7a-92aaaff9e99d' en el stack
L13:
lw $t0, 48($fp) # Obtener el valor de la variable "t16-6ad776cc-f6d5-4702-9b7a-92aaaff9e99d" del stack
li $t1, 0
beq $t0, $t1, L15 # Saltar a L15 si t16-6ad776cc-f6d5-4702-9b7a-92aaaff9e99d == 0
li $t1, 0
sw $t1, 52($fp) # guardar el valor de la variable 't17-b5f25630-b7f5-4198-ab45-2ff8f3cdb7b8' en el stack
lw $t2, 12($fp) # Obtener el valor de la variable "n" del stack
lw $t3, 52($fp) # Obtener el valor de la variable "t17-b5f25630-b7f5-4198-ab45-2ff8f3cdb7b8" del stack
bgt $t2, $t3, L17 # Saltar a L17 si n > t17-b5f25630-b7f5-4198-ab45-2ff8f3cdb7b8
li $t1, 0
sw $t1, 56($fp) # guardar el valor de la variable 't18-5b62f91a-7cff-48c1-84ea-3e9a422013c6' en el stack
j L16
L17:
li $t0, 1
sw $t0, 56($fp) # guardar el valor de la variable 't18-5b62f91a-7cff-48c1-84ea-3e9a422013c6' en el stack
L16:
lw $t0, 56($fp) # Obtener el valor de la variable "t18-5b62f91a-7cff-48c1-84ea-3e9a422013c6" del stack
li $t1, 0
beq $t0, $t1, L15 # Saltar a L15 si t18-5b62f91a-7cff-48c1-84ea-3e9a422013c6 == 0
li $t2, 1
sw $t2, 60($fp) # guardar el valor de la variable 't19-bb3e8eff-8f17-4c2d-94ce-9189ed6d5f84' en el stack
j L18
L15:
li $t0, 0
sw $t0, 60($fp) # guardar el valor de la variable 't19-bb3e8eff-8f17-4c2d-94ce-9189ed6d5f84' en el stack
L18:
lw $t0, 60($fp) # Obtener el valor de la variable "t19-bb3e8eff-8f17-4c2d-94ce-9189ed6d5f84" del stack
li $t1, 0
beq $t0, $t1, L20 # Saltar a L20 si t19-bb3e8eff-8f17-4c2d-94ce-9189ed6d5f84 == 0
li $t2, 1
sw $t2, 64($fp) # guardar el valor de la variable 't20-dacdb11a-7d75-46cb-b05f-bb8173fb21bd' en el stack
lw $t3, 8($fp) # Obtener el valor de la variable "m" del stack
lw $t4, 64($fp) # Obtener el valor de la variable "t20-dacdb11a-7d75-46cb-b05f-bb8173fb21bd" del stack
sub $t5, $t3, $t4 # Restar los valores de m y t20-dacdb11a-7d75-46cb-b05f-bb8173fb21bd
sw $t5, 68($fp) # Almacenar el resultado de la resta en t21-d4503f1a-cb9c-4194-891a-c5d6ae6f501b
li $t2, 1
sw $t2, 72($fp) # guardar el valor de la variable 't22-0f8f078c-b84f-46ca-85de-5af31a8890c8' en el stack
lw $t6, 12($fp) # Obtener el valor de la variable "n" del stack
lw $t7, 72($fp) # Obtener el valor de la variable "t22-0f8f078c-b84f-46ca-85de-5af31a8890c8" del stack
sub $t0, $t6, $t7 # Restar los valores de n y t22-0f8f078c-b84f-46ca-85de-5af31a8890c8
sw $t0, 76($fp) # Almacenar el resultado de la resta en t23-ba0a3ffc-ec42-4fbb-981a-a5f5a967ee74
lw $t1, 8($fp) # Obtener el valor de la variable "m" del stack
move $a0, $t1 # Guardar el valor de la variable 'm' en a0
lw $t0, 76($fp) # Obtener el valor de la variable "t23-ba0a3ffc-ec42-4fbb-981a-a5f5a967ee74" del stack
move $a1, $t0 # Guardar el valor de la variable 't23-ba0a3ffc-ec42-4fbb-981a-a5f5a967ee74' en a1
jal L_ackermann_2
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 80($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t1, 68($fp) # Obtener el valor de la variable "t21-d4503f1a-cb9c-4194-891a-c5d6ae6f501b" del stack
move $a0, $t1 # Guardar el valor de la variable 't21-d4503f1a-cb9c-4194-891a-c5d6ae6f501b' en a0
lw $t0, 80($fp) # Obtener el valor de la variable "t24-9fa7e047-3522-4bb2-955f-d70c41aa7d8d" del stack
move $a1, $t0 # Guardar el valor de la variable 't24-9fa7e047-3522-4bb2-955f-d70c41aa7d8d' en a1
jal L_ackermann_2
move $t0, $v0 # Obtener el valor de retorno de la funcion
sw $t0, 84($fp) # Almacenar el valor de retorno de la funcion en el stack
lw $t0, 84($fp) # Obtener el valor de la variable "t25-80b12f14-a63c-439a-9ac0-c3522a3c39ea" del stack
sw $t0, 88($fp) # guardar el valor de la variable 't26-33676ec9-829d-4d74-bd57-dbceed010333' en el stack
lw $v0, 88($fp)  # Leer el valor de retorno desde la ultima posicion
addi $sp, $sp, 88     # Limpiar espacio de variables locales
lw $fp, 4($sp)        # Restaurar $fp
lw $ra, 0($sp)        # Restaurar $ra
addi $sp, $sp, 8      # Restaurar $sp al estado previo
jr $ra                # Retornar al llamador
j L19
L20:
L19:

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
