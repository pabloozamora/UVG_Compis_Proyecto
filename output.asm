.text
.globl main
main:
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000000
lw $t0, 0x10000000
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000004
lw $t1, 0x10000004
li.s $f1, 10.0
mfc1 $t2, $f1
sw $t2, 0($t1)
lw $t3, 0x10000000
lw $t4, 0x10000004
lw $t4, 0($t4)
sw $t4, 0($t3)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000008
lw $t5, 0x10000008
li.s $f1, 10.0
mfc1 $t6, $f1
sw $t6, 0($t5)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x1000000c
lw $t7, 0x1000000c
lw $t0, 0x10000008
lw $t0, 0($t0)
sw $t0, 0($t7)
lw $t0, 0x10000000
lw $t1, 0x1000000c
lwc1 $f1, 0($t0)
lwc1 $f2, 0($t1)
mul.s $f3, $f1, $f2
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000010
lw $t0, 0x10000010
swc1 $f3, 0($t0)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000014
lw $t0, 0x10000014
li.s $f1, 5.0
mfc1 $t1, $f1
sw $t1, 0($t0)
lw $t0, 0x10000010
lw $t1, 0x10000014
lwc1 $f1, 0($t0)
lwc1 $f2, 0($t1)
div.s $f3, $f1, $f2
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000018
lw $t0, 0x10000018
swc1 $f3, 0($t0)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x1000001c
lw $t0, 0x1000001c
li.s $f1, 15.0
mfc1 $t1, $f1
sw $t1, 0($t0)
lw $t0, 0x10000018
lw $t1, 0x1000001c
lwc1 $f1, 0($t0)
lwc1 $f2, 0($t1)
add.s $f3, $f1, $f2
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000020
lw $t0, 0x10000020
swc1 $f3, 0($t0)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000024
lw $t0, 0x10000024
li.s $f1, 8.0
mfc1 $t1, $f1
sw $t1, 0($t0)
lw $t0, 0x10000020
lw $t1, 0x10000024
lwc1 $f1, 0($t0)
lwc1 $f2, 0($t1)
sub.s $f3, $f1, $f2
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000028
lw $t0, 0x10000028
swc1 $f3, 0($t0)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x1000002c
lw $t0, 0x1000002c
lw $t1, 0x10000028
lw $t1, 0($t1)
sw $t1, 0($t0)
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000030
lw $t0, 0x10000030
li.s $f1, 4.0
mfc1 $t1, $f1
sw $t1, 0($t0)
lw $t0, 0x1000002c
lw $t1, 0x10000030
lwc1 $f1, 0($t0)
lwc1 $f2, 0($t1)
add.s $f3, $f1, $f2
li $v0, 9
li $a0, 4
syscall
sw $v0, 0x10000034
lw $t0, 0x10000034
swc1 $f3, 0($t0)
lw $t0, 0x10000034
lwc1 $f1, 0($t0)
li $v0, 2
mov.s $f12, $f1
syscall
li $v0, 10
syscall
