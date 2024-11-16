.text
.globl main
main:
li $a1, 0x10000000 # Cargar la direccion asignada para la variable 't4-92840a91-9b22-4daf-b284-8a13df281b9d' en memoria estatica
li $a2, 4 # Cargar los bytes que necesita del heap
jal check_existing_variable
li.s $f1, 44.0
mfc1 $t0, $f1
addi $sp, $sp, -4 # Reservar espacio en el stack para los argumentos
sw $t0, 0($sp)
jal L_imprimir_1
li $v0, 10
syscall

L_imprimir_1:
lw $t0, 4($sp) # Obtener el valor de la variable "t0-5e9b913f-0c06-45df-8ebf-ceae167c2d21" del stack
li.s $f1, 50.0
mfc1 $t1, $f1
sw $t1, 4($sp)
lw $t2, 0($sp) # Obtener el valor de la variable "a" del stack
lw $t0, 4($sp) # Obtener el valor de la variable "t0-5e9b913f-0c06-45df-8ebf-ceae167c2d21" del stack
mtc1 $t2, $f1 # Mover el ultimo valor valido de la variable 'a' en un registro float
mtc1 $t0, $f2 # Mover el ultimo valor valido de la variable 't0-5e9b913f-0c06-45df-8ebf-ceae167c2d21' en un registro float
c.lt.s $f2, $f1
bc1t L2
lw $t3, 8($sp) # Obtener el valor de la variable "t1-5d06cce2-9d9f-49e4-abff-be0b70e6b16f" del stack
li.s $f1, 0.0
mfc1 $t4, $f1
sw $t4, 8($sp)
j L1
L2:
lw $t0, 8($sp) # Obtener el valor de la variable "t1-5d06cce2-9d9f-49e4-abff-be0b70e6b16f" del stack
li.s $f1, 1.0
mfc1 $t1, $f1
sw $t1, 8($sp)
L1:
lw $t0, 8($sp) # Obtener el valor de la variable "t1-5d06cce2-9d9f-49e4-abff-be0b70e6b16f" del stack
li.s $f1, 0.0
mfc1 $t1, $f1
mtc1 $t1, $f2 # Mover el valor de la constante '0' en un registro float
mtc1 $t0, $f1 # Mover el ultimo valor valido de la variable 't1-5d06cce2-9d9f-49e4-abff-be0b70e6b16f' en un registro float
c.eq.s $f1, $f2
bc1t L4
lw $t2, 12($sp) # Obtener el valor de la variable "t2-e1f1ba71-20e0-4524-a116-5f3b9e9a4ca4" del stack
li.s $f1, 100.0
mfc1 $t3, $f1
sw $t3, 12($sp)
lw $t2, 12($sp) # Obtener el valor de la variable "t2-e1f1ba71-20e0-4524-a116-5f3b9e9a4ca4" del stack
mtc1 $t2, $f1
li $v0, 2
mov.s $f12, $f1
syscall
j L3
L4:
lw $t0, 12($sp) # Obtener el valor de la variable "t3-225a7eff-7494-4ea2-a861-ed70e689f7cf" del stack
li.s $f1, 0.0
mfc1 $t1, $f1
sw $t1, 12($sp)
lw $t0, 12($sp) # Obtener el valor de la variable "t3-225a7eff-7494-4ea2-a861-ed70e689f7cf" del stack
mtc1 $t0, $f1
li $v0, 2
mov.s $f12, $f1
syscall
L3:
jr $ra

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
