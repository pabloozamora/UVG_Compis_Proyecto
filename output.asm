.text
.globl main
main:
li $a1, 0x10000000 # Cargar la direccion asignada para la variable 't0-ddb726ce-f356-41b4-a7f0-b6e1728c9bba' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 10.0
mfc1 $t0, $f1
li $a1, 0x10000004 # Cargar la direccion asignada para la variable 'a' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li $a1, 0x10000008 # Cargar la direccion asignada para la variable 't1-008adc86-0c18-42aa-8508-eced63452ea9' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 5.0
mfc1 $t1, $f1
mtc1 $t0, $f1 # Mover el ultimo valor valido de la variable 'a' en un registro float
mtc1 $t1, $f2 # Mover el ultimo valor valido de la variable 't1-008adc86-0c18-42aa-8508-eced63452ea9' en un registro float
c.lt.s $f2, $f1
bc1t L2
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 0.0
mfc1 $t2, $f1
lw $a3, 0x10000000 # Guardar variables antes de ambiguedad
sw $t0, 0($a3)
lw $a3, 0x10000004 # Guardar variables antes de ambiguedad
sw $t0, 0($a3)
lw $a3, 0x10000008 # Guardar variables antes de ambiguedad
sw $t1, 0($a3)
lw $a3, 0x1000000c # Guardar variables antes de ambiguedad
sw $t2, 0($a3)
j L1
L2:
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 1.0
mfc1 $t0, $f1
lw $a3, 0x1000000c # Guardar variables antes de ambiguedad
sw $t0, 0($a3)
L1:
li $a1, 0x1000000c # Cargar la direccion asignada para la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
lw $t0, 0x1000000c # La direccion del heap de la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' se carga en $t0
lw $t1, 0($t0) # El valor de la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' en el heap se carga en $t1
li.s $f1, 0.0
mfc1 $t2, $f1
mtc1 $t2, $f2 # Mover el valor de la constante '0' en un registro float
mtc1 $t1, $f1 # Mover el ultimo valor valido de la variable 't2-f06084a0-a4a5-496d-8b6c-d7afd2f2c0c4' en un registro float
c.eq.s $f1, $f2
bc1t L4
li $a1, 0x10000010 # Cargar la direccion asignada para la variable 't3-aa6e218f-0402-47da-be68-a6a1ddae4403' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 6.0
mfc1 $t3, $f1
mtc1 $t3, $f1
li $v0, 2
mov.s $f12, $f1
syscall
lw $a3, 0x1000000c # Guardar variables antes de ambiguedad
sw $t1, 0($a3)
lw $a3, 0x10000010 # Guardar variables antes de ambiguedad
sw $t3, 0($a3)
j L3
L4:
li $a1, 0x10000014 # Cargar la direccion asignada para la variable 't4-b3c4b51f-2418-4dd2-b889-a056c09830c2' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 5.0
mfc1 $t0, $f1
mtc1 $t0, $f1
li $v0, 2
mov.s $f12, $f1
syscall
lw $a3, 0x10000014 # Guardar variables antes de ambiguedad
sw $t0, 0($a3)
L3:
li $v0, 10
syscall

check_existing_variable:
lw $s0, 0($a1) # Cargar la dirección de la variable en memoria estática
bnez $s0, end_check_existing_variable # Si la direccion (argumento 1) no es 0, regresar
save_variable:
li $v0, 9
move $a0, $a2 # Obtener el tamano de la variable del argumento 2
syscall
move $a2, $v0 # Guardar la direccion de memoria asignada en $a2
sw $a2, 0($a1) # Guardar la direccion de memoria asignada en la variable en memoria estatica
end_check_existing_variable:
jr $ra
